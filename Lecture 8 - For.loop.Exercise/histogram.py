count_of_numbers = int(input())
p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0

for number in range (count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1_counter +=1
    elif current_number < 400:
        p2_counter += 1
    elif current_number < 600:
        p3_counter += 1
    elif current_number < 800:
        p4_counter += 1
    elif current_number >= 800:
        p5_counter += 1

p1_percent = p1_counter / count_of_numbers * 100
p2_percent = p2_counter / count_of_numbers * 100
p3_percent = p3_counter / count_of_numbers * 100
p4_percent = p4_counter / count_of_numbers * 100
p5_percent = p5_counter / count_of_numbers * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')