annual_fee = int(input())

sneakers_price = annual_fee - (annual_fee * 40/100)
basketball_outfit = sneakers_price - sneakers_price * 20/100
basketball_ball = basketball_outfit * 25/100
accessories = basketball_ball * 20/100

total_equipment = annual_fee+ sneakers_price + basketball_outfit + basketball_ball + accessories
print(total_equipment)