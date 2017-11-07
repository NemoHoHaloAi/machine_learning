#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
绘制Q-Q图
'''

array_a,array_b=np.loadtxt('q_q.txt', delimiter=',', unpack=True)
array_a = sorted(array_a)
array_b = sorted(array_b)
x=[]
y=[]
for i in range(len(array_b)):
    v = array_b[i]
    x.append(1.0*(i+1)/len(array_b)*100)
    for j in range(len(array_a)):
        if v <= array_a[j] or j == len(array_a)-1:
            y.append(1.0*(j+1)/len(array_a)*100)
            break

print x
print y
plt.scatter(x,y, color='k', s=25, marker="o")
#_max = array_a[-1] if array_a[-1]>array_b[-1] else array_b[-1]
plt.plot([0,120],[0,120])
plt.xlim(0,120)
plt.ylim(0,120)
plt.title('Q-Q')
plt.legend()
plt.show()
