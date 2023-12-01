import turtle as t
import random as r

letter_to_number = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
guesses = []

playing = True
all_ships_coordinates = []
guesses = []
all_ships = []

def clear_grid():
    t.reset()
    t.setpos(-10, -105, 105, 5)

def grid():
    global all_ships
    global all_ships_coordinates
    t.title("Battleship")
    t.bgcolor("navyblue")
    s = t.getscreen()  
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

    def is_duplicate_double(list1, list2):
        for entries in list2:
            if entries in list1:
                return True
        return False

    def is_duplicate_single(list1):
        unique_entries = set()
        for sublists in list1:
            sublist_tuple = tuple(sublists)
            if sublist_tuple in unique_entries:
                return True
            unique_entries.add(sublist_tuple)
        return False

    unique2 = True
    while unique2 == True:
        j = 0
        while j < 1000:
            all_ships_coordinates = []
            all_ships = []
            computer_ship1 = []
            orientation = r.randrange(1,3)
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
        

def player_turn():
    
    
    global all_ships_coordinates
    remaining_guesses = 50
    while len(all_ships_coordinates) > 0 and remaining_guesses > 0:
        guess_letter = input("Guess a letter: ").capitalize()
        guess_number = input("Guess a number: ") 
        guess = [guess_letter, guess_number]
        
        if guess_letter.isalpha() and guess_number.isdigit() and 1 <= int(guess_number) <= 10 and guess_letter in letters and guess not in guesses:
            location_coordinates = [10 * (letter_to_number[guess_letter] - 1), -10 * (int(guess_number) - 1)]
            
            if guess in all_ships_coordinates:
                for ship in all_ships:
                    if guess in ship:
                        ship.remove(guess)
                        if len(ship) == 0:
                            print("You sank a ship. Keep going!")
                all_ships_coordinates.remove(guess)
                print("HIT")
                remaining_guesses -= 1
                print("Remaining guesses: " + str(remaining_guesses))
                t.color("red")
                t.goto(location_coordinates)
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            else:
                print("MISS")
                remaining_guesses -= 1
                print("Remaining guesses: " + str(remaining_guesses))
                t.color("white")
                t.goto(location_coordinates)
                t.begin_fill()
                for j in range(4):
                    t.fd(10)
                    t.rt(90)
                t.end_fill()
            guesses.append(guess)
        elif guess in guesses:
            print("You already guessed that, try again.")
            remaining_guesses += 0
        else:
            print('Invalid input. Please try again.')
            remaining_guesses += 0
                
        if len(all_ships_coordinates) == 0:
            print("Congratulations! You've sunk all the ships. You win!")
        elif remaining_guesses == 0:
            print("Sorry, you've run out of turns. The computer wins!")

while playing == True:
    t.reset()
    t.penup()
    t.pendown()
    
    grid()
    player_turn()

    play_again = input('Do you want to play again? (yes/no): ')
    if play_again.lower() == 'yes':
        t.setpos(105, 5)
        all_ships_coordinates = []
        guesses = []
        playing = True
    else:
        playing = False
        t.bye()
