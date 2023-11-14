town = input()
sales = float(input())
error_check = False
total_commissions = 0

if town == "Sofia":
    if 0<=sales<=500:
        total_commissions = sales*0.05
    elif 500<sales<=1000:
        total_commissions = sales*0.07
    elif 1000<sales<=10000:
        total_commissions = sales*0.08
    elif sales>10000:
        total_commissions = sales*0.12
    else:
        error_check=True
elif town == "Varna":
    if 0 <= sales <= 500:
        total_commissions = sales * 0.045
    elif 500 < sales <= 1000:
        total_commissions = sales * 0.075
    elif 1000 < sales <= 10000:
        total_commissions = sales * 0.10
    elif sales > 10000:
        total_commissions = sales * 0.13
    else:
        error_check = True
elif town == "Plovdiv":
    if 0<=sales<=500:
        total_commissions = sales*0.055
    elif 500<sales<=1000:
        total_commissions = sales*0.08
    elif 1000<sales<=10000:
        total_commissions = sales*0.12
    elif sales>10000:
        total_commissions = sales*0.145
    else:
        error_check=True
else:
    error_check = True

if not error_check:
    print(f'{total_commissions:.2f}')
else:
    print('error')