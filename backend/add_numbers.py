

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))


def addNumbers(first, second):
    sum = (first + second)
    return sum


sum = addNumbers(first, second)
print("Sum of the two numbers is: ", sum)
