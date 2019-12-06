
"""
cuvant: definitie
key : value"""

"""
sala_de_clasa = {

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
    "mocheta": "una_mare"
}

print(len(sala_de_clasa))
print()
print(sala_de_clasa.keys())
print()

print(sala_de_clasa.values())
print()

for element in sala_de clasa;
	print(element)

for element in sala_de_clasa:
    print(element, "->", sala_de_clasa[element])
"""

"""
print(sala_de_clasa["mese"])

print(sala_de_clasa["studenti"])

del sala_de_clasa["studenti"]

sala_de_clasa.clear()

"""



"""
for element in sala_de_clasa.keys():
    for j in sala_de_clasa.values():
        print(element, " -> ", j)"""
"""

camera = {
    "pereti": 4,
    "mese": 7,
    "scaune": 14,
    "geam": 6,
    "usa": 1,
    "suprafata": 36,
    "temperatura": ["oribil", "horror"],
    "proiector": True,
    "neoane": 9,
    "nr": 2

}

"""
"""
magazine = {
    "filiala": ["Buziasului", "Torontalului"],
    "tura" : ["zi","noapte"],
    "zi": ["luni", "marti", "miercuri", "joi", "vineri"],
    "depozit" : ["A123","B432"],
    "nr_angajati_tura" : [5, 2],
    "inventar" : [True , False],
    "non-stop": True

}

for i in magazine:
    print(i,magazine[i])

print(magazine["tura"][1])
print(magazine["filiala"][0])
"""


"""
spor_departament= {
    "Software" : 150,
    "HR" : 100,
    "Marketing" : 50

}


angajat1={
    "nume" : "Melissa",
    "varsta" : 34,
    "departament" : "Software",
    "salariu_lunar" : 3400,
    "vechime" : 6,
    

}

def salariu_luni(salariu_lunar,nr_luni):
    return salariu_lunar * nr_luni

def salariu_total(salariu_lunar,nr_luni,spor,vechime):
    if vechime > 5:
        return salariu_luni(salariu_lunar,nr_luni) + spor
    else:
        return salariu_luni(salariu_lunar,nr_luni)

angajat1["salariu_anual"]=salariu_luni(angajat1["salariu_lunar"],12)
angajat1["salariu_total"]=salariu_total(angajat1["salariu_lunar"],12,spor_departament[angajat1["departament"]],angajat1["vechime"])

print(angajat1)
"""


"""

angajat2={
    "nume" : "Vlad",
    "varsta" : 44,
    "departament" : "HR",
    "salariu_lunar" : 4500,
    "vechime" : 12,
    

}

angajat2["salariu_anual"]=salariu_luni(angajat2["salariu_lunar"],12)
angajat2["salariu_total"]=salariu_total(angajat2["salariu_lunar"],12,spor_departament[angajat2["departament"]],angajat2["vechime"])

for i in angajat2.keys():
    print(i, angajat2[i], sep=": ")

lista_angajati = []
lista_angajati.append(angajat1)
lista_angajati.append(angajat2)

print(lista_angajati)
"""