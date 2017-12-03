#-*- coding: utf-8 -*-

import math
from decimal import Decimal,getcontext

'''
Vector类实现
判断other是否为null
'''

# 设置Decimal小数的精度范围
getcontext().prec = 30

def tip(list1, list2):
	list3=[]
	for i in range(max(len(list1),len(list2))):
		l1 = Decimal(0) if i >= len(list1) else list1[i]
		l2 = Decimal(0) if i >= len(list2) else list2[i]
		list3.append([l1,l2])
	return list3

class Vector:
	def __init__(self, coordinates):
		self.coordinates = tuple([Decimal(str(me)) for me in coordinates])

	# 判断两个Vector是否相等
	def __eq__(self, other):
        	return (not other is None) and (self.coordinates == other.coordinates)

	# 重载加法运算符
	def __add__(self, other):
    		return None if other is None else Vector([me + him for me, him in tip(self.coordinates, other.coordinates)])

	# 重载减法运算符
	def __sub__(self, other):
    		return None if other is None else Vector([me - him for me, him in tip(self.coordinates, other.coordinates)])

	# 重载乘法运算符为dot products
	def __mul__(self, other):
		return Decimal(str(sum([me * him for me, him in tip(self.coordinates, other.coordinates)])))
	
	# 返回向量与标量相乘的结果
	def mul(self, times):
		return Vector([me * times for me in self.coordinates])

	# 返回向量大小
	def size(self):
		return Decimal(str(math.sqrt(sum([me**Decimal(2) for me in self.coordinates]))))

	# 返回向量的方向向量
	def direction(self):
		try:
			return self.mul(Decimal(1) / self.size())
		except ZeroDivisionError:
			raise Exception('Can not calc direction with zero vector')
	
	# 返回两个向量的夹角弧度
	def angle_rad(self, other):
		try:
			# 此处如果为1.0会报数字域错误，因此如果判断到>=1.0统一返回1
			# 程序中全部使用Decimal来替换浮点数和整数来避免精度问题
			return Decimal(str(math.acos((self * other) / (self.size() * other.size()))))
		except ZeroDivisionError:
			raise Exception('Can not calc angle with zero vector')

	# 返回两个向量的夹角角度
	def angle_deg(self, other):
		return Decimal(str(self.angle_rad(other) * (Decimal(180) / Decimal(str(math.pi)))))

	# 返回两个向量是否平行
	def parallel(self, other):
		return (self.angle_rad(other) == Decimal(1)) or (self.angle_rad(other) == Decimal(-1))

	# 返回两个向量是否正交
	def orthogonal(self, other):
		return self.angle_rad(other) == Decimal(0)

	# 返回向量的字符串表达式
	def __str__(self):
    		return 'Vector:' + str(self.coordinates)


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
# print 'No16:' + str(Vector([0,0]).direction())
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
print 'Notest:' + str(Vector([1,1]).parallel(Vector([2,2])))
print 'Notest:' + str(Vector([1,1]).orthogonal(Vector([2,2])))
