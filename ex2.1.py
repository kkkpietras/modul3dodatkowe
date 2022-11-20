stacja1={'id': 1,
        'stationName': 'stacja pierwsza',
        'gegrLat':52.143250,
        'gegrLon':19.233225,
        'city': {'id':1,'name': 'Kalisz'},
        'addressStreet': 'szkolna 1'}
stacja2={'id': 1,
        'stationName': 'stacja pierwsza',
        'gegrLat':52.143250,
        'gegrLon':19.233225,
        'city': {'id':2,'name': 'Kalisz'},
        'addressStreet': 'szkolna 1'}
stacja3={'id': 1,
        'stationName': 'stacja pierwsza',
        'gegrLat':52.143250,
        'gegrLon':19.233225,
        'city': {'id':3,'name': 'Poznań'},
        'addressStreet': 'szkolna 1'}
stacja4={'id': 1,
        'stationName': 'stacja pierwsza',
        'gegrLat':52.143250,
        'gegrLon':19.233225,
        'city': {'id':1,'name': 'Warszawa'},
        'addressStreet': 'szkolna 1'}

baza_stacji=[stacja1, stacja2, stacja3, stacja4]

miasto=input('Podaj nazwę miasta, w którym znajdyje się stacja badawcza: ')

odpowiedz=[stacja for stacja in baza_stacji if stacja['city']['name']==miasto]
print ('wszystkie stacje pomiarowe znajdujące się w podanym mieście:')
print(*odpowiedz,  sep='\n')