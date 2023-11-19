needed_money = float(input())
available_money = float(input())
consecutive_days_spend = 0
days = 0

while available_money < needed_money and consecutive_days_spend < 5:
    action = input()
    amount = float(input())

    if action == 'save':
        available_money += amount
        consecutive_days_spend = 0
    elif action == 'spend':
        available_money -= amount
        consecutive_days_spend += 1

        if available_money < 0:
            available_money = 0

    days += 1

if consecutive_days_spend == 5:
    print("You can't save the money.")
    print(days)
else:
    print(f"You saved the money for {days} days.")