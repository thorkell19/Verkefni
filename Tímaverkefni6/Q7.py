my_int = int(input('Give me an int >= 0: '))
# Fill in the missing code

quotient = my_int
bin_str = ""

if my_int != 0:
    while quotient != 0:
        remainder = quotient % 2
        bin_str = str(remainder) + bin_str
        quotient = quotient // 2
    else: 
        bin_str + '1'
else: 
    bin_str = '0'

print("The binary of", my_int, "is", bin_str)