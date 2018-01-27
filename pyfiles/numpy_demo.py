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
import numpy as np

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

    countries = np.array([
        'Chine','English','Russia'
        ])

    employments = np.array([
        58.2,45.5,56.6
        ])

    print 'Numpy Array Demo'

    print 'Country dtype:', countries.dtype
    print 'Employment dtype:', employments.dtype

    print '获取就业率最高的值和对应的国家：'
    print '方式1：'
    print '就业率：', employments.max()
    print '国家：', countries[np.where(employments==employments.max())]
    print '方式2：'
    print '就业率：', employments[employments.argmax()]
    print '国家：', countries[employments.argmax()]

    print 'Nunpy vector operation'
    a = np.array([1,2,3])
    b = np.array([4,5,6])
    c = 10.
    print 'array +-*/** array'
    print '+:',a+b
    print '-:',a-b
    print '*:',a*b
    print '/:',a/b
    print '**:',a**b

    print 'array +-*/** constant'
    print '+:',a+c
    print '-:',a-c
    print '*:',a*c
    print '/:',a/c
    print '**:',a**c

    print '*重点：索引数据，当有两个array，对应位置元素有关联时，可以通过该方法通过一个array的数据满足某个条件来对应找到另一个array中对应的数据'
    names = np.array(['HoLoong','John','Jack'])
    ages = np.array([26,24,18])
    print 'ages 满足age大于20岁的索引数组：', ages>20
    print 'ages 满足age大于20岁的子集：', ages[ages>20]
    print 'names 满足age大于20岁的name子集：', names[ages>20]
    print 'ages 满足age大于20岁的平均值：', ages[ages>20].mean()

    print 'a=a+b 和 a+=b 的区别'
    a = np.array([1,2,3])
    c = a
    b = np.array([1,1,1])
    a=a+b
    print c
    a = np.array([1,2,3])
    c = a
    b = np.array([1,1,1])
    a+=b
    print '+=称之为原位操作，表示在原内存位置上操作，而+则是另外新开辟一段空间操作'
    print c



if __name__ == '__main__':
    main()
