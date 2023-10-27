# turtle-თი რენდომ რიცხვებით დახაზეთ შედევრი  
# forward(random.randint(100))

# import turtle
from turtle import *
# import random
from random import randint

pensize(10)
colormode(255)

while True:
    color(randint(0, 255), 
          randint(0, 255), 
          randint(0, 255))
     
    begin_fill()
    circle(20)
    end_fill()
    penup()
    pendown()
    forward(200)
    left(50)
    right(1)
    speed(50000)
    goto(0,5)
     
    goto(randint(-500, 500), randint(-300, 270))
    width(30)

    pendown()

