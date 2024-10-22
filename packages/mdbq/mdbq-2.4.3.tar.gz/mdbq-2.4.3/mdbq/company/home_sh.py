# -*- coding: UTF-8 –*-
import os
import platform
import warnings
import getpass
import sys
import configparser
import datetime
import shutil
import time
import re
import socket
from dateutil.utils import today
from mdbq.bdup import bdup
from mdbq.aggregation import aggregation
from mdbq.aggregation import query_data
from mdbq.aggregation import optimize_data
from mdbq.config import update_conf
from mdbq.config import get_myconf
from mdbq.config import set_support
from mdbq.config import products
from mdbq.mysql import mysql
if platform.system() == 'Windows':
    from mdbq.pbix import refresh_all
warnings.filterwarnings('ignore')
"""
除公司台式机外，其他主机执行下载更新任务
"""


class TbFiles:
    """
    用于定时同步pandas数据源文件到共享
    """
    def __init__(self):

        support_path = set_support.SetSupport(dirname='support').dirname

        self.my_conf = os.path.join(support_path, '.home.conf')
        self.path1 = os.path.join(support_path, 'tb_list.txt')
        self.path2 = os.path.join(support_path, 'cp_list.txt')
        self.d_path = None
        self.data_path = None
        self.share_path = None
        self.before_max_time = []
        self.sleep_minutes = 30
        self.tomorrow = datetime.date.today()

    def check_change(self):
        """ 检查 source_path 的所有文件修改日期, 函数返回最新修改日期 """
        source_path = os.path.join(self.data_path, 'pandas数据源')
        if not os.path.exists(source_path):
            return
        results = []
        for root, dirs, files in os.walk(source_path, topdown=False):
            for name in files:
                if '~$' in name or 'baiduyun' in name or name.startswith('.') or 'Icon' in name or 'xunlei' in name:
                    continue  # 排除这些文件的变动
                # stat_info = os.path.getmtime(os.path.join(root, name))
                _c = os.stat(os.path.join(root, name)).st_mtime  # 读取文件的元信息 >>>文件修改时间
                c_time = datetime.datetime.fromtimestamp(_c)  # 格式化修改时间
                results.append(c_time)
        return max(results).strftime('%Y%m%d%H%M%S')

    def check_conf(self):
        if not os.path.isfile(self.my_conf):
            self.set_conf()  # 添加配置文件
            print('因缺少配置文件, 已自动初始化')
        config = configparser.ConfigParser()  # 初始化configparser类
        try:
            config.read(self.my_conf, 'UTF-8')
            self.d_path = config.get('database', 'd_path')
            self.data_path = config.get('database', 'data_path')
            self.share_path = config.get('database', 'share_path')
            if self.d_path is None or self.data_path is None or self.share_path is None:
                self.set_conf()
                print('配置文件部分值不完整, 已自动初始化')
            if not os.path.exists(self.d_path) or not os.path.exists(self.data_path) or not os.path.exists(self.share_path):
                self.set_conf()
                print('配置文件异常(可能跨系统), 已自动初始化')
        except Exception as e:
            print(e)
            print('配置文件部分值缺失, 已自动初始化')
            self.set_conf()
        sys.path.append(self.share_path)

    def set_conf(self):
        if platform.system() == 'Windows':
            self.d_path = os.path.join('C:\\Users', getpass.getuser(), 'Downloads')
            self.data_path = os.path.join('C:\\同步空间', 'BaiduSyncdisk')
            self.share_path = os.path.join('\\\\192.168.1.198', '时尚事业部\\01.运营部\\天猫报表')  # 共享文件根目录
        elif platform.system() == 'Darwin':
            self.d_path = os.path.join('/Users', getpass.getuser(), 'Downloads')
            self.data_path = os.path.join('/Users', getpass.getuser(), '数据中心')
            self.share_path = os.path.join('/Volumes/时尚事业部/01.运营部/天猫报表')  # 共享文件根目录
        else:
            self.d_path = 'Downloads'
            self.data_path = os.path.join(getpass.getuser(), '数据中心')
            self.share_path = os.path.join('/Volumes/时尚事业部/01.运营部/天猫报表')  # 共享文件根目录

        if not os.path.exists(self.share_path):
            self.share_path = re.sub('时尚事业部', '时尚事业部-1', self.share_path)

        with open(self.my_conf, 'w+', encoding='utf-8') as f:
            f.write('[database]\n')
            f.write(f'# 配置文件\n')
            f.write(f'# home_sh.py ，当不是使用公司台式机 下载百度云文件夹进行任务更新时，读取这个配置文件\n')
            f.write('# 下载目录\n')
            f.write(f'd_path = {self.d_path}\n\n')
            f.write('# 数据中心目录\n')
            f.write(f'data_path = {self.data_path}\n\n')
            f.write('# 共享目录\n')
            f.write(f'share_path = {self.share_path}\n\n')
            f.write('# 用于触发下载百度云文件，更新至本机数据库\n')
            f.write(f'home_record = False\n\n')
        print('目录初始化!')

    def tb_file(self):

        self.check_conf()  # 检查配置文件

        now_max_time = self.check_change()
        if now_max_time in  self.before_max_time:
            return  # 不更新
        else:
            self.before_max_time = []  # 重置变量，以免越来越占内存
            self.before_max_time.append(now_max_time)

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
        res = self.check_upload_mysql()
        if not res:
            print(f'检测到源文件修改, 但今日已经同步过, 不再同步')
            return
        print(f'{now}pandas数据源文件修改, 触发同步 ({self.sleep_minutes}分钟后开始)')

        if not os.path.exists(self.data_path):
            print(f'{self.data_path}: 本地目录不存在或配置文件异常, 无法同步此目录')
            return None
        if not os.path.exists(self.share_path):
            print(f'{self.share_path}: 本机未连接共享或配置文件异常, 无法同步')
            return None

        time.sleep(self.sleep_minutes*60)  # 开始同步前休眠时间
        recent_time = 48  # 同步近N小时内更新过的文件，单位：小时
        tb_list = []
        pd_list = []
        try:
            with open(self.path1, 'r', encoding='utf-8') as f:
                content = f.readlines()
                content = [item.strip() for item in content if not item.strip().startswith('#')]
                tb_list = [item for item in content if item]

            with open(self.path2, 'r', encoding='utf-8') as f:
                content = f.readlines()
                content = [item.strip() for item in content if not item.strip().startswith('#')]
                pd_list = [item for item in content if item]
        except Exception as e:
            print(e)

        source_path = os.path.join(self.data_path, 'pandas数据源')  # \BaiduSyncdisk\pandas数据源
        target_path = os.path.join(self.share_path, 'pandas数据源')  # \01.运营部\天猫报表\pandas数据源

        if not os.path.exists(target_path):  # 检查共享主目录,创建目录
            os.makedirs(target_path, exist_ok=True)

        # 删除共享的副本
        file_list = os.listdir(self.share_path)
        for file_1 in file_list:
            if '副本_' in file_1 or 'con' in file_1:  # or '.DS' in file_1
                try:
                    os.remove(os.path.join(self.share_path, file_1))
                    print(f'移除: {os.path.join(self.share_path, file_1)}')
                except Exception as e:
                    print(e)
                    print(f'移除失败：{os.path.join(self.share_path, file_1)}')
        file_list2 = os.listdir(target_path)  # 删除乱七八糟的临时文件
        for file_1 in file_list2:
            if '.DS' in file_1 or 'con' in file_1:
                try:
                    os.remove(os.path.join(target_path, file_1))
                    print(f'移除: {os.path.join(target_path, file_1)}')
                except Exception as e:
                    print(e)

        # 删除 run_py的 副本
        del_p = os.path.join(self.data_path, '自动0备份', 'py', '数据更新', 'run_py')
        for file_1 in os.listdir(del_p):
            if '副本_' in file_1:
                try:
                    os.remove(os.path.join(del_p, file_1))
                    print(f'移除: {os.path.join(del_p, file_1)}')
                except Exception as e:
                    print(e)
                    print(f'移除失败：{os.path.join(del_p, file_1)}')

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{now} 正在同步文件...')
        # 复制 run_py的文件到共享
        for file_1 in tb_list:
            s = os.path.join(del_p, file_1)
            t = os.path.join(self.share_path, file_1)
            try:
                shutil.copy2(s, t)
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
                print(f'{now}复制: {s}')
            except Exception as e:
                print(e)
                s1 = os.path.join(del_p, f'副本_{file_1}')
                t1 = os.path.join(self.share_path, f'副本_{file_1}')
                shutil.copy2(s, s1)  # 创建副本
                shutil.copy2(s1, t1)  # 复制副本到共享
                now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
                print(f'{now}已创建副本 -->> {s1}')

        # 同步 pandas 文件到共享
        now_time = time.time()
        for filenames in pd_list:
            src = os.path.join(source_path, filenames)  # 原位置，可能是文件或文件夹
            dst = os.path.join(target_path, filenames)  # 目标位置，可能是文件或文件夹
            if os.path.isdir(src):  # 如果是文件夹
                for root, dirs, files in os.walk(src, topdown=False):
                    for name in files:
                        if '~$' in name or 'DS_Store' in name:
                            continue
                        if name.endswith('csv') or name.endswith('xlsx') or name.endswith('pbix') or name.endswith(
                                'xls'):
                            new_src = os.path.join(root, name)
                            # share_path = dst + '\\' + new_src.split(src)[1]  # 拼接目标路径
                            share_path = os.path.join(f'{dst}{new_src.split(src)[1]}')  # 拼接目标路径
                            ls_paths = os.path.dirname(os.path.abspath(share_path))  # 获取上级目录，用来创建
                            if not os.path.exists(ls_paths):  # 目录不存在则创建
                                os.makedirs(ls_paths, exist_ok=True)
                            c_stat = os.stat(new_src).st_mtime  # 读取文件的元信息 >>>文件修改时间
                            if now_time - c_stat < recent_time * 3600:  # 仅同步近期更新的文件
                                # res_name = os.path.basename(new_src)
                                try:
                                    shutil.copy2(new_src, share_path)
                                    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
                                    print(f'{now}复制文件: {new_src}')
                                except Exception as e:
                                    print(e)
            elif os.path.isfile(src) and 'DS_Store' not in src:  # 如果是文件
                if src.endswith('csv') or src.endswith('xlsx') or src.endswith('pbix') or src.endswith('xls'):
                    c_stat = os.stat(src).st_mtime  # 读取文件的元信息 >>>文件修改时间
                    if now_time - c_stat < recent_time * 3600:
                        ls_paths = os.path.dirname(os.path.abspath(src))  # 获取上级目录，用来创建
                        if not os.path.exists(ls_paths):  # 目录不存在则创建
                            os.makedirs(ls_paths, exist_ok=True)
                        # new_name = os.path.basename(src)
                        try:
                            shutil.copy2(src, dst)
                            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S ')
                            print(f'{now}复制文件: {src}')
                        except Exception as e:
                            print(e)
            else:
                print(f'{src} 所需同步的文件不存在，请检查：pd_list参数')

        if platform.system() == 'Windows':
            excel_path = os.path.join(self.share_path, 'EXCEL报表')
            files = os.listdir(excel_path)
            r = refresh_all.RefreshAll()
            for file in files:
                if file.endswith('.xlsx'):
                    # now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    # print(f'{now}正在刷新 excel: {file}')
                    r.refresh_excel2(excel_file=os.path.join(excel_path, file))
                time.sleep(10)

        self.before_max_time = self.check_change()  # 重置值, 避免重复同步

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f'{now} 同步完成！')

    def check_upload_mysql(self):
        # 每天只更新一次
        today = datetime.date.today()
        if today == self.tomorrow:
            self.tomorrow = today + datetime.timedelta(days=1)
            return True
        else:
            return False


