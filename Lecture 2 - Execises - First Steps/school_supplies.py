number_of_pencils = int(input())
number_of_markers = int(input())
number_of_detergents = int(input())
percent_discount = int(input())
pencils = 5.80
markers = 7.20
detergent = 1.20
sum = number_of_pencils*pencils + number_of_markers*markers + number_of_detergents*detergent
sum_with_discount = sum - sum * percent_discount / 100
print (sum_with_discount)

