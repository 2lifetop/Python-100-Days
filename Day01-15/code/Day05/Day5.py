'''
num = int(input('num= '))
t =0
while num > 0:
    t = t*10 + num % 10
    num //= 10
print('t=%d' %t)
'''
# 百钱百鸡
'''
for x in range(0,20): 
    for y in range(0,33):
        z = 100 -x-y
        if 5*x+3*y+z/3 == 100:
            print(x,y,z)
'''
from random import randint
money = 10000
while money > 0:
    print('你的资产为：%d' %money)
    need_go_on = False
    while True:
        debt=int(input('请下注'))
        if 0<debt<=money:
            break
    first =randint(1,6)+randint(1,6)
    print('玩家摇出了%d点'%first)
    if first == 7 or first ==11:
        print('玩家胜')
        money+=debt
    elif first==2 or first==3 or first==12:
        print('庄家胜')
        money-=debt
    else:
        need_go_on = True
    while need_go_on:
        need_go_on =False
        current=randint(1,6)+randint(1,6)
        print('玩家摇出了%d'%current)
        if current== 7:
            print('庄家胜')
            money-=debt
        elif current ==first:
            print('玩家胜')
            money+=debt
        else:
            need_go_on=True
print('你破产了')       
        

