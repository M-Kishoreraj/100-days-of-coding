print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#it is not neccessary to put the lower() command,it's only used for to make the case senstive


choice1=input("you having a great chance to win the the chest,choose left or right to decide the side: ")
if choice1 == "left":
 choice2 = input("you need either wait or swim to get across the door.which one do you choose: ").lower()
 if choice2 == "wait":
   choice3 = input("phew you just came to the final round to get your chest, it can be decided with the 3 doors,one is blue,other is red and the final is yellow. which one do you choose: ").lower()
   if choice3 == "blue":
    print("sorry,you are eaten by sea monster.")
   elif choice3 == "red":
    print("sory,you are burnt by fire. \n")
   elif choice3 == "yellow":
    print("yay! you find the one piece.")
   else:
    print("your map was wrong.")
 else:
   print("you fell into the pirates trap by swimming, game over")
else:
  print("you fell into the pirates trap by choosing the wrong direction, game over")