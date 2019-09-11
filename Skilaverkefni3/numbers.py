#PURPOSE 1: Sum of digits squared equals number.

for n in range(10,100):
    #split n into first and second digit.
    first = n // 10
    second = n % 10
    sum_dig_sq = (first + second)**2
    if sum_dig_sq == n:
        print(n)


#PURPOSE 2: Ten divisors.
count_div = 0

for m in range(1,100):
    #count how many divisors m has.
    for i in range(1,m+1):
        if m % i == 0:
            count_div += 1
    #check if m has 10 divisors.
    else:
        if count_div == 10:
            print(m)
        count_div = 0