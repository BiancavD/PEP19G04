###1. Scrieti un program care verifica numerele divizibile cu 7 ( din intervalul 1500 – 2700 ) si le introduce intr-o
##lista noua cu numele div_7. Analog pentru cele divizibile cu 5, introduse in lista div_5.
"""
div_7=[]
div_5=[]
for i in range(1500,2700):
    if i%7==0:
        div_7.append(i)        
for j in range(1500,2700):
    if j%5==1:
        div_5.append(j)
"""
######2. Scrieti un program care:
#####a. Cere ca input: temperatura in grade Celsius
####b. O transforma in grade Fahrenheit
###c. Printeaza valoarea rezultata sub forma: x grade Celsius = y grade Fahrenheit
##d. Formula pentru conversie: temperature in Fahrenheit = (temperatura in grade Celsius * 9/5)+ 32
"""T_C=float(input("Introduceti temperatura in grade Celsius: "))
T_K=(T_C*9/5)+32
print(str(T_C) + " grade celsius = "+str(T_K) +" grade Fahrenheit")"""

######3. Creati un program care:
#####a. Seteaza intr-o variabila ghici un numar pe care utilizatorul trebuie sa il ghiceasca
####b. Cere urmatorul input: ( Ghiceste numarul! : ... )
###c. Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici, se va printa un
##mesaj in consecinta. In caz contrar, utilizatorul va fi felicitat.
#i. Extra point: Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici,
###I se va cere sa introduca numere pana ajunge la numarul cautat. ( Hint: use a loop )
##d. Daca utilizatorul ghiceste numarul, se va afisa mesajul : Felicitari! Ati ghicit numarul!
"""
numar=float(input("Introduceti numarul:"))
ghici=float(input("Guess: "))
*if numar==ghici:
    print("Felicitari!Ai ghicit numarul!")
else:
    print("Nu ai ghicit numarul!")

*while numar!=ghici:
    ghici=float(input("Try again! :"))
print("Ai ghicit!")
"""

####5. Scrieti un program cu urmatoarele cerinte:
###a. Creati o lista cu 30 numere
##b. Mutati numerele pare intr-o lista nr_pare si pe cele impare intr-o lista nr_impare.
##c. Numarati cate nr. Pare si cate impare sunt.
##d. Faceti 2 print-uri in care sa specificati nr. Elemente pare/ nr. Elemente impare.
"""a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
impare=[]
pare=[]
for i in range(len(a)):
    if a[i]%2==0:
        impare.append(i)
for j in range(len(a)):
    if a[j]%2==1:
        pare.append(j)
print(pare)
print(impare)
print("Sunt "+str(len(pare))+ " numere pare")
print("Sunt "+str(len(impare))+" numere impare")"""
##6. Scrieti un program care printeaza numerele din intervalul 0 – 15, in afara de cifrele 3 si 7. (Utilizati
##instructiunea continue!)
"""a=range(0,15)
for i in range(len(a)):
    while a[i]!=3 and a[i]!=7:
        print(a[i])
        break"""
####7. Creati un program care printeaza toate numerele de la 0 la 50, avand in vedere urmatoarele conditii:
###a. In loc de 0 se va printa PythonBuzz
##b. In locul multiplilor de 5 se va printa Python5
#c. In locul multiplilor de 7 se va printa 7Python
"""
a=range(0,50)
for i in range(len(a)):
    if i==0:
        print("PythonBuzz")
    elif a[i]%5==0 and a[i]%7==0:
        print("Python5 & 7Python)
    elif a[i]%5==0:
        print("Python5")
    elif a[i]%7==0:
        print("7Python")
    else: 
        print(a[i])
"""
#2. Creati un program care: 
# a. Cere ca input un string: parola 
# b. Verifica daca:  
# i. Are cel putin 7 caractere 
# ii. Daca are cel putin o cifra 
# iii. Daca are cel putin un caracter special 
# iv. Hint: Documentati-va despre functia search() din biblioteca re 
import re
parola=input("Introduceti parola: ")
cifre=re.search('[0-9]', parola)
simbol=re.search('[!@#$%^&*(),.?":{}|<>]', parola)
for i in range(len(parola)):
    if i>=6:
        if cifre and simbol:
            cifre==True
            simbol==True
            print("Password created sucessfully!")
            break
        elif simbol:
            simbol==False
            print("Error!Cifre not found") 
            break
        elif cifre:
            cifre==False
            print("Error!Simbol not found")
            break
if i<6:
    print("Error!")
    

            
        
    







"""   if i>=6:
        if cifre==False:
            print("Error!")
            break
        if simbol==False:
                print("Error!")
                break
    print("Password created succesfully!")        
if i<6:
    print("Error!")"""