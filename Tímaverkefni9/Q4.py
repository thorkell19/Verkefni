# Here is the definition of safe_input. It should contain this exception:
def safe_input(prompt, type):
    try:
        if type(prompt) == int:
            return prompt
        elif type(prompt) == str:
            return prompt
        elif type(prompt) == float:
            return prompt
    except ValueError:
        print("Error: please enter a value of", a_type)

a_type = type(prompt)

# Do not change the lines below
print(safe_input('Please enter an integer: ', int))
print(safe_input('Please enter a float: ', float))
print(safe_input('Please enter a string: ', str))

