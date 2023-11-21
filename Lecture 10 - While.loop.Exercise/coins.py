balance = float(input())
balance = int(balance * 100)
balance_counter = 0

while balance > 0:
    if balance >= 200:
        balance_counter += 1
        balance -= 200
    elif balance >= 100:
        balance_counter += 1
        balance -= 100
    elif balance >= 50:
        balance_counter += 1
        balance -= 50
    elif balance >= 20:
        balance_counter += 1
        balance -= 20
    elif balance >= 10:
        balance_counter += 1
        balance -= 10
    elif balance >= 5:
        balance_counter += 1
        balance -= 5
    elif balance >= 2:
        balance_counter += 1
        balance -= 2
    elif balance == 1:
        balance_counter += 1
        balance -= 1
print(balance_counter)