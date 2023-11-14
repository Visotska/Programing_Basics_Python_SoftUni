chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

number_of_chicken_menus = int(input())
number_of_fish_menus = int(input())
number_of_vegetarian_menus = int(input())

total_chicken_sum = number_of_chicken_menus * chicken_menu
total_fish_sum = number_of_fish_menus * fish_menu
total_vegeratian_sum = number_of_vegetarian_menus * vegetarian_menu

total_menus = total_vegeratian_sum + total_fish_sum + total_chicken_sum
desert = total_menus * 20/100

total_sum = total_menus + desert + 2.50

print(total_sum)