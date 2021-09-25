import turtle


with open('trash.txt', 'r') as file:
    K1 = []
    K2 = []
    K3 = []

    cnt = 0
    for line in file:
        line = line.rstrip()
        K1.append(line)
        
        cnt += 1
    
    for i in range(0, cnt - 6):
        K3.append(0)

    for i in range(0, 6):
        K2.append(K1[i])
 
    
    for i in range(len(K2)):
        K2[i] = K2[i].replace('(','')
        K2[i] = K2[i].replace(')','')
        K2[i] = list(map(int, K2[i].split(', ')))

   
    for i in range(6, cnt):
        K3[i - 6] = K1[i].replace("(", '')
        K3[i - 6] = K3[i - 6].replace(")", '')
        K3[i - 6] = list(K3[i - 6].split(", "))

    
    for i in range(cnt - 6):
        for j in range(len(K3[i])):
            if (K3[i][j] == 'A'): K3[i][j] = (K2[0][0], K2[0][1])
            if (K3[i][j] == 'B'): K3[i][j] = (K2[1][0], K2[1][1])
            if (K3[i][j] == 'C'): K3[i][j] = (K2[2][0], K2[2][1])
            if (K3[i][j] == 'D'): K3[i][j] = (K2[3][0], K2[3][1])
            if (K3[i][j] == 'E'): K3[i][j] = (K2[4][0], K2[4][1])
            if (K3[i][j] == 'F'): K3[i][j] = (K2[5][0], K2[5][1])

    S1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

   
    print(K3)
    n = 0
    for i in S1:
        for j in range(len(K3[i])):

            if j % 2 == 0:
                turtle.penup()
                turtle.goto(K3[i][j][0] + 100*n, K3[i][j][1])
                turtle.pendown()
                turtle.goto(K3[i][j + 1][0] + 100*n, K3[i][j + 1][1])
                turtle.penup()  
        n = n + 1
        
   







