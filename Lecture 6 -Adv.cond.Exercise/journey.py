budget = float(input())
season = input()
destination=""
place_to_stay=""
spent_money=0
if budget <= 100:
    if season == "summer":
        spent_money=budget*0.3
        place_to_stay = "Camp"
    elif season == "winter":
        spent_money= budget*0.7
        place_to_stay = "Hotel"
    destination = "Bulgaria"
elif 100 <= budget <= 1000:
    if season == "summer":
        spent_money = budget * 0.4
        place_to_stay = "Camp"
    elif season == "winter":
        spent_money = budget * 0.8
        place_to_stay = "Hotel"
    destination = "Balkans"
elif budget > 1000:
    spent_money = budget * 0.9
    destination = "Europe"
    place_to_stay = "Hotel"

print(f"Somewhere in {destination}")
print(f"{place_to_stay} - {spent_money:.2f}")
