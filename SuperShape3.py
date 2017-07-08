import turtle
import random

turtle.width(5)
turtle.speed(4000)
turtle.pencolor("white")
turtle.bgcolor("black")

def turfp3 ():
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor("red")
	for i in range(10):
		turtle.forward(100)
		turtle.left(80)
		turtle.forward(100)
		turtle.right(120)
		
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