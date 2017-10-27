#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

'''
实现绘制横坐标为年龄，纵坐标为对应年龄范围的人数的直方图
'''
print 'please input step:'
step = int(input())

population_ages = [22,55,62,45,21,22,34,42,42,4,99,80,75,65,54,44,43,42,48]
population_ages = sorted(population_ages)
print population_ages

bins = []
for i in range(0,population_ages[-1]/10*10+10,step):
    bins.append(i)
print bins

plt.hist(population_ages, bins, histtype='bar')
plt.xlabel('age')
plt.ylabel('number')
plt.title('histogram for age--count')
plt.legend()

plt.show()
