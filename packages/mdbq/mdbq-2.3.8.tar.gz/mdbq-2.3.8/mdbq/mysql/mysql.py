# -*- coding:utf-8 -*-
import datetime
import platform
import getpass
import re
import time
from functools import wraps
import warnings
import pymysql
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import os
import calendar
from mdbq.config import get_myconf
from mdbq.config import set_support
from mdbq.dataframe import converter
from mdbq.aggregation import mysql_types

warnings.filterwarnings('ignore')
"""
建表流程:
尽可能手动建表，再上传数据
1. 每个表手动上传一个文件建表
2. 全部建表完成，建议所有表的数据类型，有问题的在数据库修改
3. 清空所有数据表，仅保留列信息
4. 下载所有数据表的 dtypes 信息到 json 文件
5. 之后可以正常上传数据

建表规范:
1. 数据库和数据表名如果有字母，必须使用小写，大写在建库后会自动变小写，再次上传数据会找不到数据库(macos和linux都有这种情况)
2. 无论是数据库/表/列名还是值，尽量避免特殊字符或者表情符号，数据库/表/列名尽量都使用 `列名` 转义，避免错误
3. 小数必须使用 decimal, 禁止 float 和 double, 因为计算精度差异，后续需要聚合数据时会引发很多问题
4. 日期类型暂时全部用 DATETIME，使用 DATE 在后续可能会重复插入不能排重，因为 df 进来的数据, 日期是带时间的，而数据库中日期不含时间
5. 目前小数自动适配类型转换，对于文本或者大数全部用 mediumtext, 因为部分表涉及爬虫数据，进来的字符长度未知，暂时统一 mediumtext 避免入库失败





"""


