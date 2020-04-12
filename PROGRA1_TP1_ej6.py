#Escribir dos funciones para imprimir por pantalla cada uno de los siguientes patrones
#de asteriscos.

def ImprimirCuadrado(n):
    """Imprime un cuadrado de asteriscos. Recibe la cantidad de filas y columnas nxn,
    e imprime el cuadrado de asteriscos"""
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
def ImprimirTriangulo(num):
    """Imprime un triangulo de asteriscos, comenzando de 2 asteriszoa. Recibe la
    cantidad de filas y columnas nxn, e imprime el cuadrado de asteriscos"""
    
    for k in range(2,num+1):
        print("*"*k)
          
def main():
    numero = int(input("Ingrese a cantidad asterizcos que desea imprimir: "))
    rectangulo = ImprimirCuadrado(numero)
    print()
    triangulo = ImprimirTriangulo(numero)
#Programa Principal
main()