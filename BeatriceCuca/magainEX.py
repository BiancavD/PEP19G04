magazin1 = {
    "lapte": 1,
    "oua": 2,
    "paste": 3,
    "bacon": 4,
    "ardei": 5,
    "salam": 5345346,
    "piper":50,
}

magazin2 = {
    "lapte": 8,
    "oua": 9,
    "paste": 10,
    "bacon": 11,
    "ardei": 12,
    "salam": 143,
    "piper": 14,
}

magazin3 = {
    "lapte": 14,
    "oua": 15,
    "paste": 56789016,
    "bacon": 17,
    "ardei": 18,
    "salam": 19,
    "piper": 20,
}

"""for i in magazin1:
    print(i, ":", magazin1[i])

for i in magazin2:
    print(i, ":", magazin2[i])

for i in magazin3:
    print(i, ":", magazin3[i])"""

lista1 = []
lista2 = []

def functie(produs):
    if magazin1[produs] < magazin2[produs]:
        print("magazin1 --> ieftin")
        lista1.append(1)
    elif magazin1[produs] > magazin2 [produs]:
        print("magain2 -->  mai ieftin")
        lista2.append(2)
    else:
        print("Au acelasi pret")

for i in magazin1:
    functie(i)

print(lista1)
print(lista2)

if len(lista1) > len(lista2):
    print("Primul magazin are mai multe produse mai ieftine") 
else:
    print("Magaiznul 2 are mai multe prof ieftine")