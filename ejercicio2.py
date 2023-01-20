# Calcular la diferencia entre dos conjuntos
cantidadA=int(input("Ingrese la cantidad de elemento que tendrá el conjunto A: "))
conjuntoA=set()
for i in range(cantidadA):
    elementoA=int(input(f"ingrese elemento  N°{i+1} : "))  
    conjuntoA.add(elementoA)
cantidadB=int(input("Ingrese la cantidad de elemento que tendrá el conjunto B: "))
conjuntoB=set()
for i in range(cantidadB):
    elementoB=int(input(f"ingrese elemento  N°{i+1} : "))  
    conjuntoB.add(elementoB)
def diferenciaConjuntos(a,b):
    return a.difference(b)
print("la diferencia de los conjuntos es", diferenciaConjuntos(conjuntoA,conjuntoB))