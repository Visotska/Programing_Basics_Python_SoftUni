trip_price = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

all_toys_price = (number_of_puzzles * 2.60) + (number_of_dolls * 3) + (number_of_bears * 4.10) + (number_of_minions * 8.20) + (number_of_trucks * 2)

all_toys = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks

if all_toys >= 50:
    all_toys_price *= 0.75 #Отстъпка 25%

rent = all_toys_price * 0.10 #Наем 10% от цялата сума
total_win = all_toys_price - rent

difference = abs(total_win - trip_price)

if total_win >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")