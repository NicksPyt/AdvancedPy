x = input("Type text: ")
x = x.replace(" ", "")

if len(x) > 1 and x.upper() == x[::-1].upper():
    print("It's a palindrome")
else:
    print("It's not a palindrome")
