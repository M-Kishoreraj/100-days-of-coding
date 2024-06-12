MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 100,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    },
    "americano": {
        "ingredients": {
            "water": 300,
            "coffee": 24,
        },
        "cost": 120,
    },
    "mocha": {
        "ingredients": {
            "water": 200,
            "milk": 100,
            "coffee": 24,
            "chocolate": 50,
        },
        "cost": 180,
    },
    "black_tea": {
        "ingredients": {
            "water": 300,
            "tea": 5,
        },
        "cost": 50,
    },
    "green_tea": {
        "ingredients": {
            "water": 300,
            "green_tea": 5,
        },
        "cost": 60,
    },
    "orange_juice": {
        "ingredients": {
            "water": 0,
            "orange_juice": 250,
        },
        "cost": 100,
    },
    "apple_juice": {
        "ingredients": {
            "water": 0,
            "apple_juice": 250,
        },
        "cost": 110,
    },
    "lemonade": {
        "ingredients": {
            "water": 200,
            "lemon_juice": 50,
            "sugar": 20,
        },
        "cost": 70,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300,
    "chocolate": 200,
    "tea": 50,
    "green_tea": 50,
    "orange_juice": 500,
    "apple_juice": 500,
    "lemon_juice": 100,
    "sugar": 100,
}

def transaction_successful(drinks_price, received_price):
    global profit
    if received_price >= drinks_price:
        change = round(received_price - drinks_price, 2)
        print(f"Here is your {change} change in rupees for your order.")
        profit += drinks_price
        return True
    else:
        print("Sorry, not enough money. Money refunded.")
        return False

def is_resources_efficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def total_coins():
    total = int(input("How many 1 rupee coins: ")) * 1
    total += int(input("How many 2 rupee coins: ")) * 2
    total += int(input("How many 5 rupee coins: ")) * 5
    total += int(input("How many 10 rupee coins: ")) * 10
    return total

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# Program to run the coffee machine
on = True
while on:
    print("welcome to our coffee shop !!!")

    choice = input("What would you like? (espresso/latte/black_tea/cappuccino/green_tea/americano/orange_juice/mocha/lemonade/apple_juice): ")

    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Profit: Rs.{profit}")
    else:
        drink = MENU[choice]
        if is_resources_efficient(drink["ingredients"]):
            payment = total_coins()
            if transaction_successful(drink["cost"], payment):
                make_coffee(choice, drink["ingredients"])
