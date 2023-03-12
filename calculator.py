# Select operator
# +
# -
# /
# *
# %
# ----------------
# num1:
# num2:

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def multiply(a, b):
    return a * b


def modulu(a, b):
    return a % b


def get_nums():
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    return num1, num2


# Select operator
# +
# -
# /
# *
# %
# ----------------
# num1:
# num2:
while True:
    print("Select an option: ")
    print("+")
    print("-")
    print("/")
    print("*")
    print("q = for quit")
    operator = input("Enter option: ")
    if operator == 'q':
        print("Good bye")
        break
    elif operator == '+':
        num1, num2 = get_nums()
        print("Result is: ", add(num1, num2))
    elif operator == '-':
        num1, num2 = get_nums()
        print("Result is: ", sub(num1, num2))
    elif operator == '/':
        num1, num2 = get_nums()
        print("Result is: ", div(num1, num2))
    elif operator == '*':
        num1, num2 = get_nums()
        print("Result is: ", multiply(num1, num2))
    elif operator == '%':
        num1, num2 = get_nums()
        print("Result is: ", modulu(num1, num2))
    else:
        print("invalid input")
