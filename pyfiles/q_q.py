#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
绘制Q-Q图
两组数据各选出99个点将每组数据分为100分，
再将这99个点分别作为横纵坐标绘制出来
'''

array_a,array_b=np.loadtxt('q_q.txt', delimiter=',', unpack=True)
array_a = sorted(array_a)
array_b = sorted(array_b)
np_a = np.array((array_a))
np_b = np.array((array_b))

x=[]
y=[]
#np.percentile(np_a,k)
#计算以np_a为数据集，k%位置对应的数据点
for i in range(1,100):
    x.append(np.percentile(np_a,i))
    y.append(np.percentile(np_b,i))

print x
print y
plt.scatter(x,y, color='k', s=25, marker="o")
_max = array_a[-1] if array_a[-1]>array_b[-1] else array_b[-1]
plt.plot([0,_max+5],[0,_max+5])
plt.xlim(0,_max+5)
plt.ylim(0,_max+5)
plt.title('Q-Q')
plt.legend()
plt.show()
