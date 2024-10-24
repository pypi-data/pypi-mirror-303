# -*- coding:utf-8 -*-
import datetime
import getpass
import json
import os
import pathlib
import platform
import re
import time
import warnings
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from mdbq.config import set_support
from selenium.webdriver.common.keys import Keys
from mdbq.aggregation import aggregation
from mdbq.clean import data_clean

warnings.filterwarnings('ignore')


if platform.system() == 'Windows':
    # windows版本
    Data_Path = r'C:\同步空间\BaiduSyncdisk'
    D_PATH = str(pathlib.Path(f'C:\\Users\\{getpass.getuser()}\\Downloads'))
    Share_Path = str(pathlib.Path(r'\\192.168.1.198\时尚事业部\01.运营部\天猫报表'))  # 共享文件根目录
    Source_Path = str(pathlib.Path(Data_Path, '原始文件2'))
elif platform.system() == 'Linux':
    Data_Path = '数据中心'
    D_PATH = 'Downloads'
    if not os.path.exists(D_PATH):
        os.makedirs(D_PATH)
    Share_Path = ''  # linux 通常是远程服务器，不需要访问共享
    Source_Path = str(pathlib.Path(Data_Path, '原始文件2'))
else:
    Data_Path = f'/Users/{getpass.getuser()}/数据中心'  # 使用Mac独立网络时
    # Data_Path = '/Volumes'  # 直接使用共享连接台式机时的配置， 后面接 + 自动0备份/***
    D_PATH = str(pathlib.Path(f'/Users/{getpass.getuser()}/Downloads'))
    Share_Path = str(pathlib.Path('/Volumes/时尚事业部/01.运营部/天猫报表'))  # 共享文件根目录
    Source_Path = str(pathlib.Path(Data_Path, '原始文件2'))


def get_cookie_aikucun():
    """
    """
    _url = 'https://gray-merc.aikucun.com/index.html'
    cookie_path = os.path.join(set_support.SetSupport(dirname='support').dirname, 'cookies')
    filename_aikucun = 'cookie_aikucun.json'
    print(_url)

    option = webdriver.ChromeOptions()  # 浏览器启动选项
    option.headless = True  # False指定为无界面模式
    # 调整chrome启动配置
    option.add_argument("--disable-gpu")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-dev-shm-usage")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option("useAutomationExtension", False)
    # if platform.system() == 'Windows':
    #     service = Service(os.path.join(f'C:\\Users\\{getpass.getuser()}\\chromedriver.exe'))
    # else:
    #     service = Service('/usr/local/bin/chromedriver')
    if platform.system() == 'Windows':
        # 设置Chrome的路径
        chrome_path = os.path.join(f'C:\\Users\\{getpass.getuser()}', 'chrome\\chrome_win64\\chrome.exe')
        chromedriver_path = os.path.join(f'C:\\Users\\{getpass.getuser()}', 'chrome\\chromedriver.exe')
        # os.environ["webdriver.chrome.driver"] = chrome_path
        option.binary_location = chrome_path  # windows 设置此参数有效
        service = Service(chromedriver_path)
        # service = Service(str(pathlib.Path(f'C:\\Users\\{getpass.getuser()}\\chromedriver.exe')))  # 旧路径
    else:
        # 设置Chrome的路径
        chrome_path = '/usr/local/chrome/Google Chrome for Testing.app'
        chromedriver_path = '/usr/local/chrome/chromedriver'
        os.environ["webdriver.chrome.driver"] = chrome_path

        service = Service(chromedriver_path)
    _driver = webdriver.Chrome(service=service, options=option)  # 创建Chrome驱动程序实例

    # 登录
    _driver.get(_url)
    time.sleep(0.1)
    _driver.maximize_window()  # 窗口最大化 方便后续加载数据
    breakpoint()

    d_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f'{d_time} 登录成功，正在获取cookie...')
    time.sleep(0.1)

    # 将cookies保存为json格式
    cookies_list = _driver.get_cookies()

    json_file = os.path.join(cookie_path, filename_aikucun)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(cookies_list, f, ensure_ascii=False, sort_keys=True, indent=4)
    print(f'cookie已保存: {json_file}')

    # _file = os.path.join(cookie_path, filename_aikucun)
    # with open(_file, 'w') as f:
    #     # 将cookies保存为json格式
    #     cookies_list = _driver.get_cookies()
    #     # for cookie in cookies_list:
    #     #     # 该字段有问题所以删除就可以
    #     #     if 'expiry' in cookie:
    #     #         del cookie['expiry']
    #     #     # if 'domain' in cookie:
    #     #     #     cookie['domain'] = '.taobao.com'
    #     cookies_list = json.dumps(cookies_list)
    #     f.write(cookies_list)
    #     print(f'cookie已保存: {_file}')
    _driver.quit()


