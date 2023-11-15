import math

min_number = math.inf

while True:
    text = input()

    if text == "Stop":
        print(min_number)
        break

    number = int(text)

    if number < min_number:
        min_number = number
