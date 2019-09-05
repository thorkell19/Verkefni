n = int(input("Input a natural number: ")) # Do not change this line

# Fill in the missing code below
count = 2
prime = True

while n > count:
    if n % count != 0:
        count += 1
    else:
        prime = False
        break

# Do not changes the lines below
if prime:
    print("Prime")
else:
    print("Not prime")
