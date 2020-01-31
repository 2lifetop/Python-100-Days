'''
求分段函数值
        3x - 5  (x > 2)
f(x) =  x + 2   (-1 <= x <= 2)
        5x + 3  (x < -1)
version：0.2
author：2life.top
date:2020.1.31
'''
x =float(input('请输入X='))
if x > 2:
    y= 3*x-5
elif x >= -1:
    y=x+2
else:
    y= 5*x + 3
print ('f(%.2f)=(%.2f)'%(x,y))