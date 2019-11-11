"""
Scrieti un program care verifica numerele divizibile cu 7 ( din intervalul 1500 – 2700 ) si le introduce intr-o
lista noua cu numele div_7. Analog pentru cele divizibile cu 5, introduse in lista div_5.
"""

"""
i=1500
div_5=[]
div_7=[]
while i<=2700:
    if (i % 5) == 0:
        div_5.append(i)
    if (i % 7) == 0:
        div_7.append(i)
    i=i+1
print(div_5)
print(div_7)
"""
#####################################################################################################################################################
"""
2. Scrieti un program care:
a. Cere ca input: temperatura in grade Celsius
b. O transforma in grade Fahrenheit
c. Printeaza valoarea rezultata sub forma: x grade Celsius = y grade Fahrenheit
d. Formula pentru conversie: temperature in Fahrenheit = (temperatura in grade Celsius * 9/5)+ 32
"""
"""
temperatura_celsius=float(input("Temperatura in grade celsius este="))
print(temperatura_celsius," grade celsius sunt",((temperatura_celsius*9/5)+32)," grade Fahrenheit")
"""
#####################################################################################################################################################
"""
Creati un program care:
a. Seteaza intr-o variabila ghici un numar pe care utilizatorul trebuie sa il ghiceasca
b. Cere urmatorul input: ( Ghiceste numarul! : ... )
c. Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici, se va printa un
mesaj in consecinta. In caz contrar, utilizatorul va fi felicitat.
i. Extra point: Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici,
I se va cere sa introduca numere pana ajunge la numarul cautat. ( Hint: use a loop )
d. Daca utilizatorul ghiceste numarul, se va afisa mesajul : Felicitari! Ati ghicit numarul!
"""
"""
ghici=32
i=int(input("Introdu un numar intre 0 si 100:"))
while (i != ghici):
    print("Nu ai ghicit , mai incearca")
    i=int(input("Introdu un numar intre 0 si 100:"))
print("Felicitari, ai ghicit")
"""
#####################################################################################################################################################
"""
Folosind doua structure for si functia print() , creati urmatorul model:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* * 
*
"""
"""
stelute=""
for i in range(5):
    stelute=stelute+" *"
    print(stelute)

for i in range(4,0,-1):
    stelute = stelute[:-2]
    print(stelute)
"""
#####################################################################################################################################################
"""
5. Scrieti un program cu urmatoarele cerinte:
a. Creati o lista cu 30 numere
b. Mutati numerele pare intr-o lista nr_pare si pe cele impare intr-o lista nr_impare.
c. Numarati cate nr. Pare si cate impare sunt.
d. Faceti 2 print-uri in care sa specificati nr. Elemente pare/ nr. Elemente impare.
"""
"""
nr_pare=[]
nr_impare=[]
lista=[1,2,3,4,5,6,7,8,9,10,12,14,54,2,43,65,87,3,65,877,456,123,457,333,444,999,878,766,554]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        nr_pare.append(lista[i])
    else:
        nr_impare.append(lista[i])
print("Numere pare sunt ",len(nr_pare))
print("Numere impare sunt ",len(nr_impare))
print(nr_pare)
print(nr_impare)
"""
#####################################################################################################################################################
"""
6. Scrieti un program care printeaza numerele din intervalul 0 – 15, in afara de cifrele 3 si 7. (Utilizati
instructiunea continue!)
"""
"""
for i in range(15):
    if ( (i ==3 ) or (i == 5) ):
        continue;
    print(i)
"""
#####################################################################################################################################################
"""
7. Creati un program care printeaza toate numerele de la 0 la 50, avand in vedere urmatoarele conditii:
a. In loc de 0 se va printa PythonBuzz
b. In locul multiplilor de 5 se va printa Python5
c. In locul multiplilor de 7 se va printa 7Python
"""
"""
print("0 - PythonBuzz")
for i in range(1,51):
    if ( i % 5 ==0 ):
        print(i," - Python5")
    if (i % 7 == 0 ):
        print(i, " - Python7")
"""
#####################################################################################################################################################
"""
Printati urmatorul model:
ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo
oooo
oooo
oooo
ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo
	         oooo
 	         oooo
 	         oooo
ooooooooooooooooo
ooooooooooooooooo
ooooooooooooooooo
"""

#print("""
#ooooooooooooooooo
#ooooooooooooooooo
#ooooooooooooooooo
#oooo
#oooo
#oooo
#ooooooooooooooooo
#ooooooooooooooooo
#ooooooooooooooooo
#	         oooo
# 	         oooo
# 	         oooo
#ooooooooooooooooo
#ooooooooooooooooo
#ooooooooooooooooo
#""")

#####################################################################################################################################################
import re
parola=str(input("Enter your pass(min 7 chars, at least 1 digit and at least 1 special character) = "))
if len(parola)>=7:
    if re.search("[0-9]",parola):
        if re.search("[+,!,@,#,$,%,^,&,*,(,)]",parola):
            print("Parola respecta cerintele")
            exit()
print("Parola nu respecta cerintele")
