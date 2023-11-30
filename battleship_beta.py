import turtle as t
import random as r

#Note: may want a code for detecting if they already guessed a coordinate

letter_to_number = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def grid():
    t.title("Battleship")
    t.bgcolor("navyblue")
    s = t.getscreen() #Can we remove the 's =' ?
    t.setworldcoordinates(-10, -105, 105, 5)
    
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
        t.fd(3)
        t.write(letters[i])
        t.fd(7)
        t.rt(90)
        t.pendown()
        t.fd(100)
        
        t.lt(90)
        t.penup()
        t.fd(10)
        t.lt(90)
        t.pendown()
        t.fd(100)
        t.penup()
        t.lt(90)
        t.fd(7)
        t.write(letters[i+1])
        t.rt(180)
        t.fd(7)
        
        i +=2
        
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
        #all_ships_coordinates is the overall list of coordinates from the ships combined into one. It is used to check if there are any duplicates.
        all_ships_coordinates = []
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
        all_ships_coordinates += computer_ship1
        
        
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
            unique = is_duplicate_double(all_ships_coordinates, computer_ship2)
        all_ships_coordinates += computer_ship2
            
        
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
            unique = is_duplicate_double(all_ships_coordinates,computer_ship3)
        all_ships_coordinates += computer_ship3
        
        
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
            unique = is_duplicate_double(all_ships_coordinates,computer_ship4)
        all_ships_coordinates += computer_ship4
        
        
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
            unique = is_duplicate_double(all_ships_coordinates,computer_ship5)
        all_ships_coordinates += computer_ship5
        break
    unique2 = is_duplicate_single(all_ships_coordinates)
    all_ships = [computer_ship1, computer_ship2, computer_ship3, computer_ship4, computer_ship5]

guesses = []

def player_turn():            # Create a function for processing player's inputs

    remaining_guesses = 50    # Create a variable remaining_guesses to keep track of the player's turns

    while len(all_ships_coordinates) > 0:                # Ask for player's inputs so long as there are ships remaining
        guess_letter = input("Guess a letter: ").capitalize()
        guess_number = input("Guess a number: ") 
        guess = [guess_letter, guess_number]            # Create a variable guess that is of type list

        # Use string methods to verify that the first input is a letter and the second is a number
        if guess_letter.isalpha() and guess_number.isdigit() and 1 <= int(guess_number) <= 10 and guess_letter in letters and guess not in guesses: # Ensure that the player has inputted a letter A - J and number 1 - 10
            location_coordinates = [10 * (letter_to_number[guess_letter] - 1), -10 * (int(guess_number) - 1)]                                        # Create a variable location_coordinates which corresponds to x and y values of the top-left corner of the box for the turtle
                                                                                                                                                    # Return the inputted guess as a list which can be searched for within Computer_locations, else return None
            if guess in all_ships_coordinates:  # Determine if the user guessed a location with a ship
                for ship in all_ships:
                    if guess in ship:
                        ship.remove(guess)
                        if len(ship) == 0:
                            print("You sank a ship. Keep going!")
                # Removes the coordinate from available ship coordinates to guess
                all_ships_coordinates.remove(guess)
                print("HIT")                    # If true, tell the user they hit a ship, tell the turtle to fill the guessed coordinates red, and decrease remaining guesses by 1
                remaining_guesses -= 1
                print("Remaining guesses: " + str(remaining_guesses))
                # Tells the turtle to fill in the guessed square red/white
                t.color("red")
                t.goto(location_coordinates)
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            else:
                print("MISS")            # If false, tell the user they missed a ship, tell the turtle to fill the guessed coordinates white, and decrease remaining guesses by 1
                remaining_guesses -= 1
                print("Remaining guesses: " + str(remaining_guesses))
                t.color("white")
                t.goto(location_coordinates)
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            guesses.append(guess)        # If the input is valid (hit or miss), add the guessed location to a list of all the guesses they make throughout the game; this ensures that the player cannot guess the same location twice
        else:                        # If the input is invalid, tell the user, and re-iterate remaining_guesses so that the code loops back
            print('Invalid input. Please try again.')
            remaining_guesses += 0

        if len(all_ships_coordinates) == 0:
            print("Congratulations! You've sunk all the ships. You win!")
        elif remaining_guesses == 0:
            print("Sorry, you've run out of turns. The computer wins!")
            
grid()
player_turn()                                               #Execute all functions
