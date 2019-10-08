# Your function definition goes here
import string

def count_case(word):
    upp = 0
    low = 0
    for letter in word:
        if letter in string.ascii_uppercase:
            upp += 1
        if letter in string.ascii_lowercase:
            low += 1
    return upp,low

user_input = input("Enter a string: ")

# Call the function here
upper = count_case(user_input)[0]
lower = count_case(user_input)[1]
print("Upper case count: ", upper)
print("Lower case count: ", lower)