import turtle

turtle.shape('turtle')
turtle.left(90)
n = 0
while(True):
	for i in range(90):
		turtle.forward(4 + n)
		turtle.right(4)
	for i in range(90):
		turtle.forward(4 + n)
		turtle.left(4)
	n = n + 1