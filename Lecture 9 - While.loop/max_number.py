import math

max_number = -math.inf

while True:
    text = input

    if text == "Stop":
        print(max_number)
        break

    number = int(text)
    if number > max_number:
        max_number = number
