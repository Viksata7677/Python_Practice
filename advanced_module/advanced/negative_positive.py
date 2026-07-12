def negative_positive():
    numbers = [int(num) for num in input().split()]
    negatives_sum = 0
    positives_sum = 0

    for num in numbers:
        if num > 0:
            positives_sum += num
        else:
            negatives_sum += num

    print(negatives_sum)
    print(positives_sum)

    if abs(negatives_sum) > positives_sum:
        print('The negatives are stronger that the positives')
    else:
        print('The positives are stronger than the negatives')

negative_positive()