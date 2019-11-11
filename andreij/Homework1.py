### 1 ###
"""
lista1 = [1, 4, 5, 7, 12, 14 ,15, 19, 20, 25, 33, 45, 49, 63, 21,2443]
lista2 = [0, 2, 5, 8, 10, 15, 12, 1, 50, 55, 70, 89, 85, 35, 25, 1705]
div_7 = []
div_5 = []

for i in range(len(lista1)):
    if lista1[i] >= 1700 and lista1[i] <= 2500:
        if lista1[i] % 7 == 0:
            div_7.append(lista1[i])
print("Lista numerelor divizibile cu 7: \n", div_7, "\n")

for i in range(len(lista2)):
    if lista2[i] >= 1700 and lista2[i] <= 2500:
        if lista2[i] % 5 == 0:
            div_5.append(lista2[i])
print("Lista numerelor divizibile cu 5: \n", div_5)"""

### 2 ###
"""
temperatura = input("Introduceti temperatura in grade celsius: ")
Fahrenheit = (float(temperatura)*9/5) + 32
print("Temperatura de", temperatura, "grade Celsius = ", Fahrenheit, "grade Fahrenheit")"""

### 3 ###
"""
ghici = 49
for i in range(100):
    ghiceste = int(input("Ghiceste numarul!: "))
    if ghiceste == ghici:
        print("Felicitari! Ati ghicit numarul!")
        break
    else:
        print("Mai incearca")
"""
### 4 ###

"""
for i in range(5):
    print("*")"""

### 5 ###
"""
v = [1, 2, 3, 4, 5, 6, 7, 8, 20, 10, 30, 15, 2, 5, 7, 8, 9, 30, 22, 32, 15, 12, 49, 50, 12, 61, 99, 100, 1005, 2003, 600, 666, 2005]

l_par = []
l_impar = []

for i in range(len(v)):
    if v[i] % 2 == 0:
        l_par.append(v[i])
    elif v[i] % 2 == 1:
        l_impar.append(v[i])
        
print("In lista para sunt ", len(l_par), "elemente\n", l_par, "\n")
print("In lista impara sunt", len(l_impar), "elemente\n", l_impar, "\n")"""


### 6 ###
"""
for i in range(50):
    if i == 0:
        print("PythonBuzz")
    elif i % 5 ==0:
        print("Python5")
    elif i % 7 == 0:
        print("Python7")
    elif i % 5 == 0 and i % 7 == 0:
        print("5Python7")
    else:
        print(i)"""

### EXTRA ###

