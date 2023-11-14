from math import ceil

series=input()
time_for_an_episode=int(input())
lunch_break_time= int(input())

lunch_time = lunch_break_time / 8
break_time = lunch_break_time / 4

time_left_for_series = lunch_break_time - lunch_time - break_time

difference = abs(time_for_an_episode-time_left_for_series)
difference = ceil(difference)

if time_left_for_series >= time_for_an_episode:
    print (f"You have enough time to watch {series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {series}, you need {difference} more minutes.")