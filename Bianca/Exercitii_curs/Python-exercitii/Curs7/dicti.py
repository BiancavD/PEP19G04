
#Utilizand dictionarele, sa se creeze 3 magazine cu cel putin 5 produse cu preturi diferite.
#Sa se creeze un program care verifica pentru fiecare produs unde este magazinul cu cel mai mic 
#si printeaza mesajul sub forma " Produsul x este cel mai ieftin in magazinul Y"




magazin1 = {
    "mere" : 3,
    "pere" : 4.5,
    "bere" : 11,
    "popcorn" : 2,
    "banane" : 5

}

magazin2 = {
    "mere" : 4,
    "pere" : 5.5,
    "bere" : 10,
    "popcorn" : 2.5,
    "banane" : 8

}

magazin3 = {
    "mere" : 2.3,
    "pere" : 5,
    "bere" : 13,
    "popcorn" : 3.2,
    "banane" : 5.5

}



"""
#Varianta 1
if magazin1["mere"]<magazin2["mere"] and magazin1["mere"]<magazin3["mere"]:
    print("Cele mai ieftine mere sunt la magazin1!")
    puncte1+=1
elif magazin2["mere"]<magazin1["mere"] and magazin2["mere"]<magazin3["mere"]:
    print("Cele mai ieftine mere sunt la magazin2!")
    puncte2+=1
elif magazin3["mere"]<magazin1["mere"] and magazin3["mere"]<magazin2["mere"]:
    print("Cele mai ieftine mere sunt la magazin3!")
    puncte3+=1

if magazin1["pere"]<magazin2["pere"] and magazin1["pere"]<magazin3["pere"]:
    print("Cele mai ieftine pere sunt la magazin1!")
    puncte1+=1
elif magazin2["pere"]<magazin1["pere"] and magazin2["pere"]<magazin3["pere"]:
    print("Cele mai ieftine pere sunt la magazin2!")
    puncte2+=1
elif magazin3["pere"]<magazin1["pere"] and magazin3["pere"]<magazin2["pere"]:
    print("Cele mai ieftine pere sunt la magazin3!")
    puncte3+=1



if puncte1>puncte2 and puncte1>puncte3:
    print("Cel mai ieftin magazin este magazinul 1!")
elif puncte3>puncte2 and puncte3>puncte1:
     print("Cel mai ieftin magazin este magazinul 3!")
elif puncte2>puncte1 and puncte2>puncte3:
     print("Cel mai ieftin magazin este magazinul 2!")
else:
    print("Egalitate")
"""
"""
#Varianta2
def ieftin_mag1(produs):
    
    if magazin1[produs]<magazin2[produs] and magazin1[produs]<magazin3[produs]:
        print("Cele mai ieftin produs:",produs,"sunt la magazin1!")
        p1=1
        return p1

    else:
        return 0

    
def ieftin_mag2(produs):
    if magazin2[produs]<magazin1[produs] and magazin2[produs]<magazin3[produs]:
        print("Cele mai ieftin produs:",produs," sunt la magazin2!")
        p2=1
        return p2
    else:
        return 0

def ieftin_mag3(produs):
    if magazin3[produs]<magazin1[produs] and magazin3[produs]<magazin2[produs]:
        print("Cele mai ieftin produs: ", produs," sunt la magazin3!")
        p3=1
        return p3
    else:
        return 0


puncte1=0
puncte2=0
puncte3=0

for produs in magazin1.keys():
    puncte1+=ieftin_mag1(produs)

for produs in magazin2.keys():
    puncte2+=ieftin_mag2(produs)

for produs in magazin3.keys():
    puncte3+=ieftin_mag3(produs)

if puncte1>puncte2 and puncte1>puncte3:
    print("Cel mai ieftin magazin este magazinul 1!")
elif puncte3>puncte2 and puncte3>puncte1:
     print("Cel mai ieftin magazin este magazinul 3!")
elif puncte2>puncte1 and puncte2>puncte3:
     print("Cel mai ieftin magazin este magazinul 2!")
else:
    print("Egalitate")


"""
"""
#Varianta 3
puncte1=0
puncte2=0
puncte3=0

def ieftin(produs):
    global puncte1,puncte2,puncte3

    if magazin1[produs]<magazin2[produs] and magazin1[produs]<magazin3[produs]:
        print("Cel mai ieftin produs [",produs,"] se gaseste la magazin1!")
        puncte1+=1
    elif magazin2[produs]<magazin1[produs] and magazin2[produs]<magazin3[produs]:
        print("Cel mai ieftin produs [",produs,"] se gaseste la magazin2!")
        puncte2+=1
    elif magazin3[produs]<magazin1[produs] and magazin3[produs]<magazin2[produs]:
        print("Cel mai ieftin produs [",produs,"] se gaseste la magazin3!")
        puncte3+=1

    return puncte1,puncte2,puncte3
lista=[]

for produs in magazin1.keys():
    lista.append(produs)

for produs in lista:
    ieftin(produs)
"""