import turtle
import numpy as np

turtle.shape('turtle')


def poly(n):
	
		turtle.penup()
		turtle.goto((n-2) * 5, 0)
		turtle.pendown()
		turtle.left(180/n)
		for i in range(n):
			turtle.forward(5 * n * np.sin(2*np.pi/n))
			turtle.left(360/n)
		turtle.right(180/n)


n = 3
turtle.left(90)
while(True):
	poly(n)
	n = n + 1	


