import turtle
from random import *

turtle.shape('turtle')

for i in range(10000):
    turtle.forward(random()*20)
    turtle.left(random()*360)