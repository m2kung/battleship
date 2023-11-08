x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
y = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'] #Make a list of possible x & y positions
    
for xpos in x:
    for ypos in y:
        locations = [xpos, ypos] #Create a nested loop of all possible locations as a pair of letter + number
        #print(locations)
        
import random as r
        
def ship_locations(): #incomplete
    shipA = [r.choice(x), r.choice(y)] #Create a shipA as a vertically placed ship of random length (1 - 5 units) in a random column
    return shipA

ship_locations()