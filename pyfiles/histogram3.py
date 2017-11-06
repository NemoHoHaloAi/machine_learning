#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
实现绘制横坐标为年龄，纵坐标为对应年龄范围的人数的直方图
'''

'''
population_ages = [10,15,20,25,15,20,25,30,20,25,30,35,25,30,35,40]
population_ages = []
for i in range(10000):
    population_ages.append(random.randint(1,110))
'''
population_ages = np.loadtxt('congruent_diff.csv', delimiter=',', unpack=True)
population_ages = sorted(population_ages)
print population_ages[0]
print population_ages[-1]

print 'please input step:'
step = int(input())

bins = []
for i in range(0,int(population_ages[-1]/10*10+10),step):
    bins.append(i)

plt.hist(population_ages, bins, histtype='bar')
plt.xlabel('age')
plt.ylabel('number')
plt.title('histogram for age--count')
plt.legend()

plt.show()
