#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
饼图，反应一个人一天的时间分布
'''

slices = [7,2,2,13]
activities = ['sleeping','eating','working','playing']
cols = ['c','m','r','b']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0.2,0.1,0,0.3),
        autopct='%1.1f%%')

plt.title('Pie Chat')

plt.show()
