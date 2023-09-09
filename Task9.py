def reading(prompt, min, max):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Error: wrong input")
        else:
            if number < min or number > max:
                print("Error: Type number between -10...10")
            else:
                return number


v = reading("Enter a number from -10 ... 10: ", -10, 10)
print("The number is:", v)
