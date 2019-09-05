m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

if m < n:
    mlow = m
else: mlow = n

for i in range(1,mlow+1):
    if m % i ==0 and n % i ==0:
        gcd = i
else: 
    print(gcd)
