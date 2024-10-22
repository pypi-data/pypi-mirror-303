# -*- coding: UTF-8 –*-
import json
import os
import platform
import getpass
import pandas as pd
from mdbq.mysql import mysql
from mdbq.config import get_myconf
from numpy.ma.core import product

""" 
天猫货品年份基准对照
用于聚合数据，通过此数据表进一步可确定商品上架年月
"""


class Products:
    def __init__(self):
        self.datas = []

    def update_my_datas(self):
        my_datas = [
            {
                '平台': '天猫', '商品id': '840499705810', '上市年份': '2024年10月'
            },
            {
                '平台': '天猫', '商品id': '830789689032', '上市年份': '2024年9月'
            },
            {
                '平台': '天猫', '商品id': '822020840000', '上市年份': '2024年8月'
            },
            {
                '平台': '天猫', '商品id': '811000000000', '上市年份': '2024年7月'
            },
            {
                '平台': '天猫', '商品id': '800000000000', '上市年份': '2024年6月'
            },
            {
                '平台': '天猫', '商品id': '791359643000', '上市年份': '2024年5月'
            },
            {
                '平台': '天猫', '商品id': '778971448000', '上市年份': '2024年4月'
            },
            {
                '平台': '天猫', '商品id': '770576016820', '上市年份': '2024年3月'
            },
            {
                '平台': '天猫', '商品id': '766115058400', '上市年份': '2024年2月'
            },
            {
                '平台': '天猫', '商品id': '759478591187', '上市年份': '2024年1月'
            },
            {
                '平台': '天猫', '商品id': '752770183000', '上市年份': '2023年12月'
            },
            {
                '平台': '天猫', '商品id': '745123890000', '上市年份': '2023年11月'
            },
            {
                '平台': '天猫', '商品id': '741000000000', '上市年份': '2023年10月'
            },
            {
                '平台': '天猫', '商品id': '736841920000', '上市年份': '2023年9月'
            },
            {
                '平台': '天猫', '商品id': '730800000000', '上市年份': '2023年8月'
            },
            {
                '平台': '天猫', '商品id': '726939636835', '上市年份': '2023年7月'
            },
            {
                '平台': '天猫', '商品id': '721366048631', '上市年份': '2023年6月'
            },
            {
                '平台': '天猫', '商品id': '716130443004', '上市年份': '2023年5月'
            },
            {
                '平台': '天猫', '商品id': '709824308589', '上市年份': '2023年4月'
            },
            {
                '平台': '天猫', '商品id': '705440027804', '上市年份': '2023年3月'
            },
            {
                '平台': '天猫', '商品id': '701096067973', '上市年份': '2023年2月'
            },
            {
                '平台': '天猫', '商品id': '696017000000', '上市年份': '2023年1月'
            },
            {
                '平台': '天猫', '商品id': '666510000000', '上市年份': '2022年货品'
            },
            {
                '平台': '天猫', '商品id': '636010000000', '上市年份': '2021年货品'
            },
            {
                '平台': '天猫', '商品id': '610485872286', '上市年份': '2020年货品'
            },
            {
                '平台': '天猫', '商品id': '585066000000', '上市年份': '2019年货品'
            },
            {
                '平台': '天猫', '商品id': '563237000000', '上市年份': '2018年货品'
            },
            {
                '平台': '天猫', '商品id': '100', '上市年份': '历史悠久'
            },
        ]
        self.datas += my_datas

    def to_mysql(self, service_databases=[{'home_lx': 'mysql'}]):
        self.update_my_datas()
        df = pd.DataFrame(self.datas)
        for service_database in service_databases:
            for service_name, database in service_database.items():
                username, password, host, port = get_myconf.select_config_values(
                    target_service=service_name,
                    database=database,
                )
                m = mysql.MysqlUpload(
                    username=username,
                    password=password,
                    host=host,
                    port=port,
                )
                m.df_to_mysql(
                    df=df,
                    db_name='属性设置2',
                    table_name='货品年份基准',
                    move_insert = False,
                    df_sql=False,  # 值为 True 时使用 df.to_sql 函数上传整个表, 不会排重
                    drop_duplicates=True,  # 值为 True 时检查重复数据再插入，反之直接上传，会比较慢
                    icm_update=[],
                    service_database=service_database,  # 用来追踪处理进度
                )

    def market_date(self, product_id: int):
        try:
            product_id = int(product_id)
        except:
            return
        self.update_my_datas()
        market_date = [item['上市年份'] for item in self.datas if product_id > int(item['商品id'])]
        if market_date:
            return market_date[0]  # 返回上市年份


def main():
    pass


if __name__ == '__main__':
    product_id = '696017020186'
    p = Products()
    year = p.market_date(product_id=product_id)
    print(f'{product_id}:  {year}')

    p.to_mysql(service_databases=[
        {
            'home_lx': 'mysql'
        },
        {
            'company': 'mysql'
        }
    ]
    )
