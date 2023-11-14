number_of_groups = int(input())
sum_of_people=0
musala_count = 0
monblan_count = 0
kilimandjaro_count = 0
k2_count = 0
everest_count = 0
for people in range (number_of_groups):
    number_of_people = int(input())
    sum_of_people += number_of_people
    if number_of_people <= 5:
        musala_count += number_of_people
    elif number_of_people <= 12:
        monblan_count += number_of_people
    elif number_of_people <= 25:
        kilimandjaro_count += number_of_people
    elif number_of_people <= 40:
        k2_count += number_of_people
    elif number_of_people >= 41:
        everest_count += number_of_people

percent_musala_climbers = musala_count / sum_of_people * 100
percent_monblan_climbers = monblan_count / sum_of_people * 100
percent_kilimandjaro_climbers = kilimandjaro_count / sum_of_people * 100
percent_k2_climbers = k2_count / sum_of_people * 100
percent_everest_climbers = everest_count / sum_of_people * 100

print(f"{percent_musala_climbers:.2f}%")
print(f"{percent_monblan_climbers:.2f}%")
print(f"{percent_kilimandjaro_climbers:.2f}%")
print(f"{percent_k2_climbers:.2f}%")
print(f"{percent_everest_climbers:.2f}%")