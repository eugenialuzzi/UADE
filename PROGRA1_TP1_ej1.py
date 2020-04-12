#Desarrollar una función que reciba tres números positivos y devuelva el mayor de los
#tres, sólo si éste es único (mayor estricto). En caso de no existir el mayor estricto
#devolver -1. No utilizar operadores lógicos (and, or, not). Desarrollar también un
#programa para ingresar los tres valores, invocar a la función y mostrar el máximo
#hallado, o un mensaje informativo si éste no existe.

def MayorEstricto(n1,n2,n3):
    """Analiza tres numeros recibidos por parámetros y devuelve el mayor estricto
       caso contrario -1. Parámetros:
       n1
       n2
       n3"""
    
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
