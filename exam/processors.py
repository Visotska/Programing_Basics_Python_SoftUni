from math import floor
planned_processors = int(input())
number_of_employees = int(input())
work_days = int(input())
work_hours = number_of_employees * work_days * 8
processors_made = floor (work_hours // 3)
difference= abs(processors_made-planned_processors) * 110.10

if processors_made < planned_processors:
    print(f"Losses: -> {difference:.2f} BGN")
else:
    print(f"Profit: -> {difference:.2f} BGN")
