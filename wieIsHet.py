geel = input ('Is de kaas geel? ')
if geel == 'ja':
    gaten = input ('Zitten er gaten in? ')
    if gaten == 'ja':
        duur = input ('Is de kaas belachelijk duur? ')
        if duur == 'ja':
            print ('EMMENTALER')
        if duur == 'nee':
            print ('LEERDAMMER')
    if gaten == 'nee':
        hard = input ('Is de kaas hard als steen? ')
        if hard == 'ja':
            print ('PARMIGIANO REGGIANO')
        if hard == 'nee':
            print ('GOUDSE KAAS')
if geel == 'nee':
    schimmels = input ('Heeft de kaas blauwe schimmels? ')
    if schimmels == 'ja':
        korst = input ('Heef de kaas een korst? ')
        if korst == 'ja':
            print ('BLEU DE ROCHBARON')
        if korst == 'nee':
            print ("FOUME D'AMBERT")
    if schimmels == 'nee':
        korst = input ('Heeft de kaas een korst? ')
        if korst == 'ja':
            print ('CAMEMBERT')
        if korst == 'nee':
            print ('MOZZARELLA')
