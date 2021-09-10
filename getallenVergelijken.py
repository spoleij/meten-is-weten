getalA = input('Geef een willekeurig getal A:  ')
getalB = input ('Geef nu nog een willekeurig getal B:  ')

if getalA > getalB:
    Max = getalA
    Min = getalB
    print ('A is het grootste getal:  ' + str(Max)) 
    print ('het minimum is ' + str(Min) +' het maximum is ' + str(Max))
elif getalA < getalB:
    Min = getalA
    Max = getalB
    print ('A is het kleinste getal:  ' + str(Min))
    print ('het minimum is ' + str(Min) +' het maximum is ' + str(Max))
else:
    Min = getalA
    Max = getalB
    print ('A en B zijn even groot')
    print ('het minimum is ' + str(Min) +' en het maximum is ' + str(Max))
