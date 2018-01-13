#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	linear algebra
function	Plane实现类
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

class Plane(object):
    """
    Plane类用于描述一个平面，定义了平面相关的各种计算，例如平行判断，同一平面判断
    求两平面相交直线等等

    Attributes:
        DIMENSION -- 维度，此处仅考虑2维情况
        normal_vector -- 平面的法向量，如果为None，则使用[0,0,0]填充
        contant_term -- 平面的常量，如果为None，则使用0代替
    """

    DIMENSION = 3

    def __init__(self, normal_vector=None, constant_term=None):
        """
        重载Plane的构造函数，设置平面法向量，常量，以及基准点等属性

        Args:
            normal_vector -- 平面法向量
            constant_term -- 平面常量

        Notes:
            法向量，方向向量 -- 二维空间中二者相等，多维空间中会存在多个方向向量
            normal vector -- 法向量，例如一般式为 aX+bY+cZ=k，则normal vector为[a b c]
            constant term -- 结果常量，也就是k
            base point -- 通过法向量，常量计算基准点并设置上去
        """
        self.normal_vector = normal_vector if normal_vector else Vector([0]*Plane.DIMENSION)
        self.constant_term = constant_term if constant_term else Decimal('0')
        self.a = normal_vector.coordinates[0]
        self.b = normal_vector.coordinates[1]
        self.c = normal_vector.coordinates[2]
        self.k = constant_term
        self.__set_base_point()

    def __eq__(self, other):
        """
        重载 == 运算符

        Args:
            other -- 对比的平面
        """
        x1 = Decimal('0') if not LaDecimal(self.a).is_near_zero() else self.k / self.a
        y1 = Decimal('0') # if not LaDecimal(self.a).is_near_zero() else self.k / self.b
        z1 = self.k / self.c if not LaDecimal(self.a).is_near_zero() else Decimal('0')
        x2 = other.k / other.a if not LaDecimal(other.c).is_near_zero() else Decimal('0')
        y2 = Decimal('0') # if not LaDecimal(other.c).is_near_zero() else other.k / other.c
        z2 = Decimal('0') if not LaDecimal(other.c).is_near_zero() else other.k / other.c
        v = Vector([str(x1-x2),str(y1-y2),str(z1-z2)])
        return self.normal_vector.orthogonal(v) and other.normal_vector.orthogonal(v)

    def __ne__(self, other):
        """
        重载 !=,<> 运算符

        Args:
            other -- 对比的平面
        """
        return not self == other

    def __str__(self):
        """
        重载Plane的str()方法，输出平面对应的一般式
        """
        return 'aX+bY+cZ=k'

    def __set_base_point(self):
        """
        计算并生成设置Plane的基准点
        """
        self.base_point = None

    def parallel(self, other):
        """
        判断两条平面是否平行

        Args:
            other -- 另一个平面

        Returns:
            result -- True表示平行，False表示不平行
        """
        return self.normal_vector.parallel(other.normal_vector)

    def intersection(self, other):
        """
        求两个平面相交的直线

        Args:
            other -- 另一个平面

        Returns:
            count -- 相交直线的个数，0表示没有相交，1表示有且只有一条直线，-1表示有无数条直线相交
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
    p1 = Plane(Vector(['1','2','3']), Decimal('0'))
    p2 = Plane(Vector(['1','2','3']), Decimal('0'))
    print 'p1,p2 is parallel plane:' + str(p1.parallel(p2))
    print 'p1,p2 is same Plane:' + str(p1==p2)
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['-0.412','3.806','0.728']), Decimal('-3.46'))
    p2 = Plane(Vector(['1.03','-9.515','-1.82']), Decimal('8.65'))
    print 'p1,p2 is parallel plane:' + str(p1.parallel(p2))
    print 'p1,p2 is same plane:' + str(p1==p2)
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['2.611','5.528','0.283']), Decimal('4.6'))
    p2 = Plane(Vector(['7.715','8.306','5.342']), Decimal('3.76'))
    print 'p1,p2 is parallel plane:' + str(p1.parallel(p2))
    print 'p1,p2 is same plane:' + str(p1==p2)
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['-7.926','8.625','-7.212']), Decimal('-7.952'))
    p2 = Plane(Vector(['-2.642','2.875','-2.404']), Decimal('-2.443'))
    print 'p1,p2 is parallel plane:' + str(p1.parallel(p2))
    print 'p1,p2 is same plane:' + str(p1==p2)
    print '-------------------------------------------------------------------'

if __name__ == '__main__':
    main()
