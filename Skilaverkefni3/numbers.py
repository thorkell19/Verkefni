#PURPOSE 1 jákvæðar tölur n frá 10-99 (formið ab)
#þar sem (a+b)^2 = n



#PURPOSE 2: Divisor counting
count_div = 0

for i in range(1,100):
    n = i
    #Count how many divisors each number n has.
    for j in range(1,n+1):
        if n % j == 0:
            count_div += 1
    #For each number n, check if it has 10 divisors. 
    else:
        if count_div == 10:
            print(n)
        count_div = 0