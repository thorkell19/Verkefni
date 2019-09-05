
num = int(input("Enter an integer: " ))

cumul = 0
large = 0
even = 0
odd = 0

if num > 0:
    while num > 0:
        if num > large:
            large = num
        if num % 2 == 0:
            even += 1
        else:
            odd +=1
        cumul += num
        print("Cumulative total:", cumul)
        num = int(input("Enter an integer: " ))
    else:
        print("Largest number:", large)
        print("Count of even numbers:", even)
        print("Count of odd numbers:", odd)
