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

coordinate = input("input coordinate: capital letter, then number, no space")
#how to improve code to make it less repetative

if coordinate =='A1':
    t.goto(0,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='A2':
    t.goto(10,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='A3':
    t.goto(20,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='A4':
        t.goto(30,0)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='A5':
    t.goto(40,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='A6':
    t.goto(50,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='A7':
    t.goto(60,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='A8':
    t.goto(70,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='A9':
    t.goto(80,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='A10':
    t.goto(90,0)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='B1':
    t.goto(0,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='B2':
    t.goto(10,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='B3':
    t.goto(20,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='B4':
        t.goto(30,-10)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='B5':
    t.goto(40,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='B6':
    t.goto(50,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='B7':
    t.goto(60,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='B8':
    t.goto(70,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='B9':
    t.goto(80,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='B10':
    t.goto(90,-10)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C1':
    t.goto(0,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='C2':
    t.goto(10,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C3':
    t.goto(20,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='C4':
        t.goto(30,-20)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='C5':
    t.goto(40,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='C6':
    t.goto(50,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C7':
    t.goto(60,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C8':
    t.goto(70,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C9':
    t.goto(80,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='C10':
    t.goto(90,-20)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='D1':
    t.goto(0,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='D2':
    t.goto(10,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='D3':
    t.goto(20,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='D4':
        t.goto(30,-30)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='D5':
    t.goto(40,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='D6':
    t.goto(50,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='D7':
    t.goto(60,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='D8':
    t.goto(70,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='D9':
    t.goto(80,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='D10':
    t.goto(90,-30)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E1':
    t.goto(0,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='E2':
    t.goto(10,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E3':
    t.goto(20,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='E4':
        t.goto(30,-40)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='E5':
    t.goto(40,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='E6':
    t.goto(50,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E7':
    t.goto(60,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E8':
    t.goto(70,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E9':
    t.goto(80,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='E10':
    t.goto(90,-40)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='F1':
    t.goto(0,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='F2':
    t.goto(10,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='F3':
    t.goto(20,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='F4':
        t.goto(30,-50)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='F5':
    t.goto(40,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='F6':
    t.goto(50,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='F7':
    t.goto(60,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='F8':
    t.goto(70,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='F9':
    t.goto(80,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='F10':
    t.goto(90,-50)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='G1':
    t.goto(0,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='G2':
    t.goto(10,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='G3':
    t.goto(20,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='G4':
        t.goto(30,-60)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='G5':
    t.goto(40,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='G6':
    t.goto(50,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='G7':
    t.goto(60,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='G8':
    t.goto(70,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='G9':
    t.goto(80,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='G10':
    t.goto(90,-60)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='H1':
    t.goto(0,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='H2':
    t.goto(10,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='H3':
    t.goto(20,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='H4':
        t.goto(30,-70)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='H5':
    t.goto(40,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='H6':
    t.goto(50,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='H7':
    t.goto(60,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='H8':
    t.goto(70,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='H9':
    t.goto(80,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='H10':
    t.goto(90,-70)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='I1':
    t.goto(0,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='I2':
    t.goto(10,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='I3':
    t.goto(20,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='I4':
        t.goto(30,-80)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='I5':
    t.goto(40,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='I6':
    t.goto(50,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='I7':
    t.goto(60,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='I8':
    t.goto(70,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='I9':
    t.goto(80,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='I10':
    t.goto(90,-80)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J1':
    t.goto(0,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='J2':
    t.goto(10,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J3':
    t.goto(20,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='J4':
        t.goto(30,-90)
        t.begin_fill()
        for i in range(4):  
            t.fd(10)
            t.rt(90)
        t.end_fill()

if coordinate =='J5':
    t.goto(40,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
    
if coordinate =='J6':
    t.goto(50,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J7':
    t.goto(60,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J8':
    t.goto(70,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J9':
    t.goto(80,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()

if coordinate =='J10':
    t.goto(90,-90)
    t.begin_fill()
    for i in range(4):  
        t.fd(10)
        t.rt(90)
    t.end_fill()
