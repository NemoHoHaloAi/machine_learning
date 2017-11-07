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
np_a = np.array((array_a))
np_b = np.array((array_b))

x=[]
y=[]
for i in range(len(array_b)):
    v = array_b[i]
    for k in range(0,1000,1):
        if np.percentile(np_a,k/10.0) > v or k==999:
            x.append(k/10.0)
            break
    for k in range(0,1000,1):
        if np.percentile(np_b,k/10.0) > v or k==999:
            y.append(k/10.0)
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
