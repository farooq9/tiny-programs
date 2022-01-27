#twitter log
from turtle import *
import turtle 
farooq = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
farooq.pensize(2)
farooq.color('#00acee')
screen.setup(710, 600)
turtle.title('Twitter Logo by Farooq')

def big_circle():
    # Abdul Farooq
    farooq.penup()  #big circle
    farooq.goto(0, 0)
    farooq.fd(214)
    farooq.rt(90)
    farooq.pendown()

    farooq.begin_fill()
    farooq.fillcolor('#00acee')
    farooq.circle(-250, 360)
    farooq.end_fill()
    farooq.lt(90)

farooq.speed(10)
def twitter_logo():
    farooq.pencolor('white')
    farooq.penup()
    farooq.goto(0,0)
    farooq.lt(90)
    farooq.fd(44)
    farooq.pendown()

    farooq.begin_fill()
    farooq.fillcolor('white')
    farooq.lt(21)
    farooq.circle(-55, 175)  #bird head

    farooq.lt(94)
    farooq.fd(48)  #beak
    farooq.rt(130)
    farooq.circle(-50, 55) #upper beak
    farooq.lt(186)  #lower beak
    farooq.rt(40)
    farooq.circle(60, 44)
    farooq.rt(150)  #beak lower lower
    farooq.circle(-74, 46)

    farooq.lt(70)  #lower body
    farooq.circle(-200, 123)
    farooq.rt(148)  #upper body
    farooq.circle(146, 42)

    farooq.lt(159)   #bottom wing 1
    farooq.circle(-54, 91)
    farooq.rt(133)    
    farooq.circle(51, 42)

    farooq.lt(154)   #wing 2
    farooq.circle(-67, 82)
    farooq.rt(118)
    farooq.circle(59, 44)

    farooq.lt(160)   #wing 3
    farooq.circle(-66, 102)
    farooq.rt(118)
    farooq.circle(200, 62)
    farooq.end_fill()


big_circle()
twitter_logo()




farooq.hideturtle()
done()
