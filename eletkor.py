nev = input("Add meg a nevedet: ")
eletkor = int(input("Add meg az életkorodat: "))

if eletkor >= 18:
    print(nev + ", nagykorú vagy!")
else:
    print(nev + ", nem vagy nagykorú.")
    if eletkor <= 16:
        print("Tanköteles vagy.")
    else:
        print("Nem vagy tanköteles.")

#############################################

import random

def páratlan(szamok):
    szamlalo = 0
    for szam in szamok:
        if szam % 2 == 1:
            szamlalo += 1
    return szamlalo

szamok_ = []

for i in range(50):
    szamok_.append(random.randint(1, 100))

print(f'A Számok listája: {szamok_}')
print(f'Ennyi paratlan szam van: {páratlan(szamok_)}')

################################################

class Superheroes:
    def __init__(self, valodi_nev, nev, univerzum):
        self.valodi_nev = valodi_nev
        self.nev = nev
        self.univerzum = univerzum

    def univerzumneve(self):
        if self.univerzum == "M":
            return "Marvel comics"
        elif self.univerzum == "DC":
            return "DC Comics"
        else:
            return "Nem található univerzum"
        

adatok = []

for i in range(3):
    valodi_nev = input("Adja meg a valódi nevét: ")
    nev = input("Adja meg a szuperhős nevét: ")
    univerzum = input("Adja meg az univerzum nevét(DC/M): ")
    hosok = Superheroes(valodi_nev, nev, univerzum)
    adatok.append(hosok)

for i in adatok:
    print(f"{i.nev} valódi neve {i.valodi_nev} a {i.univerzumneve()} univerzum tagja")


def nevelo(szó):
    maganhangzok ='aáeéiíoóöőuúüű'
    if szó[0].lower() in maganhangzok:
        return 'az'
    else:
        return 'a'

def jelzo():
    return random.choice(['piros', 'nagy', 'könnyed'])


for i in range(3):
    fonev = input('Adj meg 3 fonevet: ')
    print(nevelo(fonev).capitalize, fonev, jelzo())
