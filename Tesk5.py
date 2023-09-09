str_1 = input("Enter first text: ")
str_2 = input("Enter second text: ")

strx_1 = "".join(sorted(list(str_1.upper().replace(" ", ""))))
strx_2 = "".join(sorted(list(str_2.upper().replace(" ", ""))))

if len(strx_1) > 0 and strx_1 == strx_2:
    print("Anagrams")
else:
    print("Not Anagrams")