n = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
factor = 1

while n >= factor:
    if n % factor == 0:
        print(factor)
    factor += 1
