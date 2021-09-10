getalA = input('Geef een willekeurig getal A:  ')
getalB = input ('Geef nu nog een willekeurig getal B:  ')

if getalA > getalB:
    Max = getalA
    print ('A is het grootste getal:  ' + str(Max))
elif getalA < getalB:
    Min = getalA
    print ('A is het kleinste getal:  ' + str(Min))
else:
    print ('A en B zijn even groot')