'''
已知半径求圆的面积、周长
'''
import math
r=int(input('R='))
def area(r):
    result = math.pi*r**2
    return result
print(area(r))

def perimeter(r):
    result =math.pi*r*2
    return result
print(perimeter(r))