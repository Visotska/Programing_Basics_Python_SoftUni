protective_nylon = 1.50
paint = 14.50
paint_thinner = 5.00
protective_nylon_needed = int(input())
liters_paint = int(input())
liters_paint_thinner = int(input())
hours_work = int(input())

sum_naylon = ( protective_nylon_needed + 2 ) * protective_nylon
sum_paint = ( liters_paint + liters_paint * 10/100) * paint
sum_thinner = liters_paint_thinner * paint_thinner

sum_of_materials =  sum_thinner + sum_paint + sum_naylon + 0.40
sum_for_craftsmen = sum_of_materials * 30/100 * hours_work

total_sum = sum_of_materials + sum_for_craftsmen
print(total_sum)
