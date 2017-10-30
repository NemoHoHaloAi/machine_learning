#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random

x = []
y = []
print 'Please input your dice number:'
index = int(input())-1
print index
shaizi = []
#0,1,2
for i in range(5):
    shaizi.append([])
    #6,36,216
    for j in range(6**(i+1)):
	count = (j/(6**i)+1) + (j%6+1)*i
	shaizi[i].append(count)
for i in range(len(shaizi)):
    print shaizi[i]
for i in range(10000):
    rand = shaizi[index][random.randint(0,len(shaizi[index])-1)]
    if rand not in x:
        x.append(rand)
        y.append(1)
    else:
	y[x.index(rand)]+=1
plt.scatter([xx/(1.0+index) for xx in x],y, color='k', s=25, marker="o")
plt.ylim(1,10000/((index+1)**2))
plt.xlabel(u'色子数值')
plt.ylabel(u'数值对应个数')
plt.title('Shaizi Plot')
plt.legend()

plt.show()
