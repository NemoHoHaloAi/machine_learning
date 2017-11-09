#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
绘制Q-Q图
两组数据各选出99个点将每组数据分为100分，
再将这99个点分别作为横纵坐标绘制出来
'''
normal = [-1.28,-0.84,-0.52,-0.25,0,0.25,0.52,0.84,1.28]

array_a,array_b=np.loadtxt('q_q.txt', delimiter=',', unpack=True)
array_a = sorted(array_a)
array_b = sorted(array_b)

np_a = np.array((array_a))
np_b = np.array((array_b))
np_normal = np.array((normal))

x_a=[]
y_a=[]
x_b=[]
y_b=[]
#计算以np_xx为数据集，i%位置对应的数据点
for i in range(1,100):
    x_a.append(np.percentile(np_normal,i))
    y_a.append(np.percentile(np_a,i))
    x_b.append(np.percentile(np_normal,i))
    y_b.append(np.percentile(np_b,i))

print x_a
print y_a
print x_b
print y_b

plt.figure(0)
plt.scatter(x_a,y_a, color='k', s=25, marker="o")
plt.title('Q-Q')
plt.legend()
plt.figure(1)
plt.scatter(x_b,y_b, color='b', s=25, marker="o")
plt.title('Q-Q')
plt.legend()
plt.show()
