#1. Scrieti un program care verifica numerele divizibile cu 7 ( din intervalul 1500 – 2700 ) si le introduce intr-o
#lista noua cu numele div_7. Analog pentru cele divizibile cu 5, introduse in lista div_5.
# div_5 = []
# div_7 = []
# for i in range(1500,2700):
#         if (i % 7 == 0):
#             div_7.append(i)
#         elif(i%5 == 0):
#             div_5.append(i)    
# print("Lista numerelor divide cu 7",div_7)
# print("Lista numerelor divide cu 5",div_5)
###########################
# Scrieti un program care:
# a. Cere ca input: temperatura in grade Celsius
# b. O transforma in grade Fahrenheit
# c. Printeaza valoarea rezultata sub forma: x grade Celsius = y grade Fahrenheit
# d. Formula pentru conversie: temperature in Fahrenheit = (temperatura in grade Celsius * 9/5)+ 32


# temperatura_celsius = float(input("Introdu temperatura in grade Celsius:"))
# temperatura_fahrenheit = (float(temperatura_celsius)*9/5)+32
# print(temperatura_celsius,"grade Celsius","=",temperatura_fahrenheit,"grade Fahrenheit ")
###########################
# rows = input("Enter max star to be display on single line")
# rows = int (rows)
# for i in range (0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

####################################
# Creati un program care:
# a. Seteaza intr-o variabila ghici un numar pe care utilizatorul trebuie sa il ghiceasca
# b. Cere urmatorul input: ( Ghiceste numarul! : ... )
# c. Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici, se va printa un mesaj in consecinta. In caz contrar, utilizatorul va fi felicitat.
# i. Extra point: Daca numarul introdus de utilizator nu corespunde cu cel din variabila ghici, I se va cere sa introduca numere pana ajunge la numarul cautat. ( Hint: use a loop )

# ghici = 10
# concurent = int(input("Ghiceste un numar intre 10..100:"))
# while concurent != ghici :
#     print("Mai cauta..") 
#     concurent = int(input("Ghiceste un numar intre 10..100:"))
# print("Felicitari ai gasit numarul")

######################################
# Scrieti un program cu urmatoarele cerinte:
# a. Creati o lista cu 30 numere
# b. Mutati numerele pare intr-o lista nr_pare si pe cele impare intr-o lista nr_impare.
# c. Numarati cate nr. Pare si cate impare sunt.
# d. Faceti 2 print-uri in care sa specificati nr. Elemente pare/ nr. Elemente impare.

# lista=[22,21,33,61,73,25,90,42,55,35,44,81,4,6,8,9,10,91,92,96,61,333333333333,11111115,849494,65484984,32181865,651961598,51818,845,6515]
# # print(len(lista))
# i=0
# lista_numere_pare= []
# lista_numere_impare= []
# for i in lista:
#     if i % 2 == 0:
#         lista_numere_pare.append(i)
#     elif i % 2 == 1:
#         lista_numere_impare.append(i)
# print(lista_numere_pare)
# print("nr.Elemente pare",len(lista_numere_pare))
# print(lista_numere_impare)
# print("nr.Elemente impare",len(lista_numere_impare))



###################################### 

# print ("""
# ooooooooooooooooo
# ooooooooooooooooo
# ooooooooooooooooo
# oooo
# oooo
# oooo
# ooooooooooooooooo
# ooooooooooooooooo
# ooooooooooooooooo
#              oooo
#              oooo
#              oooo
# ooooooooooooooooo
# ooooooooooooooooo
# ooooooooooooooooo
# """)
###################################
#6. Scrieti un program care printeaza numerele din intervalul 0 – 15, in afara de cifrele 3 si 7. (Utilizati
#instructiunea continue!)
# for i in range(0,15):
#     if i ==3 or i == 7:
#         continue
#     print(i) 
##################################
#7. Creati un program care printeaza toate numerele de la 0 la 50, avand in vedere urmatoarele conditii:
#a. In loc de 0 se va printa PythonBuzz
#b. In locul multiplilor de 5 se va printa Python5
#c. In locul multiplilor de 7 se va printa 7Python

# print ("PythonBuzz")
# for i in range (1,50):
# 
#     if i%5 == 0:
#         print (i,"Python5")
#     if i%7 == 0:
#         print (i,"7Python")


####################################        
# Folosind doua structure for si functia print() , creati urmatorul model:

# for i in range (0,5):
#     for j in range (0, i+1):
#         print ("* ", end="")
#     print("\r")
# for i in range(0,5):
#     for j in range (4 ,i,-1):
#         print ("* ", end="")        
#     print()        

import re
password=input("Insert password...:")
letters=re.search('[0-9]', password)
symbol=re.search('[!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]', password)
for i in range(len(password)):
    if i >=7:
        if letters and symbol:
            letters=True
            symbol=True
            print("The password has been created!")
        elif letters:
            letters=False
            print("Failed!..The password must contain letters")
        elif symbol:
            symbol=False
            print ("Failed!..The password must contain a special character") 
if i < 6:
    print ("Failed!..The password must contain more characters...")  
