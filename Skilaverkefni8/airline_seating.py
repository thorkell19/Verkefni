import string #upper() method used for robustness

def get_rows():
    rows = int(input("Enter number of rows: "))
    return rows

def get_seats():
    seats = int(input("Enter number of seats in each row: "))
    return seats


def make_plane(rows, seats):
    '''Takes in number of rows and seats and returns list of seats in each row
        and list of list representing structure of plane seats'''
    row_list = []
    for seat in range(seats):
        row_list.append(chr(65+seat))

    plane_list = []
    for _ in range(rows):
        plane_list.append(row_list[:])
    
    return row_list, plane_list


def print_plane(plane_list):
    for rownumber, row in enumerate(plane_list):
        print("{:>2d}".format(rownumber+1), end="   ")
        
        for seat in row[:len(row)//2]:  #left isle of seats
            print(seat, end=" ")
        print("", end="  ")
        
        for seat in row[len(row)//2:]:  #right isle of seats
            print(seat, end=" ")
        
        print()


def want_seat(plane_list, seat_list):
    '''Asks which seat user wants and returns a tuple with
        indexes for seat if seat exists on plane'''
    seat_exists = False

    while seat_exists == False:
        seat = input("Input seat number (row seat): ")
        seat_split = seat.split() #input split into row-number and seat

        #make a list of rownumbers for checking if seat exists
        rowlist = []
        for row in enumerate(plane_list):
            rowlist.append(row[0]+1)
        
        try:
            if int(seat_split[0]) in rowlist and seat_split[1].upper() in seat_list:
                seat_exists = True
                #if seat exists, it's converted to tuple of indexes. later used for selecting seats
                tuple_want = (int(seat_split[0])-1, ord(seat_split[1].upper())-65)
                return tuple_want
            else:
                print("Seat number is invalid!")
        except ValueError:
            print("Seat number is invalid!")
        except IndexError:
            print("Seat number is invalid!")


def take_seat(plane_list, want_tuple):
    '''Takes plane list, puts X in wanted seat if it's free and returns updated plane list'''
    if plane_list[want_tuple[0]][want_tuple[1]] != "X": #check if seat free
        plane_list[want_tuple[0]][want_tuple[1]] = "X"  #seat reserved if free
        return plane_list
    else:
        print("That seat is taken!")
        return False


def free_seats(plane_list):
    '''Counts the number of free seats'''
    free = 0
    for row in plane_list:
        free += len(row) - row.count("X")
    return free


def ask_more():
    more = input("More seats (y/n)? ")
    if more == "y" or more == "Y":
        return True
    else:
        return False


### MAIN IS HERE ###
plane_rows = get_rows()
plane_seats = get_seats()

seat_list = make_plane(plane_rows, plane_seats)[0] #list of seats in each row
plane = make_plane(plane_rows, plane_seats)[1] #list of all seats

print_plane(plane)

more_seats = True
while more_seats:
    want_tuple = want_seat(plane, seat_list)
    if take_seat(plane, want_tuple): #if seat successfully reserved
        print_plane(plane)
        if free_seats(plane) > 0: #if there are free seats
            more_seats = ask_more()
        else:
            more_seats = False #if plane is full, loop stops