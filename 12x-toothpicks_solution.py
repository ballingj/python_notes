num_left = 13
player1 = input("enter player 1's name: ")
player2 = input("enter player 2's name: ")

while True:
    print(f"There are {num_left} toothpicks left")
    print("| " * num_left)
    p1 = int(input(f"How many do you take, {player1} ? "))
    #p1 = int(p1)
    num_left -= p1
    if num_left <= 0:
        print(f"{player1} wins!!!")
        break
    
    print(f"There are {num_left} toothpicks left")
    print("| " * num_left)
    p2 = int(input(f"How many do you take, {player2} ? "))
    num_left -= p2
    if num_left <= 0:
        print(f"{player2} wins!!!")
        break
print("GAME OVER!!")
