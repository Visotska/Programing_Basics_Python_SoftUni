number_of_cats = int(input())
g1_small_cats = 0
g2_big_cats = 0
g3_huge_cats = 0
total_grams = 0
for grams in range (number_of_cats):
    grams_of_food = int(input())
    total_grams += grams_of_food
    if 100 <= grams_of_food < 200:
        g1_small_cats+=1
    elif 200 <= grams_of_food < 300:
        g2_big_cats +=1
    elif 300<= grams_of_food < 400:
        g3_huge_cats +=1

total_kilograms = total_grams / 1000
price_per_day = total_kilograms * 12.45

print(f"Group 1: {g1_small_cats} cats.")
print(f"Group 2: {g2_big_cats} cats.")
print(f"Group 3: {g3_huge_cats} cats.")
print(f"Price for food per day: {price_per_day:.2f} lv.")
