computer_ship_locations = [('A','0'), ('A','1'), ('A','2')]

def player_turn():

    guess_letter = input("Guess a letter") 
    guess_number = input("Guess a number")                  # Ask player to input guess

    if guess_letter.isalpha() and guess_number.isdigit():   # Use string methods to verify that the first input is a letter and the second is a number
       guess = (guess_letter, guess_number)
       if guess in computer_ship_locations:   
            print('HIT')
       else:
            print('MISS')                                         # Return the inputted guess as a tuple, else return None
    else:
        print('Invalid input, please try again')

player_turn()                                               #Execute all functions

#test edit
