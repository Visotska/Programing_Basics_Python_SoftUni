square_meters_of_yards = float(input())
full_price = square_meters_of_yards * 7.61
price_with_discount = full_price * 0.18
final_price = full_price - price_with_discount

print(f"The final price is: {final_price} lv." )
print(f"The discount is: {price_with_discount} lv.")