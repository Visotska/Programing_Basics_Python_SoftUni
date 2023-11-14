number_of_tournaments = int(input())
starting_points = int(input())
total_points = 0
win_number = 0
for points in range(number_of_tournaments):
    tournament_place = input()
    if tournament_place == "W":
        win_number+=1
        total_points+=2000
    elif tournament_place == "F":
        total_points+=1200
    elif tournament_place == "SF":
        total_points+=720

average_points = total_points // number_of_tournaments
total_points += starting_points
percent_wins = win_number/number_of_tournaments * 100

print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{percent_wins:.2f}%")