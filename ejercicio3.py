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
cantidadC=int(input("Ingrese la cantidad de elemento que tendrá el conjunto C: "))
conjuntoC=set()
for i in range(cantidadC):
    elementoC=int(input(f"ingrese elemento  N°{i+1} : "))  
    conjuntoC.add(elementoC)
def diferenciaSimetrica(A,B,C):
    return ((A.difference(C.union(B))).union(B.difference(A.union(C)))).union(C.difference(A.union(B)))
print("La diferencia simetrica de los tres conjuntos es: ",diferenciaSimetrica(conjuntoA,conjuntoB,conjuntoC))