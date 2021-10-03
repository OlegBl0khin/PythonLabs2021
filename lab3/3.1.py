import turtle

A = (0, 0)
B = (50, 0)
C = (0, 50)
D = (50, 50)
E = (0, 100)
F = (50, 100)

zero = [(A, B), (A, E), (B, F), (E, F)]
one = [(C, F), (F, B)]
two = [(E, F), (F, D), (D, A), (A, B)]
free = [(E, F),(F, C), (C, D), (D, A)]
four = [(E, C), (C, D), (F, B)]
five = [(E, F), (E, C), (C, D), (D, B), (B, A)]
six = [(F, C), (C, D), (D, B), (B, A), (A, C)]
seven = [(E, F), (F, C), (C, A)]
eight = [(A, B), (A, E), (B, F), (E, F), (C, D)]
nine = [(C,E), (E, F), (F, D), (D, C), (D, A)]

S1 = [one, four, one, seven, zero, zero]
S2 = [five, six, seven, eight, nine]
n = 0
for i in S1:
    for j in i:
        turtle.penup()
        turtle.goto(j[0][0] + 100*n, j[0][1])
        turtle.pendown()
        turtle.goto(j[1][0] + 100*n, j[1][1])
        turtle.penup()
    n = n + 1