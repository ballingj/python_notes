from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

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
    comp_move = "rock"
elif num == 2:
    comp_move = "paper"
elif num == 3:
    comp_move = "scissors"

# Ask a user to enter their move
player_move = input("enter your move (rock, paper, or scissors): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("YOUR MOVE: ")
if player_move == "rock":
    print(rock)
elif player_move == "paper":
    print(paper)
elif player_move == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("COMPUTER MOVE: ")
if comp_move == "rock":
    print(rock)
elif comp_move == "paper":
    print(paper)
elif comp_move == "scissors":
    print(scissors)

# Figure out who wins and print the result!
if comp_move == player_move:
    print("IT'S A TIE!")
elif player_move == "rock" and comp_move == "scissors":
    print("YOU WIN!!!")
elif player_move == "paper" and comp_move == "rock":
    print("YOU WIN!!!")
elif player_move == "scissors" and comp_move == "paper":
    print("YOU WIN!!!")
else:
    print("YOU LOSE!!!")
