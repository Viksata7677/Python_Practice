pirating_days = int(input())
plunder_for_day = int(input())
expected_plunder = float(input())

gathered_plunder = 0

for day in range(1, pirating_days + 1):
    gathered_plunder += plunder_for_day

    if day % 3 == 0:
        gathered_plunder += plunder_for_day * 0.5

    if day % 5 == 0:
        gathered_plunder *= 0.7


if gathered_plunder >= expected_plunder:
    print(f'Ahoy! {gathered_plunder:.2f} plunder gained.')
else:
    percentage = (gathered_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
