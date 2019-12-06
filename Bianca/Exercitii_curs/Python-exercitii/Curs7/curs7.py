"""sala_de_clasa = {

    "culoare" : "verde",
    "mese": 6,
    "scaune": 22,
    "proiector": 2,
    "ferestre": 6,
    "prize": "putine",
    "becuri": 9,
    "tabla": 1,
    "cos_de_gunoi": "are",
    "studenti": "da",
    "mocheta": "una_mare",
    "profi" : ["Tanta", "leone"]

}

"""
"""
print(len(sala_de_clasa))

print(sala_de_clasa.keys())

print(sala_de_clasa.values())

print(sala_de_clasa["becuri"])


print(sala_de_clasa)


print(sala_de_clasa["studenti"])

sala_de_clasa["plante"]="fara"
sala_de_clasa["wi-fi"]="nu sunt fonduri"

print(sala_de_clasa)
"""


magazine = {
    "filiala": ["Buziasului", "Torontalului"],
    "tura" : ["zi","noapte"],
    "zi": ["luni", "marti", "miercuri", "joi", "vineri"],
    "depozit" : ["A123","B432"],
    "nr_angajati_tura" : [5, 2],
    "inventar" : [True , False],
    "non-stop": ["nu"]

}

"""magazine["ceva"]="Tuts"
magazine["ceva1"]=["Tutss","lallal"]   --> ["tuts"],["lala"]

print(magazine["ceva"][0])
print(magazine["ceva1"][0])

"""

for i in magazine.keys():
    for j in magazine[i]:
        print(i,j)




