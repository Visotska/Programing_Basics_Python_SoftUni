name_of_actor = input()
academy_points = float(input())
evaluators = int(input())
total_points = academy_points

for number_of_evaluators in range (evaluators):
    current_evaluator = input()
    points_of_evaluator = float(input())
    total_points+= ((len(current_evaluator) * points_of_evaluator) / 2)

    if total_points > 1250.5:
        print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
        break
else:
    difference = abs(total_points-1250.5)
    print(f"Sorry, {name_of_actor} you need {difference:.1f} more!")