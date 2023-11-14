from math import floor
current_record = float(input())
meters_swimming = float(input())
seconds_per_meter = float(input())

the_swim = meters_swimming*seconds_per_meter
water_resistance = floor(meters_swimming / 15) * 12.5
time_for_swim = the_swim + water_resistance

difference=abs(current_record-time_for_swim)

if time_for_swim >= current_record:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {time_for_swim:.2f} seconds.")


