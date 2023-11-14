text = input()

sum = 0

for current_letter in text:
    if current_letter == "a":
        sum += 1
    if current_letter == "e":
        sum += 2
    if current_letter == "i":
        sum += 3
    if current_letter == "o":
        sum += 4
    if current_letter == "u":
        sum += 5

print(sum)