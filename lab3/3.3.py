import turtle

turtle.shape('turtle')

x = 0
y = 0
Vx = 10
Vy = 50
a = 10
dt = 0.01
for t in range(0, 10000, 1):
    turtle.goto(x, y)
    x = x + dt*Vx
    y = y + dt*Vy 
    Vy = Vy - a*dt
    if(y < 0):
        Vy = -Vy*0.8
        Vx = Vx*0.6
