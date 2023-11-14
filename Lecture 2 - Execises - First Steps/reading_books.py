
pages_of_the_book = int(input())
pages_per_hour = int(input())
number_of_days = int(input())
hours_left = pages_of_the_book / pages_per_hour

days_left =  hours_left / number_of_days

print (int(days_left))