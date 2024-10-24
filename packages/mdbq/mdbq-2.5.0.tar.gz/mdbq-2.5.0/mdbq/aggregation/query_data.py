# -*- coding: UTF-8 –*-
import re
from unittest.mock import inplace

from mdbq.mongo import mongo
from mdbq.mysql import mysql
from mdbq.mysql import s_query
from mdbq.aggregation import optimize_data
from mdbq.config import get_myconf
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import numpy as np
from functools import wraps
import platform
import getpass
import json
import os

"""
程序用于下载数据库(调用 s_query.py 下载并清洗), 并对数据进行聚合清洗, 不会更新数据库信息;

添加新库流程：
1.  在 MysqlDatasQuery 类中创建函数，从数据库取出数据
2.  在 GroupBy 类中创建函数，处理聚合数据
3.  在 data_aggregation 类中添加 data_dict 字典键值，回传数据到数据库

"""


class MongoDatasQuery:
    """
    从 数据库 中下载数据
    self.output: 数据库默认导出目录
    self.is_maximize: 是否最大转化数据
    """
    def __init__(self, target_service):
        # target_service 从哪个服务器下载数据
        self.months = 0  # 下载几个月数据, 0 表示当月, 1 是上月 1 号至今
        # 实例化一个下载类
        username, password, host, port = get_myconf.select_config_values(target_service=target_service, database='mongodb')
        self.download = mongo.DownMongo(username=username, password=password, host=host, port=port, save_path=None)

    def tg_wxt(self):
        self.download.start_date, self.download.end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '主体id': 1,
            '花费': 1,
            '展现量': 1,
            '点击量': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
            '自然流量曝光量': 1,
            '直接成交笔数': 1,
            '直接成交金额': 1,
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            collection_name='主体报表',
            projection=projection,
        )
        return df

    @staticmethod
    def days_data(days, end_date=None):
        """ 读取近 days 天的数据 """
        if not end_date:
            end_date = datetime.datetime.now()
        start_date = end_date - datetime.timedelta(days=days)
        return pd.to_datetime(start_date), pd.to_datetime(end_date)

    @staticmethod
    def months_data(num=0, end_date=None):
        """ 读取近 num 个月的数据, 0 表示读取当月的数据 """
        if not end_date:
            end_date = datetime.datetime.now()
        start_date = end_date - relativedelta(months=num)  # n 月以前的今天
        start_date = f'{start_date.year}-{start_date.month}-01'  # 替换为 n 月以前的第一天
        return pd.to_datetime(start_date), pd.to_datetime(end_date)


