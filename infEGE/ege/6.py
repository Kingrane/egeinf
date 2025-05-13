from turtle import *
# основные команды
k = 20
screensize(3000, 3000)
dot()
tracer(0)
forward()
right()

# точки
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot()
