#Realizar operaciones de unión, intersección y diferencia de conjuntos
cantidadA=int(input("Ingrese la cantidad de elemento que tendrá el conjunto A: "))
conjuntoA=set()
for i in range(cantidadA):
    elementoA=input(f"ingrese elemento  N°{i+1} : ")  
    conjuntoA.add(elementoA)
cantidadB=int(input("Ingrese la cantidad de elemento que tendrá el conjunto B: "))
conjuntoB=set()
for i in range(cantidadB):
    elementoB=int(input(f"ingrese elemento  N°{i+1} : "))  
    conjuntoB.add(elementoB)
def unionConjuntos(a,b):
    return a.union(b)
def interseccionConjuntos(a,b):
    return a.intersection(b)
def diferenciaConjuntos(a,b):
    return a.diferencia(b)
operacion= int(input("Indique que operacion desea \n[1] Unión \n[2] Intersección \n[3] Diferencia\n ->"))
if operacion ==1:
    print("la union de los conjuntos es", unionConjuntos(conjuntoA,conjuntoB))
elif operacion ==2:
    print("la interseccion de los conjuntos es", interseccionConjuntos(conjuntoA,conjuntoB))
else:
    print("La diferencia de los conjuntos es", diferenciaConjuntos(conjuntoA,conjuntoB))    



