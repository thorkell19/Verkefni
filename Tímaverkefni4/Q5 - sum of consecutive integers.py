num = int(input("Input an int: ")) # Do not change this line

cumul = 0
for i in range(1,num+1):
    print(i+cumul)
    cumul += i