class MysqlUpload:
    def __init__(self, username: str, password: str, host: str, port: int, charset: str = 'utf8mb4'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.config = {
            'host': self.host,
            'port': self.port,
            'user': self.username,
            'password': self.password,
            'charset': charset,  # utf8mb4 支持存储四字节的UTF-8字符集
            'cursorclass': pymysql.cursors.DictCursor,
        }
        self.filename = None

    @staticmethod
    def try_except(func):  # 在类内部定义一个异常处理方法
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'{func.__name__}, {e}')  # 将异常信息返回

        return wrapper

    @try_except
    def df_to_mysql(self, df, table_name, db_name='远程数据源', icm_update=[], service_database={'home_lx': 'mysql'}, move_insert=False, df_sql=False, drop_duplicates=False, filename=None, count=None, json_path=None, reset_id=False):
        """
        将 df 写入数据库
        db_name: 数据库名称
        table_name: 集合/表名称
        move_insert: 根据df 的日期，先移除数据库数据，再插入, df_sql, drop_duplicates, icm_update 都要设置为 False
        原则上只限于聚合数据使用，原始数据插入时不要设置

        df_sql: 这是一个临时参数, 值为 True 时使用 df.to_sql 函数上传整个表, 不会排重，初创表大量上传数据的时候使用
        drop_duplicates: 值为 True 时检查重复数据再插入，反之直接上传，数据量大时会比较慢
        icm_update: 增量更新, 在聚合数据中使用，原始文件不要使用，设置此参数时需将 drop_duplicates 改为 False
                使用增量更新: 必须确保 icm_update 传进来的列必须是数据表中唯一主键，值不会发生变化，不会重复，否则可能产生错乱覆盖情况
        filename: 用来追踪处理进度，传这个参数是方便定位产生错误的文件
        service_databases: 这个参数是用来设置更新哪台服务器的 types 信息到本地 json 文件
        json_path: 这个参数同样也是是用来设置更新 json 文件
        """
        self.filename = filename
        if isinstance(df, pd.DataFrame):
            if len(df) == 0:
                print(f'{db_name}: {table_name} 传入的 df 数据长度为0, {self.filename}')
                return
        else:
            print(f'{db_name}: {table_name} 传入的 df 不是有效的 dataframe 结构, {self.filename}')
            return
        if not db_name or db_name == 'None':
            print(f'{db_name} 不能为 None')
            return

        cv = converter.DataFrameConverter()
        df = cv.convert_df_cols(df=df)  # 清理 dataframe 非法值

        connection = pymysql.connect(**self.config)  # 连接数据库
        with connection.cursor() as cursor:
            cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")  # 检查数据库是否存在
            database_exists = cursor.fetchone()
            if not database_exists:
                # 如果数据库不存在，则新建
                if '8.138.27' in str(self.host) or platform.system() == "Linux":  # 阿里云 mysql 低版本不支持 0900
                    sql = f"CREATE DATABASE `{db_name}` COLLATE utf8mb4_unicode_ci"
                    self.config.update({'charset': 'utf8mb4_unicode_ci'})
                if '192.168.1.100' in str(self.host):
                    sql = f"CREATE DATABASE `{db_name}`"
                else:
                    sql = f"CREATE DATABASE `{db_name}` COLLATE utf8mb4_0900_ai_ci"
                cursor.execute(sql)
                connection.commit()
                print(f"创建Database: {db_name}")

        self.config.update({'database': db_name})  # 添加更新 config 字段
        connection = pymysql.connect(**self.config)  # 重新连接数据库
        with connection.cursor() as cursor:
            # 1. 查询表, 不存在则创建一个空表
            sql = "SHOW TABLES LIKE %s;"  # 有特殊字符不需转义
            cursor.execute(sql, (table_name))
            if not cursor.fetchone():
                sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (id INT AUTO_INCREMENT PRIMARY KEY);"
                cursor.execute(sql)
                print(f'创建 mysql 表: {table_name}')

            for service_name, database in service_database.items():
                # 2. 列数据类型转换，将 df 数据类型转换为 mysql 的数据类型
                dtypes, cl, db_n, tb_n = self.convert_dtypes(df=df, db_name=db_name, table_name=table_name, path=json_path, service_name=service_name)

            #  有特殊字符不需转义
            sql = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s;"
            cursor.execute(sql, (db_name, table_name))
            col_exist = [item['COLUMN_NAME'] for item in cursor.fetchall()]
            cols = df.columns.tolist()
            col_not_exist = [col for col in cols if col not in col_exist]
            # 检查列，不存在则新建列
            if col_not_exist:  # 数据表中不存在的列
                for col in col_not_exist:
                    #  创建列，需转义
                    sql = f"ALTER TABLE `{table_name}` ADD COLUMN `{col}` {dtypes[col]};"
                    cursor.execute(sql)
                    print(f"添加列: {col}({dtypes[col]})")  # 添加列并指定数据类型

                    # 创建索引
                    if col == '日期':
                        sql = f"SHOW INDEXES FROM `{table_name}` WHERE `Column_name` = %s"
                        cursor.execute(sql, (col))
                        result = cursor.fetchone()  # 检查索引是否存在
                        if not result:
                            cursor.execute(f"CREATE INDEX index_name ON `{table_name}`(`{col}`)")
            connection.commit()  # 提交事务

            if df_sql:
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                print(f'{now}正在更新: mysql ({self.host}:{self.port}) {db_name}/{table_name}, {count}, {self.filename}')
                engine = create_engine(
                    f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{db_name}")  # 创建数据库引擎
                df.to_sql(
                    name=table_name,
                    con=engine,
                    if_exists='append',
                    index=False,
                    chunksize=1000
                )
                try:
                    cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'id'")
                    result = cursor.fetchone()
                    if result:
                        cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN id;")  # 删除 id  列
                    cursor.execute(
                        f"ALTER TABLE {table_name} ADD column id INT AUTO_INCREMENT PRIMARY KEY FIRST;")
                    cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")  # 设置自增从 1 开始
                except Exception as e:
                    print(f'{e}')
                    connection.rollback()
                connection.close()
                return

            # print(cl, db_n, tb_n)
            # 返回这些结果的目的是等添加完列再写 json 文件才能读到 types 信息
            # ⚠️ mysql_all_dtypes 函数默认只读取 home_lx 的数据库信息，不会读取其他系统
            if cl and db_n and tb_n:
                mysql_types.mysql_all_dtypes(service_database=service_database, db_name=db_name, table_name=table_name)  # 更新一个表的 dtypes
            elif cl and db_n:
                mysql_types.mysql_all_dtypes(service_database=service_database, db_name=db_name)  # 更新一个数据库的 dtypes
            elif cl:
                mysql_types.mysql_all_dtypes(service_database=service_database)  # 更新所有数据库所有数据表的 dtypes 信息到本地 json

            # 4. 更新插入数据
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            for service_name, database in service_database.items():
                print(f'{now}正在更新 mysql ({self.host}:{self.port}) {db_name}/{table_name}, {count}, {service_name}, {self.filename}')

            # 5. 移除指定日期范围内的数据，原则上只限于聚合数据使用，原始数据插入时不要设置
            if move_insert and '日期' in df.columns.tolist():
                # 移除数据
                dates = df['日期'].values.tolist()
                start_date = pd.to_datetime(min(dates)).strftime('%Y-%m-%d')
                end_date = (pd.to_datetime(max(dates)) + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
                sql = f"DELETE FROM `{table_name}` WHERE {'日期'} BETWEEN '%s' AND '%s'" % (start_date, end_date)
                cursor.execute(sql)
                connection.commit()

                # 插入数据
                engine = create_engine(
                    f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{db_name}")  # 创建数据库引擎
                df.to_sql(
                    name=table_name,
                    con=engine,
                    if_exists='append',
                    index=False,
                    chunksize=1000
                )
                # 6. 重置自增列
                if reset_id:
                    try:
                        cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'id'")
                        result = cursor.fetchone()
                        if result:
                            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN id;")  # 删除 id  列
                        cursor.execute(
                            f"ALTER TABLE {table_name} ADD column id INT AUTO_INCREMENT PRIMARY KEY FIRST;")
                        cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")  # 设置自增从 1 开始
                    except Exception as e:
                        print(f'{e}')
                        connection.rollback()
                connection.close()
                return

            datas = df.to_dict(orient='records')
            for data in datas:
                # data 是传进来待处理的数据, 不是数据库数据
                # data 示例: {'日期': Timestamp('2024-08-27 00:00:00'), '推广费余额': 33299, '品销宝余额': 2930.73, '短信剩余': 67471}
                try:
                    cols = ', '.join(f"`{item}`" for item in data.keys())  # 列名需要转义
                    # data.update({item: f"{data[item]}" for item in data.keys()})  # 全部值转字符, 不是必须的
                    values = ', '.join([f'"{item}"' for item in data.values()])  # 值要加引号
                    condition = []
                    for k, v in data.items():
                        condition += [f'`{k}` = "{v}"']
                    condition = ' AND '.join(condition)  # 构建查询条件
                    # print(condition)

                    if drop_duplicates:  # 查重插入
                        sql = "SELECT %s FROM %s WHERE %s" % (cols, table_name, condition)
                        # sql = f"SELECT {cols} FROM `{table_name}` WHERE `创建时间` = '2014-09-19 14:32:33'"
                        cursor.execute(sql)
                        result = cursor.fetchall()  # 获取查询结果, 有结果返回 list 表示数据已存在(不重复插入)，没有则返回空 tuple
                        # print(result)
                        if not result:  # 数据不存在则插入
                            sql = f"INSERT INTO `{table_name}` ({cols}) VALUES (%s);" % (values)
                            # print(sql)
                            cursor.execute(sql)
                        # else:
                        #     print(f'重复数据不插入: {condition[:50]}...')
                    elif icm_update:  # 增量更新, 专门用于聚合数据，其他库不要调用
                        """ 使用增量更新: 需确保 icm_update['主键'] 传进来的列必须是数据表中唯一主键，值不会发生变化且不会重复，否则可能产生覆盖情况 """
                        sql = 'SELECT COLUMN_NAME FROM information_schema.columns WHERE table_schema = %s AND table_name = %s'
                        cursor.execute(sql, (db_name, {table_name}))
                        columns = cursor.fetchall()
                        cols_exist = [col['COLUMN_NAME'] for col in columns]  # 数据表的所有列, 返回 list
                        update_col = [item for item in cols_exist if item not in icm_update and item != 'id']  # 除了主键外的其他列

                        # unique_keys 示例: `日期`, `余额`
                        unique_keys = ', '.join(f"`{item}`" for item in update_col)  # 列名需要转义
                        condition = []
                        for up_col in icm_update:
                            condition += [f'`{up_col}` = "{data[up_col]}"']
                        condition = ' AND '.join(condition)  # condition值示例: `品销宝余额` = '2930.73' AND `短信剩余` = '67471'
                        sql = f"SELECT {unique_keys} FROM `{table_name}` WHERE {condition}"
                        # print(sql)
                        # sql = f"SELECT {unique_keys} FROM `{table_name}` WHERE `创建时间` = '2014-09-19 14:32:33'"
                        cursor.execute(sql)
                        results = cursor.fetchall()  # results 是数据库取出的数据
                        if results:  # 有数据返回，再进行增量检查
                            for result in results:  # results 是数据库数据, data 是传进来的数据
                                change_col = []  # 发生变化的列名
                                change_values = []  # 发生变化的数据
                                for col in update_col:
                                    # 因为 mysql 里面有 decimal 数据类型，要移除末尾的 0 再做比较（df 默认将 5.00 小数截断为 5.0）
                                    df_value = str(data[col])
                                    mysql_value = str(result[col])
                                    if '.' in df_value:
                                        df_value = re.sub(r'0+$', '', df_value)
                                        df_value = re.sub(r'\.$', '', df_value)
                                    if '.' in mysql_value:
                                        mysql_value = re.sub(r'0+$', '', mysql_value)
                                        mysql_value = re.sub(r'\.$', '', mysql_value)
                                    if df_value != mysql_value:  # 传进来的数据和数据库比较, 有变化
                                        # print(f'{data['日期']}{data['商品id']}{col} 列的值有变化，{str(data[col])}  !=  {str(result[col])}')
                                        change_values += [f"`{col}` = \"{str(data[col])}\""]
                                        change_col.append(col)
                                not_change_col = [item for item in update_col if item not in change_col]
                                # change_values 是 df 传进来且和数据库对比后，发生了变化的数据，值示例： [`品销宝余额` = '9999.0', `短信剩余` = '888']
                                if change_values:  # change_values 有数据返回，表示值需要更新
                                    if not_change_col:
                                        not_change_values = [f'`{col}` = "{str(data[col])}"' for col in not_change_col]
                                        not_change_values = ' AND '.join(not_change_values)  # 示例: `短信剩余` = '888' AND `test1` = '93'
                                        # print(change_values, not_change_values)
                                        condition += f' AND {not_change_values}'  # 重新构建完整的查询条件，将未发生变化的列加进查询条件
                                    change_values = ', '.join(f"{item}" for item in change_values)  # 注意这里 item 外面没有反引号
                                    sql = "UPDATE `%s` SET %s WHERE %s" % (table_name, change_values, condition)
                                    # print(sql)
                                    cursor.execute(sql)
                        else:  # 没有数据返回，则直接插入数据
                            sql = f"INSERT INTO `{table_name}` ({cols}) VALUES ({values});"
                            cursor.execute(sql)
                    else:
                        sql = f"INSERT INTO `{table_name}` ({cols}) VALUES (%s);" % (values)
                        cursor.execute(sql)
                except Exception as e:
                    # print(data)
                    # print(values)
                    print(f'mysql -> df_to_mysql 报错: {e}, {self.filename}')
                    # breakpoint()

            # 6. 重置自增列
            try:
                cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'id'")
                result = cursor.fetchone()
                if result:
                    cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN id;")  # 删除 id  列
                cursor.execute(
                    f"ALTER TABLE {table_name} ADD column id INT AUTO_INCREMENT PRIMARY KEY FIRST;")
                cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")  # 设置自增从 1 开始
            except Exception as e:
                print(f'{e}')
                connection.rollback()
        connection.commit()  # 提交事务
        connection.close()

    def convert_dtypes(self, df, db_name, table_name, path=None, service_name=None):
        """
        根据本地 json 转换 df 的类型为 mysql 专有的数据类型
        可能不存在本地 json 文件 (函数按指定规则转换并更新 json)
        允许通过 json 文件手动添加或修改列的数据类型(仅影响初创数据表)
        """
        cols = df.columns.tolist()
        # path = set_support.SetSupport(dirname='support').dirname
        d = mysql_types.DataTypes(path=path, service_name=service_name)
        # 从本地文件中读取 dtype 信息
        dtypes, cl, db_n, tb_n = d.load_dtypes(cl='mysql', db_name=db_name, table_name=table_name)
        # 可能会因为没有 json 文件, 返回 None
        if dtypes:
            # 按照文件记录更新 dtypes
            dtypes.update({col: dtypes[col] for col in cols if col in dtypes.keys()})
            # 可能存在部分列不在文件记录中
            col_not_exist = [col for col in cols if col not in dtypes.keys()]
            # 这些列不存在于 df 中, 必须移除
            [dtypes.pop(col) for col in list(dtypes.keys()) if col not in cols]
        else:  # 没有 json 文件时
            dtypes = df.dtypes.apply(str).to_dict()  # 将 dataframe 数据类型转为字典形式
            col_not_exist = cols
        # 对文件不存在的列信息进行数据类型转换(按指定规则)
        dtypes.update({col: self.convert_dtype_to_sql(df=df, col=col, dtype=df[col].dtype) for col in col_not_exist})
        # print(dtypes)
        # 至此 df 中全部列类型已经转换完成
        # 返回结果, 示例: {'上市年份': 'mediumtext', '商品id': 'mediumtext', '平台': 'mediumtext'}
        return dtypes, cl, db_n, tb_n  # 返回这些结果的目的是等添加完列再写 json 文件才能读到 types 信息

    def convert_dtype_to_sql(self, df, col, dtype):
        """ 按照以下规则转换DataFrame列的数据类型为 MYSQL 专有的数据类型 """

        def find_longest_decimal_value(number_list):
            # 针对小数设置的函数, 用来获取列表中小数位数最长的值
            longest_value = None
            max_decimals = 0
            for num in number_list:
                try:
                    decimal_places = len(str(num).split('.')[1])
                    if decimal_places > max_decimals:
                        max_decimals = decimal_places
                        longest_value = num
                except:
                    longest_value = num
                    continue
            return longest_value

        if '商品编码' in col:  # 京东sku/spu商品信息
            return 'mediumtext'
        if '文件大小' in col:  # bw 程序
            return 'mediumtext'
        elif dtype == 'datetime64[ns]':
            return 'DATETIME'  # 使用 DATE 后续排重可能会引发不能排重
        elif dtype == 'int32':
            max_num = str(max(df[col].tolist()))
            if len(max_num) >= 10:  # 数值长度超限转为 mediumtext
                return 'mediumtext'
            return 'INT'
        elif dtype == 'int64':
            max_num = str(max(df[col].tolist()))
            if len(max_num) >= 10:
                return 'mediumtext'
            return 'INT'
        elif dtype == 'float64':
            res = find_longest_decimal_value(df[col].tolist())  # 取小数位数最长的值
            int_step = len(str(res).split('.')[0])   # 整数位数长度
            f_step = len(str(res).split('.')[1])  # 小数位数长度

            if int_step >= 12:
                return 'mediumtext'  # mysql 中不要使用 float 和 double 类型，会影响计算结果
            elif int_step >= 8 and f_step >= 0:
                return 'decimal(16, 2)'
            elif int_step >= 6 and f_step >= 0:
                return 'decimal(10, 2)'
            elif int_step >= 4 and f_step >= 0:
                return 'decimal(10, 2)'
            elif int_step >= 2 and f_step >= 6:
                return 'decimal(12, 6)'
            elif int_step >= 2 and f_step > 4:
                return 'decimal(10, 6)'
            elif int_step >= 2 and f_step > 2:
                return 'decimal(10, 4)'
            elif int_step >= 2 and f_step >= 0:
                return 'decimal(10, 2)'
            elif int_step >= 1 and f_step >= 6:
                return 'decimal(10, 6)'
            elif int_step >= 1 and f_step > 4:
                return 'decimal(10, 6)'
            elif int_step >= 1 and f_step > 2:
                return 'decimal(10, 4)'
            else:
                return 'decimal(10, 2)'
        elif dtype == 'object':
            return 'mediumtext'
        else:
            return 'mediumtext'

    # @try_except
    def read_mysql(self, table_name, start_date, end_date, db_name='远程数据源', date_name='日期'):
        """ 读取指定数据表，可指定日期范围，返回结果: df """
        start_date = pd.to_datetime(start_date).strftime('%Y-%m-%d')
        end_date = pd.to_datetime(end_date).strftime('%Y-%m-%d')
        df = pd.DataFrame()

        connection = pymysql.connect(**self.config)  # 连接数据库
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")  # 检查数据库是否存在
                database_exists = cursor.fetchone()
                if not database_exists:
                    print(f"Database {db_name} 数据库不存在")
                    return df
                else:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                    print(f'{now}mysql 正在查询表: {table_name}, 范围: {start_date}~{end_date}')
        except:
            return df
        finally:
            connection.close()  # 断开连接

        before_time = time.time()
        # 读取数据
        self.config.update({'database': db_name})
        connection = pymysql.connect(**self.config)  # 重新连接数据库
        try:
            with connection.cursor() as cursor:
                # 获取指定日期范围的数据
                sql = f"SELECT * FROM {db_name}.{table_name} WHERE {date_name} BETWEEN '%s' AND '%s'" % (start_date, end_date)
                cursor.execute(sql)
                rows = cursor.fetchall()  # 获取查询结果
                columns = [desc[0] for desc in cursor.description]
                df = pd.DataFrame(rows, columns=columns)  # 转为 df
        except Exception as e:
            print(f'{e} {db_name} -> {table_name} 表不存在')
            return df
        finally:
            connection.close()

        if len(df) == 0:
            print(f'database: {db_name}, table: {table_name} 查询的数据为空')
        else:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            cost_time = int(time.time() - before_time)
            if cost_time < 1:
                cost_time = round(time.time() - before_time, 2)
            print(f'{now}mysql ({self.host}) 表: {table_name} 获取数据长度: {len(df)}, 用时: {cost_time} 秒')
        return df

    def upload_pandas(self, update_path, db_name, days=None):
        """
        专门用来上传 pandas数据源的全部文件
        db_name: 数据库名: pandas数据源
        update_path: pandas数据源所在路径
        days: 更新近期数据，单位: 天, 不设置则全部更新
        """
        if days:
            today = datetime.date.today()
            start_date = pd.to_datetime(today - datetime.timedelta(days=days))
        else:
            start_date = pd.to_datetime('2000-01-01')

        root_files = os.listdir(update_path)
        for root_file in root_files:
            if '其他数据' in root_file or '年.csv' in root_file or '京东数据集' in root_file:
                continue  # 跳过的文件夹
            f_path = os.path.join(update_path, root_file)

            if os.path.isdir(f_path):
                for root, dirs, files in os.walk(f_path, topdown=False):
                    for name in files:
                        if name.endswith('.csv') and 'baidu' not in name:
                            df = pd.read_csv(os.path.join(root, name), encoding='utf-8_sig', header=0, na_filter=False)
                            # if '日期' not in df.columns.tolist():
                            #     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                            #     print(f'{now}{root_file} 缺少日期列, 不支持上传 mysql')
                            #     continue
                            if '日期' in df.columns.tolist():
                                df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x) if x else x)
                                df = df[df['日期'] >= start_date]
                            if len(df) == 0:
                                continue
                            self.df_to_mysql(df=df, db_name=db_name, table_name=root_file)
            elif os.path.isfile(f_path):
                if f_path.endswith('.csv') and 'baidu' not in f_path:
                    df = pd.read_csv(f_path, encoding='utf-8_sig', header=0, na_filter=False)
                    # if '日期' not in df.columns.tolist():
                    #     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                    #     print(f'{now}{root_file} 缺少日期列, 不支持上传 mysql')
                    #     continue
                    if '日期' not in df.columns.tolist():
                        df['日期'] = df['日期'].apply(lambda x: pd.to_datetime(x) if x else x)
                        df = df[df['日期'] >= start_date]
                    if len(df) == 0:
                        continue
                    table = f'{os.path.splitext(root_file)[0]}_f'  # 这里定义了文件表会加 _f 后缀
                    self.df_to_mysql(df=df, db_name=db_name, table_name=table)


class OptimizeDatas:
    """
    数据维护 删除 mysql 的冗余数据
    更新过程:
    1. 读取所有数据表
    2. 遍历表, 遍历列, 如果存在日期列则按天遍历所有日期, 不存在则全表读取
    3. 按天删除所有冗余数据(存在日期列时)
    tips: 查找冗余数据的方式是创建一个临时迭代器, 逐行读取数据并添加到迭代器, 出现重复时将重复数据的 id 添加到临时列表, 按列表 id 执行删除
    """
    def __init__(self, username: str, password: str, host: str, port: int, charset: str = 'utf8mb4'):
        self.username = username
        self.password = password
        self.host = host
        self.port = port  # 默认端口, 此后可能更新，不作为必传参数
        self.charset = charset
        self.config = {
            'host': self.host,
            'port': self.port,
            'user': self.username,
            'password': self.password,
            'charset': self.charset,  # utf8mb4 支持存储四字节的UTF-8字符集
            'cursorclass': pymysql.cursors.DictCursor,
        }
        self.db_name_lists: list = []  # 更新多个数据库 删除重复数据
        self.db_name = None
        self.days: int = 63  # 对近 N 天的数据进行排重
        self.end_date = None
        self.start_date = None
        self.connection = None

    @staticmethod
    def try_except(func):  # 在类内部定义一个异常处理方法
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f'{func.__name__}, {e}')  # 将异常信息返回

        return wrapper

    def optimize_list(self):
        """
        更新多个数据库 移除冗余数据
        需要设置 self.db_name_lists
        """
        if not self.db_name_lists:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            print(f'{now}尚未设置参数: self.db_name_lists')
            return
        for db_name in self.db_name_lists:
            self.db_name = db_name
            self.optimize()

    def optimize(self):
        """ 更新一个数据库 移除冗余数据 """
        if not self.db_name:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            print(f'{now}尚未设置参数: self.db_name')
            return
        tables = self.table_list(db_name=self.db_name)
        if not tables:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
            print(f'{now}{self.db_name} -> 数据表不存在')
            return

        # 日期初始化
        if not self.end_date:
            self.end_date = pd.to_datetime(datetime.datetime.today())
        else:
            self.end_date = pd.to_datetime(self.end_date)
        if self.days:
            self.start_date = pd.to_datetime(self.end_date - datetime.timedelta(days=self.days))
        if not self.start_date:
            self.start_date = self.end_date
        else:
            self.start_date = pd.to_datetime(self.start_date)
        start_date_before = self.start_date
        end_date_before = self.end_date

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        print(f'{now}mysql({self.host}: {self.port}) {self.db_name} 数据库优化中(日期长度: {self.days} 天)...')
        for table_dict in tables:
            for key, table_name in table_dict.items():
                # if '店铺指标' not in table_name:
                #     continue
                self.config.update({'database': self.db_name})  # 添加更新 config 字段
                self.connection = pymysql.connect(**self.config)
                with self.connection.cursor() as cursor:
                    sql = f"SELECT 1 FROM {table_name} LIMIT 1"
                    cursor.execute(sql)
                    result = cursor.fetchone()
                    if not result:
                        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                        print(f'{now}数据表: {table_name}, 数据长度为 0')
                        continue  # 检查数据表是否为空

                    cursor.execute(f"SHOW FULL COLUMNS FROM {table_name}")  # 查询数据表的列信息
                    columns = cursor.fetchall()
                    date_exist = False
                    for col in columns:  # 遍历列信息，检查是否存在类型为日期的列
                        if col['Field'] == '日期' and (col['Type'] == 'date' or col['Type'].startswith('datetime')):
                            date_exist = True
                            break
                    if date_exist:  # 存在日期列
                        sql_max = f"SELECT MAX(日期) AS max_date FROM {table_name}"
                        sql_min = f"SELECT MIN(日期) AS min_date FROM {table_name}"
                        cursor.execute(sql_max)
                        max_result = cursor.fetchone()
                        cursor.execute(sql_min)
                        min_result = cursor.fetchone()
                        # print(min_result['min_date'], max_result['max_date'])
                        # 匹配修改为合适的起始和结束日期
                        if self.start_date < pd.to_datetime(min_result['min_date']):
                            self.start_date = pd.to_datetime(min_result['min_date'])
                        if self.end_date > pd.to_datetime(max_result['max_date']):
                            self.end_date = pd.to_datetime(max_result['max_date'])
                        dates_list = self.day_list(start_date=self.start_date, end_date=self.end_date)
                        for date in dates_list:
                            self.delete_duplicate(table_name=table_name, date=date)
                        self.start_date = start_date_before  # 重置，不然日期错乱
                        self.end_date = end_date_before
                    else:  # 不存在日期列的情况
                        self.delete_duplicate2(table_name=table_name)

                    # 5. 重置自增列 (id 列)
                    try:
                        cursor.execute(f"SHOW COLUMNS FROM {table_name} LIKE 'id'")
                        result = cursor.fetchone()
                        if result:
                            cursor.execute(f"ALTER TABLE {table_name} DROP COLUMN id;")  # 删除 id  列
                        cursor.execute(
                            f"ALTER TABLE {table_name} ADD column id INT AUTO_INCREMENT PRIMARY KEY FIRST;")
                        cursor.execute(f"ALTER TABLE {table_name} AUTO_INCREMENT = 1")  # 设置自增从 1 开始
                    except Exception as e:
                        print(f'{e}')
                        self.connection.rollback()
                self.connection.close()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        print(f'{now}mysql({self.host}: {self.port}) {self.db_name} 数据库优化完成!')

    def delete_duplicate(self, table_name, date):
        datas = self.table_datas(db_name=self.db_name, table_name=str(table_name), date=date)
        if not datas:
            return
        duplicate_id = []  # 出现重复的 id
        all_datas = []  # 迭代器
        for data in datas:
            delete_id = data['id']
            del data['id']
            data = re.sub(r'\.0+\', ', '\', ', str(data))  # 统一移除小数点后面的 0
            if data in all_datas:  # 数据出现重复时
                duplicate_id.append(delete_id)  # 添加 id 到 duplicate_id
                continue
            all_datas.append(data)  # 数据没有重复
        del all_datas

        if not duplicate_id:  # 如果没有重复数据，则跳过该数据表
            return

        try:
            with self.connection.cursor() as cursor:
                placeholders = ', '.join(['%s'] * len(duplicate_id))
                # 移除冗余数据
                sql = f"DELETE FROM {table_name} WHERE id IN ({placeholders})"
                cursor.execute(sql, duplicate_id)
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                print(f"{now}{table_name} -> {date.strftime('%Y-%m-%d')} before: {len(datas)}, remove: {cursor.rowcount}")
            self.connection.commit()  # 提交事务
        except Exception as e:
            print(f'{self.db_name}/{table_name}, {e}')
            self.connection.rollback()  # 异常则回滚

    def delete_duplicate2(self, table_name):
        with self.connection.cursor() as cursor:
            sql = f"SELECT * FROM {table_name}"  # 如果不包含日期列，则获取全部数据
            cursor.execute(sql)
            datas = cursor.fetchall()
        if not datas:
            return
        duplicate_id = []  # 出现重复的 id
        all_datas = []  # 迭代器
        for data in datas:
            delete_id = data['id']
            del data['id']
            data = re.sub(r'\.0+\', ', '\', ', str(data))  # 统一移除小数点后面的 0
            if data in all_datas:  # 数据出现重复时
                duplicate_id.append(delete_id)  # 添加 id 到 duplicate_id
                continue
            all_datas.append(data)  # 数据没有重复
        del all_datas

        if not duplicate_id:  # 如果没有重复数据，则跳过该数据表
            return

        try:
            with self.connection.cursor() as cursor:
                placeholders = ', '.join(['%s'] * len(duplicate_id))
                # 移除冗余数据
                sql = f"DELETE FROM {table_name} WHERE id IN ({placeholders})"
                cursor.execute(sql, duplicate_id)
                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                print(f"{now}{table_name} -> before: {len(datas)}, "
                      f"remove: {cursor.rowcount}")
            self.connection.commit()  # 提交事务
        except Exception as e:
            print(f'{self.db_name}/{table_name}, {e}')
            self.connection.rollback()  # 异常则回滚

    def database_list(self):
        """ 获取所有数据库 """
        connection = pymysql.connect(**self.config)  # 连接数据库
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()  # 获取所有数据库的结果
        connection.close()
        return databases

    def table_list(self, db_name):
        """ 获取指定数据库的所有数据表 """
        connection = pymysql.connect(**self.config)  # 连接数据库
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SHOW DATABASES LIKE '{db_name}'")  # 检查数据库是否存在
                database_exists = cursor.fetchone()
                if not database_exists:
                    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
                    print(f'{now}{db_name}: 数据表不存在!')
                    return
        except Exception as e:
            print(f'002 {e}')
            return
        finally:
            connection.close()  # 断开连接

        self.config.update({'database': db_name})  # 添加更新 config 字段
        connection = pymysql.connect(**self.config)  # 重新连接数据库
        with connection.cursor() as cursor:
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()  # 获取所有数据表
        connection.close()
        return tables

    def table_datas(self, db_name, table_name, date):
        """
        获取指定数据表的数据, 按天获取
        """
        self.config.update({'database': db_name})  # 添加更新 config 字段
        connection = pymysql.connect(**self.config)
        try:
            with connection.cursor() as cursor:
                sql = f"SELECT * FROM {table_name} WHERE {'日期'} BETWEEN '%s' AND '%s'" % (date, date)
                cursor.execute(sql)
                results = cursor.fetchall()
        except Exception as e:
            print(f'001 {e}')
        finally:
            connection.close()
        return results

    def day_list(self, start_date, end_date):
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)
        date_list = []
        while start_date <= end_date:
            date_list.append(pd.to_datetime(start_date.date()))
            start_date += datetime.timedelta(days=1)
        return date_list

    def rename_column(self):
        """ 批量修改数据库的列名 """
        """
        # for db_name in ['京东数据2', '推广数据2', '市场数据2', '生意参谋2', '生意经2', '属性设置2',]:
        #     s = OptimizeDatas(username=username, password=password, host=host, port=port)
        #     s.db_name = db_name
        #     s.rename_column()
        """
        tables = self.table_list(db_name=self.db_name)
        for table_dict in tables:
            for key, table_name in table_dict.items():
                self.config.update({'database': self.db_name})  # 添加更新 config 字段
                self.connection = pymysql.connect(**self.config)
                with self.connection.cursor() as cursor:
                    cursor.execute(f"SHOW FULL COLUMNS FROM {table_name}")  # 查询数据表的列信息
                    columns = cursor.fetchall()
                    columns = [{column['Field']: column['Type']} for column in columns]
                    for column in columns:
                        for key, value in column.items():
                            if key.endswith('_'):
                                new_name = re.sub(r'_+$', '', key)
                                sql = f"ALTER TABLE {table_name} CHANGE COLUMN {key} {new_name} {value}"
                                cursor.execute(sql)
                self.connection.commit()
        if self.connection:
            self.connection.close()


