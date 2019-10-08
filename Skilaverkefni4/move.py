#constants for setting range
MIN = 1
MAX = 10

def posi(pos):
#function for graphing current position of character
    seq = ""
    if MIN <= pos <= MAX:
        for i in range(MIN, MAX+1):
            if i != pos:
                seq += "x"
            else:
                seq += "o"
    return seq

def move(next):
#function for moving character
    if next == "l" and pos > 1:
        return -1
    elif next == "r" and pos < 10:
        return 1
    else:
        return 0

#receive and print initial position
pos = int(input("Input a position between 1 and 10: "))
print(posi(pos))

#explain rules
print("l - for moving left")
print("r - for moving right")
print("Any other letter for quitting")

#receive second position befor entering loop
next = input("Input your choice: ")

#keep receiving and printing next position until input is invalid
while next == "l" or next == "r":
    pos += move(next)
    print(posi(pos))
    next = input("Input your choice: ")
else:
    print(posi(pos))

