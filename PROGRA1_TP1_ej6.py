def ImprimirCuadrado(n):
    for i in range(n):
        for j in range(n):
            print("*", end="")
        print()
def ImprimirTriangulo(num):
    for k in range(2,num+1):
        print("*"*k)
          
def main():
    numero = int(input("Ingrese a cantidad asterizcos que desea imprimir: "))
    rectangulo = ImprimirCuadrado(numero)
    print()
    triangulo = ImprimirTriangulo(numero)
#Programa Principal
main()