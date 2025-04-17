minutes_in_control = int(input())
seconds_in_control = int(input())
ulei_length = float(input())
seconds_for_100_meters = int(input())

control_in_seconds = minutes_in_control * 60 + seconds_in_control
time_lost_on_hill = ulei_length / 120
total_time_lost = time_lost_on_hill * 2.5
marin_time = (ulei_length / 100) * seconds_for_100_meters - total_time_lost
time_difference = abs(control_in_seconds - marin_time)

if control_in_seconds >= marin_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {marin_time:.3f}.")
else:
    print(f"No, Marin failed! He was {time_difference:.3f} second slower.")