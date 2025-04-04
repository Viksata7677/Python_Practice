num_tournaments = int(input())
start_points = int(input())
win_count = 0
earned_points = 0

for i in range(num_tournaments):
    etap = input()
    if etap == 'W':
        earned_points += 2000
        win_count += 1
    elif etap == 'F':
        earned_points += 1200
    elif etap == 'SF':
        earned_points += 720

final_points = earned_points + start_points
avg_points = earned_points // num_tournaments
percent_tournaments_won = (win_count / num_tournaments) * 100

print(f"Final points: {final_points}")
print(f"Average points: {avg_points}")
print(f'{percent_tournaments_won:.2f}%')