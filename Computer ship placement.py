import random as r
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

#ship1 - width 5
orientation = r.randrange(1,3)
i=0
Used_coordinates = []
if orientation == 1:
    rand_letter = r.randrange(0,6)
    rand_number = str(r.randrange(1,11))
    while (i < 5):
        Used_coordinates += [alphabet[rand_letter + i] + rand_number]
        i += 1
else:
    rand_letter = r.randrange(0,10)
    rand_number = r.randrange(1,7)
    while (i < 5):
        Used_coordinates += [alphabet[rand_letter] + str(rand_number + i)]
        i +=1


#ship2- width 4
unique = True
while unique == True:
    orientation = r.randrange(1,3)
    i=0
    if orientation == 1:
        rand_letter = r.randrange(0,7)
        rand_number = str(r.randrange(1,11))
        while (i < 4):
            Used_coordinates += [alphabet[rand_letter + i] + rand_number]
            i += 1
    else:
        rand_letter = r.randrange(0,10)
        rand_number = r.randrange(1,8)
        while (i < 4):
            Used_coordinates += [alphabet[rand_letter] + str(rand_number + i)]
            i +=1
    unique = len(Used_coordinates) != len(set(Used_coordinates))
    

#ship3 - width 3
unique = True
while unique == True:
    orientation = r.randrange(1,3)
    i=0
    if orientation == 1:
        rand_letter = r.randrange(0,8)
        rand_number = str(r.randrange(1,11))
        while (i < 3):
            Used_coordinates += [alphabet[rand_letter + i] + rand_number]
            i += 1
    else:
        rand_letter = r.randrange(0,10)
        rand_number = r.randrange(1,9)
        while (i < 3):
            Used_coordinates += [alphabet[rand_letter] + str(rand_number + i)]
            i +=1
    unique = len(Used_coordinates) != len(set(Used_coordinates))

#ship2 - width 2
unique = True
while unique == True:
    orientation = r.randrange(1,3)
    i=0
    if orientation == 1:
        rand_letter = r.randrange(0,9)
        rand_number = str(r.randrange(1,11))
        while (i < 2):
            Used_coordinates += [alphabet[rand_letter + i] + rand_number]
            i += 1
    else:
        rand_letter = r.randrange(0,10)
        rand_number = r.randrange(1,10)
        while (i < 2):
            Used_coordinates += [alphabet[rand_letter] + str(rand_number + i)]
            i +=1
    unique = len(Used_coordinates) != len(set(Used_coordinates))

print(Used_coordinates)