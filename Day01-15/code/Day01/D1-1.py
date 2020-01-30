"""
用Python的turtle模块画简单图形
"""
import turtle
def draw_rectangle (x, y, width,height):
    "绘制矩形"
    turtle.goto(x, y)
    turtle.pencolor('red')
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)   
        turtle.left(45)#角度
        turtle.forward(height)
        turtle.left(135)
    turtle.end_fill()
def main():
    '主程序'
    turtle.speed(1)
    turtle.penup()
    x, y = -0, -0#起始点
    width, height = 540, 360#长宽
    draw_rectangle(x, y, width, height)
    turtle.ht() #隐藏箭头
    turtle.mainloop() #显示绘图窗口
if __name__ == "__main__":
    main()


