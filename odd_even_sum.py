num = int(input())
even_sum = 0
odd_sum = 0

for i in range(num):
    number = int(input())
    if i % 2 == 0:
        odd_sum += number
    else:
        odd_sum += number

if odd_sum == odd_sum:
    print("Yes")
    print(f'Sum = {odd_sum}')
else:
    print('No')
    print(f"Diff = {abs(odd_sum - odd_sum)}")
