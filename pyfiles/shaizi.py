#-*- coding: utf-8 -*-
  2 
  3 import matplotlib.pyplot as plt
  4 import numpy as np
  5 import random
  6 
  7 '''
  8 生成二维数组[[],[],[],[],[],[]]
  9 1.参数为1：[[1],[2],[3],[4],[5],[6]]
 10 2.参数为2：[[1+1,1+2,1+3,1+4,1+5,1+6]......[6+1,6+2,6+3,6+4,6+5,6+6]]
 11 3.参数为3：[[1+1+1,1+1+2,1+1+3,1+1+4,1+1+5,1+1+6,  1+2+1,1+2+2,1+2+3,1+2+4,1+2+5,1+2+6,]......]
 12 '''
 13 def makeArray(dimension):
 14     array=[[],[],[],[],[],[]]
 15     for i in range(dimension):
 16         if i==0:
 17             for j in range(6):
 18                 array[j].append(j+1)
 19         else:
 20             for j in range(len(array)):
 21                 temp = array[j]
 22                 array[j]=[]
 23                 for k in range(6):
 24                     for m in range(len(temp)):
 25                         array[j].append(temp[m]+k+1)
 26     target = []
 27     for i in range(len(array)):
 28         target+=array[i]
 29     return target
 30 
 31 #print 'Please input your dice number:'
 32 #index = int(input())
 33 index = [1,2,3,6,8,10]
 34 shaizi = []
 35 for i in range(len(index)):
 36     shaizi.append(makeArray(index[i]))
 37 count = 100000
 38 for z in range(len(index)):
 39     x = []
 40     y = []
 41     for i in range(count):
 42         rand = shaizi[z][random.randint(0,len(shaizi[z])-1)]
 43         if rand not in x:
 44             x.append(rand)
 45             y.append(1)
 46         else:
 47             y[x.index(rand)]+=1
 48     plt.figure(z+1)
 49     plt.scatter([xx/(1.0*(index[z])) for xx in x],y, color='k', s=25, marker="o")
 50     plt.xlim(0,7)
 51     plt.ylim(1,count/5)
 52     plt.xlabel(u'number')
 53     plt.ylabel(u'count')
 54     plt.title('Dice : '+str(index[z]))
 55     plt.legend()
 56 
 57 plt.show()
