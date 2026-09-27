
def add(a, b):
    return a+b

def substract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    if  b == 0:
        return "can't divide by zero"
    else:
        return a/b

num1 = int(input("enter ur first number: "))
num2 = int(input("enter ur second number: "))

operator  =  input("enter the operator u want to use: ")

if operator  == "+":
    result = add(num1, num2)
    print(result)
elif operator == "-":
    result = substract(num1, num2)
    print(result)
elif operator == "*":
    result = multiply(num1, num2)
    print(result)

elif operator == "/":
    result = divide(num1, num2)
    print(result)

else:
    print("please enter a valid operator")