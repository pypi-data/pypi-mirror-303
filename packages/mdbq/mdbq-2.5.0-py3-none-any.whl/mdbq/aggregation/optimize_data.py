# -*- coding: UTF-8 –*-
from mdbq.mongo import mongo
from mdbq.mysql import mysql
from mdbq.config import get_myconf
import socket
import subprocess
import psutil
import time
import platform
"""
对指定数据库所有冗余数据进行清理
"""


def restart_mongodb():
    """
    检查服务, 并重启, 只能操作本机
    """

    def get_pid(program_name):
        # macos 系统中，使用psutil.process_iter()遍历系统中所有运行的进程
        for process in psutil.process_iter(['name', 'pid']):
            if process.info['name'] == program_name:
                return process.info['pid']
        return None

    if platform.system() == 'Windows':
        print(f'即将重启 mongodb 服务')
        time.sleep(60)
        stop_command = f'net stop MongoDB'
        subprocess.call(stop_command, shell=True)  # 停止MongoDB服务

        time.sleep(30)
        start_command = f'net start MongoDB'
        subprocess.call(start_command, shell=True)  # 启动MongoDB服务
        time.sleep(30)

    elif platform.system() == 'Darwin':
        print(f'即将重启 mongodb 服务')
        time.sleep(60)
        result = get_pid('mongod')  # 获取进程号
        if result:  # 有 pid, 重启服务
            command = f'kill {result}'
            subprocess.call(command, shell=True)
            time.sleep(10)
            command = f'mongod --config /usr/local/mongodb/mongod.conf'
            subprocess.call(command, shell=True)
            # print('已重启服务')
        else:  # 没有启动, 则启动服务
            command = f'mongod --config /usr/local/mongodb/mongod.conf'
            subprocess.call(command, shell=True)

    elif platform.system() == 'Linux':
        print(f'即将重启 mongodb 服务')
        time.sleep(60)
        command = f'service mongod restart'
        subprocess.call(command, shell=True)


def op_data(db_name_lists, service_databases=None, days: int = 63, is_mongo=True, is_mysql=True):
    """ service_databases 这个参数暂时没有用 """
    # for service_database in service_databases:
    #     for service_name, database in service_database.items():
    #         username, password, host, port = get_myconf.select_config_values(target_service=service_name, database=database)
    #         s = mysql.OptimizeDatas(username=username, password=password, host=host, port=port)
    #         s.db_name_lists = [
    #             '聚合数据',
    #         ]
    #         s.days = days
    #         s.optimize_list()

    if socket.gethostname() == 'xigua_lx' or socket.gethostname() == 'xigua1' or socket.gethostname() == 'Mac2.local':
        # mongodb
        if is_mongo:
            username, password, host, port = get_myconf.select_config_values(
                target_service='home_lx',
                database='mongodb',
            )
            m = mongo.OptimizeDatas(username=username, password=password, host=host, port=port)
            m.db_name_lists = db_name_lists
            m.days = days
            m.optimize_list()
            if m.client:
                m.client.close()
                print(f'已关闭 mongodb 连接')

            if socket.gethostname() == 'xigua_lx':
                restart_mongodb()  # mongodb 太占内存了, 重启服务， 释放内存

        # Mysql
        if is_mysql:
            username, password, host, port = get_myconf.select_config_values(
                target_service='home_lx',
                database='mysql',
            )
            s = mysql.OptimizeDatas(username=username, password=password, host=host, port=port)
            s.db_name_lists = db_name_lists
            s.days = days
            s.optimize_list()

    elif socket.gethostname() == 'company':
        # Mysql
        if is_mysql:
            username, password, host, port = get_myconf.select_config_values(
                target_service='company',
                database='mysql',
            )
            s = mysql.OptimizeDatas(username=username, password=password, host=host, port=port)
            s.db_name_lists = db_name_lists
            s.days = days
            s.optimize_list()


if __name__ == '__main__':
    op_data(db_name_lists=['聚合数据'], service_databases=[{'company': 'mysql'}], days=3650, is_mongo=True, is_mysql=True)
