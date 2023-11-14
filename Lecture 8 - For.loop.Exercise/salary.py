number_of_open_tabs = int(input())
salary = int(input())
for current_tab in range(number_of_open_tabs):
    opened_tab = input()
    if opened_tab == "Facebook":
        salary -= 150
    elif opened_tab == "Instagram":
        salary -= 100
    elif opened_tab == "Reddit":
        salary -=50
    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)