hole = 1

while hole <= 18:
    par = int(input("Par of hole " + str(hole) + ": "))
    score = int(input("Score on hole " + str(hole)+ ": "))
 
    if par-score > 3:
        print("invalid score")
    elif par-score == 3:
        print("albatross")
    elif par-score == 2:
        print("eagle")
    elif par-score == 1:
        print("birdie")
    elif par-score == 0:
        print("par")
    elif par-score == -1:
        print("bogey")
    elif par-score == -2:
        print("double bogey")
    elif par-score == -3:
        print("triple bogey")
    else:
        print("bad hole")
    hole += 1
