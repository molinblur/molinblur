import turtle as t
import datetime as dt
import time

# 创建窗口, 背景
game = t.Screen()
game.bgcolor('white')
game.setup(600, 600)
game.tracer(0)  #自动更新频率0

# 画圈
pen = t.Turtle()
pen.ht()  # 隐藏
pen.speed(0)
pen.pensize(3)
pen.up()


def draw_clock(h, m, s):
    pen.clear()
    pen.pensize(3)
    pen.up()
    pen.color('black')
    pen.goto(0, -210)
    pen.down()
    pen.setheading(0)  # 设定画笔的方向
    pen.circle(210)

    # 刻度
    for _ in range(12):
        pen.up()
        pen.goto(0, 0)
        pen.setheading(90 + _ * 30)
        pen.fd(190)
        pen.down()
        pen.fd(20)

    # 时针
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.pensize(7)
    pen.setheading(90)
    pen.rt((h + m/60)/12*360)
    pen.color('blue')
    pen.fd(90)

    # 分针
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.pensize(5)
    pen.setheading(90)
    pen.rt((m + s/60) / 60 * 360)
    pen.color('yellow')
    pen.fd(130)

    # 秒针
    pen.up()
    pen.goto(0, 0)
    pen.down()
    pen.pensize(2)
    pen.setheading(90)
    pen.rt(s / 60 * 360)
    pen.color('black')
    pen.fd(150)

    # 标题
    pen.up()
    pen.goto(-130, 260)
    pen.color('black')
    font = ('Arial', 20, 'bold')
    hello = "Today is {}-{}-{}.".format(now.year, now.month, now.day)
    pen.write(hello, 'center', font=font)

    pen.up()
    pen.goto(-150, 230)
    pen.color('black')
    pen.write("     Happy Every Tian!", 'center', font=font)


now = dt.datetime.now()
draw_clock(now.hour, now.minute, now.second)

while True:
    game.update()
    time.sleep(1)
    now = dt.datetime.now()
    draw_clock(now.hour, now.minute, now.second)



