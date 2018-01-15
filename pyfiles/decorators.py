#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
project_name	common
function	装饰器工具包
author		Ho Loong
date		2018-01-15
company		Aispeech,Inc.
ps              Please be pythonic.
'''

def MethodCallDCRT(func):
    """
    日志装饰器，打印调用方法名，以及调用参数等
    """
    def wrapper(*args, **kwargs):
        print 'Call method:'+str(func.__name__)+' with '+str(args)
        return func(*args)
    return wrapper

@MethodCallDCRT
def testMethodCallDCRT(i,j):
    print 'my self print!!!'

def main():
    testMethodCallDCRT(1,2) # 测试日志装饰器

if __name__ == '__main__':
    main()
