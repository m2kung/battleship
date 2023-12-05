# Melanie Kung (MK)
# Moira Mcmurtrie (MM)
# Yoasitha Pratheepan (YP)
# Vidhi Patel (VP)

import turtle as t
import random as r

letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}            # Creates a dictionary for 'converting' letters to their corresponding numbers
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']                                                    # Creates a dictionary of possible letters that can be guessed
guesses = []                                                                                                    # Initializes an empty list that will log all the player's guesses throughout the game

playing = True
all_ships_coordinates = []
all_ships = []

def clear_grid():
    t.reset()
    t.setpos(-10, -105, 105, 5)

# YP
def grid():
    global all_ships
    global all_ships_coordinates
    t.title("Battleship")
    t.bgcolor("navyblue")
    t.getscreen()  
    t.setworldcoordinates(-10, -105, 105, 5)

    t.color("white")
    t.pensize(1)

    for i in range(4):  
        t.fd(100)
        t.rt(90)



    i = 0
    while i <= (len(letters) - 1):  # giving i a value from a list of letters
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
        t.write(letters[i + 1])
        t.lt(180)  # Change this line from t.rt(180) to t.lt(180)
        t.fd(7)

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
        t.write(j + 1)
        t.lt(90)
        t.fd(10)
        t.pendown()
        t.fd(100)

        j += 2

    t.penup()

#MM (unless otherwise stated)
    def is_duplicate_double(list1, list2): #This function checks to see if there are any duplicate sublists in a list.
        for entries in list2:
            if entries in list1:
                return True
        return False

    def is_duplicate_single(list1): #This function checks to see if there are any duplicate sublists in two lists.
        unique_entries = set()
        for sublists in list1:
            sublist_tuple = tuple(sublists)
            if sublist_tuple in unique_entries:
                return True
            unique_entries.add(sublist_tuple)
        return False

    unique2 = True #The following code randomly finds the coordinates of the 5 ships.
    while unique2 == True: #This loop makes sure that if j reaches 1000 and the computer hasn't found unique coordinates for all of the ships yet then it will restart from the beginning.
        j = 0
        while j < 1000: #This loop makes sure that if one of the loops repeats indefinitly, then it will restart from the beinning.
            all_ships_coordinates = [] #all_ships_coordinates is the overall list of coordinates from the ships combined into one.
            all_ships = [] #MK all_ships is a list of the sublist of the different ships, which is used to tell if a ship has sunk.
            
            #ship1 - width 5
            computer_ship1 = [] 
            orientation = r.randrange(1,3) #orientation determines if the ship will be horizontal or vertical
            i=0
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
            unique = True
            while unique == True: #unique is what ensures that there are no duplicate coordinates
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
        all_ships = [computer_ship1, computer_ship2, computer_ship3, computer_ship4, computer_ship5] #MK
        

def player_turn():  #MK (unless otherwise stated)                       # Create a function for processing player's inputs
    
    
    global all_ships_coordinates        # VP
    remaining_guesses = 50                                              # Create a variable remaining_guesses to keep track of the player's turns; player gets a total of 50 guesses
    while len(all_ships_coordinates) > 0 and remaining_guesses > 0:     # Ask for player's inputs so long as there are ships remaining AND turns remaining (i.e. not WIN or LOSE)
        guess_letter = input("Guess a letter: ").capitalize()           # Asks the player for a letter and capitalizes it if it isn't capitalized
        guess_number = input("Guess a number: ")                        # Asks the player for a number
        guess = [guess_letter, guess_number]                            # Create a variable guess that is of type list. This is so that we can check whether or not the entry is also a sublist in all_ships_coordinates, in which case the guess is a HIT
        
        if guess_letter.isalpha() and guess_number.isdigit() and int(guess_number) in range(1,11) and guess_letter in letters and guess not in guesses:  # Ensure that the player has inputted a letter A - J and number 1 - 10
            location_coordinates = [10 * (letter_to_number[guess_letter] - 1), -10 * (int(guess_number) - 1)]       # Create a variable location_coordinates which corresponds to x and y values of the top-left corner of the box for the turtle
            
            remaining_guesses -= 1
            
            if guess in all_ships_coordinates:                          # Determine if the user guessed a location with a ship
                for ship in all_ships:
                    if guess in ship:                                   
                        ship.remove(guess)                              # For the ship that was hit, remove that ship from its remaining locations
                        if len(ship) == 0:                              # check if computer_shipX is empty (SUNK); in which case, tell the player
                            print("You sank a ship. Keep going!")
                all_ships_coordinates.remove(guess)                                     # Removes the coordinate from available ship coordinates to guess
                print("HIT")                                            # If true, execute the following "hit" sequence: tell the user they hit a ship, 
                print("Remaining guesses: " + str(remaining_guesses))
                t.color("red")                                          # Tell the turtle to go to the guessed coordinates and fill the square red
                t.goto(location_coordinates)
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            else:
                print("MISS")                                           # If false, execute the following "miss" sequence: tell the user they missed a ship,
                print("Remaining guesses: " + str(remaining_guesses))
                t.color("white")
                t.goto(location_coordinates)                            # Tell the turtle to go to the guessed coordinates and fill the square white,
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            guesses.append(guess)                                       # If the input is valid (hit OR miss), add the guessed location to a list of all the guesses they make throughout the game; this ensures that the player cannot guess the same location twice
        elif guess in guesses:                                          # If the input is invalid, tell the user the reason why, and re-iterate remaining_guesses so that the code loops back, without lowering the number of guesses remaining
            print("You already guessed that, try again.")
            remaining_guesses += 0
        else:
            print('Invalid input. Please try again.')
            remaining_guesses += 0
            
            #VP:
                # Check if there are no remaining ships on the board
        if len(all_ships_coordinates) == 0:     # Check if the list of all ship coordinates is empty
            print("Congratulations! You've sunk all the ships. You win!") # Display a victory message
        elif remaining_guesses == 0:
            print("Sorry, you've run out of turns. The computer wins!")  # Display a defeat message when the player is out of turns
    
#This loop controls the overall flow of the game, allowing the player to 
#play multiple rounds. It resets the game state if the player chooses 
#to play again and exits the game if the player chooses not to play again.

while playing == True:
    t.reset()          # Restes the turtle graphics to clear the previuos game's and ships
    t.penup()          # pen up to prevent drawing lines when moving the turtle
    t.pendown()        # Pen down to start drawing again

    # grid() and player_turn() are both called to draw the grid and handle the player's turn
    grid()
    player_turn()

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() == 'yes':          # Checks if the player wants to play agin
        t.setpos(105, 5)                     # Moves te turtle to a certain position
        all_ships_coordinates = []           # Reset the list of player's guesses
        guesses = []                         # Resets the list of player's guesses
        playing = True                       # Continues playing the game if true
    else:
        playing = False                      # Stops playing the game if false
        t.bye()                              # Closes the turtle graphics window