def year_month_day_bak(start_date, end_date):
    """
    使用date_range函数和DataFrame来获取从start_date至end_date之间的所有年月日
    calendar.monthrange： 获取当月第一个工作日的星期值(0,6) 以及当月天数
    """
    # 替换年月日中的日, 以便即使传入当月日期也有返回值
    try:
        start_date = f'{pd.to_datetime(start_date).year}-{pd.to_datetime(start_date).month}-01'
    except Exception as e:
        print(e)
        return []
    # 使用pandas的date_range创建一个日期范围，频率为'MS'代表每月开始
    date_range = pd.date_range(start=start_date, end=end_date, freq='MS')
    # 转换格式
    year_months = date_range.strftime('%Y-%m').drop_duplicates().sort_values()

    results = []
    for year_month in year_months:
        year = re.findall(r'(\d{4})', year_month)[0]
        month = re.findall(r'\d{4}-(\d{2})', year_month)[0]
        s, d = calendar.monthrange(int(year), int(month))
        results.append({'起始日期': f'{year_month}-01', '结束日期': f'{year_month}-{d}'})

    return results  # start_date至end_date之间的所有年月日


def download_datas_bak(table_name, save_path, start_date):
    username, password, host, port = get_myconf.select_config_values(target_service='home_lx', database='mysql')
    print(username, password, host, port)
    m = MysqlUpload(username=username, password=password, host=host, port=port)
    m.port = port
    results = year_month_day(start_date=start_date, end_date='today')
    # print(results)
    for result in results:
        start_date = result['起始日期']
        end_date = result['结束日期']
        # print(start_date, end_date)
        df = m.read_mysql(db_name='天猫数据1', table_name=table_name, start_date=start_date, end_date=end_date)
        if len(df) == 0:
            continue
        path = os.path.join(save_path, f'{table_name}_{str(start_date)}_{str(end_date)}.csv')
        df['日期'] = df['日期'].apply(lambda x: re.sub(' .*', '', str(x)))
        df.to_csv(path, index=False, encoding='utf-8_sig', header=True)


if __name__ == '__main__':
    username, password, host, port = get_myconf.select_config_values(target_service='home_lx', database='mysql')
    # print(username, password, host, port)
    path = '/Users/xigua/Downloads/人群洞察.csv'
    df = pd.read_csv(path, encoding='utf-8_sig', header=0, na_filter=False)
    # print(df)
    m = MysqlUpload(username=username, password=password, host=host, port=port)
    m.df_to_mysql(
        df=df,
        db_name='test',
        table_name='测试数据',
        drop_duplicates=True,
        # service_name=service_name,
        # service_databases=service_databases,
    )

