groups = int(input())
obsht_broi_hora = 0
musala = 0
monblan = 0
kilima = 0
k2 = 0
everest = 0

for i in range(groups):
    people = int(input())
    obsht_broi_hora += people
    if people <= 5:
        musala += people
    elif 6 <= people <= 12:
        monblan += people
    elif 13 <= people <= 25:
        kilima += people
    elif 26 <= people <= 40:
        k2 += people
    elif people >= 41:
        everest += people


p1 = musala / obsht_broi_hora * 100
p2 = monblan / obsht_broi_hora * 100
p3 = kilima / obsht_broi_hora * 100
p4 = k2 / obsht_broi_hora * 100
p5 = everest / obsht_broi_hora * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")



