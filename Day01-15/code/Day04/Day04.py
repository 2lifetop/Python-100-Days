import random
answer = random.randint(1,100)
counter = 0
while True :
    counter += 1
    number=int(input('输入你所猜的数：'))
    if number > answer:
        print('稍微大了一点')
    elif number < answer: 
        print('稍微小了一点')
    else:
        print('你猜对了')
        break
#用break终止循环
print ('你一共猜了%d次'% counter)
if counter <= 7:
    print('你真聪明')
elif counter <= 10:
    print('你是一个普通人')
else:
    print('你的智商堪忧啊')

