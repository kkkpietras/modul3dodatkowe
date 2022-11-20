liczba_1=int(input('podaj pierwszą liczbę: '))
liczba_2=int(input('podaj drugą liczbę: '))
liczba_max=max(liczba_1,liczba_2)
liczba_min=min(liczba_1,liczba_2)
dzielnik=liczba_min
if liczba_max % liczba_min ==0:
    s=f'NWD liczb {liczba_max}, {liczba_min} wynosi: {liczba_min}'
    print(s)
else:
    dzielnik = round(0.5 * liczba_min)
    while dzielnik!=1:
        if liczba_max % dzielnik == 0 and liczba_min % dzielnik==0:
            s = f'NWD liczb {liczba_max}, {liczba_min} wynosi: {dzielnik}'
            print(s)
            break
        else:
            dzielnik-=1

if dzielnik==1:
    s = f'NWD liczb {liczba_max}, {liczba_min} wynosi: {dzielnik}'
    print(s)
