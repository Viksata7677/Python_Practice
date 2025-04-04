n = int(input())
broi_pod_200 = 0
broi_mejdu_200_399 = 0
broi_mejdu_400_599 = 0
broi_mejdu_600_799 = 0
broi_nad_ili_800 = 0

for i in range(n):
    numbers = int(input())
    if numbers < 200:
        broi_pod_200 += 1
    elif 200 <= numbers <= 399:
        broi_mejdu_200_399 += 1
    elif 400 <= numbers <= 599:
        broi_mejdu_400_599 += 1
    elif 600 <= numbers <= 799:
        broi_mejdu_600_799 += 1
    else:
        broi_nad_ili_800 += 1

p1 = broi_pod_200 / n * 100
p2 = broi_mejdu_200_399 / n * 100
p3 = broi_mejdu_400_599 / n * 100
p4 = broi_mejdu_600_799 / n * 100
p5 = broi_nad_ili_800 / n * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")