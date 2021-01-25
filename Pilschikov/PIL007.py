# task 9.16 page 51
# fill array with integers
n = 10
m = 10
matrix1 = []
matrix1 = [[row[i] for row in matrix1] for i in range(10)]
for i in range(10):
    matrix1[i] = 0
matrix2 = [matrix1 for i in range(10)]

print(matrix2)
