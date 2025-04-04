age = int(input())
peralnq = float(input())
igrachka = 0
cena_igrachka = int(input())
money = 0
money_gift = 10

for i in range(1, age+1):
    if i % 2 == 0:
        money += money_gift
        money -= 1
        money_gift += 10
    else:
        igrachka += 1

pari_ot_igrachki = igrachka * cena_igrachka
money += pari_ot_igrachki


if money >= peralnq:
    print(f"Yes! {money - peralnq:.2f}")
else:
    print(f"No! {abs(money - peralnq):.2f}")


