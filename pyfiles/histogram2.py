#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

'''
实现绘制横坐标为大洲，纵坐标为对应人口数的条形图
'''

continent = ['Asia','South America','North America','Europe','Africa','Antarctica']
population = [[423,78,213,145,310,6],[453,93,243,148,320,10]]
label = ['2010','2015']
color = ['g','b']
bar_width = 0.08
bar_widths = [[0,0.2,0.4,0.6,0.8,1],[0.1,0.3,0.5,0.7,0.9,1.1]]
for i in range(len(population)):
    plt.bar(bar_widths[i], population[i], bar_width, label = label[i], color = color[i])
plt.xticks([0.05,0.25,0.45,0.65,0.85,1.05], continent)
plt.xlabel('continent')
plt.ylabel('population(ten-million)')
plt.title('2010~2015 world population chat')
plt.legend()

plt.show()
