fruit = input()
day = input()
quantity = float(input())
price = 0
error_check = False

if day == "Monday" or day == "Tuesday" or day == "Thursday" or day == "Wednesday" or day == "Friday":
    if fruit == 'banana':
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == 'grapes':
        price = quantity * 3.85
    else:
        error_check=True
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == 'grapes':
        price = quantity * 4.20
    else:
        error_check=True
else:
    error_check = True
if error_check:
    print('error')
else:
    print(f'{price:.2f}')