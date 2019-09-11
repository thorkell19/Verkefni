name = input("Input a name: ")

first_initial = name[name.find(",")+2].capitalize()+"."
lastname = name[:name.find(",")].capitalize()
print(first_initial+" "+lastname)