#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	xxx
function	xxx
author		Ho Loong
date		xxxx-xx-xx
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os

import pandas as pd

import matplotlib.pyplot as plt

import seaborn

def enviroment_init():
    """
    程序运行环境初始化
    """
    pass

def main():
    """
    程序入口
    """
    enviroment_init()

    print 'Pandas处理一维数据demo'

    a = pd.Series([
        12,5,8,17
        ])
    b = pd.Series([
        3.3,2.4,5.6,7.7
        ])

    print 'Pandas Series 比较，逻辑，索引数组：'
    print 'a，b都大于平均值的元素索引列表：\n', ((a>a.mean()) & (b>b.mean()))
    print 'a，b都大于平均值的元素子集：\n', a[((a>a.mean()) & (b>b.mean()))]
    print 'a，b都大于平均值的元素子集：\n', b[((a>a.mean()) & (b>b.mean()))]
    print 'a，b都大于平均值的元素个数：\n', (((a>a.mean()) & (b>b.mean()))).sum()
    print 'a，b都小于平均值的元素索引列表：\n', ((a<a.mean()) & (b<b.mean()))
    print 'a，b都小于平均值的元素子集：\n', a[((a<a.mean()) & (b<b.mean()))]
    print 'a，b都小于平均值的元素子集：\n', b[((a<a.mean()) & (b<b.mean()))]
    print 'a，b都小于平均值的元素个数：\n', (((a<a.mean()) & (b<b.mean()))).sum()

    print 'Pandas Series 索引位置：'
    ages = pd.Series([
        24,26,18
        ],index=[
            'HoLoong','Lour','Mark'
            ])
    print '角标访问：', ages[0]
    print 'iloc访问：', ages.iloc[0]
    print 'loc访问：', ages.loc['HoLoong']
    print 'max:', ages.max()
    print 'argmax:', ages.idxmax() # idxmax 代替了 argmax
    ages_2 = pd.Series([
        24,26,18
        ],index=[
            'HoLoong','Lour','Mark'
            ])

    print 'ages 与 ages_2 具有同样的index:'
    print 'ages+ages_2:\n', ages+ages_2
    print 'ages-ages_2:\n', ages-ages_2
    print 'ages*ages_2:\n', ages*ages_2
    print 'ages/ages_2:\n', ages/ages_2

    ages_2 = pd.Series([
        24,26,18
        ],index=[
            'Helong','Liudongyuan','Aqiang'
            ])
    print 'ages 与 ages_2 具有完全不相同的index:'
    print 'ages+ages_2:\n', ages+ages_2
    
    ages_2 = pd.Series([
        24,26,18
        ],index=[
            'Helong','Lour','Mark'
            ])
    print 'ages 与 ages_2 具有部分相同的index:'
    print 'ages+ages_2:\n', ages+ages_2

    print '删除NaN：'
    print 'Series.dropna:\n', (ages+ages_2).dropna()
    print 'notnull获取索引数组:\n', (ages+ages_2)[pd.notnull(ages+ages_2)]
    print '填充NaN：'
    print 'Series.fillna同类型数据:\n', (ages+ages_2).fillna(0)
    print 'Series.fillna不同类数据:\n', (ages+ages_2).fillna('xxx')
    print '取默认值的四则运算（不存在的index会取0作为默认值去做加法操作，也就不会减少列，也不会出现NaN）：'
    print 'add:\n', ages.add(ages_2, fill_value=0)
    print 'sub:\n', ages.sub(ages_2, fill_value=0)

    print 'Series.apply:'
    names = pd.Series(['helong','Lour','mark','lily'])
    print '将以下所有人物名字全部规范化首字母大写：'
    print names
    print '定义apply方法：'
    def clean_name(name):
        return name[0].upper()+name[1:]
    print names.apply(clean_name)

    print 'Pandas Series plot直接绘图：'
    a.plot()
    plt.show()

if __name__ == '__main__':
    main()
