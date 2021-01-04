TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]


# nastavit oddelovace
oddelovac = ('-' * 40)
print(oddelovac)
#privitani a udaje
print('Welcome to the app. Please log in:')
username = input('USERNAME: ')
password = input('PASSWORD: ')
#slovnik s jmeny
print(oddelovac)
slovnik_jmen = {'bob' : '123', 'ann' : 'pass123', 'mike' : 'password123', 'liz' : 'pass123'}
#podminka jmen
if slovnik_jmen.get(username) == password:
    print('We have 3 texts to be analyzed.')
    cislo = input('Enter a number btw. 1 and 3 to select: ')
else:
    print('Nejste zaregistrovaný')
print(oddelovac)
#nazvy
paragraf = TEXTS[int(cislo) - 1]
rozdeleni_textu = paragraf.split()
pocet_slov = 0
pocet_velkych_zac_slov = 0
pocet_slov_zacinajich_vel_pis = 0
pocet_slov_psanych_mal_pis = 0
pocet_cisel = 0
#pocet slov v paragrafu
pocet_slov_celkem = len(rozdeleni_textu)
print('There are ' + str(pocet_slov_celkem) + ' words in the selected text.')
#smycka
while rozdeleni_textu:
    rozdeleni = rozdeleni_textu.pop()
    if rozdeleni.istitle():
        pocet_velkych_zac_slov = pocet_velkych_zac_slov + 1
    elif rozdeleni.isupper():
        pocet_slov_zacinajich_vel_pis = pocet_slov_zacinajich_vel_pis + 1
    elif rozdeleni.islower():
        pocet_slov_psanych_mal_pis = pocet_slov_psanych_mal_pis + 1
    elif rozdeleni.isdigit():
        pocet_cisel = pocet_cisel + 1
print('There are ' + str(pocet_velkych_zac_slov) + ' titlecase words')
print('There are ' + str(pocet_slov_zacinajich_vel_pis) + ' uppercase words')
print('There are ' + str(pocet_slov_psanych_mal_pis) + ' lowercase words')
print('There are ' + str(pocet_cisel) + ' numeric strings')
print(oddelovac)
#druha cast
pocet_slov = {}
rozdeleni_textu_2 = TEXTS[1]
no_integer = ''.join([rozdeleni_textu_2 for rozdeleni_textu_2 in rozdeleni_textu_2 if not rozdeleni_textu_2.isdigit()])
no_integer =  str(no_integer).replace( ','  , ' ' )
no_integer =  str(no_integer).replace( '.'  , ' ' )
no_integer = [len(x) for x in no_integer.split()]
while no_integer:
    rozdeleni = no_integer.pop()
    pocet_slov[rozdeleni] = pocet_slov.get(rozdeleni,0) + 1
pocet_slov = dict(sorted(pocet_slov.items()))
for keys,values in pocet_slov.items():
    print(keys, '*'* values, values)
print(oddelovac)
#treti cast
cisla = []
for word in paragraf.split():
   if word.isdigit():
      cisla.append(int(word))
print('If we summed all the numbers in this text we would get:',float(sum(cisla)))
print(oddelovac)