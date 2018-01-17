#!/usr/bin/env python
#-*- coding: utf-8 -*-

'''
project_name	linear algebra
function	Vector实现类
author		Ho Loong
date		2017-12-23
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import math
from decimal import Decimal,getcontext

ZERO = 1e-10

def enviroment_init():
    """
    当前程序运行环境初始化
    """
    getcontext().prec = 30  # 设置Decimal小数的精度范围

# 使用build-in的zip即可
# def tip(list1, list2):
#     """
#     同时遍历两个列表，每次迭代返回两个列表同一位置的元素，短的列表将用0填充
# 
#     Args:
#         list1 -- 遍历列表1
#         list2 -- 遍历列表2
# 
#     Returns:
#         result -- 返回一个二维列表，第一维长度与较长的被遍历列表一致，每个一维元素为一个大小为2的列表
#     """
#     return [[(Decimal(0) if i >= len(list1) else list1[i]), (Decimal(0) if i >= len(list2) else list2[i])] for i in range(max(len(list1),len(list2)))]

def Beyond3Dimension(func):
    """
    三维向量装饰器，处理当向量超过三维时，抛出异常
    """
    def wrapper(*args, **kwargs):
        """
        Returns:
            result -- func的执行结果
            
        Raises:
            Exception -- 当计算中出现除0时抛出该异常
        """
        # TODO(Ho Loong): 暂时使用这种方法判断是否other或者self为空，后续看有没有更优雅的方法
        self = kwargs.get('self') if kwargs.get('self') else args[0]
        other = kwargs.get('other') if kwargs.get('other') else args[1]
        if len(self) not in (2,3) or len(other) not in (2,3):
            raise Exception('Vector Exception:No support beyond 3 or less 2 dimension vector to calc.')
        if len(self) == 2: 
            self.full(3)
        if len(other) == 2: 
            other.full(3)
        return func(*args, **kwargs)
    return wrapper

def ZeroReturnTrue(func):
    """
    零向量装饰器，处理当other为零向量时直接返回True，也就不需要对零向量特殊处理
    """
    def wrapper(*args, **kwargs):
        """
        Returns:
            result -- 包含一个零向量时返回True，否则返回func
        """
        # TODO(Ho Loong): 暂时使用这种方法判断是否other或者self为空，后续看有没有更优雅的方法
        self = kwargs.get('self') if kwargs.get('self') else args[0]
        other = kwargs.get('other') if kwargs.get('other') else args[1]
        if (self and self.is_zero()) or (other and other.is_zero()):
            return True
        return func(*args, **kwargs)
    return wrapper

def ZeroReturnZeroVector(func):
    """
    零向量装饰器，处理当other为零向量时直接返回零向量，也就不需要对零向量特殊处理
    """
    def wrapper(*args, **kwargs):
        """
        Returns:
            result -- 包含一个零向量时返回True，否则返回func
        """
        # TODO(Ho Loong): 暂时使用这种方法判断是否other或者self为空，后续看有没有更优雅的方法
        self = kwargs.get('self') if kwargs.get('self') else args[0]
        other = kwargs.get('other') if kwargs.get('other') else args[1]
        if self and self.is_zero():
            return self
        if other and other.is_zero():
            return other
        return func(*args, **kwargs)
    return wrapper

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
            raise Exception('Vector Exception:can not calc with zero vector.')
    return wrapper
    
def NoneVector(func):
    """
    None装饰器，处理当other为None时直接抛出异常
    """
    def wrapper(*args, **kwargs):
        """
        Returns:
            result -- func
            
        Raises:
            ValueError -- 当参数other不存在或者为None时，抛出该异常
        """
        if not kwargs.get('other') and not args[1]:
            raise Exception('Vector Exception:Parameter is NoneType.')
        return func(*args, **kwargs)
    return wrapper

class Vector(object):
    """
    Vector实现类，实现了向量的基本操作，重载了向量的加+，减-，点乘*运算符，
    实现了与标量相乘，获取向量大小，求向量之间夹角等等功能

    Attributes:
        coordinates -- 用于描述向量的一维元组
    """
    def __init__(self, coordinates):
        """
        初始化函数，主要是做了Decimal处理

        Args:
            coordinates -- 向量值列表
        """
    	self.coordinates = tuple([Decimal(me) for me in coordinates])
        self.dimension = len(self.coordinates)

    def __len__(self):
        """
        重载len()运算，返回coordinates长度
        """
        return len(self.coordinates)

    def __eq__(self, other):
        """
        重载==运算符，当Vector中的coordinates相等时表示两个向量相等

        Args:
            other -- ==右侧的参数

        Returns:
            result -- 两个向量是否相等的bool值
        """
    	return other and (self.coordinates == other.coordinates)

    @NoneVector
    def __add__(self, other):
        """
        重载+运算符，向量相加即对应元组的每个值相加得到一个新的元组

        Args:
            other -- +右侧的参数

        Returns:
            result -- 相加后的列表创建的新的Vector对象

        Decorates:
            NoneVector
        """
        return Vector([me + him for me, him in zip(self.coordinates, other.coordinates)])

    @NoneVector
    def __sub__(self, other):
        """
        重载-运算符，向量相减即对应元组的每个值相减得到一个新的元组

        Args:
            other -- -右侧的参数

        Returns:
            result -- 相减后的列表创建的新的Vector对象

        Decorates:
            NoneVector
        """
        return Vector([me - him for me, him in zip(self.coordinates, other.coordinates)])

    @NoneVector
    def __mul__(self, other):
        """
        重载*运算符，向量点乘即对应元组的每个值相乘得到一个新的列表，然后求列表项的和

        Args:
            other -- *右侧的参数

        Returns:
            result -- 点乘后求得的和

        Decorates:
            NoneVector
        """
    	return Decimal(sum([me * him for me, him in zip(self.coordinates, other.coordinates)]))

    def get_coordinates(self):
        """
        获取当前向量的值列表

        Returns:
            result -- 当前向量的值列表
        """
        return self.coordinates

    def full(self, dimension):
        """
        用0填充当前向量使其匹配更高维度的向量

        Args:
            dimension -- 目标维度
        """
        if len(self) < dimension:
            self.coordinates = tuple(list(self.coordinates) + ([0] * (dimension - len(self))))

    def is_zero(self):
        """
        判断当前向量是不是零向量

        Returns:
            result -- True表示是零向量，False表示不是
        """
        return abs(sum(self.coordinates)) <= ZERO
    
    # TODO(Ho Loong): 暂时使用mul，后续看有没有更好的名字用以描述一个向量乘以标量的功能
    def scala(self, times):
        """
        实现向量与标量相乘，即向量的每一项都乘以标量

        Args:
            times -- 要乘的标量

        Returns:
            result -- 每一项乘以标量后组成的新的列表创建的新Vector对象
        """
    	return Vector([me * times for me in self.coordinates])

    def size(self):
        """
        计算并返回向量的大小，也就是向量的模

        Returns:
            result -- 每一项的平方和再开方
        """
    	return Decimal(Decimal.sqrt(sum([me**Decimal(2) for me in self.coordinates])))

    @ZeroCalc
    def direction(self):
        """
        计算并返回向量的方向

        Returns:
            result -- 标准化

        Decorates:
            ZeroCalc
        """
    	return self.scala(Decimal(1) / self.size())
    
    @ZeroCalc
    @NoneVector
    def angle_rad(self, other):
        """
        计算两个向量之间的夹角，以弧度单位返回结果

        Args:
            other -- 与本向量计算夹角的另一个向量

        Returns:
            result -- 向量夹角弧度值

        Decorates:
            ZeroCalc
            NoneVector
        """
        return Decimal(str(math.acos((self * other) / (self.size() * other.size()))))

    @NoneVector
    def angle_deg(self, other):
        """
        计算两个向量之间的夹角，以角度单位返回结果

        Args:
            other -- 与本向量计算夹角的另一个向量

        Returns:
            result -- 向量夹角角度值

        Decorates:
            NoneVector
        """
    	return Decimal(self.angle_rad(other) * (Decimal(180) / Decimal(str(math.pi))))

    @ZeroReturnTrue
    @NoneVector
    def parallel(self, other):
        """
        计算并返回两个向量是否平行，平行判断方式为如果其中之一为零向量直接返回True，
        否则判断是否每个对应位置的值的倍数都是一致的，也就是任何一个向量都可以通过
        乘以某一个标量来转成另一个向量

        Args:
            other -- 判断是否平行的另一个变量

        Returns:
            result -- 是否平行的bool值

        Decorates:
            ZeroReturnTrue
            NoneVector
        """
        return (self.coordinates and other and other.coordinates and (abs(self.angle_deg(other) - Decimal(0)) <= ZERO or abs(self.angle_deg(other) - Decimal(180)) <= ZERO))

    @ZeroReturnTrue
    @NoneVector
    def orthogonal(self, other):
        """
        计算并返回两个向量是否正交，平行判断方式为如果其中之一为零向量直接返回True，
        否则判断两者的夹角弧度制是否为0

        Args:
            other -- 判断是否正交的另一个变量

        Returns:
            result -- 是否正交的bool值

        Decorates:
            ZeroReturnTrue
            NoneVector
        """
    	return abs(self * other - Decimal(0)) <= ZERO

    @ZeroCalc
    @NoneVector
    def parallel_vector(self, other):
        """
        基于basis向量计算当前向量在basis上的投影向量

        Args:
            other -- 基向量

        Returns:
            result -- self在other上的投影向量

        Notes:
            formula -- proj(self)_basis = (self.u_basis).u_basis

        Decorates:
            ZeroCalc
            NoneVector
        """
        u_basis = other.direction()  # 计算basis的标准化向量，也就是它的单位向量，用direction方法即可
        return u_basis.scala(self * (u_basis))

    @ZeroCalc
    @NoneVector
    def orth_vector(self, other):
        """
        基于basis向量计算当前向量在basis上的正交向量

        Args:
            other -- 基向量

        Returns:
            result -- self在other上的正交向量

        Notes:
            formula -- self - proj(self)_basis

        Decorates:
            ZeroCalc
            NoneVector
        """
        return self - self.parallel_vector(other)

    @ZeroReturnZeroVector
    @Beyond3Dimension
    @NoneVector
    def cross(self, other):
        """
        计算self与basis的叉乘结果

        Args:
            basis -- 与self计算叉乘的向量

        Returns:
            result -- 叉乘结果对应的向量

        Notes:
            formula -- self x other

        Decorates:
            ZeroCalc
            NoneVector
        """
        x1,y1,z1 = self.get_coordinates();
        x2,y2,z2 = other.get_coordinates();
        return Vector([y1*z2-y2*z1,-(x1*z2-x2*z1),x1*y2-x2*y1])

    @NoneVector
    def parallelogram(self, other):
        """
        计算self与basis围成的平行四边形的面积

        Args:
            basis -- 与self计算平行四边形面积的向量

        Returns:
            result -- 平行四边形的面积

        Notes:
            formula -- (self x other).size()

        Decorates:
            NoneVector
        """
        return self.cross(other).size()

    @NoneVector
    def triangle(self, other):
        """
        计算self与basis围成的三角形的面积

        Args:
            basis -- 与self计算三角面积的向量

        Returns:
            result -- 三角的面积

        Notes:
            formula -- (self x other).size()/2

        Decorates:
            NoneVector
        """
        return self.cross(other).size()/Decimal(2)

    def __str__(self):
        """
        返回向量的字符串表达式
        """
	return 'Vector:' + str(self.coordinates)


def main():
    """
    程序入口
    """
    enviroment_init()
    
    v1 = Vector(['1','2'])
    v2 = Vector(['2','3'])
    print 'v1=' + str(v1)
    print 'v2=' + str(v2)
    v3 = v1 + v2
    print 'v1+v2=' + str(v3)
    v4 = v1 - v2
    print 'v1-v2=' + str(v4)
    v5 = v2 - v1
    print 'v2-v1=' + str(v5)
    v1 += v2
    print 'v1+=v2=' + str(v1)
    v6 = v1.scala(2)
    print 'v1*2=' + str(v6)
    print 'v1-v2是否等于v2-v1=' + str((v1-v2)==(v2-v1))
    v1 = Vector([3,4])
    print v1
    print 'v1 size=' + str(v1.size())
    print 'v1 direction=' + str(v1.direction())
    print '--------------No1--------------'
    print 'No1:' + str(Vector(['0.221','7.437']).size())
    print 'No2:' + str(Vector(['8.813','-1.331','-6.247']).size())
    print 'No3:' + str(Vector(['5.581','-2.136']).direction())
    print 'No4:' + str(Vector(['1.996','3.108','-4.554']).direction())
    print 'No5:' + str(Vector(['0','0']).size())
    print '--------------No2--------------'
    print 'No1:' + str(Vector(['7.887','4.138']) * Vector(['-8.802','6.776']))
    print 'No2:' + str(Vector(['-5.955','-4.904','-1.874']) * Vector(['-4.496','-8.755','7.103']))
    print 'No3:' + str(Vector(['3.183','-7.627']).angle_rad(Vector(['-2.668','5.319'])))
    print 'No4:' + str(Vector(['7.35','0.221','5.188']).angle_deg(Vector(['2.751','8.259','3.985'])))
    print 'Notest:' + str(Vector(['1','1','1']).angle_deg(Vector(['2','2','2'])))
    print '--------------No3--------------'
    print 'No1:' + str(Vector(['-7.579','-7.88']).parallel(Vector(['22.737','23.64'])))
    print 'No1:' + str(Vector(['-7.579','-7.88']).orthogonal(Vector(['22.737','23.64'])))
    print 'No2:' + str(Vector(['-2.029','9.97','4.172']).parallel(Vector(['-9.231','-6.639','-7.245'])))
    print 'No2:' + str(Vector(['-2.029','9.97','4.172']).orthogonal(Vector(['-9.231','-6.639','-7.245'])))
    print 'No3:' + str(Vector([-2.328,-7.284,-1.214]).parallel(Vector([-1.821,1.072,-2.94])))
    print 'No3:' + str(Vector([-2.328,-7.284,-1.214]).orthogonal(Vector([-1.821,1.072,-2.94])))
    print 'No4:' + str(Vector([2.118,4.827]).parallel(Vector([0,0])))
    print 'No4:' + str(Vector([2.118,4.827]).orthogonal(Vector([0,0])))
    print '--------------No4--------------'
    print 'No1:' + str(Vector([3.039,1.879]).parallel_vector(Vector([0.825,2.036])))
    print 'No2:' + str(Vector([-9.88,-3.264,-8.159]).orth_vector(Vector([-2.155,-9.353,-9.473])))
    print 'No3:' + str(Vector([3.009,-6.172,3.692,-2.51]).parallel_vector(Vector([6.404,-9.144,2.759,8.718])))
    print 'No4:' + str(Vector([3.009,-6.172,3.692,-2.51]).orth_vector(Vector([6.404,-9.144,2.759,8.718])))
    print '--------------No5--------------'
    print 'No1:' + str(Vector(['8.462','7.893','-8.187']).cross(Vector(['6.984','-5.975','4.778'])))
    print 'No2:' + str(Vector(['-8.987','-9.838','5.031']).parallelogram(Vector(['-4.268','-1.861','-8.866'])))
    print 'No3:' + str(Vector(['1.5','9.547','3.691']).triangle(Vector(['-6.007','0.124','5.772'])))

if __name__ == '__main__':
    main()
