product = input()
city = input()
quantity = float(input())
total = 0

if city == "Sofia":
    if product == "coffee":
        total =quantity* 0.50
    if product == "water":
        total=quantity*0.80
    if product == "beer":
        total=quantity*1.20
    if product == "sweets":
        total=quantity*1.45
    if product == "peanuts":
        total=quantity*1.60

elif city == "Plovdiv":
    if product == "coffee":
        total =quantity* 0.40
    if product == "water":
        total=quantity*0.70
    if product == "beer":
        total=quantity*1.15
    if product == "sweets":
        total=quantity*1.30
    if product == "peanuts":
        total=quantity*1.50

elif city == "Varna":
    if product == "coffee":
        total = quantity * 0.45
    if product == "water":
        total= quantity*0.70
    if product == "beer":
        total= quantity*1.10
    if product == "sweets":
        total= quantity*1.35
    if product == "peanuts":
        total=quantity*1.55

print(total)
