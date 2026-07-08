matrix = [[int(num) for num in input().split(', ')] for row in range(int(input()))]
flattened_matrix = [num for sublist in matrix for num in sublist]
print(flattened_matrix)