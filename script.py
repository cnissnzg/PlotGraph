import os
import sys
import re
import numpy as np

import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

str = open('logdat.txt', 'r').read()
result = re.findall('\[.*\]\s*\d*\s*(\d*)\s\(',str)
output = ''
avgs = []
avgnum = []
for txt in result:
    output += txt+'\n'
    avgnum.append(float(txt) / 1000.0)
    if(len(avgnum)==10):
        avgs.append(np.mean(avgnum).astype('str'))
        avgnum.clear()
    #print(txt)
print(avgs)

f = open('output.txt', 'w')
f.write(','.join(avgs[0:24]))
f.write('\n')
f.write(','.join(avgs[24:48]))
f.write('\n')
f.write(','.join(avgs[48:]))






x = range(1,25)
y_read = avgs[0:24]
y_nstore=avgs[24:48]
y_nclwb=avgs[48:]
plt.plot(x, y_read, marker='^',label=u'Read')
plt.plot(x, y_nstore, marker='v',label=u'Write(nstore)')
plt.plot(x, y_nclwb, marker='o',label=u'Write(clwb)')
plt.legend()  # 让图例生效
plt.xticks(x, x, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"# Threads") #X轴标签
plt.ylabel("Bandwidth (GB/s)") #Y轴标签
plt.title("Optane") #标题

plt.show()