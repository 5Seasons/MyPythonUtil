# python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]
from matplotlib import pyplot as plt
from numpy import random as random
from matplotlib import rc as rc
from matplotlib import font_manager as fm
import numpy as np
x=range(30)
y=[]
for a in x:
    y.append(random.randint(0,high=10))
#figsize 宽高 dpi dot per inch
fig=plt.figure(figsize=(30,10),dpi=80)
# font = {'family' : 'MicroSoft YaHei',
#               'weight' : 'bold',
#               'size'   : 'xx-large'}
# rc('font', **font)
font=fm.FontProperties(fname="C:\Windows\Fonts\simfang.ttf")
plt.plot(x,y)
# X轴刻度 步长为2
x_labels = ["第{}个".format(i) for i in x]
plt.xticks(x,x_labels,rotation=45,fontproperties=font)
plt.xlabel("试试",fontproperties=font)
plt.title("标题",fontproperties=font)
plt.show()
plt.savefig("D:\project\py\dada.png")
#矢量格式保存
#plt.savefig("D:\project\py\dada.svg")
#Add something and push using SSH

from matplotlib import pyplot as plt
from matplotlib import font_manager as fm
x=range(11,30)
y1=[1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1]
y2=[1,0,3,1,2,4,3,2,1,1,1,1,1,1,1,1,1,1,1]
maxy1=y1.index(max(y1))
maxy2=y2.index(max(y2))
miny1=y1.index(min(y1))
miny2=y2.index(min(y2))
plt.figure(figsize=(20,10))
plt.plot(x,y1,label="我",color="orange",linestyle=":")
# 标注最大点
plt.annotate("123",xy=(maxy1+11,y1[maxy1]),textcoords='offset points')
plt.plot(x,y2,label="他",color="cyan",linestyle="--")
# linewidth粗细 alpha 透明度
myft=fm.FontProperties(fname="C:\Windows\Fonts\simfang.ttf")
plt.xticks(x,["{}岁".format(i) for i in x],fontproperties=myft)
plt.yticks(y,["{}个".format(i) for i in y],fontproperties=myft)
plt.xlabel("年龄",fontproperties=myft)
plt.ylabel("个数",fontproperties=myft)
plt.legend(prop=myft)
plt.grid()
plt.show()
