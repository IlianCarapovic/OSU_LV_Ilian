
numbers = []

while True:
    number = input("Enter numeric value")
    if number.lower() == "done":
        break
    try:
        num = float(number)
        numbers.append(num)
    except ValueError:
        print("Please enter numeric values only")

if numbers:
    print(len(numbers))
    print(min(numbers))
    print(max(numbers))
    print(sum(numbers)/len(numbers))
    numbers.sort()
    print(numbers)