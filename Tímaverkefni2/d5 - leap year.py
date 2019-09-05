year = int(input("Input a year: ")) # Do not change this line

# Fill in the missing code below
if year % 4 != 0:
    print(False)
elif year % 100 !=0:
    print(True)
elif year % 400 ==0:
    print(True)
else:
    print(False)
