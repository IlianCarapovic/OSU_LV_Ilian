try:
    number = float(input())

    if number < 0.0 or number > 1:
        print("Invalid number")
        exit()

    if number >= 0.9:
        print("A")
    elif number >= 0.8:
        print("B")
    elif number >= 0.7:
        print("C")
    elif number >= 0.6:
        print("D")
    else:
        print("F")

except ValueError:
    print("Enter a valid number between 0.0 and 1.0")