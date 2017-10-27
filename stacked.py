#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
堆叠图，一周五天，每天的时间使用分布情况
'''

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating =   [2,3,4,3,2]
working =  [7,8,7,2,2]
playing =  [8,5,7,8,13]
plt.stackplot(days, sleeping, eating, working, playing, labels=['sleeping','eating','working','playing'], colors=['m','c','r','k'])
plt.xlabel('date')
plt.ylabel('hours')
plt.title('Stacked for DayTimeUse')
plt.legend()

plt.show()