class UpdateMysql:
    def __init__(self):
        support_path = set_support.SetSupport(dirname='support').dirname
        self.my_conf = os.path.join(support_path, '.home.conf')
        self.ch_record = False
        self.d_path = None

    def check_date(self):
        """ 检查文件中的 home_record 值，决定是否执行更新"""
        config = configparser.ConfigParser()  # 初始化configparser类
        try:
            config.read(self.my_conf, 'UTF-8')
            self.ch_record = config.get('database', 'home_record').lower()
            self.d_path = f'/Users/{getpass.getuser()}/Downloads'
        except Exception as e:
            print(e)
        if self.ch_record == 'false':
            return False, self.d_path
        elif self.ch_record == 'true':
            return True, self.d_path
        else:
            print(f'配置可能有误: {self.ch_record}, home_record 值应为: true 或 false')
            return False, self.d_path


def op_data(days: int =100):

    # 清理数据库， 除了 聚合数据
    if socket.gethostname() != 'company':  #
        # # Mysql
        # username, password, host, port = get_myconf.select_config_values(
        #     target_service='company',
        #     database='mysql',
        # )
        # s = mysql.OptimizeDatas(username=username, password=password, host=host, port=port)
        # s.db_name_lists = [
        #     '京东数据2',
        #     '推广数据2',
        #     '市场数据2',
        #     '生意参谋2',
        #     '生意经2',
        #     '属性设置2',
        #     # '聚合数据',  # 不在这里清理聚合数据, 还未开始聚合呢
        # ]
        # s.days = days
        # s.optimize_list()

        # 清理所有非聚合数据的库
        optimize_data.op_data(
            db_name_lists=[
                '京东数据2',
                '推广数据2',
                '市场数据2',
                '生意参谋2',
                '生意经2',
                '属性设置2',
                # '聚合数据',  # 不在这里清理聚合数据, 还未开始聚合呢
            ],
            days=days,
        )

        # 数据聚合
        query_data.data_aggregation(service_databases=[{'home_lx': 'mysql'}], months=3,)
        time.sleep(60)

        # 清理聚合数据
        optimize_data.op_data(db_name_lists=['聚合数据'], days=3650, )


