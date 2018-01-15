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

def ZeroCalc(func):
    """
    除0异常装饰器，处理function中可能发生的除0异常
    """
    def wrapper(*args, **kwargs):
        """
        Returns:
            result -- func的执行结果
            
        Raises:
            Exception -- 当计算中出现除0时抛出该异常
        """
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            return None
    return wrapper

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
    NONZERO_PARAM_NOT_FOUND = 'No zero parameter not exist!!'

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
        self.a = self.normal_vector.coordinates[0]
        self.b = self.normal_vector.coordinates[1]
        self.c = self.normal_vector.coordinates[2]
        self.k = Decimal(self.constant_term)
        self.params = [self.a,self.b,self.c]
        self.first_nonzero_idx = self.__first_nonzero_index()
        self.dimension = len(self.normal_vector)
        self.__set_base_point()

    def __eq__(self, other):
        """
        重载 == 运算符

        Args:
            other -- 对比的平面
        """
        x1 = Decimal('0') if not LaDecimal(self.c).is_near_zero() else (Decimal('0') if not LaDecimal(self.b).is_near_zero() else (self.k / self.a if not LaDecimal(self.a).is_near_zero() else Decimal('0')))
        y1 = Decimal('0') if not LaDecimal(self.c).is_near_zero() else (self.k / self.b if not LaDecimal(self.b).is_near_zero() else Decimal('0'))
        z1 = self.k / self.c if not LaDecimal(self.c).is_near_zero() else Decimal('0')

        x2 = other.k / other.a if not LaDecimal(other.a).is_near_zero() else Decimal('0')
        y2 = Decimal('0') if not LaDecimal(other.a).is_near_zero() else (other.k / other.b if not LaDecimal(other.b).is_near_zero() else Decimal('0'))
        z2 = Decimal('0') if not LaDecimal(other.a).is_near_zero() else (Decimal('0') if not LaDecimal(other.b).is_near_zero() else (other.k / other.c if not LaDecimal(other.c).is_near_zero() else Decimal('0')))

        v = Vector([str(x1-x2),str(y1-y2),str(z1-z2)])

        return self.normal_vector.orthogonal(v) and other.normal_vector.orthogonal(v)

    def __ne__(self, other):
        """
        重载 !=,<> 运算符

        Args:
            other -- 对比的平面
        """
        return not self == other

    def __cmp__(self, other):
        """
        重载比较运算符，使用Plane类对象可以被sort或者sorted操作

        Args:
            other -- 用于与自身比较的另一个Plane对象

        Returns:
            -1 -- 自己比较小
            1 -- 自己比较大
            0 -- 一样大小
        """
        return 1 if self.first_nonzero_idx is -1 else self.first_nonzero_idx - other.first_nonzero_idx # 使得在顺序排序时，直接得到正三角形方程式，没有非0项的话用于返回1，放到最后

    def __str__(self):
        """
        重载Plane的str()方法，输出平面对应的一般式
        """
        return '('+str(self.a)+')X+('+str(self.b)+')Y+('+str(self.c)+')Z'+'='+str(self.k)

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

    def intersection_line(self, other):
        """
        求两个平面相交的直线

        Args:
            other -- 另一个平面

        Returns:
            count -- 相交直线的个数，0表示没有相交，1表示有且只有一条直线，-1表示有无数条直线相交
            interseciton -- 当count=1时，该值存在(x,y,z)，为-1时，同样给出一个结果
        """
        return 0 if (self.parallel(other) and self != other) else (1 if not self.parallel(other) else -1)

    @ZeroCalc
    def intersection_point(self, other, other2):
        """
        求三个平面交点

        Args:
            other -- 另一个平面
            other2 -- 第三个平面

        Notes:
            formula -- 高斯消去法

        Returns:
            interseciton -- 交点(a,b,c)

        Raises:
            ZeroCalc -- 除0异常处理，返回None表示出现异常
        """
        a1,b1,c1,k1 = self.a,self.b,self.c,self.k
        a2,b2,c2,k2 = other.a,other.b,other.c,other.k
        a3,b3,c3,k3 = other2.a,other2.b,other2.c,other2.k

        # step 1 : 消去方程2,3中的x
        ratio = -(a2/a1) if a2!=0 else Decimal('0')
        a2,b2,c2,k2 = a2+ratio*a1,b2+ratio*b1,c2+ratio*c1,k2+ratio*k1

        ratio = -(a3/a1) if a3!=0 else Decimal('0')
        a3,b3,c3,k3 = a3+ratio*a1,b3+ratio*b1,c3+ratio*c1,k3+ratio*k1

        # step 2 : 消去方程3中的y
        ratio = -(b3/b2) if b3!=0 else Decimal('0')
        a3,b3,c3,k3 = a3+ratio*a2,b3+ratio*b2,c3+ratio*c2,k3+ratio*k2

        print 'function 1:('+str(a1)+')X+('+str(b1)+')Y+('+str(c1)+')Z'+'='+str(k1)
        print 'function 2:('+str(a2)+')X+('+str(b2)+')Y+('+str(c2)+')Z'+'='+str(k2)
        print 'function 3:('+str(a3)+')X+('+str(b3)+')Y+('+str(c3)+')Z'+'='+str(k3)
        
        x,y,z=0,0,0
        if LaDecimal(k3).is_near_zero() and LaDecimal(c3).is_near_zero():
            print '0==0 case'
        else:
            z = k3 / c3
            y = (k2-z*c2) / b2
            x = (k1-z*c1-y*b1) / a1

        return Vector([str(x),str(y),str(z)])

    def __first_nonzero_index(self):
        """
        获取params中第一个非零元素的角标

        Returns:
            index -- 第一个非零元素的角标

        Raises:
            Exception -- 不存在符合条件的元素时抛出该异常
        """
        for i in range(len(self.params)):
            if not LaDecimal(self.params[i]).is_near_zero():
                return i
        return -1


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

    p1 = Plane(Vector(['-1','1','1']), Decimal('-2'))
    p2 = Plane(Vector(['1','-4','4']), Decimal('21'))
    p3 = Plane(Vector(['7','-5','-11']), Decimal('0'))
    print 'p1,p2 has intersection point:' + str(p1.intersection_point(p2,p3))
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['1','-2','1']), Decimal('-1'))
    p2 = Plane(Vector(['-1','4','-4']), Decimal('0'))
    p3 = Plane(Vector(['1','0','-2']), Decimal('2'))
    print 'p1,p2 has intersection point:' + str(p1.intersection_point(p2,p3))
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['3','-4','1']), Decimal('1'))
    p2 = Plane(Vector(['1','-1','1']), Decimal('2'))
    p3 = Plane(Vector(['0','1','-1']), Decimal('2'))
    print 'p1,p2 has intersection point:' + str(p1.intersection_point(p2,p3))
    print '-------------------------------------------------------------------'

    p1 = Plane(Vector(['1','2','1']), Decimal('-1'))
    p2 = Plane(Vector(['3','6','2']), Decimal('1'))
    p3 = Plane(Vector(['-1','-2','-1']), Decimal('1'))
    print 'p1,p2 has intersection point:' + str(p1.intersection_point(p2,p3))
    print '-------------------------------------------------------------------'

if __name__ == '__main__':
    main()
