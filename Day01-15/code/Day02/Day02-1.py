'''
a = 1
b = 1.2131
c = 'sasda'
d = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
'''
"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: 骆昊
"""
'''
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))
'''
'''
a = 1
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 想想这里会输出什么
'''
'''
centigrade
华氏温度与摄氏温度转换器
'''
'''
a = int(input('华氏温度 = '))
b = float((a-32)/1.8)
print('%.0f华氏温度为 = %.0f摄氏温度 ?%.0f'%(a, b))
'''

'''
圆的计算
'''
'''
import math
a = int(input('R ='))
b = float(a*math.pi*2)
c = float(a**2*math.pi)
print('周长=%.2f 面积=%.2f'%(b, c))
'''
#判断年份是否为闰年
year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(is_leap)