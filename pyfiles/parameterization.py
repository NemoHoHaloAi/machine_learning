#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	linear algebra
function	输出方程式有多个解时对应的解集
author		Ho Loong
date		2018-01-17
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os
from decorators import MethodCallDCRT
from vector import Vector

class Parameterization(object):
    """
    实现方程式无数个解时的解集输出
    """

    HAS_DIFFERENT_DIMENSION = 'Here has different dimension vector!!!'

    def __init__(self, basepoint_vct, direction_vcts):
        self.basepoint_vct = basepoint_vct
        self.dimension = basepoint_vct.dimension
        self.direction_vcts = direction_vcts
        try:
            for vct in self.direction_vcts:
                assert vct.dimension == self.dimension
        except AssertionError:
            raise Exception(Parameterization.HAS_DIFFERENT_DIMENSION)

    def __str__(self):
        res_str = '基准点:'+str(self.basepoint_vct)
        for vct in self.direction_vcts:
            res_str += '\n方向向量:'+str(vct)
        res_str += '\nx='
        return res_str

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
    pass

if __name__ == '__main__':
    main()
