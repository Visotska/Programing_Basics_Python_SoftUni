length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_of_aquarium = length * width * height
volume_in_liters = volume_of_aquarium / 1000
occupied_space = percent / 100

needed_liters_water = volume_in_liters * (1 - occupied_space)
print(needed_liters_water)