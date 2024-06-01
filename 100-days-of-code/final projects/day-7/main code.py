import random

# Step 1-Update the word list to use the 'word_list' from hangman_words.py
from word_chosen import word_list

chose_word = random.choice(word_list)
word_length = len(chose_word)

# Step 2
end_of_game = False
lives = 6 

# Step 3-Import the logo from hangman_art.py and print it at the start of the game.
from hangman_arts import logo 
print(logo)

# Step 4-Testing code
# print(f'Pssst, the solution is {chosen_word}.')(if needed without giving hint)

#Create blanks
display = ["_"] * word_length  # Corrected display initialization

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Step 6-If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

    # step=7-Check guessed letter
    for position in range(word_length):
        letter = chose_word[position]
        if letter == guess:
            display[position] = letter

    # step-8-Check if guessed letter is not in the chosen word
    if guess not in chose_word:
        print(f"You guessed {guess}, which is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose the game.")

    # Display current progress and Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if the player has won
    if "_" not in display:
        end_of_game = True
        print("You won the game!")

    # Print the current state of hangman
    from hangman_arts import hangmanpics  # Import hangmanpics from ihangman_arts
    print(hangmanpics[lives])