class AikuCun:
    def __init__(self):
        # self.url = 'https://gray-merc.aikucun.com/index.html'
        self.sp_url = 'https://treasurebox.aikucun.com/dashboard/commodity/ranking/merchant?LS=true&shopId=1814114991487782914&from=menu&v=0.1936043279838604'
        self.cookie_path = os.path.join(set_support.SetSupport(dirname='support').dirname, 'cookies')

    def login(self, shop_name='aikucun'):
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")  # 设置无界面模式
        # 调整chrome启动配置
        option.add_argument("--disable-gpu")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        option.add_experimental_option("excludeSwitches", ["enable-automation"])
        option.add_experimental_option('excludeSwitches', ['enable-logging'])  # 禁止日志输出，减少控制台干扰
        option.add_experimental_option("useAutomationExtension", False)
        option.add_argument('--ignore-ssl-error')  # 忽略ssl错误
        prefs = {
            'profile.default_content_settings.popups': 0,  # 禁止弹出所有窗口
            "browser.download.manager. showAlertOnComplete": False,  # 下载完成后不显示下载完成提示框
            "profile.default_content_setting_values.automatic_downloads": 1,  # 允许自动下载多个文件
        }

        option.add_experimental_option('perfLoggingPrefs', {
            'enableNetwork': True,
            'enablePage': False,
        })
        option.set_capability("goog:loggingPrefs", {
            'browser': 'ALL',
            'performance': 'ALL',
        })
        option.set_capability("goog:perfLoggingPrefs", {
            'enableNetwork': True,
            'enablePage': False,
            'enableTimeline': False
        })

        option.add_experimental_option('prefs', prefs)
        option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 实验性参数, 左上角小字

        # # 通过excludeSwitches参数禁用默认的启动路径
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])

        if platform.system() == 'Windows':
            # 设置 chrome 和 chromedriver 启动路径
            chrome_path = os.path.join(f'C:\\Users\\{getpass.getuser()}', 'chrome\\chrome_win64\\chrome.exe')
            chromedriver_path = os.path.join(f'C:\\Users\\{getpass.getuser()}', 'chrome\\chromedriver.exe')
            # os.environ["webdriver.chrome.driver"] = chrome_path
            option.binary_location = chrome_path  # windows 设置此参数有效
            service = Service(chromedriver_path)
            # service = Service(str(pathlib.Path(f'C:\\Users\\{getpass.getuser()}\\chromedriver.exe')))  # 旧路径
        elif platform.system() == 'Darwin':
            chrome_path = '/usr/local/chrome/Google Chrome for Testing.app'
            chromedriver_path = '/usr/local/chrome/chromedriver'
            os.environ["webdriver.chrome.driver"] = chrome_path
            # option.binary_location = chrome_path  # Macos 设置此参数报错
            service = Service(chromedriver_path)
        else:
            chrome_path = '/usr/local/chrome/Google Chrome for Testing.app'
            chromedriver_path = '/usr/local/chrome/chromedriver'
            os.environ["webdriver.chrome.driver"] = chrome_path
            # option.binary_location = chrome_path  # macos 设置此参数报错
            service = Service(chromedriver_path)
        _driver = webdriver.Chrome(options=option, service=service)  # 创建Chrome驱动程序实例
        _driver.maximize_window()  # 窗口最大化 方便后续加载数据

        # 登录
        _driver.get(self.sp_url)
        _driver.delete_all_cookies()  # 首先清除浏览器打开已有的cookies
        name_lists = os.listdir(self.cookie_path)  # cookie 放在主目录下的 cookies 文件夹
        for name in name_lists:
            if shop_name in name and name.endswith('.json') and '~' not in name and '.DS' not in name:
                with open(os.path.join(self.cookie_path, name), 'r') as f:
                    cookies_list = json.load(f)  # 使用json读取cookies 注意读取的是文件 所以用load而不是loads
                    for cookie in cookies_list:
                        _driver.add_cookie(cookie)  # 添加cookies信息
        _driver.refresh()
        time.sleep(3)
        return _driver

    def get_data(self, shop_name='aikucun', date_num=1):
        """
        date_num: 获取最近 N 天数据，0表示今天
        所有数据都是逐日下载
        """

        _driver = self.login(shop_name=shop_name)

        _driver.get(self.sp_url)
        time.sleep(3)
        # breakpoint()

        today = datetime.date.today()
        for date_s in range(date_num):
            new_date = today - datetime.timedelta(days=date_s)  # 会用作文件名
            str_date = str(new_date)[2:]
            wait = WebDriverWait(_driver, timeout=15)  #
            elements = _driver.find_elements(
                By.XPATH, '//input[@placeholder="开始日期"]')
            # _driver.execute_script("arguments[0].click();", elements[0])  # 点击

            input_box = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//input[@placeholder="开始日期"]')))  #

            # from selenium.webdriver.common.keys import Keys
            for i in range(8):
                input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys(str_date)
            time.sleep(1)
            input_box = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//input[@placeholder="结束日期"]')))  # 文件名输入框

            for i in range(8):
                input_box.send_keys(Keys.BACKSPACE)
            input_box.send_keys(str_date)
            time.sleep(2)
            input_box.send_keys(Keys.ENTER)
            time.sleep(2)
            wait.until(EC.presence_of_element_located((By.XPATH, '//button/span[contains(text(), "查询")]')))
            elements = _driver.find_elements(
                By.XPATH, '//button/span[contains(text(), "查询")]')
            _driver.execute_script("arguments[0].click();", elements[0])  # 点击
            time.sleep(3)
            wait.until(EC.presence_of_element_located(
                (By.XPATH,
                 '//button[@class="el-button el-button--primary el-button--small is-plain"]/span[contains(text(), "下载数据")]')))
            elements = _driver.find_elements(
                By.XPATH,
                '//button[@class="el-button el-button--primary el-button--small is-plain"]/span[contains(text(), "下载数据")]')
            _driver.execute_script("arguments[0].click();", elements[0])  # 点击
            time.sleep(3)
            self.clean_data(date=new_date)
        _driver.quit()

    def clean_data(self, date):
        for root, dirs, files in os.walk(D_PATH, topdown=False):
            for name in files:
                if '~$' in name or 'DS_Store' in name:
                    continue
                if name.endswith('csv'):
                    pattern = re.findall('[\u4e00-\u9fff]+', name)
                    if pattern:
                        continue
                    pattern = re.findall('^[0-9a-zA-Z_]{5,}-[0-9a-zA-Z_]+-[0-9a-zA-Z_]+-[0-9a-zA-Z_]+', name)
                    if not pattern:
                        continue
                    df = pd.read_csv(os.path.join(root, name), encoding='gb2312', header=0, na_filter=False)
                    if len(df) == 0:
                        print(f'数据长度为 0 : {name}')
                        os.remove(os.path.join(root, name))
                        continue
                    df.insert(loc=0, column='日期', value=date)  # df中插入新列
                    df.rename(columns={'spuId': 'spu_id'}, inplace=True)
                    df['数据更新时间'] = pd.to_datetime(df['数据更新时间'], format='%Y-%m-%d %H:%M:%S', errors='ignore')
                    # df['数据更新时间'] = df['数据更新时间'].apply(lambda x: re.sub('  ', ' ', str(x)) if x else x)
                    # print(df['数据更新时间'])
                    # breakpoint()
                    new_name = f'爱库存_商品榜单_spu_{date}_{date}.csv'
                    df.to_csv(os.path.join(root, new_name), encoding='utf-8_sig', index=False)
                    os.remove(os.path.join(root, name))


