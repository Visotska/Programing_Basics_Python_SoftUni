bought_kg_food = int(input())
grams_bought = bought_kg_food * 1000
total_eaten = 0

while True:
    grams_eated = input()

    if grams_eated == "Adopted":
        break

    grams_eated = int(grams_eated)
    total_eaten+=grams_eated

difference = abs(total_eaten-grams_bought)
if total_eaten <= grams_bought:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more.")