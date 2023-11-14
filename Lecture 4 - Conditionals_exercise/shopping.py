budget = float(input())
video_cards=int(input())
processors=int(input())
ram_storages=int(input())

videocard_price = video_cards * 250
processor_price = (videocard_price*35/100)*processors
ram_price = (videocard_price*10/100)*ram_storages

all_price = videocard_price + processor_price + ram_price
if video_cards>processors:
    all_price = all_price-(all_price*15/100)

difference= abs(budget-all_price)

if budget >=all_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")