# is_prime function definition goes here
def prime(x):
    divisors = 0
    for i in range(2,x+1):
        if x % i == 0:
            divisors += 1
    if divisors == 0:
        return True
    
num = int(input("Input an integer greater than 1: "))

# Call the function here and print out the appropriate message
if prime(num) == True:
    print(num, "is a prime")
else:
    print(num, "is not a prime")