import turtle
import numpy as np

def circle(r, x, y, a):	    # функция построения дуги, принимает в себя радиус, координаты центра, и угол дуги 
	turtle.penup()
	turtle.goto(x + r, y)
	turtle.pendown()
	for i in range(int(a/4)):
		turtle.forward(4.0*r/360*np.pi*2)
		turtle.left(4)

turtle.shape('turtle')

turtle.color("yellow")			# Желтое лицо
turtle.left(90)
turtle.begin_fill()
circle(100, 0, 0, 360)
turtle.end_fill()

turtle.color("red")				# Красные глаза

turtle.begin_fill() 
circle(10, -40, 50, 360)        # Левый глаз
turtle.end_fill()


turtle.begin_fill()
circle(10, 40, 50, 360)			# Правый глаз
turtle.end_fill()

turtle.color("black")
								# Черный нос

turtle.penup()
turtle.goto(-10, 10)
turtle.pendown()
turtle.width(10)
turtle.forward(20)

	
turtle.color("green")			# Рот, не использовали функцию, потому что она строит дуги в другую сторону
turtle.penup()
turtle.goto(50, 0)		
turtle.pendown()
turtle.left(180)
for i in range(int(180/4)):
	turtle.forward(4.0*50/360*np.pi*2)
	turtle.right(4)







