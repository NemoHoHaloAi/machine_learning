#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	linear algebra
function	Line实现类
author		Ho Loong
date		2017-12-23
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os
from decimal import Decimal,getcontext
from ladecimal import LaDecimal

from vector import Vector

def enviroment_init():
    """
    程序运行环境初始化
    """
    getcontext().prec = 30  # 设置Decimal小数的精度范围

class Line(object):
    """
    Line类用于描述一条直线，定义了直线相关的各种计算，例如平行判断，同一直线判断
    求两直线交点等等

    Attributes:
        DIMENSION -- 维度，此处仅考虑2维情况
        normal_vector -- 直线的法向量，如果为None，则使用[0,0]填充
        contant_term -- 直线的常量，如果为None，则使用0代替
    """

    DIMENSION = 2 

    def __init__(self, normal_vector=None, constant_term=None):
        """
        重载Line的构造函数，设置直线法向量，常量，以及基准点等属性

        Args:
            normal_vector -- 直线法向量
            constant_term -- 直线常量

        Notes:
            法向量，方向向量 -- 二维空间中二者相等，多维空间中会存在多个方向向量
            normal vector -- 法向量，例如一般式为 aX+bY=k，则normal vector为[a b]
            constant term -- 结果常量，也就是k
            base point -- 通过法向量，常量计算基准点并设置上去
        """
        self.normal_vector = normal_vector if normal_vector else Vector([0]*Line.DIMENSION)
        self.constant_term = constant_term if constant_term else Decimal('0')
        self.a = normal_vector.coordinates[0]
        self.b = normal_vector.coordinates[1]
        self.k = constant_term
        self.__set_base_point()

    def __eq__(self, other):
        """
        重载 == 运算符

        Args:
            other -- 对比的直线
        """
        x1 = Decimal('0') if not LaDecimal(self.a).is_near_zero() else self.k / self.a
        y1 = self.k / self.b if not LaDecimal(self.a).is_near_zero() else Decimal('0')
        x2 = other.k / other.a if not LaDecimal(other.b).is_near_zero() else Decimal('0')
        y2 = Decimal('0') if not LaDecimal(other.b).is_near_zero() else other.k / other.b
        v = Vector([str(x1-x2),str(y1-y2)])
        return self.normal_vector.orthogonal(v) and other.normal_vector.orthogonal(v)

    def __ne__(self, other):
        """
        重载 !=,<> 运算符

        Args:
            other -- 对比的直线
        """
        return not self == other

    def __str__(self):
        """
        重载Line的str()方法，输出直线对应的一般式
        """
        return 'ax+by=k'

    def __set_base_point(self):
        """
        计算并生成设置Line的基准点
        """
        self.base_point = None

    def parallel(self, other):
        """
        判断两条直线是否平行

        Args:
            other -- 另一条直线

        Returns:
            result -- True表示平行，False表示不平行
        """
        return self.normal_vector.parallel(other.normal_vector)

    def intersection(self, other):
        """
        求两条直线的交点

        Args:
            other -- 另一条直线

        Returns:
            count -- 交点个数，0表示没有交点，1表示有且只有一个交点，-1表示有无数个交点
            interseciton -- 当count=1时，该值存在(x,y)，为-1时，同样给出一个结果
        """
        return 0 if (self.parallel(other) and self != other) else (1 if not self.parallel(other) else -1)

    @staticmethod
    def first_nonzero_index(iterable):
        """
        工具方法获取可迭代对象中第一个非零元素的角标

        Args:
            iterable -- 被迭代的对象

        Returns:
            index -- 第一个非零元素的角标

        Raises:
            Exception -- 不存在符合条件的元素时抛出该异常
        """
        return 1


def main():
    """
    程序入口
    """
    enviroment_init()
    
    print 'testing:'
    l1 = Line(Vector(['1.0','2.0']), Decimal('0.0'))
    l2 = Line(Vector(['1.0','2.0']), Decimal('0.0'))
    print 'l1,l2 has intersection:' + str(l1.intersection(l2))
    print 'l1,l2 is same line:' + str(l1==l2)
    print '-------------------------------------------------------------------'

    l1 = Line(Vector(['4.046','2.836']), Decimal('1.21'))
    l2 = Line(Vector(['10.115','7.09']), Decimal('3.025'))
    print 'l1,l2 has intersection:' + str(l1.intersection(l2))
    print 'l1,l2 is same line:' + str(l1==l2)
    print '-------------------------------------------------------------------'


if __name__ == '__main__':
    main()