def akucun():
    akc = AikuCun()
    akc.get_data(shop_name='aikucun', date_num=7)
    # akc.clean_data()

    # 新版 数据分类
    dp = aggregation.DatabaseUpdate(path=D_PATH)
    dp.new_unzip(is_move=True)
    dp.cleaning(is_move=False, is_except=['临时文件'])  # 清洗数据, 存入 self.datas, 不需要立即移除文件，仍保留文件到原始文件中
    # 将 self.datas 更新至数据库
    dp.upload_df(service_databases=[
        # {'home_lx': 'mongodb'},
        # {'home_lx': 'mysql'},
        {'company': 'mysql'},
        # {'nas': 'mysql'},
    ])
    # 数据分类
    c = data_clean.DataClean(path=D_PATH, source_path=Source_Path)
    c.set_up_to_mogo = False  # 不再使用 data_clean 更新数据库，改为 aggregation.py
    c.set_up_to_mysql = False  # 不再使用 data_clean 更新数据库，改为 aggregation.py
    c.new_unzip(is_move=True, )  # 解压文件
    c.change_and_sort(is_except=['临时文件'])
    c.move_all(is_except=['临时文件'])  # 移到文件到原始文件夹


if __name__ == '__main__':
    pass
    # get_cookie_aikucun()
    akucun()
