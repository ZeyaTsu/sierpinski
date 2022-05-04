

from turtle import *
import turtle
turtle.setup(1920, 1080)
turtle.bgcolor("black")
turtle.speed(5000000000)
turtle.goto(-80,-80)
shape("triangle")
fillcolor("yellow")
right(30)
pu()
ht()



def sier(size, order):
	if order == 0:
		stamp()
	else:

		for i in range(0, 3):

			turtle.color("cyan")
			forward(size)
			sier(size/2, order-1)
			backward(size)
			left(120)

sier(300, 6)







mainloop()

