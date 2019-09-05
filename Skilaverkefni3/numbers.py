#Virkni 1 jákvæðar tölur n frá 10-99 (formið ab)
#þar sem (a+b)^2 = n

#Virkni 2 jákvæðar tölur n frá 1-99
#þar sem count af divisors = 10

count_div = 0

for i in range(1,100):
    print()
    n = i
    print("number:", n)
    print("divisors:", end=" ")
    for j in range(1,n+1):
        if n % j == 0:
            count_div += 1
            print(j, end=" ")
    else: 
        print()
        print("divisor count:", count_div)
        if count_div == 10:
            print("DIVISOR COUNT IS 10")
        count_div = 0