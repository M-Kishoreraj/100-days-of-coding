from random import randint
from logo import art

easy_level=10
hard_level=5

#step-1
def difficulty():
    level=input("select your level: 'easy' or 'hard': ")
    if level=="easy":
        return easy_level
    else:
        return hard_level

#step-2
def check_answer(guess,answer,turn):
    if answer > guess:
        print("too low,try again")
        return turn-1
    elif answer<guess:
        print("too high,try again")
        return turn-1
    else:
        print(f"Congratulations, you guessed the correct number {answer}!")
        return turn 

#step-3
def game():
    print(art)
    print("i am thinking a number between 1 and 100")
    answer= randint(1,100)

    turn=difficulty()

    guess = None

    while guess != answer and turn>0:
        print(f"you have {turn} guesses left")

        guess=int(input("make a random guess: "))

        turn = check_answer(guess,answer,turn)
        if turn == 0:
            print(f"You've run out of guesses, he correct answer was {answer}")
            return
        elif guess != answer:
            print("try again.")

#step-4
while input("Do you want to play a game of guessing a random number? Type 'y' or 'n': ") == 'y':
    game()

print("Thank you for playing this game!")



