#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	sklearn feature engineering
function	feature engineering
author		Ho Loong
date		2018-10-11
company		Aispeech,Inc.
ps              Please be pythonic.
link            https://blog.csdn.net/weishiym/article/details/79629329
'''

import sys
import os

from sklearn.datasets import load_iris  
  
def enviroment_init():
    """
    env init
    """
    pass

def main():
    """
    app start
    """
    enviroment_init()
    iris = load_iris()
    print 'data:'
    print iris.data[:3]
    print 'target:'
    print iris.target[:3]

if __name__ == '__main__':
    main()