class MysqlDatasQuery:
    """
    从数据库中下载数据
    """
    def __init__(self, target_service):
        # target_service 从哪个服务器下载数据
        self.months = 0  # 下载几个月数据, 0 表示当月, 1 是上月 1 号至今
        # 实例化一个下载类
        username, password, host, port = get_myconf.select_config_values(target_service=target_service, database='mysql')
        self.download = s_query.QueryDatas(username=username, password=password, host=host, port=port)

    def tg_wxt(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '主体id': 1,
            '花费': 1,
            '展现量': 1,
            '点击量': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
            '自然流量曝光量': 1,
            '直接成交笔数': 1,
            '直接成交金额': 1,
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            table_name='主体报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def syj(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '宝贝id': 1,
            '商家编码': 1,
            '行业类目': 1,
            '销售额': 1,
            '销售量': 1,
            '订单数': 1,
            '退货量': 1,
            '退款额': 1,
            '退款额（发货后）': 1,
            '退货量（发货后）': 1,
        }
        df = self.download.data_to_df(
            db_name='生意经2',
            table_name='宝贝指标',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def tg_rqbb(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '主体id': 1,
            '花费': 1,
            '展现量': 1,
            '点击量': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
            '直接成交笔数': 1,
            '直接成交金额': 1,
            '人群名字': 1,
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            table_name='人群报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def tg_gjc(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '宝贝id': 1,
            '词类型': 1,
            '词名字/词包名字': 1,
            '花费': 1,
            '展现量': 1,
            '点击量': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
            '直接成交笔数': 1,
            '直接成交金额': 1,
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            table_name='关键词报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def tg_cjzb(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '人群名字': 1,
            '计划名字': 1,
            '花费': 1,
            '展现量': 1,
            '进店量': 1,
            '粉丝关注量': 1,
            '观看次数': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
            '直接成交笔数': 1,
            '直接成交金额': 1,
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            table_name='超级直播',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def pxb_zh(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '报表类型': 1,
            '搜索量': 1,
            '搜索访客数': 1,
            '展现量': 1,
            # '自然流量增量曝光': 1,
            '消耗': 1,
            '点击量': 1,
            '宝贝加购数': 1,
            '成交笔数': 1,
            '成交金额': 1,
            # '成交访客数': 1
        }
        df = self.download.data_to_df(
            db_name='推广数据2',
            table_name='品销宝',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def idbm(self):
        """ 用生意经日数据制作商品 id 和编码对照表 """
        data_values = self.download.columns_to_list(
            db_name='生意经2',
            table_name='宝贝指标',
            columns_name=['宝贝id', '商家编码', '行业类目'],
        )
        df = pd.DataFrame(data=data_values)
        return df

    def sp_picture(self):
        """ 用生意经日数据制作商品 id 和编码对照表 """
        data_values = self.download.columns_to_list(
            db_name='属性设置2',
            table_name='商品素材导出',
            columns_name=['日期', '商品id', '商品白底图', '方版场景图'],
        )
        df = pd.DataFrame(data=data_values)
        return df

    def dplyd(self):
        """ 新旧版取的字段是一样的 """
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '一级来源': 1,
            '二级来源': 1,
            '三级来源': 1,
            '访客数': 1,
            '支付金额': 1,
            '支付买家数': 1,
            '支付转化率': 1,
            '加购人数': 1,
        }
        df = self.download.data_to_df(
            db_name='生意参谋2',
            table_name='店铺来源_日数据',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def dplyd_old(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '一级来源': 1,
            '二级来源': 1,
            '三级来源': 1,
            '访客数': 1,
            '支付金额': 1,
            '支付买家数': 1,
            '支付转化率': 1,
            '加购人数': 1,
        }
        df = self.download.data_to_df(
            db_name='生意参谋2',
            table_name='店铺来源_日数据_旧版',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def sp_cost(self):
        """ 电商定价 """
        data_values = self.download.columns_to_list(
            db_name='属性设置2',
            table_name='电商定价',
            columns_name=['日期', '款号', '年份季节', '吊牌价', '商家平台', '成本价', '天猫页面价', '天猫中促价'],
        )
        df = pd.DataFrame(data=data_values)
        return df

    def jdjzt(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '产品线': 1,
            '触发sku id': 1,
            '跟单sku id': 1,
            '花费': 1,
            '展现数': 1,
            '点击数': 1,
            '直接订单行': 1,
            '直接订单金额': 1,
            '总订单行': 1,
            '总订单金额': 1,
            '直接加购数': 1,
            '总加购数': 1,
            'spu id': 1,
        }
        df = self.download.data_to_df(
            db_name='京东数据2',
            table_name='推广数据_京准通',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df
    def jdqzyx(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '产品线': 1,
            '花费': 1,
            '全站roi': 1,
            '全站交易额': 1,
            '全站订单行': 1,
            '全站订单成本': 1,
            '全站费比': 1,
            '核心位置展现量': 1,
            '核心位置点击量': 1,
        }
        df = self.download.data_to_df(
            db_name='京东数据2',
            table_name='推广数据_全站营销',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df
    def jd_gjc(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '产品线': 1,
            '计划类型': 1,
            '计划id': 1,
            '推广计划': 1,
            '搜索词': 1,
            '关键词': 1,
            '关键词购买类型': 1,
            '广告定向类型': 1,
            '花费': 1,
            '展现数': 1,
            '点击数': 1,
            '直接订单行': 1,
            '直接订单金额': 1,
            '总订单行': 1,
            '总订单金额': 1,
            '总加购数': 1,
            '下单新客数_去重': 1,
            '领券数': 1,
            '商品关注数': 1,
            '店铺关注数': 1
        }
        df = self.download.data_to_df(
            db_name='京东数据2',
            table_name='推广数据_关键词报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df
    def sku_sales(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '商品id': 1,
            '货号': 1,
            '成交单量': 1,
            '成交金额': 1,
            '访客数': 1,
            '成交客户数': 1,
            '加购商品件数': 1,
            '加购人数': 1,
        }
        df = self.download.data_to_df(
            db_name='京东数据2',
            table_name='sku_商品明细',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df
    def spu_sales(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '商品id': 1,
            '货号': 1,
            '成交单量': 1,
            '成交金额': 1,
            '访客数': 1,
            '成交客户数': 1,
            '加购商品件数': 1,
            '加购人数': 1,
        }
        df = self.download.data_to_df(
            db_name='京东数据2',
            table_name='spu_商品明细',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    @staticmethod
    def months_data(num=0, end_date=None):
        """ 读取近 num 个月的数据, 0 表示读取当月的数据 """
        if not end_date:
            end_date = datetime.datetime.now()
        start_date = end_date - relativedelta(months=num)  # n 月以前的今天
        start_date = f'{start_date.year}-{start_date.month}-01'  # 替换为 n 月以前的第一天
        return pd.to_datetime(start_date), pd.to_datetime(end_date)

    def tm_search(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '关键词': 1,
            '访客数': 1,
            '支付转化率': 1,
            '支付金额': 1,
            '下单金额': 1,
            '支付买家数': 1,
            '下单买家数': 1,
            '加购人数': 1,
            '新访客': 1,
        }
        df = self.download.data_to_df(
            db_name='生意参谋2',
            table_name='店铺来源_手淘搜索',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def zb_ccfx(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '店铺': 1,
            '场次信息': 1,
            '场次id': 1,
            '直播开播时间': 1,
            '开播时长': 1,
            '封面图点击率': 1,
            '观看人数': 1,
            '观看次数': 1,
            '新增粉丝数': 1,
            '流量券消耗': 1,
            '观看总时长（秒）': 1,
            '人均观看时长（秒）': 1,
            '次均观看时长（秒）': 1,
            '商品点击人数': 1,
            '商品点击次数': 1,
            '商品点击率': 1,
            '加购人数': 1,
            '加购件数': 1,
            '加购次数': 1,
            '成交金额（元）': 1,
            '成交人数': 1,
            '成交件数': 1,
            '成交笔数': 1,
            '成交转化率': 1,
            '退款人数': 1,
            '退款笔数': 1,
            '退款件数': 1,
            '退款金额（元）': 1,
            '预售定金支付金额（元）': 1,
            '预售预估总金额（元）': 1,
        }
        df = self.download.data_to_df(
            db_name='生意参谋2',
            table_name='直播场次分析',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def tg_by_day(self):
        """
        汇总各个店铺的推广数据，按日汇总
        """
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '场景名字': 1,
            '花费': 1,
            '展现量': 1,
            '点击量': 1,
            '总购物车数': 1,
            '总成交笔数': 1,
            '总成交金额': 1,
        }
        df_tm = self.download.data_to_df(
            db_name='推广数据2',
            table_name='营销场景报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_tm.rename(columns={'场景名字': '营销场景'}, inplace=True)
        df_tm = df_tm.groupby(
            ['日期', '营销场景', '花费'],
            as_index=False).agg(
            **{
                '展现量': ('展现量', np.max),
                '点击量': ('点击量', np.max),
                '加购量': ('总购物车数', np.max),
                '成交笔数': ('总成交笔数', np.max),
                '成交金额': ('总成交金额', np.max)
            }
        )
        df_tm.insert(loc=1, column='店铺', value='WLM天猫旗舰店')  # df中添加列

        df_tb = self.download.data_to_df(
            db_name='推广数据_淘宝店',
            table_name='营销场景报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        # print(df_tb)
        # df_tm.to_csv('/Users/xigua/Downloads/test2.csv', index=False, header=True, encoding='utf-8_sig')
        # df_tb.to_csv('/Users/xigua/Downloads/test.csv', index=False, header=True, encoding='utf-8_sig')
        df_tb.rename(columns={'场景名字': '营销场景'}, inplace=True)
        df_tb = df_tb.groupby(
            ['日期', '营销场景', '花费'],
            as_index=False).agg(
            **{
                '展现量': ('展现量', np.max),
                '点击量': ('点击量', np.max),
                '加购量': ('总购物车数', np.max),
                '成交笔数': ('总成交笔数', np.max),
                '成交金额': ('总成交金额', np.max)
            }
        )
        df_tb.insert(loc=1, column='店铺', value='淘宝c店')  # df中添加列

        projection = {
            '日期': 1,
            '报表类型': 1,
            '消耗': 1,
            '展现量': 1,
            '点击量': 1,
            '宝贝加购数': 1,
            '成交笔数': 1,
            '成交金额': 1,
        }
        df_tm_pxb = self.download.data_to_df(
            db_name='推广数据2',
            table_name='品销宝',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_tm_pxb = df_tm_pxb[df_tm_pxb['报表类型'] == '账户']
        df_tm_pxb = df_tm_pxb.groupby(
            ['日期', '报表类型', '消耗'],
            as_index=False).agg(
            **{
                '展现量': ('展现量', np.max),
                '点击量': ('点击量', np.max),
                '加购量': ('宝贝加购数', np.max),
                '成交笔数': ('成交笔数', np.max),
                '成交金额': ('成交金额', np.max)
            }
        )
        df_tm_pxb.rename(columns={'报表类型': '营销场景', '消耗': '花费'}, inplace=True)
        df_tm_pxb['营销场景'] = '品销宝'
        df_tm_pxb.insert(loc=1, column='店铺', value='WLM天猫旗舰店')  # df中添加列

        projection = {
            '日期': 1,
            '产品线': 1,
            '触发sku id': 1,
            '跟单sku id': 1,
            '花费': 1,
            '展现数': 1,
            '点击数': 1,
            '直接订单行': 1,
            '直接订单金额': 1,
            '总订单行': 1,
            '总订单金额': 1,
            '直接加购数': 1,
            '总加购数': 1,
            'spu id': 1,
        }
        df_jd = self.download.data_to_df(
            db_name='京东数据2',
            table_name='推广数据_京准通',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_jd = df_jd.groupby(['日期', '产品线', '触发sku id', '跟单sku id', 'spu id', '花费', '展现数', '点击数'],
                        as_index=False).agg(
            **{'直接订单行': ('直接订单行', np.max),
               '直接订单金额': ('直接订单金额', np.max),
               '成交笔数': ('总订单行', np.max),
               '成交金额': ('总订单金额', np.max),
               '直接加购数': ('直接加购数', np.max),
               '加购量': ('总加购数', np.max),
               }
        )
        df_jd = df_jd[['日期', '产品线', '花费', '展现数', '点击数', '加购量', '成交笔数', '成交金额']]
        df_jd.rename(columns={'产品线': '营销场景', '展现数': '展现量', '点击数': '点击量'}, inplace=True)
        df_jd = df_jd[df_jd['花费'] > 0]
        df_jd.insert(loc=1, column='店铺', value='京东箱包')  # df中添加列

        projection = {
            '日期': 1,
            '产品线': 1,
            '花费': 1,
            '全站roi': 1,
            '全站交易额': 1,
            '全站订单行': 1,
            '全站订单成本': 1,
            '全站费比': 1,
            '核心位置展现量': 1,
            '核心位置点击量': 1,
        }
        df_jd_qzyx = self.download.data_to_df(
            db_name='京东数据2',
            table_name='推广数据_全站营销',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_jd_qzyx = df_jd_qzyx.groupby(['日期', '产品线', '花费'], as_index=False).agg(
            **{'全站roi': ('全站roi', np.max),
               '成交金额': ('全站交易额', np.max),
               '成交笔数': ('全站订单行', np.max),
               '全站订单成本': ('全站订单成本', np.max),
               '全站费比': ('全站费比', np.max),
               '展现量': ('核心位置展现量', np.max),
               '点击量': ('核心位置点击量', np.max),
               }
        )
        df_jd_qzyx.rename(columns={'产品线': '营销场景'}, inplace=True)
        df_jd_qzyx = df_jd_qzyx[['日期', '营销场景', '花费', '展现量', '点击量', '成交笔数', '成交金额']]
        df_jd_qzyx = df_jd_qzyx[df_jd_qzyx['花费'] > 0]
        df_jd_qzyx.insert(loc=1, column='店铺', value='京东箱包')  # df中添加列

        _datas = [item for item in  [df_tm, df_tb, df_tm_pxb, df_jd, df_jd_qzyx] if len(item) > 0]  # 阻止空的 dataframe
        df = pd.concat(_datas, axis=0, ignore_index=True)
        return df

    def aikucun_bd_spu(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            'spi_id': 1,
            '商品名称': 1,
            '品牌名称': 1,
            '商品款号': 1,
            '一级类目名称': 1,
            '二级类目名称': 1,
            '三级类目名称': 1,
            '转发次数': 1,
            '转发爱豆人数': 1,
            '访客量': 1,
            '浏览量': 1,
            '下单gmv': 1,
            '成交gmv': 1,
            '供货额': 1,
            '供货价': 1,
            '销售爱豆人数_成交': 1,
            '支付人数_交易': 1,
            '支付人数_成交': 1,
            '销售量_成交': 1,
            '销售量_交易': 1,
            '订单数_成交': 1,
            '订单数_交易': 1,
            '成交率_交易': 1,
            '成交率_成交': 1,
            '可售库存数': 1,
            '售罄率': 1,
            '在架sku数': 1,
            '可售sku数': 1,
            'sku数_交易': 1,
            'sku数_成交': 1,
            '营销后供货额': 1,
            '营销后供货价': 1,
        }
        projection = {}
        df = self.download.data_to_df(
            db_name='爱库存2',
            table_name='商品spu榜单',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        return df

    def dmp_crowd(self):
        start_date, end_date = self.months_data(num=self.months)
        projection = {
            '日期': 1,
            '人群id': 1,
            '人群规模': 1,
            '用户年龄': 1,
            '消费能力等级': 1,
            '用户性别': 1,
        }
        # projection = {}
        df_crowd = self.download.data_to_df(
            db_name='达摩盘2',
            table_name='我的人群属性',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_crowd.sort_values('日期', ascending=True, ignore_index=True, inplace=True)
        df_crowd.drop_duplicates(subset=['人群id',], keep='last', inplace=True, ignore_index=True)
        df_crowd.pop('日期')
        # print(df_crowd)

        projection = {}
        df_dmp = self.download.data_to_df(
            db_name='推广数据2',
            table_name='达摩盘_dmp报表',
            start_date=start_date,
            end_date=end_date,
            projection=projection,
        )
        df_dmp.sort_values('日期', ascending=True, ignore_index=True, inplace=True)
        df_dmp.drop_duplicates(subset=['日期', '人群id', '消耗(元)'], keep='last', inplace=True, ignore_index=True)
        df = pd.merge(df_dmp, df_crowd, left_on=['人群id'], right_on=['人群id'], how='left')
        # 清除一些不必要的字符
        df['用户年龄'] = df['用户年龄'].apply(lambda x: '~'.join(re.findall(r'^(\d+).*-(\d+)岁$', str(x))[0]) if '岁' in str(x) else x)
        df['消费能力等级'] = df['消费能力等级'].apply(lambda x: f'L{''.join(re.findall(r'(\d)', str(x)))}' if '购买力' in str(x) else x)
        # df.to_csv('/Users/xigua/Downloads/test3.csv', index=False, header=True, encoding='utf-8_sig')
        # breakpoint()
        return df



class GroupBy:
    """
    数据聚合和导出
    """
    def __init__(self):
        # self.output: 数据库默认导出目录
        if platform.system() == 'Darwin':
            self.output = os.path.join('/Users', getpass.getuser(), '数据中心/数据库导出')
        elif platform.system() == 'Windows':
            self.output = os.path.join('C:\\同步空间\\BaiduSyncdisk\\数据库导出')
        else:
            self.output = os.path.join('数据中心/数据库导出')
        self.data_tgyj = {}  # 推广综合聚合数据表
        self.data_jdtg = {}  # 京东推广数据，聚合数据
        self.sp_index_datas = pd.DataFrame()  # 商品 id 索引表

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
    def groupby(self, df, table_name, is_maximize=True):
        """
        self.is_maximize: 是否最大转化数据
        table_name： 聚合数据库处的名称，不是原始数据库
        """
        if isinstance(df, pd.DataFrame):
            if len(df) == 0:
                print(f' query_data.groupby 函数中 {table_name} 传入的 df 数据长度为0')
                self.data_tgyj.update(
                    {
                        table_name: pd.DataFrame(),
                    }
                )
                return pd.DataFrame()
        # elif '多店推广场景_按日聚合' in table_name:  # 这个函数传递的是多个 df 组成的列表，暂时放行
        #     pass
        else:
            print(f'query_data.groupby函数中 {table_name} 传入的 df 不是 dataframe 结构')
            return pd.DataFrame()
        # print(table_name)
        if '天猫_主体报表' in table_name:
            df.rename(columns={
                '场景名字': '营销场景',
                '主体id': '商品id',
                '总购物车数': '加购量',
                '总成交笔数': '成交笔数',
                '总成交金额': '成交金额'
            }, inplace=True)
            df.fillna(0, inplace=True)
            df = df.astype({
                '商品id': str,
                '花费': float,
                '展现量': int,
                '点击量': int,
                '加购量': int,
                '成交笔数': int,
                '成交金额': float,
                '自然流量曝光量': int,
                '直接成交笔数': int,
                '直接成交金额': float,
            }, errors='raise')
            if is_maximize:
                df = df.groupby(['日期', '营销场景', '商品id', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{'加购量': ('加购量', np.max),
                       '成交笔数': ('成交笔数', np.max),
                       '成交金额': ('成交金额', np.max),
                       '自然流量曝光量': ('自然流量曝光量', np.max),
                       '直接成交笔数': ('直接成交笔数', np.max),
                       '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            else:
                df = df.groupby(['日期', '营销场景', '商品id', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{
                        '加购量': ('加购量', np.min),
                        '成交笔数': ('成交笔数', np.min),
                        '成交金额': ('成交金额', np.min),
                        '自然流量曝光量': ('自然流量曝光量', np.min),
                        '直接成交笔数': ('直接成交笔数', np.max),
                        '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            df.insert(loc=1, column='推广渠道', value='万相台无界版')  # df中插入新列
            df_new = df.groupby(['日期', '商品id'], as_index=False).agg(
                    **{
                        '花费': ('花费', np.sum),
                        '成交笔数': ('成交笔数', np.max),
                        '成交金额': ('成交金额', np.max),
                        '自然流量曝光量': ('自然流量曝光量', np.max),
                        '直接成交笔数': ('直接成交笔数', np.max),
                        '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            self.data_tgyj.update(
                {
                    table_name: df_new,
                }
            )
            self.data_tgyj.update(
                {
                    '天猫汇总表调用': df,
                }
            )
            # df_pic：商品排序索引表, 给 powerbi 中的主推款排序用的,(从上月1号到今天的总花费进行排序)
            today = datetime.date.today()
            last_month = today - datetime.timedelta(days=30)
            if last_month.month == 12:
                year_my = today.year - 1
            else:
                year_my = today.year
            # 截取 从上月1日 至 今天的花费数据, 推广款式按此数据从高到低排序（商品图+排序）
            df_pic = df.groupby(['日期', '商品id'], as_index=False).agg({'花费': 'sum'})
            df_pic = df_pic[~df_pic['商品id'].isin([''])]  # 指定列中删除包含空值的行
            df_pic = df_pic[(df_pic['日期'] >= f'{year_my}-{last_month.month}-01')]
            df_pic = df_pic.groupby(['商品id'], as_index=False).agg({'花费': 'sum'})
            df_pic.sort_values('花费', ascending=False, ignore_index=True, inplace=True)
            df_pic.reset_index(inplace=True)
            df_pic['index'] = df_pic['index'] + 100
            df_pic.rename(columns={'index': '商品索引'}, inplace=True)
            df_pic_new = pd.merge(df, df_pic, how='left', on=['商品id'])
            df_pic_new['商品索引'].fillna(1000, inplace=True)
            self.sp_index_datas = df_pic_new[['商品id', '商品索引']]
            return df
        elif '商品索引表' in table_name:
            return df
        elif '爱库存_商品spu榜单' in table_name:
            df.drop_duplicates(
                subset=[
                    '日期',
                    'spu_id',
                    '访客量',
                    '浏览量',
                    '下单gmv',
                    '成交gmv',
                ], keep='last', inplace=True, ignore_index=True)
            return df
        elif '天猫_人群报表' in table_name and '达摩盘' not in table_name:
            """ 天猫推广人群报表独立生成消费力、年龄层、分类等特征，不依赖于达摩盘数据表 """
            df.rename(columns={
                '场景名字': '营销场景',
                '主体id': '商品id',
                '总购物车数': '加购量',
                '总成交笔数': '成交笔数',
                '总成交金额': '成交金额'
            }, inplace=True)
            df.fillna(0, inplace=True)
            df = df.astype({
                '商品id': str,
                '花费': float,
                '展现量': int,
                '点击量': int,
                '加购量': int,
                '成交笔数': int,
                '成交金额': float,
                '直接成交笔数': int,
                '直接成交金额': float,
            }, errors='raise')
            if is_maximize:
                df = df.groupby(['日期', '营销场景', '商品id', '花费', '展现量', '点击量', '人群名字'], as_index=False).agg(
                    **{'加购量': ('加购量', np.max),
                       '成交笔数': ('成交笔数', np.max),
                       '成交金额': ('成交金额', np.max),
                       '直接成交笔数': ('直接成交笔数', np.max),
                       '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            else:
                df = df.groupby(['日期', '营销场景', '商品id', '花费', '展现量', '点击量', '人群名字'], as_index=False).agg(
                    **{
                        '加购量': ('加购量', np.min),
                        '成交笔数': ('成交笔数', np.min),
                        '成交金额': ('成交金额', np.min),
                        '直接成交笔数': ('直接成交笔数', np.max),
                        '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            df.insert(loc=1, column='推广渠道', value='万相台无界版')  # df中插入新列
            # 1. 匹配 L后面接 2 个或以上数字，不区分大小写，示例：L345
            # 2. 其余情况，L 后面接多个数字的都会被第一条 if 命中，不区分大小写
            df['消费力层级'] = df.apply(
                lambda x:
                ''.join(re.findall(r'(l\d+)', x['人群名字'].upper(), re.IGNORECASE)) if re.findall(r'(l\d{2,})', x['人群名字'], re.IGNORECASE)
                else 'L5' if re.findall(r'(l\d*5)', x['人群名字'], re.IGNORECASE)
                else 'L4' if re.findall(r'(l\d*4)', x['人群名字'], re.IGNORECASE)
                else 'L3' if re.findall(r'(l\d*3)', x['人群名字'], re.IGNORECASE)
                else 'L2' if re.findall(r'(l\d*2)', x['人群名字'], re.IGNORECASE)
                else 'L1' if re.findall(r'(l\d*1)', x['人群名字'], re.IGNORECASE)
                else '', axis=1)
            # 1. 匹配连续的 4 个数字且后面不能接数字或"元"或汉字，筛掉的人群示例：月均消费6000元｜受众20240729175213｜xxx2024真皮公文包
            # 2. 匹配 2数字_2数字且前面不能是数字，合法匹配：人群_30_50_促； 非法示例：L345_3040 避免识别出 35～20 岁用户的情况
            # pattern = r'(\d{4})(?!\d|[\u4e00-\u9fa5])'  # 匹配 4 个数字，后面不能接数字或汉字
            # pattern = r'(?<![\d\u4e00-\u9fa5])(\d{4})' # 匹配前面不是数字或汉字的 4 个连续数字

            # 匹配 4 个数字，前面和后面都不能是数字或汉字
            pattern1 = r'(?<![\d\u4e00-\u9fa5])(\d{4})(?!\d|[\u4e00-\u9fa5])'
            # 匹配指定字符，前面不能是数字或 l 或 L 开头
            pattern2 = r'(?<![\dlL])(\d{2}_\d{2})'
            df['用户年龄'] = df.apply(
                lambda x:
                ''.join(re.findall(pattern1, x['人群名字'].upper())) if re.findall(pattern1, x['人群名字'])
                # else ''.join(re.findall(r'[^\d|l|L](\d{2}_\d{2})', x['人群名字'].upper())) if re.findall(r'[^\d|l|L](\d{2}_\d{2})', x['人群名字'])
                else ''.join(re.findall(pattern2, x['人群名字'].upper())) if re.findall(pattern2, x['人群名字'])
                else ''.join(re.findall(r'(\d{2}-\d{2})岁', x['人群名字'].upper())) if re.findall(r'(\d{2}-\d{2})岁', x['人群名字'])
                else '', axis=1)
            df['用户年龄'] = df['用户年龄'].apply(
                lambda x: f'{x[:2]}~{x[2:4]}' if str(x).isdigit()
                else str(x).replace('_', '~') if '_' in x
                else str(x).replace('-', '~') if '-' in x
                else x
            )
            # 年龄层不能是 0 开头
            df['用户年龄'] = df['用户年龄'].apply(
                lambda x: '' if str(x).startswith('0') else x)
            # df = df.head(1000)
            # df.to_csv('/Users/xigua/Downloads/test.csv', index=False, header=True, encoding='utf-8_sig')
            # breakpoint()

            # 下面是添加人群 AIPL 分类
            dir_file = f'\\\\192.168.1.198\\时尚事业部\\01.运营部\\0-电商周报-每周五更新\\分类配置文件.xlsx'
            dir_file2 = '/Volumes/时尚事业部/01.运营部/0-电商周报-每周五更新/分类配置文件.xlsx'
            if platform.system() == 'Windows':
                dir_file3 = 'C:\\同步空间\\BaiduSyncdisk\\原始文件2\\分类配置文件.xlsx'
            else:
                dir_file3 = '/Users/xigua/数据中心/原始文件2/分类配置文件.xlsx'
            if not os.path.isfile(dir_file):
                dir_file = dir_file2
            if not os.path.isfile(dir_file):
                dir_file = dir_file3
            if os.path.isfile(dir_file):
                df_fl = pd.read_excel(dir_file, sheet_name='人群分类', header=0)
                df_fl = df_fl[['人群名字', '人群分类']]
                # 合并并获取分类信息
                df = pd.merge(df, df_fl, left_on=['人群名字'], right_on=['人群名字'], how='left')
                df['人群分类'].fillna('', inplace=True)
            if '人群分类' in df.columns.tolist():
                # 这行决定了，从文件中读取的分类信息优先级高于内部函数的分类规则
                # 这个 lambda 适配人群名字中带有特定标识的分类，强匹配
                df['人群分类'] = df.apply(
                    lambda x: self.set_crowd(keyword=str(x['人群名字']), as_file=False) if x['人群分类'] == ''
                    else x['人群分类'], axis=1
                )
                # 这个 lambda 适配人群名字中聚类的特征字符，弱匹配
                df['人群分类'] = df.apply(
                    lambda x: self.set_crowd2(keyword=str(x['人群名字']), as_file=False) if x['人群分类'] == ''
                    else x['人群分类'], axis=1
                )
            else:
                df['人群分类'] = df['人群名字'].apply(lambda x: self.set_crowd(keyword=str(x), as_file=False))
                df['人群分类'] = df.apply(
                    lambda x: self.set_crowd2(keyword=str(x['人群名字']), as_file=False) if x['人群分类'] == ''
                    else x['人群分类'], axis=1
                )
            df['人群分类'] = df['人群分类'].apply(lambda x: str(x).upper() if x else x)
            # df.to_csv('/Users/xigua/Downloads/test_人群分类.csv', index=False, header=True, encoding='utf-8_sig')
            # breakpoint()
            return df

        elif '天猫_关键词报表' in table_name:
            df.rename(columns={
                '场景名字': '营销场景',
                '宝贝id': '商品id',
                '总购物车数': '加购量',
                '总成交笔数': '成交笔数',
                '总成交金额': '成交金额'
            }, inplace=True)
            df.fillna(0, inplace=True)
            df = df.astype({
                '商品id': str,
                '花费': float,
                '展现量': int,
                '点击量': int,
                '加购量': int,
                '成交笔数': int,
                '成交金额': float,
                '直接成交笔数': int,
                '直接成交金额': float,
            }, errors='raise')
            if is_maximize:
                df = df.groupby(['日期', '营销场景', '商品id', '词类型', '词名字/词包名字', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{'加购量': ('加购量', np.max),
                       '成交笔数': ('成交笔数', np.max),
                       '成交金额': ('成交金额', np.max),
                       '直接成交笔数': ('直接成交笔数', np.max),
                       '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            else:
                df = df.groupby(['日期', '营销场景', '商品id', '词类型', '词名字/词包名字', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{
                        '加购量': ('加购量', np.min),
                        '成交笔数': ('成交笔数', np.min),
                        '成交金额': ('成交金额', np.min),
                        '直接成交笔数': ('直接成交笔数', np.max),
                        '直接成交金额': ('直接成交金额', np.max)
                       }
                )
            df.insert(loc=1, column='推广渠道', value='万相台无界版')  # df中插入新列
            df['是否品牌词'] = df['词名字/词包名字'].str.contains('万里马|wanlima', regex=True)
            df['是否品牌词'] = df['是否品牌词'].apply(lambda x: '品牌词' if x else '')
            dir_file = f'\\\\192.168.1.198\\时尚事业部\\01.运营部\\0-电商周报-每周五更新\\分类配置文件.xlsx'
            dir_file2 = '/Volumes/时尚事业部/01.运营部/0-电商周报-每周五更新/分类配置文件.xlsx'
            if not os.path.isfile(dir_file):
                dir_file = dir_file2
            if os.path.isfile(dir_file):
                df_fl = pd.read_excel(dir_file, sheet_name='关键词分类', header=0)
                # df_fl.rename(columns={'分类1': '词分类'}, inplace=True)
                df_fl = df_fl[['关键词', '词分类']]
                # 合并并获取词分类信息
                df = pd.merge(df, df_fl, left_on=['词名字/词包名字'], right_on=['关键词'], how='left')
                df.pop('关键词')
                df['词分类'].fillna('', inplace=True)
            if '词分类' in df.columns.tolist():
                # 这行决定了，从文件中读取的词分类信息优先级高于 ret_keyword 函数的词分类
                df['词分类'] = df.apply(
                    lambda x: self.ret_keyword(keyword=str(x['词名字/词包名字']), as_file=False) if x['词分类'] == ''
                    else x['词分类'], axis=1
                )
            else:
                df['词分类'] = df['词名字/词包名字'].apply(lambda x: self.ret_keyword(keyword=str(x), as_file=False))
            # df.to_csv('/Users/xigua/Downloads/test.csv', index=False, header=True, encoding='utf-8_sig')
            # breakpoint()
            return df
        elif '天猫_超级直播' in table_name:
            df.rename(columns={
                '观看次数': '观看次数',
                '总购物车数': '加购量',
                '总成交笔数': '成交笔数',
                '总成交金额': '成交金额',
                '场景名字': '营销场景',
            }, inplace=True)
            df['营销场景'] = '超级直播'
            df.fillna(0, inplace=True)
            df = df.astype({
                '花费': float,
                # '点击量': int,
                '加购量': int,
                '成交笔数': int,
                '成交金额': float,
                '进店量': int,
                '粉丝关注量': int,
                '观看次数': int,
            }, errors='raise')
            if is_maximize:
                df = df.groupby(['日期', '营销场景', '人群名字', '计划名字', '花费', '观看次数', '展现量'],
                                as_index=False).agg(
                    **{
                        '进店量': ('进店量', np.max),
                        '粉丝关注量': ('粉丝关注量', np.max),
                        '加购量': ('加购量', np.max),
                        '成交笔数': ('成交笔数', np.max),
                        '成交金额': ('成交金额', np.max),
                        '直接成交笔数': ('直接成交笔数', np.max),
                        '直接成交金额': ('直接成交金额', np.max),
                       }
                )
            else:
                df = df.groupby(['日期', '营销场景', '人群名字', '计划名字', '花费', '观看次数', '展现量'],
                                as_index=False).agg(
                    **{
                        '进店量': ('进店量', np.min),
                        '粉丝关注量': ('粉丝关注量', np.min),
                        '加购量': ('加购量', np.min),
                        '成交笔数': ('成交笔数', np.min),
                        '成交金额': ('成交金额', np.min),
                        '直接成交笔数': ('直接成交笔数', np.min),
                        '直接成交金额': ('直接成交金额', np.min),
                    }
                )
            df.insert(loc=1, column='推广渠道', value='万相台无界版')  # df中插入新列
            # df.insert(loc=2, column='营销场景', value='超级直播')  # df中插入新列
            # df = df.loc[df['日期'].between(start_day, today)]
            df_new = df.groupby(['日期', '推广渠道', '营销场景'], as_index=False).agg(
                **{
                    '花费': ('花费', np.sum),
                    '展现量': ('展现量', np.sum),
                    '观看次数': ('观看次数', np.sum),
                    '加购量': ('加购量', np.sum),
                    '成交笔数': ('成交笔数', np.sum),
                    '成交金额': ('成交金额', np.sum),
                    '直接成交笔数': ('直接成交笔数', np.sum),
                    '直接成交金额': ('直接成交金额', np.sum),
                }
            )
            self.data_tgyj.update(
                {
                    table_name: df_new,
                }
            )
            return df
        elif '天猫_品销宝账户报表' in table_name:
            df = df[df['报表类型'] == '账户']
            df.fillna(value=0, inplace=True)
            df.rename(columns={
                '消耗': '花费',
                '宝贝加购数': '加购量',
                '搜索量': '品牌搜索量',
                '搜索访客数': '品牌搜索人数'
            }, inplace=True)
            df = df.astype({
                '花费': float,
                '展现量': int,
                '点击量': int,
                '加购量': int,
                '成交笔数': int,
                '成交金额': float,
                '品牌搜索量': int,
                '品牌搜索人数': int,
            }, errors='raise')
            if is_maximize:
                df = df.groupby(['日期', '报表类型', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{
                        '加购量': ('加购量', np.max),
                        '成交笔数': ('成交笔数', np.max),
                        '成交金额': ('成交金额', np.max),
                        '品牌搜索量': ('品牌搜索量', np.max),
                        '品牌搜索人数': ('品牌搜索人数', np.max),
                       }
                )
            else:
                df = df.groupby(['日期', '报表类型', '花费', '展现量', '点击量'], as_index=False).agg(
                    **{
                        '加购量': ('加购量', np.min),
                        '成交笔数': ('成交笔数', np.min),
                        '成交金额': ('成交金额', np.min),
                        '品牌搜索量': ('品牌搜索量', np.min),
                        '品牌搜索人数': ('品牌搜索人数', np.min),
                       }
                )
            df.insert(loc=1, column='推广渠道', value='品销宝')  # df中插入新列
            df.insert(loc=2, column='营销场景', value='品销宝')  # df中插入新列
            df_new = df.groupby(['日期', '推广渠道', '营销场景'], as_index=False).agg(
                **{
                    '花费': ('花费', np.sum),
                    '展现量': ('展现量', np.sum),
                    '点击量': ('点击量', np.sum),
                    '加购量': ('加购量', np.sum),
                    '成交笔数': ('成交笔数', np.sum),
                    '成交金额': ('成交金额', np.sum)
                }
            )
            self.data_tgyj.update(
                {
                    table_name: df_new,
                }
            )
            return df
        elif '宝贝指标' in table_name:
            """ 聚合时不可以加商家编码，编码有些是空白，有些是 0 """
            df['宝贝id'] = df['宝贝id'].astype(str)
            df.fillna(0, inplace=True)
            # df = df[(df['销售额'] != 0) | (df['退款额'] != 0)]  # 注释掉, 因为后续使用生意经作为基准合并推广表，需确保所有商品id 齐全
            df = df.groupby(['日期', '宝贝id', '行业类目'], as_index=False).agg(
                **{'销售额': ('销售额', np.min),
                   '销售量': ('销售量', np.min),
                   '订单数': ('订单数', np.min),
                   '退货量': ('退货量', np.max),
                   '退款额': ('退款额', np.max),
                   '退款额（发货后）': ('退款额（发货后）', np.max),
                   '退货量（发货后）': ('退货量（发货后）', np.max),
                   }
            )
            df['件均价'] = df.apply(lambda x: x['销售额'] / x['销售量'] if x['销售量'] > 0 else 0, axis=1).round(
                0)  # 两列运算, 避免除以0
            df['价格带'] = df['件均价'].apply(
                lambda x: '2000+' if x >= 2000
                else '1000+' if x >= 1000
                else '500+' if x >= 500
                else '300+' if x >= 300
                else '300以下'
            )
            self.data_tgyj.update(
                {
                    table_name: df[['日期', '宝贝id', '销售额', '销售量', '退款额（发货后）', '退货量（发货后）']],
                }
            )
            return df
        elif '店铺来源_日数据' in table_name and '旧版' not in table_name:
            # 包含三级来源名称和预设索引值列
            # 截取 从上月1日 至 今天的花费数据, 推广款式按此数据从高到低排序（商品图+排序）
            df_visitor3 = df.groupby(['日期', '三级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor3 = df_visitor3[~df_visitor3['三级来源'].isin([''])]  # 指定列中删除包含空值的行
            # df_visitor = df_visitor[(df_visitor['日期'] >= f'{year_my}-{last_month.month}-01')]
            df_visitor3 = df_visitor3.groupby(['三级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor3.sort_values('访客数', ascending=False, ignore_index=True, inplace=True)
            df_visitor3.reset_index(inplace=True)
            df_visitor3['index'] = df_visitor3['index'] + 100
            df_visitor3.rename(columns={'index': '三级访客索引'}, inplace=True)
            df_visitor3 = df_visitor3[['三级来源', '三级访客索引']]

            # 包含二级来源名称和预设索引值列
            df_visitor2 = df.groupby(['日期', '二级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor2 = df_visitor2[~df_visitor2['二级来源'].isin([''])]  # 指定列中删除包含空值的行
            # df_visitor2 = df_visitor2[(df_visitor2['日期'] >= f'{year_my}-{last_month.month}-01')]
            df_visitor2 = df_visitor2.groupby(['二级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor2.sort_values('访客数', ascending=False, ignore_index=True, inplace=True)
            df_visitor2.reset_index(inplace=True)
            df_visitor2['index'] = df_visitor2['index'] + 100
            df_visitor2.rename(columns={'index': '二级访客索引'}, inplace=True)
            df_visitor2 = df_visitor2[['二级来源', '二级访客索引']]

            df = pd.merge(df, df_visitor2, how='left', left_on='二级来源', right_on='二级来源')
            df = pd.merge(df, df_visitor3, how='left', left_on='三级来源', right_on='三级来源')
            return df
        elif '天猫_店铺来源_日数据_旧版' in table_name:

            # 包含三级来源名称和预设索引值列
            # 截取 从上月1日 至 今天的花费数据, 推广款式按此数据从高到低排序（商品图+排序）
            df_visitor3 = df.groupby(['日期', '三级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor3 = df_visitor3[~df_visitor3['三级来源'].isin([''])]  # 指定列中删除包含空值的行
            # df_visitor = df_visitor[(df_visitor['日期'] >= f'{year_my}-{last_month.month}-01')]
            df_visitor3 = df_visitor3.groupby(['三级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor3.sort_values('访客数', ascending=False, ignore_index=True, inplace=True)
            df_visitor3.reset_index(inplace=True)
            df_visitor3['index'] = df_visitor3['index'] + 100
            df_visitor3.rename(columns={'index': '三级访客索引'}, inplace=True)
            df_visitor3 = df_visitor3[['三级来源', '三级访客索引']]

            # 包含二级来源名称和预设索引值列
            df_visitor2 = df.groupby(['日期', '二级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor2 = df_visitor2[~df_visitor2['二级来源'].isin([''])]  # 指定列中删除包含空值的行
            # df_visitor2 = df_visitor2[(df_visitor2['日期'] >= f'{year_my}-{last_month.month}-01')]
            df_visitor2 = df_visitor2.groupby(['二级来源'], as_index=False).agg({'访客数': 'sum'})
            df_visitor2.sort_values('访客数', ascending=False, ignore_index=True, inplace=True)
            df_visitor2.reset_index(inplace=True)
            df_visitor2['index'] = df_visitor2['index'] + 100
            df_visitor2.rename(columns={'index': '二级访客索引'}, inplace=True)
            df_visitor2 = df_visitor2[['二级来源', '二级访客索引']]

            df = pd.merge(df, df_visitor2, how='left', left_on='二级来源', right_on='二级来源')
            df = pd.merge(df, df_visitor3, how='left', left_on='三级来源', right_on='三级来源')
            return df
        elif '商品id编码表' in table_name:
            df['宝贝id'] = df['宝贝id'].astype(str)
            df.drop_duplicates(subset='宝贝id', keep='last', inplace=True, ignore_index=True)
            # df['行业类目'] = df['行业类目'].apply(lambda x: re.sub(' ', '', x))
            try:
                df[['一级类目', '二级类目', '三级类目']] = df['行业类目'].str.split(' -> ', expand=True).loc[:, 0:2]
            except:
                try:
                    df[['一级类目', '二级类目']] = df['行业类目'].str.split(' -> ', expand=True).loc[:, 0:1]
                except:
                    df['一级类目'] = df['行业类目']
            df.drop('行业类目', axis=1, inplace=True)
            df.sort_values('宝贝id', ascending=False, inplace=True)
            df = df[(df['宝贝id'] != '973') & (df['宝贝id'] != '973')]
            self.data_tgyj.update(
                {
                    table_name: df[['宝贝id', '商家编码']],
                }
            )
            return df
        elif '商品id图片对照表' in table_name:
            df['商品id'] = df['商品id'].astype('int64')
            df['日期'] = df['日期'].astype('datetime64[ns]')
            df = df[(df['商品白底图'] != '0') | (df['方版场景图'] != '0')]
            # 白底图优先
            df['商品图片'] = df[['商品白底图', '方版场景图']].apply(
                lambda x: x['商品白底图'] if x['商品白底图'] !='0' else x['方版场景图'], axis=1)
            # # 方版场景图优先
            # df['商品图片'] = df[['商品白底图', '方版场景图']].apply(
            #     lambda x: x['方版场景图'] if x['方版场景图'] != '0' else x['商品白底图'], axis=1)
            df.sort_values(by=['商品id', '日期'], ascending=[False, True], ignore_index=True, inplace=True)
            df.drop_duplicates(subset=['商品id'], keep='last', inplace=True, ignore_index=True)
            df = df[['商品id', '商品图片', '日期']]
            df['商品图片'] = df['商品图片'].apply(lambda x: x if 'http' in x else None)  # 检查是否是 http 链接
            df.dropna(how='all', subset=['商品图片'], axis=0, inplace=True)  # 删除指定列含有空值的行
            df['商品链接'] = df['商品id'].apply(
                lambda x: f'https://detail.tmall.com/item.htm?id={str(x)}' if x and '.com' not in str(x) else x)
            df.sort_values(by='商品id', ascending=False, ignore_index=True, inplace=True)  # ascending=False 降序排列
            self.data_tgyj.update(
                {
                    table_name: df[['商品id', '商品图片']],
                }
            )
            df['商品id'] = df['商品id'].astype(str)
            return df
        elif '商品成本' in table_name:
            df.sort_values(by=['款号', '日期'], ascending=[False, True], ignore_index=True, inplace=True)
            df.drop_duplicates(subset=['款号'], keep='last', inplace=True, ignore_index=True)
            self.data_tgyj.update(
                {
                    table_name: df[['款号', '成本价']],
                }
            )
            return df
        elif '京东_京准通' in table_name and '全站营销' not in table_name:
            df = df.groupby(['日期', '产品线', '触发sku id', '跟单sku id', 'spu id', '花费', '展现数', '点击数'], as_index=False).agg(
                **{'直接订单行': ('直接订单行', np.max),
                   '直接订单金额': ('直接订单金额', np.max),
                   '总订单行': ('总订单行', np.max),
                   '总订单金额': ('总订单金额', np.max),
                   '直接加购数': ('直接加购数', np.max),
                   '总加购数': ('总加购数', np.max),
                   }
            )
            df = df[df['花费'] > 0]
            self.data_jdtg.update(
                {
                    table_name: df[['日期', '产品线', '触发sku id', '跟单sku id', '花费']],
                }
            )
            return df
        elif '京东_京准通_全站营销' in table_name:
            df = df.groupby(['日期', '产品线', '花费'], as_index=False).agg(
                **{'全站roi': ('全站roi', np.max),
                   '全站交易额': ('全站交易额', np.max),
                   '全站订单行': ('全站订单行', np.max),
                   '全站订单成本': ('全站订单成本', np.max),
                   '全站费比': ('全站费比', np.max),
                   '核心位置展现量': ('核心位置展现量', np.max),
                   '核心位置点击量': ('核心位置点击量', np.max),
                   }
            )
            df = df[df['花费'] > 0]
            return df
        elif '京东_sku_商品明细' in table_name:
            df = df[df['商品id'] != '合计']
            df = df.groupby(['日期', '商品id', '货号', '访客数', '成交客户数', '加购商品件数', '加购人数'],
                            as_index=False).agg(
                **{
                    '成交单量': ('成交单量', np.max),
                    '成交金额': ('成交金额', np.max),
                   }
            )
            self.data_jdtg.update(
                {
                    table_name: df,
                }
            )
            return df
        elif '京东_spu_商品明细' in table_name:
            df = df[df['商品id'] != '合计']
            df = df.groupby(['日期', '商品id', '货号', '访客数', '成交客户数', '加购商品件数', '加购人数'],
                            as_index=False).agg(
                **{
                    '成交单量': ('成交单量', np.max),
                    '成交金额': ('成交金额', np.max),
                   }
            )
            self.data_jdtg.update(
                {
                    table_name: df,
                }
            )
            return df
        elif '京东_关键词报表' in table_name:
            df_lin = df[['计划id', '推广计划']]
            df_lin.drop_duplicates(subset=['计划id'], keep='last', inplace=True, ignore_index=True)
            df = df.groupby(['日期', '产品线', '计划类型', '计划id', '搜索词', '关键词', '关键词购买类型', '广告定向类型', '展现数', '点击数', '花费'],
                            as_index=False).agg(
                **{
                    '直接订单行': ('直接订单行', np.max),
                    '直接订单金额': ('直接订单金额', np.max),
                    '总订单行': ('总订单行', np.max),
                    '总订单金额': ('总订单金额', np.max),
                    '总加购数': ('总加购数', np.max),
                    '下单新客数': ('下单新客数_去重', np.max),
                    '领券数': ('领券数', np.max),
                    '商品关注数': ('商品关注数', np.max),
                    '店铺关注数': ('店铺关注数', np.max)
                }
            )
            df = pd.merge(df, df_lin, how='left', left_on='计划id', right_on='计划id')
            df['k_是否品牌词'] = df['关键词'].str.contains('万里马|wanlima', regex=True)
            df['k_是否品牌词'] = df['k_是否品牌词'].apply(lambda x: '品牌词' if x else '')
            df['s_是否品牌词'] = df['搜索词'].str.contains('万里马|wanlima', regex=True)
            df['s_是否品牌词'] = df['s_是否品牌词'].apply(lambda x: '品牌词' if x else '')
            return df
        elif '天猫店铺来源_手淘搜索' in table_name:
            df = df.groupby(
                ['日期', '关键词'],
                as_index=False).agg(
                **{
                    '访客数': ('访客数', np.max),
                    '支付转化率': ('支付转化率', np.max),
                    '支付金额': ('支付金额', np.max),
                    '下单金额': ('下单金额', np.max),
                    '支付买家数': ('支付买家数', np.max),
                    '下单买家数': ('下单买家数', np.max),
                    '加购人数': ('加购人数', np.max),
                    '新访客': ('新访客', np.max),
                }
            )
            return df
        elif '直播场次分析' in table_name:
            df.drop_duplicates(subset=['场次id'], keep='first', inplace=True, ignore_index=True)
            return df
        elif '多店推广场景_按日聚合' in table_name:
            df = df.groupby(
                ['日期', '店铺', '营销场景'],
                as_index=False).agg(
                **{
                    '花费': ('花费', np.sum),
                    '展现量': ('展现量', np.sum),
                    '点击量': ('点击量', np.sum),
                    '加购量': ('加购量', np.sum),
                    '成交笔数': ('成交笔数', np.sum),
                    '成交金额': ('成交金额', np.sum)
                }
            )
            df.sort_values(['日期', '店铺', '花费'], ascending=[False, False, False], ignore_index=True, inplace=True)
            # df.to_csv('/Users/xigua/Downloads/test.csv', encoding='utf-8_sig', index=False, header=True)
            return df
        elif '达摩盘_人群报表' in table_name:
            return df

        else:
            print(f'<{table_name}>: Groupby 类尚未配置，数据为空')
            return pd.DataFrame({})

    def ret_keyword(self, keyword, as_file=False):
        """ 推广关键词报表，关键词分类， """
        datas = [
            {
                '类别': '品牌词',
                '值': [
                    '万里马',
                    'wanlima',
                    'fion',
                    '菲安妮',
                    '迪桑娜',
                    'dissona',
                    'hr',
                    'vh',
                    'songmont',
                    'vanessahogan',
                    'dilaks',
                    'khdesign',
                    'peco',
                    'giimmii',
                    'cassile',
                    'grotto',
                    'why',
                    'roulis',
                    'lesschic',
                    'amazing song',
                    'mytaste',
                    'bagtree',
                    '红谷',
                    'hongu',
                ]
            },
            {
                '类别': '智选',
                '值': [
                    '智选',
                ]
            },
            {
                '类别': '智能',
                '值': [
                    '智能',
                ]
            },
            {
                '类别': '年份',
                '值': [
                    '20',
                ]
            },
            {
                '类别': '材质',
                '值': [
                    '皮',
                    '牛仔',
                    '丹宁',
                    '帆布',
                ]
            },
            {
                '类别': '季节',
                '值': [
                    '春',
                    '夏',
                    '秋',
                    '冬',
                ]
            },
            {
                '类别': '一键起量',
                '值': [
                    '一键起量',
                ]
            },
            {
                '类别': '款式',
                '值': [
                    '水桶',
                    '托特',
                    '腋下',
                    '小方',
                    '通用款',
                    '手拿',
                    '马鞍',
                    '链条',
                    '菜篮',
                    'hobo',
                    '波士顿',
                    '凯莉',
                    '饺子',
                    '盒子',
                    '牛角',
                    '公文',
                    '月牙',
                    '单肩',
                    '枕头',
                    '斜挎',
                    '手提',
                    '手拎',
                    '拎手',
                    '斜肩',
                    '棒球',
                    '饺包',
                    '保龄球',
                    '戴妃',
                    '半月',
                    '弯月',
                    '法棍',
                    '流浪',
                    '拎包',
                    '中式',
                    '手挽',
                    '皮带',
                    '眼镜',
                    '斜跨',
                    '律师',
                    '斜背',
                ]
            },
            {
                '类别': '品类词',
                '值': [
                    '老花',
                    '包包',
                    '通勤',
                    '轻奢',
                    '包',
                    '新款',
                    '小众',
                    '爆款',
                    '工作',
                    '精致',
                    '奢侈',
                    '袋',
                    '腰带',
                    '裤带',
                    '女士',
                    '复古',
                    '高级',
                    '容量',
                    '时尚',
                    '商务',
                ],
            },
        ]
        if as_file:
            with open(os.path.join(self.output, f'分类配置.json'), 'w') as f:
                json.dump(datas, f, ensure_ascii=False, sort_keys=False, indent=4)
            breakpoint()
        result = ''
        res = []
        is_continue = False
        for data in datas:
            for item in data['值']:
                if item == '20':
                    pattern = r'\d\d'
                    res = re.findall(f'{item}{pattern}', str(keyword), re.IGNORECASE)
                else:
                    res = re.findall(item, str(keyword), re.IGNORECASE)
                if res:
                    result = data['类别']
                    is_continue = True
                    break
            if is_continue:
                break
        return result

    def set_crowd(self, keyword, as_file=False):
        """ 推广人群报表，人群分类， """
        result_a = re.findall('_a$|_a_|_ai|^a_', str(keyword), re.IGNORECASE)
        result_i = re.findall('_i$|_i_|^i_', str(keyword), re.IGNORECASE)
        result_p = re.findall('_p$|_p_|_pl|^p_||^pl_', str(keyword), re.IGNORECASE)
        result_l = re.findall('_l$|_l_|^l_', str(keyword), re.IGNORECASE)

        datas = [
            {
                '类别': 'A',
                '值': result_a,
            },
            {
                '类别': 'I',
                '值': result_i,
            },
            {
                '类别': 'P',
                '值': result_p,
            },
            {
                '类别': 'L',
                '值': result_l,
            }
        ]

        is_res = False
        for data in datas:
            if data['值']:
                data['值'] = [item for item in data['值'] if item != '']
                if data['值']:
                    return data['类别']
        if not is_res:
            return ''

    def set_crowd2(self, keyword, as_file=False):
        """ 推广人群报表，人群分类， """
        datas = [
            {
                '类别': 'A',
                '值': [
                    '相似宝贝',
                    '相似店铺',
                    '类目',
                    '88VIP',
                    '拉新',
                    '潮流',
                    '会场',
                    '意向',
                    '>>',  # 系统推荐的搜索相关人群
                    '关键词：',  # 系统推荐的搜索相关人群
                    '关键词_',  # 自建的搜索相关人群
                    '扩展',
                    '敏感人群',
                    '尝鲜',
                    '小二推荐',
                    '竞争',
                    '资深',
                    '女王节',
                    '本行业',
                    '618',
                    '包包树',
                    '迪桑娜',
                    '菲安妮',
                    '卡思乐',
                    '场景词',
                    '竞对',
                    '精选',
                    '发现',
                    '行业mvp'
                    '特征继承',
                    '机会',
                    '推荐',
                    '智能定向',
                ]
            },
            {
                '类别': 'I',
                '值': [
                    '行动',
                    '收加',
                    '收藏',
                    '加购',
                    '促首购',
                    '店铺优惠券',
                    '高转化',
                    '认知',
                    '喜欢我',  # 系统推荐宝贝/店铺访问相关人群
                    '未购买',
                    '种草',
                    '兴趣',
                    '本店',
                    '领券',
                ]
            },
            {
                '类别': 'P',
                '值': [
                    '万里马',
                    '购买',
                    '已购',
                    '促复购'
                    '店铺会员',
                    '店铺粉丝',
                    '转化',
                ]
            },
            {
                '类别': 'L',
                '值': [
                    'L人群',
                ]
            },
        ]
        if as_file:
            with open(os.path.join(self.output, f'分类配置_推广人群分类_函数内置规则.json'), 'w') as f:
                json.dump(datas, f, ensure_ascii=False, sort_keys=False, indent=4)
            breakpoint()
        result = ''
        res = []
        is_continue = False
        for data in datas:
            for item in data['值']:
                res = re.findall(item, str(keyword), re.IGNORECASE)
                if res:
                    result = data['类别']
                    is_continue = True
                    break
            if is_continue:
                break
        return result

    # @try_except
    def performance(self, bb_tg=True):
         # print(self.data_tgyj)
        tg, syj, idbm, pic, cost = (
            self.data_tgyj['天猫_主体报表'],
            self.data_tgyj['天猫生意经_宝贝指标'],
            self.data_tgyj['商品id编码表'],
            self.data_tgyj['商品id图片对照表'],
            self.data_tgyj['商品成本'])  # 这里不要加逗号
        pic['商品id'] = pic['商品id'].astype(str)
        df = pd.merge(idbm, pic, how='left', left_on='宝贝id', right_on='商品id')  # id 编码表合并图片表
        df = df[['宝贝id', '商家编码', '商品图片']]
        df = pd.merge(df, cost, how='left', left_on='商家编码', right_on='款号')  # df 合并商品成本表
        df = df[['宝贝id', '商家编码', '商品图片', '成本价']]
        df = pd.merge(tg, df, how='left', left_on='商品id', right_on='宝贝id')  # 推广表合并 df
        df.drop(labels='宝贝id', axis=1, inplace=True)
        if bb_tg is True:
            # 生意经合并推广表，完整的数据表，包含全店所有推广、销售数据
            df = pd.merge(syj, df, how='left', left_on=['日期', '宝贝id'], right_on=['日期', '商品id'])
            df.drop(labels='商品id', axis=1, inplace=True)  # 因为生意经中的宝贝 id 列才是完整的
            df.rename(columns={'宝贝id': '商品id'}, inplace=True)
            # df.to_csv('/Users/xigua/Downloads/test.csv', encoding='utf-8_sig', index=False, header=True)
        else:
            # 推广表合并生意经 , 以推广数据为基准，销售数据不齐全
            df = pd.merge(df, syj, how='left', left_on=['日期', '商品id'], right_on=['日期', '宝贝id'])
            df.drop(labels='宝贝id', axis=1, inplace=True)
        df.drop_duplicates(subset=['日期', '商品id', '花费', '销售额'], keep='last', inplace=True, ignore_index=True)
        df.fillna(0, inplace=True)
        df['成本价'] = df['成本价'].astype('float64')
        df['销售额'] = df['销售额'].astype('float64')
        df['销售量'] = df['销售量'].astype('int64')
        df['商品成本'] = df.apply(lambda x: (x['成本价'] + x['销售额']/x['销售量'] * 0.11 + 6) * x['销售量'] if x['销售量'] > 0 else 0, axis=1)
        df['商品毛利'] = df.apply(lambda x: x['销售额'] - x['商品成本'], axis=1)
        df['毛利率'] = df.apply(lambda x: round((x['销售额'] - x['商品成本']) / x['销售额'], 4) if x['销售额'] > 0 else 0, axis=1)
        df['盈亏'] = df.apply(lambda x: x['商品毛利'] - x['花费'], axis=1)
        return df
    def performance_concat(self, bb_tg=True):
        tg,  zb, pxb = self.data_tgyj['天猫汇总表调用'], self.data_tgyj['天猫_超级直播'], self.data_tgyj['天猫_品销宝账户报表']
        zb.rename(columns={
            '观看次数': '点击量',
        }, inplace=True)
        zb.fillna(0, inplace=True)  # astype 之前要填充空值
        tg.fillna(0, inplace=True)
        zb = zb.astype({
            '花费': float,
            '展现量': int,
            '点击量': int,
            '加购量': int,
            '成交笔数': int,
            '成交金额': float,
            '直接成交笔数': int,
            '直接成交金额': float,
        }, errors='raise')
        tg = tg.astype({
            '商品id': str,
            '花费': float,
            '展现量': int,
            '点击量': int,
            '加购量': int,
            '成交笔数': int,
            '成交金额': float,
            '直接成交笔数': int,
            '直接成交金额': float,
            '自然流量曝光量': int,
        }, errors='raise')
        # tg = tg.groupby(['日期', '推广渠道', '营销场景', '商品id', '花费', '展现量', '点击量'], as_index=False).agg(
        #     **{'加购量': ('加购量', np.max),
        #        '成交笔数': ('成交笔数', np.max),
        #        '成交金额': ('成交金额', np.max),
        #        '自然流量曝光量': ('自然流量曝光量', np.max),
        #        '直接成交笔数': ('直接成交笔数', np.max),
        #        '直接成交金额': ('直接成交金额', np.max)
        #        }
        # )
        df = pd.concat([tg, zb, pxb], axis=0, ignore_index=True)
        df.fillna(0, inplace=True)  # concat 之后要填充空值
        df = df.astype(
            {
                '商品id': str,
                '自然流量曝光量': int,
        }
        )
        return df

    def performance_jd(self, jd_tg=True):
        jdtg, sku_sales = self.data_jdtg['京东_京准通'], self.data_jdtg['京东_sku_商品明细']
        jdtg = jdtg.groupby(['日期', '跟单sku id'],
                        as_index=False).agg(
            **{
                '花费': ('花费', np.sum)
            }
        )
        cost = self.data_tgyj['商品成本']
        df = pd.merge(sku_sales, cost, how='left', left_on='货号', right_on='款号')
        df = df[['日期', '商品id', '货号', '成交单量', '成交金额', '成本价']]
        df['商品id'] = df['商品id'].astype(str)
        jdtg['跟单sku id'] = jdtg['跟单sku id'].astype(str)
        if jd_tg is True:
            # 完整的数据表，包含全店所有推广、销售数据
            df = pd.merge(df, jdtg, how='left', left_on=['日期', '商品id'], right_on=['日期', '跟单sku id'])  # df 合并推广表
        else:
            df = pd.merge(jdtg, df, how='left', left_on=['日期', '跟单sku id'], right_on=['日期', '商品id'])  # 推广表合并 df
        df = df[['日期', '跟单sku id', '花费', '货号', '成交单量', '成交金额', '成本价']]
        df.fillna(0, inplace=True)
        df['成本价'] = df['成本价'].astype('float64')
        df['成交金额'] = df['成交金额'].astype('float64')
        df['花费'] = df['花费'].astype('float64')
        df['成交单量'] = df['成交单量'].astype('int64')
        df['商品成本'] = df.apply(
            lambda x: (x['成本价'] + x['成交金额'] / x['成交单量'] * 0.11 + 6) * x['成交单量'] if x['成交单量'] > 0 else 0,
            axis=1)
        df['商品毛利'] = df.apply(lambda x: x['成交金额'] - x['商品成本'], axis=1)
        df['毛利率'] = df.apply(
            lambda x: round((x['成交金额'] - x['商品成本']) / x['成交金额'], 4) if x['成交金额'] > 0 else 0, axis=1)
        df['盈亏'] = df.apply(lambda x: x['商品毛利'] - x['花费'], axis=1)
        return df

    def as_csv(self, df, filename, path=None, encoding='utf-8_sig',
               index=False, header=True, st_ascend=None, ascend=None, freq=None):
        """
        path: 默认导出目录 self.output, 这个函数的 path 作为子文件夹，可以不传，
        st_ascend: 排序参数 ['column1', 'column2']
        ascend: 升降序 [True, False]
        freq: 将创建子文件夹并按月分类存储,  freq='Y', 或 freq='M'
        """
        if len(df) == 0:
            return
        if not path:
            path = self.output
        else:
            path = os.path.join(self.output, path)
        if not os.path.exists(path):
            os.makedirs(path)
        if filename.endswith('.csv'):
            filename = filename[:-4]
        if st_ascend and ascend:
            try:
                df.sort_values(st_ascend, ascending=ascend, ignore_index=True, inplace=True)
            except:
                print(f'{filename}: sort_values排序参数错误！')
        if freq:
            if '日期' not in df.columns.tolist():
                return print(f'{filename}: 数据缺少日期列，无法按日期分组')
            groups = df.groupby(pd.Grouper(key='日期', freq=freq))
            for name1, df in groups:
                if freq == 'M':
                    sheet_name = name1.strftime('%Y-%m')
                elif freq == 'Y':
                    sheet_name = name1.strftime('%Y年')
                else:
                    sheet_name = '_未分类'
                new_path = os.path.join(path, filename)
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                new_path = os.path.join(new_path, f'{filename}{sheet_name}.csv')
                if st_ascend and ascend:  # 这里需要重新排序一次，原因未知
                    try:
                        df.sort_values(st_ascend, ascending=ascend, ignore_index=True, inplace=True)
                    except:
                        print(f'{filename}: sort_values排序参数错误！')

                df.to_csv(new_path, encoding=encoding, index=index, header=header)
        else:
            df.to_csv(os.path.join(path, filename + '.csv'), encoding=encoding, index=index, header=header)

    def as_json(self, df, filename, path=None, orient='records', force_ascii=False, st_ascend=None, ascend=None):
        if len(df) == 0:
            return
        if not path:
            path = self.output
        else:
            path = os.path.join(self.output, path)
        if not os.path.exists(path):
            os.makedirs(path)
        if st_ascend and ascend:
            try:
                df.sort_values(st_ascend, ascending=ascend, ignore_index=True, inplace=True)
            except:
                print(f'{filename}: sort_values排序参数错误！')
        df.to_json(os.path.join(path, filename + '.json'),
                   orient=orient, force_ascii=force_ascii)

    def as_excel(self, df, filename, path=None, index=False, header=True, engine='openpyxl',
                 freeze_panes=(1, 0), st_ascend=None, ascend=None):
        if len(df) == 0:
            return
        if not path:
            path = self.output
        else:
            path = os.path.join(self.output, path)
        if not os.path.exists(path):
            os.makedirs(path)
        if st_ascend and ascend:
            try:
                df.sort_values(st_ascend, ascending=ascend, ignore_index=True, inplace=True)
            except:
                print(f'{filename}: sort_values排序参数错误！')
        df.to_excel(os.path.join(path, filename + '.xlsx'), index=index, header=header, engine=engine, freeze_panes=freeze_panes)
        

def g_group():
    pass


def data_aggregation_one(service_databases=[{}], months=1):
    """
    # 单独处理某一个聚合数据库，修改添加 data_dict 的值
    """
    for service_database in service_databases:
        for service_name, database in service_database.items():
            sdq = MysqlDatasQuery(target_service=service_name)  # 实例化数据处理类
            sdq.months = months  # 设置数据周期， 1 表示近 2 个月
            g = GroupBy()  # 实例化数据聚合类
            # 实例化数据库连接
            username, password, host, port = get_myconf.select_config_values(target_service=service_name, database=database)
            m = mysql.MysqlUpload(username=username, password=password, host=host, port=port)

            # 从数据库中获取数据, 返回包含 df 数据的字典
            # 单独处理某一个聚合数据库，在这里修改添加 data_dict 的值
            ######################################################
            #################    修改这里    ##########################
            ######################################################
            data_dict = [
                {
                    '数据库名': '聚合数据',  # 清洗完回传的目的地数据库
                    '集合名': '天猫_推广汇总',  # 清洗完回传的数据表名
                    '唯一主键': ['日期', '商品id'],
                    '数据主体': sdq.jd_gjc(),
                },
            ]
            ######################################################
            #################    修改这里    ##########################
            ######################################################

            for items in data_dict:  # 遍历返回结果
                db_name, table_name, unique_key_list, df = items['数据库名'], items['集合名'], items['唯一主键'], items['数据主体']
                df = g.groupby(df=df, table_name=table_name, is_maximize=True)  # 2. 聚合数据
                # g.as_csv(df=df, filename=table_name + '.csv')  # 导出 csv
                m.df_to_mysql(
                    df=df,
                    db_name=db_name,
                    table_name=table_name,
                    move_insert=False,  # 先删除，再插入
                    df_sql=True,
                    drop_duplicates=False,
                    # icm_update=unique_key_list,
                    service_database=service_database,
                )  # 3. 回传数据库


def data_aggregation(service_databases=[{}], months=1, is_juhe=True):
    """
    1. 从数据库中读取数据
    2. 数据聚合清洗
    3. 统一回传数据库: <聚合数据>  （不再导出为文件）
    公司台式机调用
    """
    for service_database in service_databases:
        for service_name, database in service_database.items():
            sdq = MysqlDatasQuery(target_service=service_name)  # 实例化数据处理类
            sdq.months = months  # 设置数据周期， 1 表示近 2 个月
            g = GroupBy()  # 实例化数据聚合类
            # 实例化数据库连接
            username, password, host, port = get_myconf.select_config_values(target_service=service_name, database=database)
            m = mysql.MysqlUpload(username=username, password=password, host=host, port=port)

            # 从数据库中获取数据, 返回包含 df 数据的字典
            data_dict = [
                # {
                #     '数据库名': '聚合数据',  # 清洗完回传的目的地数据库
                #     '集合名': '天猫_主体报表',  # 清洗完回传的数据表名
                #     '唯一主键': ['日期', '推广渠道', '营销场景', '商品id', '花费'],
                #     '数据主体': sdq.tg_wxt(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫生意经_宝贝指标',
                #     '唯一主键': ['日期', '宝贝id'],  # 不能加其他字段做主键，比如销售额，是变动的，不是唯一的
                #     '数据主体': sdq.syj(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_店铺来源_日数据',
                #     '唯一主键': ['日期', '一级来源', '二级来源', '三级来源', '访客数'],
                #     '数据主体': sdq.dplyd(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_店铺来源_日数据_旧版',
                #     '唯一主键': ['日期', '一级来源', '二级来源', '三级来源'],
                #     '数据主体': sdq.dplyd_old(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '商品id编码表',
                #     '唯一主键': ['宝贝id'],
                #     '数据主体': sdq.idbm(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '商品id图片对照表',
                #     '唯一主键': ['商品id'],
                #     '数据主体': sdq.sp_picture(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '商品成本',
                #     '唯一主键': ['款号'],
                #     '数据主体': sdq.sp_cost(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '京东_京准通',
                #     '唯一主键': ['日期', '产品线', '触发sku id', '跟单sku id', '花费', ],
                #     '数据主体': sdq.jdjzt(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '京东_京准通_全站营销',
                #     '唯一主键': ['日期', '产品线', '花费'],
                #     '数据主体': sdq.jdqzyx(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '京东_sku_商品明细',
                #     '唯一主键': ['日期', '商品id', '成交单量'],
                #     '数据主体': sdq.sku_sales(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '京东_spu_商品明细',
                #     '唯一主键': ['日期', '商品id', '成交单量'],
                #     '数据主体': sdq.spu_sales(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_人群报表',
                #     '唯一主键': ['日期', '推广渠道', '营销场景', '商品id', '花费', '人群名字'],
                #     '数据主体': sdq.tg_rqbb(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_关键词报表',
                #     '唯一主键': ['日期', '推广渠道', '营销场景', '商品id', '花费', '词类型', '词名字/词包名字',],
                #     '数据主体': sdq.tg_gjc(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_超级直播',
                #     '唯一主键': ['日期', '推广渠道', '营销场景', '花费'],
                #     '数据主体': sdq.tg_cjzb(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '京东_关键词报表',
                #     '唯一主键': ['日期', '产品线', '搜索词',  '关键词', '展现数', '花费'],
                #     '数据主体': sdq.jd_gjc(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫_品销宝账户报表',
                #     '唯一主键': ['日期', '报表类型', '推广渠道', '营销场景', '花费'],
                #     '数据主体': sdq.pxb_zh(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '天猫店铺来源_手淘搜索',
                #     '唯一主键': ['日期', '关键词', '访客数'],
                #     '数据主体': sdq.tm_search(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '生意参谋_直播场次分析',
                #     '唯一主键': ['场次id'],
                #     '数据主体': sdq.zb_ccfx(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '多店推广场景_按日聚合',
                #     '唯一主键': [],
                #     '数据主体': sdq.tg_by_day(),
                # },
                # {
                #     '数据库名': '聚合数据',
                #     '集合名': '爱库存_商品spu榜单',
                #     '唯一主键': [],
                #     '数据主体': sdq.aikucun_bd_spu(),
                # },
                {
                    '数据库名': '聚合数据',
                    '集合名': '达摩盘_人群报表',
                    '唯一主键': [],
                    '数据主体': sdq.dmp_crowd(),
                },
            ]
            for items in data_dict:  # 遍历返回结果
                db_name, table_name, unique_key_list, df = items['数据库名'], items['集合名'], items['唯一主键'], items['数据主体']
                df = g.groupby(df=df, table_name=table_name, is_maximize=True)  # 2. 聚合数据
                if len(g.sp_index_datas) != 0:
                    # 由推广主体报表，写入一个商品索引表，索引规则：从上月 1 号至今花费从高到低排序
                    m.df_to_mysql(
                        df=g.sp_index_datas,
                        db_name='属性设置2',
                        table_name='商品索引表',
                        move_insert=False,  # 先删除，再插入
                        # df_sql=True,
                        drop_duplicates=False,
                        icm_update=['商品id'],
                        service_database=service_database,
                    )
                    g.sp_index_datas = pd.DataFrame()  # 重置，不然下个循环会继续刷入数据库
                # # g.as_csv(df=df, filename=table_name + '.csv')  # 导出 csv
                if '日期' in df.columns.tolist():
                    m.df_to_mysql(
                        df=df,
                        db_name=db_name,
                        table_name=table_name,
                        move_insert=True,  # 先删除，再插入
                        # df_sql=True,
                        # drop_duplicates=False,
                        # icm_update=unique_key_list,
                        service_database=service_database,
                    )  # 3. 回传数据库
                else:  # 没有日期列的就用主键排重
                    m.df_to_mysql(
                        df=df,
                        db_name=db_name,
                        table_name=table_name,
                        move_insert=False,  # 先删除，再插入
                        # df_sql=True,
                        drop_duplicates=False,
                        icm_update=unique_key_list,
                        service_database=service_database,
                    )  # 3. 回传数据库
            if is_juhe:
                res = g.performance(bb_tg=True)   # 盈亏表，依赖其他表，单独做
                m.df_to_mysql(
                    df=res,
                    db_name='聚合数据',
                    table_name='_全店商品销售',
                    move_insert=True,  # 先删除，再插入
                    # df_sql=True,
                    # drop_duplicates=False,
                    # icm_update=['日期', '商品id'],  # 设置唯一主键
                    service_database=service_database,
                )
                res = g.performance(bb_tg=False)  # 盈亏表，依赖其他表，单独做
                m.df_to_mysql(
                    df=res,
                    db_name='聚合数据',
                    table_name='_推广商品销售',
                    move_insert=True,  # 先删除，再插入
                    # df_sql=True,
                    # drop_duplicates=False,
                    # icm_update=['日期', '商品id'],  # 设置唯一主键
                    service_database=service_database,
                )
                res = g.performance_concat(bb_tg=False)  # 推广主体合并直播表，依赖其他表，单独做
                m.df_to_mysql(
                    df=res,
                    db_name='聚合数据',
                    table_name='天猫_推广汇总',
                    move_insert=True,  # 先删除，再插入
                    # df_sql=True,
                    # drop_duplicates=False,
                    # icm_update=['日期', '推广渠道', '营销场景', '商品id', '花费', '展现量', '点击量'],  # 设置唯一主键
                    service_database=service_database,
                )
                res = g.performance_jd(jd_tg=False)  # 盈亏表，依赖其他表，单独做
                m.df_to_mysql(
                    df=res,
                    db_name='聚合数据',
                    table_name='_京东_推广商品销售',
                    move_insert=True,  # 先删除，再插入
                    # df_sql=True,
                    # drop_duplicates=False,
                    # icm_update=['日期', '跟单sku id', '货号', '花费'],  # 设置唯一主键
                    service_database=service_database,
                )

    # 这里要注释掉，不然 copysh.py 可能有问题，这里主要修改配置文件，后续触发 home_lx 的 optimize_datas.py(有s)程序进行全局清理
    # optimize_data.op_data(service_databases=service_databases, days=3650)  # 立即启动对聚合数据的清理工作


def main():
    pass


if __name__ == '__main__':
    data_aggregation(service_databases=[{'company': 'mysql'}], months=24, is_juhe=False)  # 正常的聚合所有数据
    # data_aggregation_one(service_databases=[{'company': 'mysql'}], months=1)  # 单独聚合某一个数据库，具体库进函数编辑
    # optimize_data.op_data(service_databases=[{'company': 'mysql'}], days=3650)  # 立即启动对聚合数据的清理工作
