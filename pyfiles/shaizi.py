#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

'''
生成二维数组[[],[],[],[],[],[]]
1.参数为1：[[1],[2],[3],[4],[5],[6]]
2.参数为2：[[1+1,1+2,1+3,1+4,1+5,1+6]......[6+1,6+2,6+3,6+4,6+5,6+6]]
3.参数为3：[[1+1+1,1+1+2,1+1+3,1+1+4,1+1+5,1+1+6,  1+2+1,1+2+2,1+2+3,1+2+4,1+2+5,1+2+6,]......]
'''
def makeArray(dimension):
    array=[[],[],[],[],[],[]]
    for i in range(dimension):
        if i==0:
            for j in range(6):
                array[j].append(j+1)
        else:
            for j in range(len(array)):
                temp = array[j]
                array[j]=[]
                for k in range(6):
                    for m in range(len(temp)):
                        array[j].append(temp[m]+k+1)
    target = []
    for i in range(len(array)):
        target+=array[i]
    return target

#print 'Please input your dice number:'
#index = int(input())
index = [1,2,3,9]
shaizi = []
for i in range(len(index)):
    shaizi.append(makeArray(index[i]))
count = 100000
for z in range(len(index)):
    x = []
    y = []
    for i in range(count):
        rand = shaizi[z][random.randint(0,len(shaizi[z])-1)]
        if rand not in x:
            x.append(rand)
            y.append(1)
        else:
            y[x.index(rand)]+=1
    plt.figure(z+1)
    plt.scatter([xx/(1.0*(index[z])) for xx in x],y, color='k', s=25, marker="o")
    plt.xlim(0,7)
    plt.ylim(1,count/5)
    plt.xlabel(u'number')
    plt.ylabel(u'count')
    plt.title('Dice : '+str(index[z]))
    plt.legend()

plt.show()
