number_of_birthdays = int(input())
laundry_price = float(input())
one_toy_price = int(input())
total_money = 0
count_of_toys = 0
current_money = 0

for birthday in range(1,number_of_birthdays+1):
    if birthday % 2 == 0:
        current_money += 10
        total_money += current_money - 1
    else:
        count_of_toys +=1

total_toy_money = count_of_toys * one_toy_price
total_money += total_toy_money
difference = abs(total_money-laundry_price)

if total_money>=laundry_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}" )