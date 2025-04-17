serial_name = input()
seasons = int(input())
episodes = int(input())
episode_length = float(input())
total_watch_time = 0

for i in range(seasons):
    for j in range(episodes):
        total_watch_time += episode_length * 1.2
    total_watch_time += 10

print(f'Total time needed to watch the {serial_name} series is {total_watch_time:.0f} minutes.')