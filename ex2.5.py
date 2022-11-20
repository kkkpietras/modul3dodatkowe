liczby=(900,800,700,600,500,400,300,200,100,90,80,70,60,50,40,30,20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1)

slowa=('dziewiećset','osiemset','siedemset','sześćset','pięćset','czterysta','trzysta','dwieście', 'sto',
       'dziewięćdziesiąt','osiemdziesiąt','siedemdziesiąt','szecdziesiąt', 'pięćdziesiąt','czterdzieści',
        'trzydzieści', 'dwadziescia','dziewiętnaście','osiemnaście','siedemnaście','szesnaście','piętnaście',
        'czternaście', 'trzynaście','dwanaści','jedenaście','dziesięć','dziewięć','osiem','siedem','sześć','pięć',
       'cztery','trzy','dwa','jeden')

na_slowa = dict(zip(liczby,slowa))
liczba = int(input('Podaj liczbę <1000: ' ))
podana_liczba = liczba

if 1 <= liczba <=999:
    slownie=' '
    for liczb in liczby:
        if liczba >= liczb:
            slownie += na_slowa[liczb]+' '
            liczba -= liczb
    print ( podana_liczba,'= ', slownie )
elif liczba ==0:
    print ('zero')
else:
    print ('Podałeś niewłaściwą lilczbę')
