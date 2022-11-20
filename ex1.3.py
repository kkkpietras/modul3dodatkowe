liczba_1=int(input('podaj pierwszą liczbę: '))
liczba_2=int(input('podaj drugą liczbę: '))
liczba_max=max(liczba_1,liczba_2)
liczba_min=min(liczba_1,liczba_2)
reszta=liczba_min
while reszta!=1:
    if liczba_max % liczba_min ==0:
        s=f'NWD liczb {liczba_1}, {liczba_2} wynosi: {liczba_min}'
        print(s)
        break
    else:
        reszta=liczba_max % liczba_min
        liczba_max=liczba_min
        liczba_min=reszta

if reszta==1:
    s = f'NWD liczb {liczba_1}, {liczba_2} wynosi: 1'
    print(s)
