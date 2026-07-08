matrix = [[int(num) for num in input().split(', ')] for row in range(int(input()))]
even_matrix = [[num2 for num2 in row2 if num2 % 2 == 0] for row2 in matrix]
print(even_matrix)