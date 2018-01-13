#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	linear algebra
function	MyDecimal实现类，扩展了is_near_zero方法
author		Ho Loong
date		2017-12-24
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os
from decimal import Decimal

class LaDecimal(Decimal):

    ZERO = 1e-10

    def is_near_zero(self):
        return abs(self) <= LaDecimal.ZERO

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
