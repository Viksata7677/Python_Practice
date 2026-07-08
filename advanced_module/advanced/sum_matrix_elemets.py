rows, columns = input().split(', ')
matrix = []

for row in range(int(rows)):
    matrix.append([])
    numbers = input().split(', ')
    for j in numbers:
        matrix[row].append(int(j))

matrix_sum = 0
for row in matrix:
    for num in row:
        matrix_sum += num

print(matrix_sum)
print(matrix)

