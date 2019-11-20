"""lista_div5=[]#1
lista_div7=[]
nr=1500
while (nr<=2100):
    if nr%5==0:
        lista_div5.append(nr)
    if nr%7==0:
         lista_div7.append(nr)
    nr=nr+1
print ("Cele divizibile cu 5 sunt: ", lista_div5)
print("Cele divizibile cu 7 sunt: " , lista_div7)



c=input("Spune-mi te rog cate grade C sunt afara: ")#2
f=(int(c)*9/5)+32
print(int(c), "grade Celsius:=", int(f),"grade firen")


ghici=input("Ghiceste numarul: ")#3
if int(ghici)==25:
    print("Bravo!")
while int(ghici)!=25:
    print("Mai incearca!")


lista_nr_par=[]#5
lista_nr_impar=[]
a=range(30,60)
i=30
while (i<=60):
    if i%2==0:
        lista_nr_par.append(i)
    if i%2==1:
        lista_nr_impar.append(i)
    i=i+1
print ("Numelere pare sunt: " , lista_nr_par)  
print ("Dimensiunea listei de nr pare este: ", len(lista_nr_par))
print("Numelere impare sunt: ", lista_nr_impar)
print ("Dimensiunea listei de nr impare este: " ,len(lista_nr_impar))

a=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)#6
for i in range (len(a)):
    if(a[i]==3) or(a[i]==7):
        continue
print(a[i])

print("ooooooooooooooooooooo")#8
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("oooooo")
print("oooooo")
print("oooooo")
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("               oooooo")
print("               oooooo")
print("               oooooo")
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
print("ooooooooooooooooooooo")
"""


lista_all=[]
i=0
for i in range(0,50):
    if (i==0):
       lista_all.append("PythonBuzz") 
    if (i%5==0):
        lista_all.append("Python5")
    if (i%7==0):
        lista_all.append("Python7")
    if (i%5==0) and (i%7==0):
        lista_all.append("5Python7") 
    i=i+1

print(lista_all)

