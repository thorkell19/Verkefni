size = int(input("Input vector size: "))
v1 = []
v2 = []

def makevectors(size):
    for i in range(size):
        ele = float(input("Element no " + str(i+1) +": "))
        v1.append(ele)
    for i in range(size):
        ele = float(input("Element no " + str(i+1) + ": "))
        v2.append(ele)
    return(v1, v2)

def dotproduct(v1, v2):
    dotprod = 0
    for i in range(len(v1)):
        dotprod += v1[i]*v2[i]
    return(dotprod)

# Main program starts here
# Should only be a sequence of function calls
v1, v2 = makevectors(size)

print("Dot product is:", dotproduct(v1, v2))