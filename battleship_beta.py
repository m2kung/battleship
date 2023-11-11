import turtle as t

t.title("Battleship")
t.bgcolor("navyblue")
s = t.getscreen()

t.color("white")
t.pensize(1)

for i in range(4):   #code for the main square
    t.fd(100)
    t.rt(90)

#  NOTE THE ORIGIN OF THE GRID IS ON THE TOP LEFT OF THE MAIN SQUARE

# start while loop to draw grid

# Can we switch the letters and the numbers?

i = 1

while i <= 10:
    
    t.penup()
    t.fd(10)
    t.write(i)
    t.rt(90)
    t.pendown()
    t.fd(100)
    
    t.lt(90)
    t.penup()
    t.fd(10)
    t.lt(90)
    t.pendown()
    t.fd(100)
    t.write(i+1)
    t.rt(90)
    
    i += 2

# horizontal lines

t.rt(90)
t.penup()
t.fd(10)
t.rt(90)
t.pendown()
t.fd(100)
t.penup()
t.fd(10)
t.write('A')

t.lt(90)
t.fd(10)
t.write('B')
t.lt(90)
t.fd(10)
t.pendown()
t.fd(100)

t.penup()
t.rt(90)
t.fd(10)
t.rt(90)
t.pendown()
t.fd(100)
t.penup()
t.fd(10)
t.write('C')

t.lt(90)
t.fd(10)
t.write('D')
t.lt(90)
t.fd(10)
t.pendown()
t.fd(100)

t.penup()
t.rt(90)
t.fd(10)
t.rt(90)
t.pendown()
t.fd(100)
t.penup()
t.fd(10)
t.write('E')

t.lt(90)
t.fd(10)
t.write('F')
t.lt(90)
t.fd(10)
t.pendown()
t.fd(100)

t.penup()
t.rt(90)
t.fd(10)
t.rt(90)
t.pendown()
t.fd(100)
t.penup()
t.fd(10)
t.write('G')

t.lt(90)
t.fd(10)
t.write('H')
t.lt(90)
t.fd(10)
t.pendown()
t.fd(100)

t.penup()
t.rt(90)
t.fd(10)
t.rt(90)
t.pendown()
t.fd(100)
t.penup()
t.fd(10)
t.write('I')

t.lt(90)
t.fd(10)
t.write('J')
t.lt(90)
t.fd(10)
t.pendown()
t.fd(100)
t.penup()

#this is the end of the grid code

#below if the code for filling in a coordinate

computer_ship_locations = [('A','0'), ('A','1'), ('A','2')]
guess_x = {'A' : 1, 'B' : 2} # Make this more streamlined

def player_turn():

    guess_letter = input("Guess a letter") 
    guess_number = input("Guess a number")                  # Ask player to input guess
    location_coordinates = [10 * (guess_x[guess_letter] - 1), -10 * (int(guess_number) - 1)]           # Have to fix indexing for proper positions in relation to turtle

    if guess_letter.isalpha() and guess_number.isdigit():   # Use string methods to verify that the first input is a letter and the second is a number
       guess = (guess_letter, guess_number)
       if guess in computer_ship_locations:   
            print('HIT')
            t.color("red")
            t.goto(location_coordinates)
            t.begin_fill()
            for j in range(4):
                t.fd(10)
                t.rt(90)
            t.end_fill()
       else:
            print('MISS')                                         # Return the inputted guess as a tuple, else return None
            t.color("white")
            t.goto(location_coordinates)                        # This can probably be streamlined with the hit code; just change the color, don't have to repeat turtle code
            t.begin_fill()
            for j in range(4):
                t.fd(10)
                t.rt(90)
            t.end_fill()
    else:
        print('Invalid input, please try again')

player_turn()                                               #Execute all functions