import random

from art import logo

print("Welcome to Blackjack game!!!")
def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return the calculated score from the cards."""
    # Check for a blackjack (a hand with only 2 cards: ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If there's an 11 (ace) and the score is over 21, remove the 11 and add a 1 instead
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    """Compares the scores and returns the result of the game."""
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif computer_score == 0:
        return "You lose, opponent has Blackjack!"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"

def play_game():
#    to print the logo each time when starting the new program
    print(logo)


    user_cards = []
    computer_cards = []
    game_over = False
  
# Deal 2 cards to each player (user and computer)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

# Check for game ending conditions
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_continue == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
              
# The computer draws cards until it reaches a score of at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
# Print the final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Loop to keep the game running until the user decides to stop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()

print("Thank you for playing the Blackjack game!")
