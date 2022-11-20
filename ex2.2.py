stanowisko1={'id':1,
             'stationId':1,
             'param':{'paramName':'dwutlenek azotu', 'paramFormula':'NO2', 'paramCode':'NO2', 'idParam':10}}

stanowisko2={'id':2,
             'stationId':1,
             'param':{'paramName':'pył zawieszony PM10', 'paramFormula':'NO2', 'paramCode':'NO2', 'idParam':10}}

stanowisko3={'id':3,
             'stationId':1,
             'param':{'paramName':'dwutlenek azotu', 'paramFormula':'NO2', 'paramCode':'NO2', 'idParam':10}}

stanowisko4={'id':4,
             'stationId':2,
             'param':{'paramName':'dwutlenek azotu', 'paramFormula':'NO2', 'paramCode':'NO2', 'idParam':10}}
baza_stanowisk=[stanowisko1, stanowisko2, stanowisko3, stanowisko4]
id=int(input('Podaj id stacji: '))

odpowiedz=[stanowisko['param']['paramName'] for stanowisko in baza_stanowisk if stanowisko['stationId']==id]
print ('wszystkie parametry, jakie jest w stanie mierzyć dana stacja pomiarowa')
print(*odpowiedz,  sep='\n')