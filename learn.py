# -*- coding: UTF-8 -*-
print(7**3)
print(min(1, 2, 3))
print(max(1, 2, 3))
print(abs(32))
print(abs(-32))
print(float(10))
print(int(3.33))
# They can even be called on strings!
print(int('807') + 1)
print(type(10))
help(print)
help(round(-2.01))
print(ccs.encode('我'))
# _means the value return from last line of code in Interactive mode or python cmd.
# j**2=-1 e.g. 3+5j
print('"Yes," they said.')
print("""
This is paragraph:
o
""")
# \ will avoid /n ahead of the paragraph and the end of paragraph.
print("""\
This is paragraph:
o
""")
print('Put several strings within parentheses '
         'to have them joined together.')
print('abcdec'[:3])
squares=[1,2,3,4,5]
squares=squares+['a',"b",'c']
# clear the list by replacing all the elements with an empty list
squares[:] = []

#斐波那契数列
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

print(_,end=',')
# output for below line
range(0, 10, 3)

for n in range(10):
    for x in range(2):
        if n == 2:
            # Means do nothing.
            pass
    else:
        print('no')

def cheeseshop(kind, *arguments, **keywords):
# *arguments几个变量，**keywords 几个键值对
    pass
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# 结果为[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

def myfunction():
    "abc"
    pass
print(myfunction.__doc__)

class MyClass:
    def _donothing():
        "lalal"
        pass
    pass
print(MyClass._donothing.__doc__)

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]


[[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]、

# 转置数组
list(zip(_))

#tuple无法修改 但是可以包含可修改的元素。
_tuple=(1,2,3)
_tuple
# 下面会出错
_[0]=2

import sys
# 当使用python编译本类时传入的参数
sys.argv[0]

import scipy
# 包寻找的顺序，当前文件夹，path目录，python自带包。
a=[1,2,4]
b=[1,3,4]
for i in range(max(len(a),len(b))):
    print(a[i],b[i],"\b",end='')
    print(' ',end='')
pass

[print(a[i],b[i],' ',end='') for i in range(len(a))]