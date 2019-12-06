""" class Masa:
   
    picioare = None
    lungime = None
    material = None

    def __init__(self, picioare, lungime, material):
        self.picioare = picioare
        self.lungime = lungime
        self.material = material

   ### Note: Self - referinta instantei curente a clasei --> se utilizeaza pentru a accesa variabilele care apartin clasei.
   ### self poate fi numit oricum, dar trebuie neaparat sa fie primul parametru al oricarei metode scrire in clasa


    def afisare(self):
        print("Masa are", self.picioare, "picioare, o lungime de", self.lungime, "m si este fabricata din", 
                                                                                                    self.material)
print()
m1 = Masa(2,1.80,"lemn")
m1.afisare()

print()
m2 = Masa(4,1.3,"plastic")
m2.afisare()

"""

"""
class Camera():

    def __init__(self,numar,suprafata):
        self.numar = numar
        self.suprafata = suprafata
    
    def print(self): #metoda
        print("Camera",self.numar,"are o suprafata de",self.suprafata,"mp") #functie
        print("Suprafata camerei este",self.suprafata)

a = Camera(307,32)
a.print() #metoda, apeleaza metoda definita in clasa
print()
#print(a) #functie, printeaza zona de memorie unde se afla obiectul a
#print()
b = Camera(306,18)
b.print()
print()
c = Camera(305,22)
c.print()
"""
"""
casa = []
casa.append(a)
casa.append(b)
"""


