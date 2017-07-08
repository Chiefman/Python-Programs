import turtle
import random
disp = 0
jumpx = 600
jumpy = 300
turtle.width(.1)
turtle.speed(4000)
#turtle.pencolor("blue")
turtle.bgcolor("black")
#mycolour = ["red", "blue", "green", "yellow", "purple", "cyan", "violet", "grey", "tomato", "LightBlue", "Lightgreen", ]
mycolour = ["red", "blue", "green", "yellow",]

def turcir ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(55):
		turtle.forward(3)
		turtle.right(7)
	turtle.penup()
	return

def turtri ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(3):
		turtle.left(120)
		turtle.forward(40)
	turtle.penup()
	return

def tursqr ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(4):
		turtle.forward(40)
		turtle.right(90)
	turtle.penup()
	return
	
def turpen ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(5):
		turtle.left(72)
		turtle.forward(30)
	turtle.penup()
	return
	
def turhex ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(6):
		turtle.forward(25)
		turtle.right(60)
	turtle.penup()
	return
	
def turoct ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(8):
		turtle.forward(17)
		turtle.right(45)
	turtle.penup()
	return
	
def tursta ():
	turtle.pendown()
	turtle.pencolor (random.choice(mycolour))
	for i in range(5):
		turtle.right(144)
		turtle.forward(45)
	turtle.penup()
	return
	
def turstr (): #Super Triangle shape
	turtle.pendown()
	turtle.right(80)
	turtle.pencolor (random.choice(mycolour))
	for i in range(3):
		turtle.forward(25)
		turtle.left(40)
		turtle.forward(25)
		turtle.right(160)
		
	turtle.penup()
	return
	
def turfps (): # four pointed start
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(4):
		turtle.forward(20)
		turtle.left(50)
		turtle.forward(20)
		turtle.right(140)
		
	turtle.penup()
	return
def turfp2 (): # four pointed start version 2 
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(4):
		turtle.forward(20)
		turtle.left(70)
		turtle.forward(20)
		turtle.right(160)
		
	turtle.penup()
	return
def turfp3 ():
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(6):
		turtle.forward(17)
		turtle.left(80)
		turtle.forward(17)
		turtle.right(140)
		
	turtle.penup()
	return

def turfp4 ():
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(10):
		turtle.forward(12)
		turtle.left(80)
		turtle.forward(12)
		turtle.right(120)
		
	turtle.penup()
	return

def turfp5():
	turtle.pendown()
	turtle.right(70)
	turtle.pencolor (random.choice(mycolour))
	for i in range(6):
		turtle.forward(9)
		turtle.left(70)
		turtle.forward(9)
		turtle.right(140)
		turtle.forward(18)
		turtle.left(140)
		turtle.forward(18)
		turtle.right(130)
		
	turtle.penup()
	return
	

while (disp == 0):
	myshapes = [turcir, turtri, tursqr, turpen, turhex, turoct,tursta, turstr, turfps, turfp2, turfp3, turfp4, turfp5]
	turtle.penup()
	turtle.setposition((random.randint(-jumpx,jumpx)), (random.randint(-jumpy,jumpy)))
	random.choice(myshapes)()
	
# for disp in range(300):
	# myshapes = [turcir, turtri, tursqr, turpen, turhex, turoct]
	# turtle.penup()
	# turtle.setposition((random.randint(-jumpx,jumpx)), (random.randint(-jumpy,jumpy)))
	# random.choice(myshapes)()

turtle.done()
