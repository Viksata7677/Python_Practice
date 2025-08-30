# numbers_list = int(input()).split(", ")
# result = 1
#
# for i in range(numbers_list):
#     number = numbers_list[i + 1]
#     if number <= 5:
#         result *= number
#     elif 5 < number <= 10:
#         result /= number
#
# print(total)

# FIXED:

numbers_list = [int(num) for num in input().split(", ")]
result = 1.0

for number in numbers_list:
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)