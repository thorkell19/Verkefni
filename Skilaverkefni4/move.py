# Athugið eftirfarandi:
# Tölurnar 1 og 10 sem afmarka bilið eiga að vera útfærðar með föstum. Fasti í Python er breyta hvers gildi á ekki að breytast í forriti. 
# Góð regla er að nota hástafi fyrir nöfn á föstum. Þið eigið að nota föll í útfærslunni á verkefninu. 
# Það er í lagi að aðalforritið ykkar innihaldi lykkjuna en meginmál lykkjunnar á að mestu að vera framkvæmt með fallaköllum.

pos = int(input("Input a position between 1 and 10: "))
tenx = "xxxxxxxxxx"

if 1 <= pos <= 10:
    for index, letter in enumerate(tenx):
        if index != pos-1:
            print(letter, end="")
        else:
            print("o", end="")
    print()
    print("l - for moving left")
    print("r - for moving right")
    print("Any other letter for quitting")

    move = input("Input your choice: ")
    if move == "l" and pos > 1:
        pos -= 1
    if move == "r" and pos < 10:
        pos += 1

    while move == "l" or move == "r":
        for index, letter in enumerate(tenx):
            if index != pos-1:
                print(letter, end="")
            else:
                print("o", end="")
        print()
        move = input("Input your choice: ")
        if move == "l" and pos > 1:
            pos -= 1
        if move == "r" and pos < 10:
            pos += 1
    else:
        for index, letter in enumerate(tenx):
            if index != pos-1:
                print(letter, end="")
            else:
                print("o", end="")