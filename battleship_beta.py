import turtle as t
import random as r

#Note: may want a code for detecting if they already guessed a coordinate

letter_to_number = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def grid():
    t.title("Battleship")
    t.bgcolor("navyblue")
    s = t.getscreen() #Can we remove the 's =' ?
    
    t.color("white")
    t.pensize(1)
    
    for i in range(4):   #code for the main square
        t.fd(100)
        t.rt(90)
    
    #  NOTE THE ORIGIN OF THE GRID IS ON THE TOP LEFT OF THE MAIN SQUARE
    
    # start while loop to draw grid
        
    i = 0

    while i <= (len(letters) - 1):
        
        t.penup()
        t.fd(10)
        t.write(letters[i])
        t.rt(90)
        t.pendown()
        t.fd(100)
        
        t.lt(90)
        t.penup()
        t.fd(10)
        t.lt(90)
        t.pendown()
        t.fd(100)
        t.write(letters[i+1])
        t.rt(90)
        
        i += 2
        
    j = 1

    while j <= 10:
        
        t.rt(90)
        t.penup()
        t.fd(10)
        t.rt(90)
        t.pendown()
        t.fd(100)
        t.penup()
        t.fd(10)
        t.write(j)
        
        t.lt(90)
        t.fd(10)
        t.write(j+1)
        t.lt(90)
        t.fd(10)
        t.pendown()
        t.fd(100)
        
        j += 2
    t.penup()

def is_duplicate_double(list1, list2):
    for entries in list2:
        if entries in list1:
            return True
    return False

#This function checks to see if there are any duplicate sublists in a list
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
        Computer_coordinates = []
        #ship1 - width 5
        #This code finds the coordinates for the first ship.
        #orientation determines if the ship will be horizontal or vertical
        orientation = r.randrange(1,3)
        i=0
        #Computer_coordinates is a collection of the coordinates found so far, it is used to check for duplicate coordinates and as the final result of the computers ship placements.
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

def player_turn():

    guess_letter = input("Guess a letter") 
    guess_number = input("Guess a number")                  # Ask player to input guess
    location_coordinates = [10 * (letter_to_number[guess_letter] - 1), -10 * (int(guess_number) - 1)]

    if guess_letter.isalpha() and guess_number.isdigit():   # Use string methods to verify that the first input is a letter and the second is a number
       guess = [guess_letter, guess_number]                  # Return the inputted guess as a list which can be searched for within Computer_locations, else return None
       if guess in Computer_coordinates:                    # Determine if the user guessed a location with a ship
            print('HIT')
            list.remove(Computer_coordinates, guess)        # Removes the coordinate from available ship coordinates to guess
            t.color("red")                                  # Tells the turtle to fill in the guessed square red/white
            t.goto(location_coordinates)
            t.begin_fill()
            for j in range(4):
                t.fd(10)
                t.rt(90)
            t.end_fill()
       else:
            print('MISS')                                        
            t.color("white")
            t.goto(location_coordinates)                        # This can maybe be streamlined with the hit code; just change the color, don't have to repeat turtle code
            t.begin_fill()
            for j in range(4):
                t.fd(10)
                t.rt(90)
            t.end_fill()
    else:
        print('Invalid input, please try again')

grid()
player_turn()                                               #Execute all functions