# The function definition goes here
def isin(x):
    if x in range(2,555):
        return True

num = int(input("Enter a number: "))

# You call the function here
if isin(num) == True:
    print(num, "is in range.")
else:
    print(num, "is outside the range!")