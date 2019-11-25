"""A) Sa se creeze un program care creeaza 3 dictionare:
	1. sport departament ( 3 departamente si salariul pe departament )
	2. angajat1 ( nume, varsta, departament,salariu_lunar,vechime )
	3. angajat2 ( nume, varsta, departament,salariu_lunar,vechime )

B) Sa se defineasca o functie salariu_luni(salariu_lunar,nr_luni) care calculeaza salariul in functie de nr. de luni dorit
C) Sa se defineasca o functie salariu_total(salariu_lunar,nr_luni,spor,vechime):	
	a. Daca angajatul are o vechime mai mare de 5 ani, i se adauga la salariu un spor
	b. In caz contrar, salariul se calculeaza in mod obisnuit, fara spor.

D) Sa se adauge in dictionar 2 key noi ("salariu_anual" si "salariu_total") calculate prin intermediu functiilor de la punctele B) si C)
1. Parcurgere exercitii curs ( intrebari, consolidare pe subiect )

2. Problema dictionar ( parcurgere, intrebari, consolidare pe subiect ):
	- sa se adauge pentru fiecare angajat alte 2 valori: ore_suplimentare, proiecte_extracurriculare, tarif_suplimentare
	- sa se scrie o functie care verifica daca angajatul are ore suplimentare si sa adauge la salariul un bonus in functie de orele suplimentare si tariful
 pe orele suplimentare
	- sa se scrie o functie care adauga la salariul fiecarui angajat un bonus in functie de nr. de proiecte extracurriculare ( 200 lei/proiect )
"""


spor_departament= {
    "Software" : 300,
    "HR" : 100,
    "Marketing" : 50

}


angajat1={
    "nume" : "Melissa",
    "varsta" : 34,
    "departament" : "Software",
    "salariu_lunar" :100,
    "vechime" : 2,
    "ore_suplimentare" :2,
    "proiecte_extracurriculare" : 2,
    "tarif_suplimentare" : 10


}

def salariu_luni(salariu_lunar,nr_luni):
    return salariu_lunar * nr_luni

def salariu_total(salariu_lunar,nr_luni,spor,vechime):
    if vechime > 5:
        return salariu_luni(salariu_lunar,nr_luni) + spor
    else:
        return salariu_luni(salariu_lunar,nr_luni)

def ore_supli(salariu_lunar, vechime,nr_luni, ore_suplimentare, spor, tarif_suplimentare):
    if ore_suplimentare > 0:
        return salariu_luni(salariu_lunar,nr_luni) + spor + (ore_suplimentare * tarif_suplimentare)
    else:
        return salariu_luni(salariu_lunar,nr_luni)

def bonus(salariu_lunar, vechime,nr_luni, ore_suplimentare, spor, tarif_suplimentare, proiecte_extracurriculare):
    if  proiecte_extracurriculare >0:
        return salariu_luni(salariu_lunar,nr_luni) + spor + (ore_suplimentare* tarif_suplimentare)+ (proiecte_extracurriculare*200)
    else:
        return salariu_luni(salariu_lunar,nr_luni)

angajat1["salariu_anual"]=salariu_luni(angajat1["salariu_lunar"],12)
angajat1["salariu_total"]=salariu_total(angajat1["salariu_lunar"],12,spor_departament[angajat1["departament"]],angajat1["vechime"])
angajat1["ore_supli"]=ore_supli(angajat1["salariu_lunar"],angajat1["vechime"],12, angajat1["ore_suplimentare"],spor_departament[angajat1["departament"]], angajat1["tarif_suplimentare"])
angajat1["bonus"]=bonus((int)(angajat1["salariu_lunar"]),(int)(angajat1["vechime"]), 12,(int)(angajat1["ore_suplimentare"]), spor_departament[(angajat1["departament"])], (int)(angajat1["tarif_suplimentare"]),(int)(angajat1["proiecte_extracurriculare"]))

print(angajat1)




angajat2={
    "nume" : "Vlad",
    "varsta" : 44,
    "departament" : "HR",
    "salariu_lunar" : 4500,
    "vechime" : 12,
    "ore_suplimentare" :15,
    "proiecte_extracurriculare" : 5,
    "tarif_suplimentare" : 80


}

angajat2["salariu_anual"]=salariu_luni(angajat2["salariu_lunar"],12)
angajat2["salariu_total"]=salariu_total(angajat2["salariu_lunar"],12,spor_departament[angajat2["departament"]],angajat2["vechime"])

for i in angajat2.keys():
    print(i, angajat2[i], sep=": ")

lista_angajati = []
lista_angajati.append(angajat1)
lista_angajati.append(angajat2)

print(lista_angajati)