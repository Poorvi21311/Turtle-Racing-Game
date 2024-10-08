import turtle
from turtle import *
from random import *
import time

#screen
setup(800,500)
title("Turtle Race")
bgcolor("green")
speed(0)


#heading
penup()
goto(-100,205)
color("white")
write("Turtle Race", font=("arial",20,"bold"))

#racing path area
goto(-350,200)
color("chocolate")
begin_fill()
for i in range (2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

#turtles

player_1=Turtle()
player_1.color("blue")
player_1.shape("turtle")
player_1.shapesize(2)
player_1.penup()
player_1.goto(-300,150)
player_1.pendown()

player_2=Turtle()
player_2.color("purple")
player_2.shape("turtle")
player_2.shapesize(2)
player_2.penup()
player_2.goto(-300,50)
player_2.pendown()

player_3=Turtle()
player_3.color("green")
player_3.shape("turtle")
player_3.shapesize(2)
player_3.penup()
player_3.goto(-300,-50)
player_3.pendown()

player_4=Turtle()
player_4.color("pink")
player_4.shape("turtle")
player_4.shapesize(2)
player_4.penup()
player_4.goto(-300,-150)
player_4.pendown()


#finish line

gap_size=20
shape("square")
penup()
color("white")
for i in range (10):
    goto(250,(170-((i*gap_size*2))))
    stamp()

while player_1.xcor()<=250 and player_2.xcor()<=250 and player_3.xcor()<=250 and player_4.xcor()<=250:
    player_1.forward(randint(1,10)) 
    player_2.forward(randint(1,10))
    player_3.forward(randint(1,10))
    player_4.forward(randint(1,10))

#winner
if player_1.xcor()>player_2.xcor() and player_1.xcor()>player_3.xcor() and player_1.xcor()>player_4.xcor():
    print("player 1 turtle wins!")
    penup()
    goto(-350,180)
    pendown()
    turtle.write("player 1 turtle wins!!",font=("arial",25,"bold"))
    for i in range(72):
        player_1.right(5)
        player_1.shapesize(2.5)
        
elif player_2.xcor()>player_3.xcor() and player_2.xcor()>player_4.xcor() and player_2.xcor()>player_1.xcor():
    print("player 2 turtle wins!")
    penup()
    goto(-350,180)
    pendown()
    turtle.write("player 2 turtle wins!!",font=("arial",25,"bold"))
    for i in range(72):
        player_2.right(5)
        player_2.shapesize(2.5)
elif player_3.xcor()>player_1.xcor() and player_3.xcor()>player_2.xcor() and player_3.xcor()>player_4.xcor():
    print("player 3 turtle wins!")
    penup()
    goto(-350,150)
    pendown()
    turtle.write("player 3 turtle wins!!",font=("arial",25,"bold"))
    for i in range(72):
        player_3.right(5)
        player_3.shapesize(2.5)
else:

    print("player 4 turtle wins!")
    penup()
    goto(-350,150)
    pendown()
    turtle.write("player 4 turtle wins!!",font=("arial",25,"bold"))
    for i in range(72):
        player_4.right(5)
        player_4.shapesize(2.5)


mainloop()
