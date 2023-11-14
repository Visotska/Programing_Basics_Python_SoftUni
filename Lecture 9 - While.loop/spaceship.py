ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_astronaut_height = float(input())

ship_volume = ship_width * ship_length * ship_height
room_volume = (average_astronaut_height + 0.40) * 2 * 2
astronauts = ship_volume // room_volume

if 3 <= astronauts <= 10:
    print(f"The spacecraft holds {int(astronauts)} astronauts.")
elif astronauts < 3:
    print("The spacecraft is too small.")
else:
    print("The spacecraft is too big.")