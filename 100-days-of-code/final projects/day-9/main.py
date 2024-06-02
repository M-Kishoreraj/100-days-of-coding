# Import necessary modules
import os
from art import logo

# Print a welcome message
print("Hello everyone, welcome to the blind-auction game!!")

# Print the logo from the art module
print(logo)

# Initialize an empty dictionary to store user bids
user_bids = {}
# Initialize a variable to control the bidding loop
bidding_over = False

# Function to find the highest bidder
def highest_bidder(bidding_record):
    highest_bid = 0  # Variable to store the highest bid
    winner = ""  # Variable to store the name of the highest bidder
    # Iterate through the bidding_record dictionary
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]  # Get the bid amount for each bidder
        # Check if the current bid is higher than the highest bid found so far
        if bid_amount > highest_bid:
            highest_bid = bid_amount  # Update the highest bid
            winner = bidder  # Update the winner's name
    # Print the winner and the highest bid amount
    print(f"The auction winner is {winner} with a bid of Rs.{highest_bid}")

# Loop to collect bids until there are no more bidders
while not bidding_over:
    # Prompt the user for their name and bid amount
    name = input("What is your name:\n")
    bid_amount = int(input("For how much you are bidding:\nRs."))
    # Store the name and bid amount in the user_bids dictionary
    user_bids[name] = bid_amount
    # Ask if there are any other bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    
    # If no more bidders, set bidding_over to True and find the highest bidder
    if should_continue.lower() == "no":
        bidding_over = True
        highest_bidder(user_bids)
    # If there are more bidders, clear the console screen
    elif should_continue.lower() == "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
