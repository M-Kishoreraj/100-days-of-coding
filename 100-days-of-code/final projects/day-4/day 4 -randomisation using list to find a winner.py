names = ["adam","mike","gyan","david","skanda","gopar","moulesh","santa","dababy"]
# The code above converts the input into an array separating
#each name in the input by a comma and space.
import random

# Get the total number of items in list.
num_items = len(names)

# Generate random numbers between 0 and the last index.
random_name = random.randint(0 , num_items-1)
selected_person = names[random_name]
print(selected_person + " is going to buy the meal today!")

#nested list(definition)-A nested list is a list that appears as an element in another list

fruits=["apple","banana","slice","raw mango","pineapple"]
vegetables=["potato","garlic","carrot"]
eatables =[fruits,vegetables]
print(eatables)

#Using a negative index offsets from the end of the list the code could be: fruits To offset from the start of the list the code would be: fruits[2]
fruits=["apple","banana","slice","raw mango","pineapple","g","s"]
print(fruits[-1])