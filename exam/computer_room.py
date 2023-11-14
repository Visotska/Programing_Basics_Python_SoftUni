month = input()
spent_hours = int(input())
number_of_people = int(input())
time_of_day = input()
price_per_hour = 0

if month == "march" or month == "april" or month == "may":
    if time_of_day == "day":
        price_per_hour = 10.50
    elif time_of_day == "night":
        price_per_hour = 8.40
elif month == "june" or month == "july" or month == "august":
    if time_of_day == "day":
        price_per_hour = 12.60
    elif time_of_day == "night":
        price_per_hour = 10.20

if number_of_people >= 4:
    price_per_hour *= 0.9

if spent_hours >= 5:
    price_per_hour *= 0.5

total_price = (price_per_hour * number_of_people) * spent_hours

print(f"Price per person for one hour: {price_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")
