"""

task 9.16 page 51
fill array with integers

"""
n = 10
matrix1 = [[0 for i in range(n)] for i in range(n)]
for i in range(n):          #task A
    matrix1[i][i] = i
    print(matrix1[i])

loc = 1         #taskB
for i in range(n):
    for j in range(n):
        matrix1[i][j] = loc
        loc +=1
    print(matrix1[i])