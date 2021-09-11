print ('Welkom bij onze sollicitatieprocedure voor de openstaande baan: Circusdirecteur voor Circus HotelDeBotel')
naam = input ('Wat is uw naam?: ')

#ERVARINGEN: 

dierenReq = None
jongerenReq = None
acrobatiekReq = None
ervaringen = None

ervaringDieren = int(input ('Hoeveel jaar praktijkervaring met dieren-dressuur heeft u?: '))
if ervaringDieren >= 4:
    dierenReq = True

ervaringJongeren = int(input ('Hoeveel jaar ervaring met jongeren heeft u?: '))
if ervaringJongeren >= 5:
    jongerenReq = True

ervaringAcrobatiek = int(input ('Hoeveel jaar praktijkervaring met acrobatiek heeft u?: '))
if ervaringAcrobatiek >= 3:
    acrobatiekReq = True

if dierenReq or jongerenReq or acrobatiekReq == True:
    ervaringen = True
# gebruik OR want je hoeft maar 1/3 te hebben!

#BEZITTINGEN:

diplomaReq = None
rijbewijsReq = None
hoedReq = None
bezittingen = None

bezitDiploma = input ('Heeft u een diploma MBO-4 ondernemen?: ')
if bezitDiploma == 'ja':
    diplomaReq = True

neppeVraag1 = input ('Heeft u een Netflix account?: ')

bezitRijbewijs = input ('Heeft u een geldig Vrachtwagen rijbewijs?: ')
if bezitRijbewijs == 'ja':
    rijbewijsReq = True

neppeVraag2 = input ('Kunt u een handstand?: ')

bezitHoed = input ('Bent u in het bezit van een hoge hoed?: ')
if bezitHoed == 'ja':
    hoedReq = True

if diplomaReq and rijbewijsReq and hoedReq == True:
    bezittingen = True
else: False
# gebruik hier wel AND

# MAN / VROUW:

snorLengteReq = None
roodHaarLengteReq = None
manVrouw = None

geslacht = input ('Bent u een man of een vrouw?: ')
if geslacht == 'man':
    snor = input ('Heeft u een snor?: ')
    if snor == 'ja':
        snorLengte = int(input ('Hoeveel cm breed is uw snor?: '))
        if snorLengte >= 10:
            snorLengteReq = True
        
#else: False
if geslacht == 'vrouw':
    roodHaar = input ('Heeft u rood krullend haar?: ')
    if  roodHaar == 'ja':
        roodHaarLengte = int(input ('Hoeveel cm is uw haar?: '))
        if roodHaarLengte >= 20:
            roodHaarLengteReq = True

neppeVraag3 = input ('Heeft u huisdieren?: ')

if snorLengteReq or roodHaarLengteReq == True:
    manVrouw = True    

# lengte / gewicht / certificaat

lengteReq = None
gewichtReq = None
certificaatReq = None
lgc = None

lengte = int(input ('Hoe lang bent u in cm?: '))
if lengte > 150:
    lengteReq = True

gewicht = int(input ('Wat is uw lichaamsgewicht in KG?: '))
if gewicht > 90:
    gewichtReq = True

neppeVraag4 = input ('Hoeveel moedervlekken heeft u ongeveer?: ')

bezitCertificaat = input ('Bezit u het certificaat "Overleven met gevaarlijk personeel"?: ')
if bezitCertificaat == 'ja':
    certificaatReq = True

if lengteReq and gewichtReq and certificaatReq == True:
    lgc = True

if ervaringen and bezittingen and manVrouw and lgc == True:
    print ('Gefeliciteerd ' + naam + ' U voldoet aan al onze criteria en wij willen u graag uitnodigen voor een sollicitatiegesprek.')
else:
    print ('Helaas voldoet u niet aan onze eisen. Het spijt ons.')





    
