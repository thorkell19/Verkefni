top_num = int(input("Upper number for the range: ")) # Do not change this line

for i in range(1,top_num+1):
    sum_of_int = 0
    for n in range(1,i):
        if i % n == 0:
            sum_of_int += n
    if sum_of_int == i:
        print(sum_of_int)
