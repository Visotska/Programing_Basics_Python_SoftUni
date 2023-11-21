length = int(input())
width = int(input())
number_of_pieces = length * width
piece = input()
last_piece = False

while piece != "STOP" or number_of_pieces <= 0:
    current_piece = int(piece)
    number_of_pieces -= current_piece
    if number_of_pieces <= 0:
        last_piece = True
        break
    piece = input()

if last_piece:
    print(f'No more cake left! You need {abs(number_of_pieces)} pieces more.')
else:
    print(f"{number_of_pieces} pieces are left.")