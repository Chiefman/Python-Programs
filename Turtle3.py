import turtle
import random
disp = 0
jumpx = 500
jumpy = 250
turtle.width(10)
turtle.speed(4000)
turtle.pencolor("blue")
turtle.bgcolor("black")

def turcir ():
	turtle.pendown()
	turtle.pencolor("red")
	for i in range(120):
		turtle.forward(1)
		turtle.right(3)
	turtle.penup()
	return

def turtri ():
	turtle.pendown()
	turtle.pencolor("blue")
	for i in range(3):
		turtle.left(120)
		turtle.forward(40)
	turtle.penup()
	return

def tursqr ():
	turtle.pendown()
	turtle.pencolor("green")
	for i in range(4):
		turtle.forward(40)
		turtle.right(90)
	turtle.penup()
	return
	
def turpen ():
	turtle.pendown()
	turtle.pencolor("purple")
	for i in range(5):
		turtle.left(72)
		turtle.forward(30)
	turtle.penup()
	return
	
def turhex ():
	turtle.pendown()
	turtle.pencolor("cyan")
	for i in range(6):
		turtle.forward(25)
		turtle.right(60)
	turtle.penup()
	return
	
def turoct ():
	turtle.pendown()
	turtle.pencolor("yellow")
	for i in range(8):
		turtle.forward(17)
		turtle.right(45)
	turtle.penup()
	return
	
def tursta ():
	turtle.pendown()
	turtle.pencolor("violet")
	for i in range(5):
		turtle.right(144)
		turtle.forward(45)
	turtle.penup()
	return

while (disp == 0):
	myshapes = [turcir, turtri, tursqr, turpen, turhex, turoct,tursta]
	turtle.penup()
	turtle.setposition((random.randint(-jumpx,jumpx)), (random.randint(-jumpy,jumpy)))
	random.choice(myshapes)()
	
# for disp in range(300):
	# myshapes = [turcir, turtri, tursqr, turpen, turhex, turoct]
	# turtle.penup()
	# turtle.setposition((random.randint(-jumpx,jumpx)), (random.randint(-jumpy,jumpy)))
	# random.choice(myshapes)()
turtle.done()
