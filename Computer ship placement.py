import random as r
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#This function checks to see if there are any duplicate sublists in a list
def is_duplicate_double(list1, list2):
    for entries in list2:
        if entries in list1:
            return True
    return False

#This function checks to see if there are any duplicate sublists in two lists, it is very type sensitive, so if there are any changes in type we need to make sure it works with this function.
def is_duplicate_single(list1):
    unique_entries = set()
    for sublists in list1:
        sublist_tuple = tuple(sublists)
        if sublist_tuple in unique_entries:
            return True
        unique_entries.add(sublist_tuple)
    return False

#This loop is required to make sure that if j reaches 100 and the computer hasn't found unique coordinates for all of the ships yet then it will restart from the beginning.
unique2 = True
while unique2 == True:
    j = 0
    #This loop is required to make sure that if one of the loops repeats indefinitly, then it will restart from the beinning.
    while j < 1000:
        #Computer_coordinates is the overall list of coordinates from the ships combined into one. It is used to check if there are any duplicates.
        Computer_coordinates = []
        #ship1 - width 5
        #This code finds the coordinates for the first ship.
        #orientation determines if the ship will be horizontal or vertical
        orientation = r.randrange(1,3)
        i=0
        #Each ship has its own list of coordinates, this is required to make sure that the coordinates reset every time that duplicates are found.
        computer_ship1 = []
        if orientation == 1:
            rand_letter = r.randrange(0,6)
            rand_number = str(r.randrange(1,11))
            while (i < 5):
                computer_ship1 += [[letters[rand_letter + i] , rand_number]]
                i += 1
        else:
            rand_letter = r.randrange(0,10)
            rand_number = r.randrange(1,7)
            while (i < 5):
                computer_ship1 += [[letters[rand_letter] , str(rand_number + i)]]
                i +=1
        Computer_coordinates += computer_ship1
        
        
        #ship2- width 4
        #This is the loop to find the coordinates of the second ship
        #unique is what ensures that there are no duplicate coordinates
        unique = True
        while unique == True:
            computer_ship2 = []
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,7)
                rand_number = str(r.randrange(1,11))
                while (i < 4):
                    computer_ship2 += [[letters[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,8)
                while (i < 4):
                    computer_ship2 += [[letters[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate_double(Computer_coordinates, computer_ship2)
        Computer_coordinates += computer_ship2
            
        
        #ship3 - width 3
        #This is the loop to find the coordinates of the third ship
        unique = True
        while unique == True:
            computer_ship3 = []
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,8)
                rand_number = str(r.randrange(1,11))
                while (i < 3):
                    computer_ship3 += [[letters[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,9)
                while (i < 3):
                    computer_ship3 += [[letters[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate_double(Computer_coordinates,computer_ship3)
        Computer_coordinates += computer_ship3
        
        
        #ship4 - width 3
        #This is the loop to find the coordinates of the fouth ship
        unique = True
        while unique == True:
            computer_ship4 = []
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,8)
                rand_number = str(r.randrange(1,11))
                while (i < 3):
                    computer_ship4 += [[letters[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,9)
                while (i < 3):
                    computer_ship4 += [[letters[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate_double(Computer_coordinates,computer_ship4)
        Computer_coordinates += computer_ship4
        
        
        #ship5 - width 2
        #This is the loop to find the coordinates of the fith ship.
        unique = True
        while unique == True:
            computer_ship5 = []
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,9)
                rand_number = str(r.randrange(1,11))
                while (i < 2):
                    computer_ship5 += [[letters[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,10)
                while (i < 2):
                    computer_ship5 += [[letters[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate_double(Computer_coordinates,computer_ship5)
        Computer_coordinates += computer_ship5
        break    
    unique2 = is_duplicate_single(Computer_coordinates)    

print(Computer_coordinates)
