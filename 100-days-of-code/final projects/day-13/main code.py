import random
#importing logo and vs symbols
from art import logo,vs
from data_storage import data

#a function to get a random account from the data
def random_account():
  return random.choice(data)

#a function to get the accoutn details 
def account_storage(account):
  name=account["name"]
  country=account["country"]
  description =account["description"]
  return f"{name} a {description},from {country}"

#a function the check the guess and return whether the guess is correct or not 
def check_guess(guess,account_a_followers,account_b_followers):
  if account_a_followers>account_b_followers:
    return guess=="a"
  else:
    return guess=="b"

#a function to start and run the game
def game():
  print(logo) #to print the logo
  score=0
  should_continue=True
  account_a=random_account() #get the first random account
  account_b=random_account() #get the second random account


#a loop to run the game
  while should_continue:
    account_a = account_b
    account_b =random_account()
#to ensure the 2 accounts are not the same 
    while account_a == account_b:
        account_b=random_account()
#to dislpay the acc details for comparison
    print(f"Compare A: {account_storage(account_a)}")
    print(vs)
    print(f"Compare B: {account_storage(account_b)}")

#to get the guess between a and b
    guess=input("Check who has more followers? type 'A' or 'B': ").lower()
    # Ensure account_a and account_b are not the same initially
    a_followers_count=account_a["follower_count"]
    b_followers_count=account_b["follower_count"]
    # Call the check_guess function to check the guess 
    is_correct=check_guess(guess,a_followers_count,b_followers_count)

    print(logo)
    if is_correct:
        score += 1 #increase score by 1 with the help of increment from score=0
        print(f"you are right,your current score is {score}")

    else:
      should_continue=False
      print(f"Sorry that's wrong, Final score: {score}")

# Start the game
game()




