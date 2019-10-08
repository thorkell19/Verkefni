# palindrome function definition goes here
def palindrome(s):
    '''Returns True if the given string is a palindrome and False otherwise.'''
    s_clean = ''
    for ch in s:
        if ch.isalnum():
            s_clean += ch.lower()
    return s_clean == s_clean[::-1]

in_str = input("Enter a string: ")

# call the function and print out the appropriate message
if palindrome(in_str) == True:
    print('"'+ in_str+'"'+' '+'is a palindrome.')
else:
    print('"'+ in_str+'"'+' '+'is not a palindrome.')