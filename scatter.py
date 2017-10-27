#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
散点图，每个年龄与人数的展示
'''
x = []
y = []
for i in range(30):
    while True:
        rand = random.randint(10,110)
        if rand not in x:
            x.append(rand)
            y.append(random.randint(100,10000))
            break

plt.scatter(x,y, color='k', s=25, marker="o")
plt.xlabel(u'年龄')
plt.ylabel(u'人数')
plt.title('Scatter Plot')
plt.legend()

plt.show()
