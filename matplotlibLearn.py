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
plt.save("D:\project\py\dada.png")
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

a=["a","b","c","d"]
b_1 = [15746,312,4497,319]
b_2 = [12357,156,2045,168]
b_3 = [2358,399,2358,362]
step=0.2
x_1=list(range(len(a)))
x_2=[i+step for i in x_1]
x_3=[i+step for i in x_2]
plt.bar(x_1,b_1,width=step,color='#DCDCDC')
plt.bar(x_2,b_2,width=step)
plt.bar(x_3,b_3,width=step)
plt.xticks(x_2,a)
plt.show()

#直方图
#a is from [random.randint(0,250) for i in range(100)]
a=[202, 217, 185, 130, 238, 57, 146, 165, 80, 166, 164, 72, 204, 37, 98, 143, 117, 166, 77, 149, 48, 181, 154, 218, 245, 193, 169, 25, 110, 21, 4, 109, 60, 61, 227, 24, 58, 129, 39, 16, 11, 81, 85, 161, 37, 7, 217, 153, 151, 139, 158, 126, 57, 210, 240, 174, 209, 139, 95, 40, 162, 200, 85, 158, 48, 42, 202, 25, 199, 19, 227, 94, 217, 115, 135, 209, 53, 54, 135, 232, 106, 215, 5, 79, 60, 166, 198, 124, 79, 39, 153, 241, 122, 73, 102, 88, 187, 28, 175, 94]
plt.figure(figsize=(20,8),dpi=80)
plt.hist(a,(max(a)-min(a))//20,normed=1)
# plt.hist(a,(max(a)-min(a))//20,normed=1) 频率直方图
plt.xticks(range(min(a),max(a),20))
plt.grid()
plt.show()

# plotly 可视化工具的github。 很漂亮