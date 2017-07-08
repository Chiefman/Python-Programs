import turtle
import random

turtle.width(5)
turtle.speed(4000)
turtle.pencolor("white")
turtle.bgcolor("black")
mycolour = ["red", "blue", "green", "yellow"]

def turfp3 ():
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(6):
		turtle.forward(50)
		turtle.left(70)
		turtle.forward(50)
		turtle.right(140)
		turtle.forward(100)
		turtle.left(140)
		turtle.forward(100)
		turtle.right(130)
		
	turtle.penup()
	return
	
def turfps (): # four pointed start
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor("red")
	for i in range(4):
		turtle.forward(100)
		turtle.left(50)
		turtle.forward(100)
		turtle.right(140)
		
	turtle.penup()
	return
	
#turfps()
turfp3()

turtle.done()