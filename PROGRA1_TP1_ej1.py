def MayorEstricto(n1,n2,n3):
    mayor=0
    if n1 > mayor:
        mayor=n1
    if n2 > mayor:
        mayor=n2
    if n3 > mayor:
        mayor = n3
    if mayor == False:
        mayor = -1
 
    return mayor

def main():
    a = int(input("Ingrese un numero entero positivo: "))
    b = int(input("Ingrese un numero entero positivo: "))
    c = int(input("Ingrese un numero entero positivo: "))
    mayores = MayorEstricto(a,b,c)
    print(mayores)

#Programa Principal
    
main()
