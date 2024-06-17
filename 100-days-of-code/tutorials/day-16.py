# class user:
#     #pass is used to create an empty class
#     # pass (optional)

  
# # #user1 is the object and user is the class
# # user1 = user()
# # user1.id = 101
# # user1.name="goat"
# # print(user1.name)

# # #user2 is the object and user is the class
# # user2=user()
# # user2.id=102
# # user.name="messi"
# # print(user2.name)

# #with the help of __init__ function,we can reduce the steps by 2 lines of code and will be easier rather than using pass function

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #001 will be printed as user_id and bonito will be printed as user_name
# user1= user("001","bonito")
# print(user1.id) #to print the id as 001
# print(user1.name) #to print the name as bonito

# user2= user("002","flakes")
# print(user2.id)
# print(user2.name)


#a clear example of object and class 

class Dog:
    
    species="mammal"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def dog(self,species,breed,country):
        self.species=species
        self.breed=breed
        self.country=country
    
my_dog1=Dog("Duke",1)

print(my_dog1.name)
print(my_dog1.age)


my_dog1.dog("mammal","Pitbull","USA")

print(my_dog1.species)
print(my_dog1.breed)
print(my_dog1.country)


#or else we can go with this method
class Dog:
    def __init__(self, name, age, species, breed, country):
        self.name = name
        self.age = age
        self.species = species
        self.breed = breed
        self.country = country

my_dog1 = Dog("Duke", 1, "mammal", "Pitbull", "USA")

print(my_dog1.name)
print(my_dog1.age)
print(my_dog1.species)
print(my_dog1.breed)
print(my_dog1.country)
