class Masa:
   
    picioare = None
    lungime = None
    material = None

    def __init__(self, picioare, lungime, material):
        self.picioare = picioare
        self.lungime = lungime
        self.material = material


    def afisare(self):
        print("Masa are", self.picioare, "picioare, o lungime de", self.lungime,"m si este fabricata din",self.material)


masa1=Masa(2,1.80,"lemn")
masa2=Masa(3,1.23,"otel")
masa3=Masa(4,22.3,"lemn")


masa1.afisare()