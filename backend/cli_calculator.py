# Calculator Operations

def addition(first, second):
    sum = first + second
    return sum


def substraction(first, second):
    sub = first - second
    return sub


def division(first, second):
    div = first / second
    return div


def multiplication(first, second):
    mult = first * second
    return mult


def modulus(first, second):
    mod_result = (first % second)
    return mod_result

# Calculator function


def calculator(first, second, operation):

    if(operation == 1):
        return addition(first, second)
    elif(operation == 2):
        return substraction(first, second)
    elif(operation == 3):
        return multiplication(first, second)
    elif(operation == 4):
        return division(first, second)
    elif(operation == 5):
        return modulus(first, second)
    else:
        print("Give input of numbers from 1 to 5")
        return


print("Select the operation you wish to carryout:\n 1. Addition\n 2. Subtraction\n 3. multiplication\n 4. division\n 5. Modulus")

cond = 1
while cond == 1:
    try:
        user_input = int(input("Enter the operation here: "))
        a = float(input("Please enter the first number: "))
        b = float(input("Please enter the second number: "))
        print("Result of select operation: ", calculator(a, b, user_input))
        cond = 0
        if cond == 0:
            break

    except (ValueError):
        print("Please enter valid integers. Try again.")
    except (ZeroDivisionError):
        print("Please division by zero not possible. Try again")
