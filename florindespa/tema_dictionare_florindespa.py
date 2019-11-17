"""
# varianta a

lista_cumparaturi = {
    "mere":1,
    "banane":2,
    "paine":4,
    "carne":3,
    "orez":1
}

magazin1 = {
    "mere":3,
    "banane": 4,
    "paine": 4,
    "carne": 15,
    "orez": 2
}

def pret_cumparaturi(lista,magazin):
    suma=0
    for i in lista:
        if i in magazin:
            suma=suma+float(lista[i])*float(magazin[i])
        else:
            print(i," nu se regaseste in magazin")
    print(suma)

pret_cumparaturi(lista_cumparaturi,magazin1)
"""

# Varianta b
lista_cumparaturi = {
    "mere":1,
    "banane":2,
    "paine":4,
    "carne":3,
    "ore":1    ### Scris intentionat gresit sa nu apara in nici un magazin
}


magazin1 = {
    "mere":3,
    "banane": 4,
    "paine": 4,
    "carne": 15,
    "orez": 2
}

magazin2 = {
    "mere":2,
    "banane": 5,
    "paine": 3,
    "carne": 16,
    "orez": 1.5
}
magazin3 = {
    "mere":1,
    "banane": 3.4,
    "paine": 4,
    "carne": 12,
    "orez": 4
}

magazine = [magazin1,magazin2,magazin3]

def pret_minim(produs):
    minim=999999
    for i in range(len(magazine)):
        if produs in magazine[i]:
           if magazine[i][produs] < minim:
               minim=magazine[i][produs]
    return(minim)

def pret_cumparaturi(lista):
    suma=0
    for i in lista:
        pret=pret_minim(i)
        if pret == 999999:
            print(i," nu a fost gasit in nici un magazin")
        else:
            suma=suma+float(lista[i])*pret
    print(suma)

pret_cumparaturi(lista_cumparaturi)