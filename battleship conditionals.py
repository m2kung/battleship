import turtle as t

letter_to_number = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5, 'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10}
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
Computer_coordinates = [['A', '1'], ['A', '2'], ['A', '3']]

def player_turn():

    guess_letter = input("Guess a letter") 
    guess_number = input("Guess a number")                  # Ask player to input guess

    if guess_letter.isalpha() and guess_number.isdigit() and len(guess_letter) == 1 and len(guess_number) == 1:   # Use string methods to verify that the first input is a letter and the second is a number
        if guess_letter.islower():
            guess_letter = str.capitalize(guess_letter)
        guess = [guess_letter, guess_number]                  # Return the inputted guess as a list which can be searched for within Computer_locations, else return None
        location_coordinates = [10 * (letter_to_number[guess_letter] - 1), -10 * (int(guess_number) - 1)]
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

player_turn()                                               #Execute all functions