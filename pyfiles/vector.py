#-*- coding: utf-8 -*-

"""
vector.py -- Vector自我实现类
"""

import math
from decimal import Decimal,getcontext

getcontext().prec = 3  # 设置Decimal小数的精度范围

def tip(list1, list2):
    """
    同时遍历两个列表，每次迭代返回两个列表同一位置的元素，短的列表将用0填充

    Args:
        list1 -- 遍历列表1
        list2 -- 遍历列表2

    Returns:
        result -- 返回一个二维列表，第一维长度与较长的被遍历列表一致，每个一维元素为一个大小为2的列表
    """
    return [[(Decimal(0) if i >= len(list1) else list1[i]), (Decimal(0) if i >= len(list2) else list2[i])] for i in range(max(len(list1),len(list2)))]

def ZeroVector(func):
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
        if (self and sum(self.coordinates) == 0) or (other and sum(other.coordinates) == 0):
            return True
        return func(*args, **kwargs)
    return wrapper

def ZeroDivision(func):
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
        return Vector([me + him for me, him in tip(self.coordinates, other.coordinates)])

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
        return Vector([me - him for me, him in tip(self.coordinates, other.coordinates)])

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
    	return Decimal(sum([me * him for me, him in tip(self.coordinates, other.coordinates)]))
    
    # TODO(Ho Loong): 暂时使用mul，后续看有没有更好的名字用以描述一个向量乘以标量的功能
    def mul(self, times):
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

    @ZeroDivision
    def direction(self):
        """
        计算并返回向量的方向

        Returns:
            result -- 标准化

        Decorates:
            ZeroDivision
        """
    	return self.mul(Decimal(1) / self.size())
    
    @ZeroDivision
    @NoneVector
    def angle_rad(self, other):
        """
        计算两个向量之间的夹角，以弧度单位返回结果

        Args:
            other -- 与本向量计算夹角的另一个向量

        Returns:
            result -- 向量夹角弧度值

        Decorates:
            ZeroDivision
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

    @ZeroVector
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
            ZeroVector
            NoneVector
        """
        if not self.coordinates or not other or not other.coordinates:
            return False
        pre = self.coordinates[0] / other.coordinates[0]
        for me, him in tip(self.coordinates, other.coordinates):
            if me / him != pre:
                return False
        return True

    @ZeroVector
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
            ZeroVector
            NoneVector
        """
    	return self.angle_rad(other) == Decimal(0)

    def __str__(self):
        """
        返回向量的字符串表达式
        """
	return 'Vector:' + str(self.coordinates)


def main():
    v1 = Vector([1,2])
    v2 = Vector([2,3])
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
    v6 = v1.mul(2)
    print 'v1*2=' + str(v6)
    print 'v1-v2是否等于v2-v1=' + str((v1-v2)==(v2-v1))
    v1 = Vector([3,4])
    print v1
    print 'v1 size=' + str(v1.size())
    print 'v1 direction=' + str(v1.direction())
    print '--------------No1--------------'
    print 'No1:' + str(Vector([-0.221,7.437]).size())
    print 'No2:' + str(Vector([8.813,-1.331,-6.247]).size())
    print 'No3:' + str(Vector([5.581,-2.136]).direction())
    print 'No4:' + str(Vector([1.996,3.108,-4.554]).direction())
    print 'No5:' + str(Vector([0,0]).size())
    print '--------------No2--------------'
    print 'No1:' + str(Vector([7.887,4.138]) * Vector([-8.802,6.776]))
    print 'No2:' + str(Vector([-5.955,-4.904,-1.874]) * Vector([-4.496,-8.755,7.103]))
    print 'No3:' + str(Vector([3.183,-7.627]).angle_rad(Vector([-2.668,5.319])))
    print 'No4:' + str(Vector([7.35,0.221,5.188]).angle_deg(Vector([2.751,8.259,3.985])))
    print 'Notest:' + str(Vector([1,1,1]).angle_deg(Vector([2,2,2])))
    print '--------------No3--------------'
    print 'No1:' + str(Vector([-7.579,-7.88]).parallel(Vector([22.737,23.64])))
    print 'No1:' + str(Vector([-7.579,-7.88]).orthogonal(Vector([22.737,23.64])))
    print 'No2:' + str(Vector([-2.029,9.97,4.172]).parallel(Vector([-9.231,-6.639,-7.245])))
    print 'No2:' + str(Vector([-2.029,9.97,4.172]).orthogonal(Vector([-9.231,-6.639,-7.245])))
    print 'No3:' + str(Vector([-2.328,-7.284,-1.214]).parallel(Vector([-1.821,1.072,-2.94])))
    print 'No3:' + str(Vector([-2.328,-7.284,-1.214]).orthogonal(Vector([-1.821,1.072,-2.94])))
    print 'No4:' + str(Vector([2.118,4.827]).parallel(Vector([0,0])))
    print 'No4:' + str(Vector([2.118,4.827]).orthogonal(Vector([0,0])))

if __name__ == '__main__':
    main()
