player1 = input("Enter player 1's name: ")
player2 = input("Enter player 2's name: ")
toothpick_count = 13

print("| "* toothpick_count)
print(f"There are {toothpick_count} toothpicks left")
isplayer1 = True
while toothpick_count > 0:
    if isplayer1:
        take_away = int(input(f"How many do you take, {player1} "))
        print(take_away)
        isplayer1 = False
    else:
        take_away = int(input(f"How many do you take, {player2} "))
        print(take_away)
        isplayer1 = True
    toothpick_count -= take_away
    print("| " * toothpick_count)
    if toothpick_count > 0: 
        print(f"There are {toothpick_count} toothpicks left")
    if toothpick_count == 0 and isplayer1:
        print(f"{player2} wins!!!")
    elif toothpick_count == 0 and isplayer1 == False:
        print(f"{player1} wins!!!")
    