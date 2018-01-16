#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
project_name	linear algebra
function	线性方程组实现类
author		Ho Loong
date		2018-01-14
company		Aispeech,Inc.
ps              Please be pythonic.
'''

import sys
import os
from decimal import Decimal,getcontext
from ladecimal import LaDecimal
from plane import Plane
from vector import Vector
from copy import deepcopy

def enviroment_init():
    """
    程序运行环境初始化
    """
    getcontext().prec = 30  # 设置Decimal小数的精度范围

def IndexOutOfBounds(func):
    """
    角标越界异常装饰器，处理function中可能发生的角标越界异常
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
        except ArrayIndexOutOfBoundsException:
            raise Exception(LinearSystem.INDEX_OUT_OF_BOUNDS)
    return wrapper

class LinearSystem(object):
    """
    LinearSystem类用于描述线性方程组，定义了相关操作，例如交换行，获取第一个非零项等等，
    用于辅助进行方程组求解

    Attributes:
        planes -- 存放方程组中每一个方程式
    """

    INDEX_OUT_OF_BOUNDS = 'Row number out of planes array bounds!!'
    DIMENSION_ERROR = 'Planes has different dimensiton!!'
    NOT_CAN_SWAP_ROW = 'Can swap row not exist!!'

    def __init__(self, planes=[]):
        """
        重载LinearSystem的构造函数，设置各个方程式组

        Args:
            planes -- 方程式列表
        """

        try:    
            dim = planes[0].dimension
            for p in planes:
                assert p.dimension == dim # 防止各个plane的维度不一致
            self.planes = planes
            self.dimension = dim
        except AssertionError:
            raise Exception(LinearSystem.DIMENSION_ERROR)

    def __str__(self):
        """
        重载LinearSystem的str函数
        """

        res_str = 'LinearSystem:\n'
        for p in self.planes:
            res_str += '\t'+str(p)+'\n'
        return res_str[:-1]

    def __len__(self):
        """
        重载LinearSystem的len方法，使得该类能够被len(xx)这种方式使用
        """
        return len(self.planes) if self.planes else 0

    def __getitem__(self, n):
        """
        重载LinearSystem的getitem方法，使得该类能够被类似ls[5]这种方式使用
        """
        return self.planes[n]

    @IndexOutOfBounds
    def swap_rows(self, row1, row2):
        """
        实现方程组中交换行的操作

        Args:
            row1 -- 要交换的行
            row2 -- 要交换的行

        Raises:
            IndexOutOfBounds -- 处理这个函数中可能出现的角标越界异常
        """
        self.planes[row1],self.planes[row2]=self.planes[row2],self.planes[row1]

    @IndexOutOfBounds
    def multiply_coefficient_and_row(self, ratio, row):
        """
        实现方程组中将某一行乘以一定倍数的操作

        Args:
            ratio -- 乘以的系数
            row -- 要乘的行号

        Raises:
            IndexOutOfBounds -- 处理这个函数中可能出现的角标越界异常
        """
        self.planes[row] = Plane(Vector([self.planes[row].a * ratio, self.planes[row].b * ratio, self.planes[row].c * ratio]), self.planes[row].k * ratio)

    @IndexOutOfBounds
    def add_multiple_times_row_to_row(self, ratio, row_to_add, row_to_added_to):
        """
        实现方程组中将某一行乘以一定倍数后加到某一行上的操作

        Args:
            ratio -- 要乘以的系数
            row_to_add -- 加到另一行上的方程，也就是被乘的那个
            row_to_added_to -- 被加的那一行

        Raises:
            IndexOutOfBounds -- 处理这个函数中可能出现的角标越界异常
        """
        row_to_add_plane = Plane(Vector([self.planes[row_to_add].a * ratio, self.planes[row_to_add].b * ratio, self.planes[row_to_add].c * ratio]), self.planes[row_to_add].k * ratio)
        self.planes[row_to_added_to] = Plane(Vector([self.planes[row_to_added_to].a+row_to_add_plane.a, self.planes[row_to_added_to].b+row_to_add_plane.b,
                self.planes[row_to_added_to].c+row_to_add_plane.c]), self.planes[row_to_added_to].k+row_to_add_plane.k)


    def compute_triangular_form(self):
        """
        更抽象封装的方式实现该函数功能
        """
        system = deepcopy(self)

        system.planes.sort() # step 1 : 对planes进行排序，是的符合三角形排列，从上到下，非0项元素角标依次增加

        for i in range(len(system)-2,-1,-1): # step 2 : 将每一行首个不为0的元素对应列其他元素全部消掉
            idx = system[i].first_nonzero_idx
            if not idx is -1:
                for j in range(i+1,len(system)):
                    if j!=i and not LaDecimal(system[j].params[idx]).is_near_zero():
                        system.add_multiple_times_row_to_row(-(system[j].params[idx]/system[i].params[idx]),i,j)

        system.planes.sort() # step 3 : 再度排序避免由于step 2的影响

        return system

    def compute_triangular_form_2(self):
        """
        实现将方程组变化为三角形的函数

        Returns:
            result -- 形状为三角形的新LinearSystem对象

        Notes:
            1 -- 将零系数的行与下列行进行交换时，选择第一个满足要求的行进行交换，例如为了保证第一行的a不为0需要交行时，如果第2,3都满足，选择第2行
            2 -- 不要将某一行乘以系数，也就是调用multiply_coefficient_and_row方法
            3 -- 仅将几倍的行与它下方的行相加，也就是说为了消除第二行的x时，只能用第一行的n倍相加来消除
        """
        system = deepcopy(self)
        #######
        # x
        p1 = system[0]
        if LaDecimal(p1.a).is_near_zero():
            i = 1
            for p in system[i:]:
                if not LaDecimal(p.a).is_near_zero():
                    system.swap_rows(0,i)
                    break
                i += 1
            if i == len(system):
                raise Exception(LinearSystem.NOT_CAN_SWAP_ROW)
        p1 = system[0]
        
        # y
        p2 = system[1]
        if LaDecimal(p2.b).is_near_zero():
            i = 2
            for p in system[i:]:
                if not LaDecimal(p.b).is_near_zero():
                    system.swap_rows(1,i)
                    break
                i += 1
            if i == len(system):
                raise Exception(LinearSystem.NOT_CAN_SWAP_ROW)
        p2 = system[1]


        # z
        for idx in range(2,len(system)):
            pn = system[idx]
            if LaDecimal(pn.c).is_near_zero():
                i = idx + 1
                for p in system[i:]:
                    if not LaDecimal(p.c).is_near_zero():
                        system.swap_rows(idx,i)
                        break
                    i += 1
                if i == len(system):
                    raise Exception(LinearSystem.NOT_CAN_SWAP_ROW)

        # 去x
        for idx in range(1,len(system)):
            p = system[idx]
            p_pre = system[0]
            if not LaDecimal(p.a).is_near_zero():
                system.add_multiple_times_row_to_row(-(p.a/p_pre.a),0,idx)

        # 去y
        for idx in range(2,len(system)):
            p = system[idx]
            p_pre = system[1]
            if not LaDecimal(p.b).is_near_zero():
                system.add_multiple_times_row_to_row(-(p.b/p_pre.b),1,idx)

        # 去z
        for idx in range(3,len(system)):
            p = system[idx]
            p_pre = system[2]
            if not LaDecimal(p.c).is_near_zero():
                system.add_multiple_times_row_to_row(-(p.c/p_pre.c),2,idx)
        #######
        return system

    def compute_rref(self):
        """
        实现将方程式变换为最简梯形的函数

        Returns:
            result -- 形状为梯形且首项系数为1的方程式

        Notes:
            pre handle -- compute_triangular_form获取三角形方程式
            algorithm -- 流程：先将最后一行的第一个非0元素系数化为1，然后将该列所有其他元素化为0，然后倒数第二行，以此类推直至第一行未知
        """

        system = self.compute_triangular_form() # pre handle

        for i in range(len(system)-1,-1,-1):
            p = system[i]
            param_idx = len(p.params)-1 if i>len(p.params)-1 else i 
            if not p.first_nonzero_idx is -1:
                param_make_1 = p.params[p.first_nonzero_idx]
                if not LaDecimal(param_make_1-1).is_near_zero(): # 先将第一个非0元素系数化为1
                    system.multiply_coefficient_and_row(1/param_make_1,i)
                for j in range(len(system)):
                    if j != i:
                        p_make_0 = system[j]
                        param_make_0 = p_make_0.params[p.first_nonzero_idx]
                        ratio = -(param_make_0 / param_make_1)
                        system.add_multiple_times_row_to_row(ratio,i,j) # 将该位置对应列其他元素全部消去

        return system

    def compute_solutions(self):
        """
        实现求方程组解的函数

        Returns:
            status -- 0:该方程组无解 1:该方程有唯一解 -1:该方程组有无数解
            result -- 当方程组有唯一解时，返回该值[x,y,z....]存储该值
        """

        def has_not_solutions(system):
            """
            判断方程式是否无解

            Args:
                system -- 被判断的方程式组

            Notes:
                algorithm -- 判断条件是是否存在0=k，k不为0的情况
            """
            for plane in system:
                params = plane.params
                k = plane.k
                if LaDecimal(k).is_near_zero():
                    break
                all_zero = True
                for p in params:
                    if not LaDecimal(p).is_near_zero():
                        all_zero = False
                        break
                if all_zero:
                    return True

        def has_so_much_solutions(system):
            """
            判断方程式是否有无数的解

            Args:
                system -- 被判断的方程式组

            Notes:
                algorithm -- 判断条件是有用的方程式个数是否不小于需要求的变量的个数
            """
            num_pivots = sum([1 if not p.first_nonzero_idx is -1 else 0 for p in system])
            num_dimension = system[0].dimension
            return num_dimension > num_pivots

        def calc_solution(system):
            """
            求解方程唯一解

            Args:
                system -- 求解的方程式组

            Notes:
                
            """

            return Vector([p.k for p in system[:system[0].dimension]])

        system = self.compute_rref() # 获取方程式对应的rref式
        print system

        if has_not_solutions(system):
            return 0,None
        if has_so_much_solutions(system):
            return -1,None
        return 1,calc_solution(system)


def main():
    """
    程序入口
    """
    enviroment_init()

    p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

    print 'Test swap_rows ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    s = LinearSystem([p0,p1,p2,p3])
    s.swap_rows(0,1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print 'test case 1 failed'

    s.swap_rows(1,3)
    if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
        print 'test case 2 failed'

    s.swap_rows(3,1)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print 'test case 3 failed'
    
    print 'Test multiply_coefficient_and_row ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    s.multiply_coefficient_and_row(1,0)
    if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
        print 'test case 4 failed'
    
    s.multiply_coefficient_and_row(-1,2)
    if not (s[0] == p1 and
            s[1] == p0 and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print 'test case 5 failed'
    
    s.multiply_coefficient_and_row(10,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print 'test case 6 failed'
    
    print 'Test add_multiple_times_row_to_row ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    s.add_multiple_times_row_to_row(0,0,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print 'test case 7 failed'
    
    s.add_multiple_times_row_to_row(1,0,1)
    if not (s[0] == p1 and
            s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print 'test case 8 failed'
    
    s.add_multiple_times_row_to_row(-1,1,0)
    if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
            s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
            s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
            s[3] == p3):
        print 'test case 9 failed'

    print 'Test compute_triangular_form ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
    s = LinearSystem([p1,p2])
    t = s.compute_triangular_form()
    if not (t[0] == p1 and
    	t[1] == p2):
        print 'test case 1 failed'
    
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
    s = LinearSystem([p1,p2])
    t = s.compute_triangular_form()
    if not (t[0] == p1 and
    	t[1] == Plane(constant_term='1')):
        print 'test case 2 failed'
    
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
    s = LinearSystem([p1,p2,p3,p4])
    t = s.compute_triangular_form()
    if not (t[0] == p1 and
    	t[1] == p2 and
    	t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
    	t[3] == Plane()):
        print 'test case 3 failed'
    
    p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
    s = LinearSystem([p1,p2,p3])
    t = s.compute_triangular_form()
    if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
    	t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
    	t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
        print 'test case 4 failed'

    print 'Test computer_rref ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
    s = LinearSystem([p1,p2])
    r = s.compute_rref()
    if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
            r[1] == p2):
        print 'test case 1 failed'
    
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
    s = LinearSystem([p1,p2])
    r = s.compute_rref()
    if not (r[0] == p1 and
            r[1] == Plane(constant_term='1')):
        print 'test case 2 failed'
    
    p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
    s = LinearSystem([p1,p2,p3,p4])
    r = s.compute_rref()
    if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
            r[1] == p2 and
            r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
            r[3] == Plane()):
        print 'test case 3 failed'
    
    p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
    p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
    p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
    s = LinearSystem([p1,p2,p3])
    r = s.compute_rref()
    if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
            r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
            r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
        print 'test case 4 failed'

    """
    print 'Debug:'
    p1 = Plane(normal_vector=Vector(['0','0','3']), constant_term='2')
    p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
    p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
    p4 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
    s = LinearSystem([p1,p2,p3,p4])
    t = s.compute_triangular_form()
    """

    print 'Test compute_rref 求解方程组~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    p1 = Plane(normal_vector=Vector(['5.862','1.178','-10.366']), constant_term='-8.15')
    p2 = Plane(normal_vector=Vector(['-2.931','-0.589','5.183']), constant_term='-4.075')
    s = LinearSystem([p1,p2])
    status,solution = s.compute_solutions()
    print '是否有解：'+str(status)
    print '唯一解：'+str(solution)

    p1 = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
    p2 = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
    p3 = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')
    s = LinearSystem([p1,p2,p3])
    status,solution = s.compute_solutions()
    print '是否有解：'+str(status)
    print '唯一解：'+str(solution)

    p1 = Plane(normal_vector=Vector(['5.262','2.739','-9.878']), constant_term='-3.441')
    p2 = Plane(normal_vector=Vector(['5.111','6.358','7.638']), constant_term='-2.152')
    p3 = Plane(normal_vector=Vector(['2.016','-9.924','-1.367']), constant_term='-9.278')
    p4 = Plane(normal_vector=Vector(['2.167','-13.543','-18.883']), constant_term='-10.567')
    s = LinearSystem([p1,p2,p3,p4])
    status,solution = s.compute_solutions()
    print '是否有解：'+str(status)
    print '唯一解：'+str(solution)

if __name__ == '__main__':
    main()
