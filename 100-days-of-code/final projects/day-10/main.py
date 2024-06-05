from art import logo

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

print("hello welcome to the calculator game!!")
print(logo)

symbols={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

num1=int(input("Enter your first no:"))

for symbol in symbols:
    print(symbol)

continue_the_problem=True


while continue_the_problem:

    desired_symbol=input("Enter your symbol from the above line:")
    num2=int(input("Enter your next no:"))
    calcuation_function=symbols[desired_symbol]

    answer=calcuation_function(num1,num2)

    if desired_symbol in symbols:
        answer = symbols[desired_symbol](num1, num2)
        print(f"The answer is {num1} {desired_symbol} {num2} = {answer}")
    else:
        print("Invalid symbol")


    if input(f"if want to continue the operation with {answer} ,press y or else type n:\n") == "y":
     num1=answer
    else:
     continue_the_problem=False
     print("Thank you for using this calculator")
     break
    
    
