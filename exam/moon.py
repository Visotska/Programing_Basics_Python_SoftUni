from math import ceil

average_speed = float(input())
liters_per_100_km = float(input())
total_distace = 768800
hours_per_trip = ceil(total_distace / average_speed) + 3
total_liters = total_distace * liters_per_100_km / 100

print(hours_per_trip)
print(int(total_liters))
