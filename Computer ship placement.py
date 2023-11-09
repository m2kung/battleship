import random as r
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#This function checks to see if there are any duplicate sublists in a list
def is_duplicate(list1):
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
    while j < 100:
        
        #ship1 - width 5
        #This code finds the coordinates for the first ship.
        #orientation determines if the ship will be horizontal or vertical
        orientation = r.randrange(1,3)
        i=0
        #Computer_coordinates is a collection of the coordinates found so far, it is used to check for duplicate coordinates and as the final result of the computers ship placements.
        Computer_coordinates = []
        if orientation == 1:
            rand_letter = r.randrange(0,6)
            rand_number = str(r.randrange(1,11))
            while (i < 5):
                Computer_coordinates += [[alphabet[rand_letter + i] , rand_number]]
                i += 1
        else:
            rand_letter = r.randrange(0,10)
            rand_number = r.randrange(1,7)
            while (i < 5):
                Computer_coordinates += [[alphabet[rand_letter] , str(rand_number + i)]]
                i +=1
        
        
        #ship2- width 4
        #This is the loop to find the coordinates of the second ship
        #unique is what ensures that there are no duplicate coordinates
        unique = True
        while unique == True:
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,7)
                rand_number = str(r.randrange(1,11))
                while (i < 4):
                    Computer_coordinates += [[alphabet[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,8)
                while (i < 4):
                    Computer_coordinates += [[alphabet[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate(Computer_coordinates)
            
        
        #ship3 - width 3
        #This is the loop to find the coordinates of the third ship
        unique = True
        while unique == True:
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,8)
                rand_number = str(r.randrange(1,11))
                while (i < 3):
                    Computer_coordinates += [[alphabet[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,9)
                while (i < 3):
                    Computer_coordinates += [[alphabet[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate(Computer_coordinates)
        
        
        #ship4 - width 3
        #This is the loop to find the coordinates of the fouth ship
        unique = True
        while unique == True:
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,8)
                rand_number = str(r.randrange(1,11))
                while (i < 3):
                    Computer_coordinates += [[alphabet[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,9)
                while (i < 3):
                    Computer_coordinates += [[alphabet[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate(Computer_coordinates)
        
        
        #ship5 - width 2
        #This is the loop to find the coordinates of the fith ship.
        unique = True
        while unique == True:
            orientation = r.randrange(1,3)
            i=0
            if orientation == 1:
                rand_letter = r.randrange(0,9)
                rand_number = str(r.randrange(1,11))
                while (i < 2):
                    Computer_coordinates += [[alphabet[rand_letter + i] , rand_number]]
                    i += 1
                    j += 1
            else:
                rand_letter = r.randrange(0,10)
                rand_number = r.randrange(1,10)
                while (i < 2):
                    Computer_coordinates += [[alphabet[rand_letter] , str(rand_number + i)]]
                    i += 1
                    j += 1
            unique = is_duplicate(Computer_coordinates)
        break    
    unique2 = is_duplicate(Computer_coordinates)    

print(Computer_coordinates)
