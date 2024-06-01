print("welcome to the love calculator")
name1 = input()
name2 = input() 
combined_name = name1+name2

lower_name=combined_name.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
digit1=t+r+u+e

l=lower_name.count("t")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
digit2=l+o+v+e

love_score=int(str(digit1)+str(digit2))

if (love_score < 10) or (love_score > 90):
 print(f"your score is {love_score}, you go together like coke and mentos.")

elif(love_score>40) and (love_score<50):
  print(f"your score is {love_score}, you have like normal relationship.")

else:
  print(f"your score is {love_score}.")