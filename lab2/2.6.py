import turtle

turtle.shape('turtle')
n = int(input())
for i in range(n):
	turtle.forward(100)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(100)
	turtle.left(180)
	turtle.left(360/n)
	