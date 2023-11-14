deposit = float(input())
months = int(input())
annual_percent_of_interest = float(input())
sum = deposit + months * (deposit * annual_percent_of_interest/100)/12
print (sum)