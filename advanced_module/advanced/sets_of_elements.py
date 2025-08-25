length_of_sets = [int(i) for i in input().split(" ")]

first_set = {input() for i in range(length_of_sets[0])}
second_set = {input() for i in range(length_of_sets[1])}

for num in first_set.intersection(second_set):
    print(num)