import math

n = int(input())
max_number = -math.inf
sum_of_numbers = 0

for i in range (0,n):
    num = int(input())
    if num > max_number:
        max_number = num
    sum_of_numbers+=num

if max_number == sum_of_numbers - max_number:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    sum_of_numbers -= max_number
    difference = abs(max_number-sum_of_numbers)
    print("No")
    print(f"Diff = {difference}")