def main():
    t = TbFiles()
    u = UpdateMysql()
    while True:
        res, d_path = u.check_date()  # 文件中的 ch_record 值，决定是否执行更新
        if res:
            upload_path = f'windows/{str(datetime.date.today().strftime("%Y-%m"))}/{str(datetime.date.today())}'
            b = bdup.BaiDu()
            b.download_dir(local_path=d_path, remote_path=upload_path)

            dp = aggregation.DatabaseUpdate(path=d_path)
            dp.new_unzip(is_move=True)
            dp.cleaning(is_move=True, is_except=[])  # 临时任务 需要移除自身下载的文件
            dp.upload_df(service_databases=[{'home_lx': 'mysql'}])
            dp.date_table(service_databases=[{'home_lx': 'mysql'}])  # 因为日期表不受 days 参数控制，因此单独更新日期表
            dp.other_table(service_databases=[{'home_lx': 'mysql'}])  # 上传 support 文件夹下的 主推商品.csv

            # 此操作用于修改 .home.conf 文件，将 home_record 改为 false (更新完成)
            w = update_conf.UpdateConf()
            w.update_config(filename='.home.conf', option='home_record', new_value='False')
            time.sleep(60)
            op_data(days=100)  # 数据清理和聚合

        t.sleep_minutes = 5  # 同步前休眠时间
        t.tb_file()
        time.sleep(600)  # 检测间隔


if __name__ == '__main__':
    main()
    # # 聚合数据，并清理聚合数据
    # query_data.data_aggregation(service_databases=[{'company': 'mysql'}], months=1)

