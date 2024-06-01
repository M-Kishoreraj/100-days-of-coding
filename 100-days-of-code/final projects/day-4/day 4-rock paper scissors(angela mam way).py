import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#avoid using "" or '' in rock,paper and scissors
given_images=[rock,paper,scissors]
#enter the user wish
user_choice = int(input("what do you choose... 0 for rock, 1 for paper and 2 for scissors.\n"))
#this below step is most important and it like "(variable) given_images: list[str]
print(given_images[user_choice])

# using random and randint to give computer_choice
computer_choice = random.randint(0,2)
print("computer chose: ")
print(given_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("you lose")
elif computer_choice == 0 and user_choice == 2:
  print("you win")
elif user_choice > computer_choice :
  print("you win")
elif computer_choice > user_choice :
  print("you lose")
elif user_choice == computer_choice:
  print("it is a tie")
