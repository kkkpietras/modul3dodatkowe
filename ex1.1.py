a1=int(input('podaj wspołrzędna początku pierwszego odcinka: '))
a2=int(input('podaj wspołrzędna końca pierwszego odcinka: '))
b1=int(input('podaj wspołrzędna początku drugiego odcinka: '))
b2=int(input('podaj wspołrzędna końca drugiego odcinka: '))
if b1>a1:
    x1=a1
    x2=a2
    y1=b1
    y2=b2
else:
    y1 = a1
    y2 = a2
    x1 = b1
    x2 = b2

if x1<=y1<=x2:
    if y2>=x2:  ## przypadek 1
        poczatek=str (y1)
        koniec=str(x2)
        if y1==x2:
            s = 'czesc wspólna:{'+poczatek+'}'
            print(s)
        else:
            s=f'czesc wspólna: odcinek [{poczatek}; {koniec}]'
            print(s)
        poczatek = str(x1)
        koniec = str(y2)
        s = f'suma odcinek: [{poczatek}; {koniec}]'
        print(s)
    elif y2<x2: ##przypadek 2
        poczatek = str(y1)
        koniec = str(y2)
        s = f'czesc wspólna: odcinek [{poczatek}; {koniec}]'
        print(s)
        poczatek = str(x1)
        koniec = str(x2)
        s = f'suma odcinek: [{poczatek}; {koniec}]'
        print(s)
else:
    print ('odcinki sa rozlaczne') ## przypadek 3
