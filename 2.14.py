import turtle
import numpy as np

turtle.shape('turtle')

def star(n):
	if n % 2 == 1:  			#звезда с нечетным количеством углов 
									
		turtle.penup()				
		turtle.goto(200, 0)
		turtle.pendown()
		turtle.left(90 - 360/(n*4))

		for i in range(n):
			turtle.forward(200 * 2 * np.sin((np.pi - np.pi/n)/2))
			turtle.left(180 - 180/n)

		turtle.right(90 - 360/(n*4))

	elif n % 4 == 0: 			#звезда с четным количеством граней,но те которые можно изоюрахить, не отрывая руки

		turtle.penup()	
		turtle.goto(200, 0)
		turtle.pendown()
		turtle.left(90 - 360/(n*2))

		for i in range(n):
			turtle.forward(200 * 2 * np.cos((np.pi/n)))
			turtle.left(180 - 360/n)
		turtle.right(90 - 360/(n*2))
	else:						# звезды, с четным количеством углов, которые нельзя нарисовать, не отрывая руки

		turtle.penup()
		turtle.goto(200, 0)
		turtle.pendown()
		turtle.left(90 - 360/(n*2))

		for i in range(int(n/2)):
			turtle.forward(200 * 2 * np.cos((np.pi/n)))
			turtle.left(180 - 360/n)
		turtle.right(90 - 360/(n*2))

		turtle.left(90)				# переход (момент когда приходится оторвать руку)
		turtle.penup()
		turtle.forward(200)
		turtle.right(180-360/n)
		turtle.forward(200)
		turtle.left(90)
		turtle.left(90 - 360/(n*2))
		turtle.pendown()			
		for i in range(int(n/2)):
			turtle.forward(200 * 2 * np.cos((np.pi/n)))
			turtle.left(180 - 360/n)
		turtle.right(90 - 360/(n*2))


n = int(input())
turtle.left(90)
star(n)
