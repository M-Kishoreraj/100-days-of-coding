
# Rock paper scissors python code for single game
import random

actions = ['rock', 'paper', 'scissors']

user_choice = input('Enter your choice (rock, paper or scissors): ')
# using random and choice to give computer_choice
computer_choice = random.choice(actions)

print(f"Your choice was {user_choice} and computer choice was {computer_choice}\n")
#if the user and computer choice was same thing
if user_choice == computer_choice:
    print(f"Both players selected {user_choice}. It's a tie!")

#if the user's choice was rock
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("You win! because Rock smashes scissors.")
    else:
        print("You lose :( Paper covers rock!")

#if the user's choice was paper
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win! because Paper covers rock.")
    else:
        print("You lose :( Scissors cuts paper!")

#if the user's choice was scissors
elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win! because Scissors cuts paper.")
    else:
        print("You lose :( Rock smashes scissors!")
