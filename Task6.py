date = input("Type your date (8 digits: YYYYDDMM): ")
if len(date) != 8 or not date.isdigit():
    print("Wrong date")
else:
    while len(date) > 1:
        sum = 0
        for dig in date:
            sum += int(dig)
        date = str(sum)

    print(f"your digit of life is {date}")