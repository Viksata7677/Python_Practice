actor_name = input()
actor_points = float(input())
ocenqvashti = int(input())

for i in range(ocenqvashti):
    ocenqvasht_name = input()
    points_from_ocenqvash = float(input())

    points_to_give = ((len(ocenqvasht_name) * points_from_ocenqvash) / 2)
    actor_points += points_to_give
    if actor_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actor_points:.1f}!")
        break

if actor_points < 1250.5:
    print(f"Sorry, {actor_name} you need {1250.5 - actor_points:.1f} more!")

