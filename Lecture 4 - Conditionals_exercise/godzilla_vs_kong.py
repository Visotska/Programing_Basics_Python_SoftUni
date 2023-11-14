budget = float(input())
number_of_statists = int(input())
clothes_for_statists = float(input())


decor = budget - budget* 0.9

sum_for_clothes=number_of_statists*clothes_for_statists

if number_of_statists > 150:
    sum_for_clothes*=0.9
sum_for_film = sum_for_clothes+decor

difference = abs(budget-sum_for_film)

if budget>=sum_for_film:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")

else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more." )
