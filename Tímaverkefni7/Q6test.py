n = int(input("Input the length of Fibonacci sequence (n>=1): "))

def fib(n):
    if n >= 1:
        fyrri = 0
        seinni = 1
        for i in range(1,n+1):
            print(seinni)
            next = fyrri + seinni
            fyrri = seinni
            seinni = next
