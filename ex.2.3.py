import statistics

zestaw_danych1={'key':'02',
                'values':{'date':'2017-03-28 12:00:00','value':2}}
zestaw_danych2={'key':'03',
                'values': {'date':'2017-03-28 12:00:00','value':6}}
zestaw_danych3={'key':'04',
                'values': {'date':'2017-03-28 12:00:00','value':'None'}}

baza_zest_danych=[zestaw_danych1, zestaw_danych2, zestaw_danych3]

wyniki=[zestaw['values']['value'] for zestaw in baza_zest_danych]



for element in range(len(wyniki)):
    if wyniki[element] =='None':
        wyniki.remove('None')

print(wyniki)

print('średnia arytmetyczna danych pomiarowych: ', statistics.mean(wyniki))
print('dominanta danych pomiarowych: ', statistics.mode(wyniki))
print('mediana danych pomiarowych: ', statistics.median(wyniki))
print('odchylenie standardowe danych pomiarowych: ', statistics.pstdev(wyniki))

