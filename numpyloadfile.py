#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
使用numpy模块加载csv格式文件
'''
x, y = np.loadtxt('example.txt', delimiter=',', unpack=True)
plt.plot(x,y, label='Data from example')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Numpy load file to draw img')
plt.legend()
plt.show()
