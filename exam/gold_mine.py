num_locations = int(input())

for i in range(num_locations):
    expected_gold_per_day = float(input())
    num_days = int(input())
    total_gold = 0

    for j in range(num_days):
        gold_per_day = float(input())
        total_gold += gold_per_day
    average_gold_per_day = total_gold / num_days

    difference = abs(expected_gold_per_day - average_gold_per_day)
    if average_gold_per_day >= expected_gold_per_day:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")
    else:
        print(f"You need {difference:.2f} gold.")
