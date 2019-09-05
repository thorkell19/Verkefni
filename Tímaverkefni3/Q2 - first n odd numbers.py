num = int(input("Input an int: ")) # Do not change this line

# Fill in the missing code below
count = 0
oddint = 0

while count < num:
    if oddint % 2 == 1:
        print(oddint)
        count += 1
    oddint += 1
