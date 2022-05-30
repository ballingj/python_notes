from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
if num == 1:
    computer_move = rock
elif num == 2:
    computer_move = paper
else:
    computer_move = scissors


# Ask a user to enter their move
player = input("Enter your move (rock, paper, or scissors): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if player == "rock":
    print(f"Your MOVE \n {rock}")
elif player == "paper":
    print(f"Your MOVE \n {paper}")
elif player == "scissors":
    print(f"Your MOVE \n {scissors}")


# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
if computer_move == rock:
    print(f"Computer MOVE \n {rock}")
elif computer_move == paper:
    print(f"Computer MOVE \n {paper}")
elif computer_move == scissors:
    print(f"Computer MOVE \n {scissors}")


# Figure out who wins and print the result!
if player == "rock" and computer_move == paper:
    print("You Lose!")
elif player == "rock" and computer_move == scissors:
    print("You Win!")
elif player == "rock" and computer_move == rock:
    print("Tie")
elif player == "paper" and computer_move == scissors:
    print("You Lose!")
elif player == "paper" and computer_move == rock:
    print("You Win!")
elif player == "paper" and computer_move == paper:
    print("Tie")
elif player == "scissors" and computer_move == rock:
    print("You Lose!")
elif player == "scissors" and computer_move == paper:
    print("You Win!")
elif player == "scissors" and computer_move == scissors:
    print("Tie")
else:
    print("Something went wrong.")
    