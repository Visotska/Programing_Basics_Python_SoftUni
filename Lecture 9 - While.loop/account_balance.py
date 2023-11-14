balance_sum = 0

while True:
    text = input()
    if text == "NoMoreMoney":
        break
    current_deposit = float(text)

    if current_deposit >= 0:
        balance_sum+=current_deposit
        print(f"Increase: {current_deposit:.2f}")
    else:
        print("Invalid operation!")
        break

print(f'Total: {balance_sum:.2f}')