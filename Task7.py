def pos(string1, string2):
    result = "Yes"
    i = 0
    for char in string1:
        if char in string2[i:]:
            i = string2.find(char)
        else:
            result = "No"
    print(result)


string1 = input("Is this string: ")
string2 = input("Hidden in this string: ")

pos(string1, string2)
