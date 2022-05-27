# About intro to python programming
# implemetation of a number guessing game
# check if a number is positive
def divide_integers():

    cond = 1
    while cond == 1:
        try:
            a = int(input("Please enter the numerator: "))
            b = int(input("Please enter the denominator: "))
            print(a / b)
            print(cond)
            cond = 0
            if cond == 0:
                break

        except (ZeroDivisionError, ValueError):
            print("Please enter valid integers.")


divide_integers()
