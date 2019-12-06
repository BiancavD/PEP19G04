"""def print_smth():
    print("Hello, I am Bianca!")"""
"""
"""
"""Functie cu 1 argument
def print_nume(nume):
    print("Hello! My name is: ",nume)

print_nume("Bianca")
"""

"""Functie cu 2 argumente
def print_nume(nume,varsta):
    print("Hello! My name is:",nume, "and I am:",varsta,"years old")

print_nume("Bianca",21)
"""
"""Functie cu 2 argumente dintre care unul predefinit
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("James Bond")
"""
""" Argument - lista

def suma_lista(lista):
    suma=0
    
    for x in lista:
        suma+=x 
    print(suma)

x=[1,2,43,2]

suma_lista(x)

"""

""" Return - oprire functie

def adevar(adevar = True):
    print("Adevarat? ")

    if not adevar:
        return
    
    print("Este adevarat!")

adevar(True) # adevar(False) 

"""

"""
def none_func(n):
    if n % 2 == 0:
        return True

print(none_func(4))
print(none_func(3))
"""
"""Return Functions
def function(name, fname):
    return name, fname


print(function("Bianca", "Dumitriu"))
print(function(fname="Bianca", name = "Dumitriu"))
"""
"""
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
    weight < 20 or weight > 200:
        return None
    
    return weight / height ** 2

print(bmi(352.5, 1.65))
"""


"""
def functie():
    
    n = 0
    print(n)
    n = n + 1
    print(n)"""

"""
def functie1():
    global n
    n=2
    n = n + 1
    print(n)

n=4
###print(n) --- cat o sa fie n

print(functie1()) ## de ce apare None - print 
"""


"""

def fact(n):

    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print(fact(100))"""

"""def something():
    for i in range(77):
        if i <= 3 :
            continue
        else:
            print(i) 
            break

print(something())"""
"""
