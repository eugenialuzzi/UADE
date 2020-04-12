def ValidarNumero():
    n = int(input("Ingrese un numero del 1 a 9: "))
    while (n < 1) or (n > 9):
        print("El numero ingresado no está en el rango del 1 al 9")
        n = int(input("Ingrese nuevamente un numero del 1 a 9: "))
    return n

def SumaSucesivas (n): 
    numero = 0
    suma = 0
    for i in range (0,4):
        numero = n*(10**i) + numero
        suma = suma + numero
    return suma

def main():
    numero = ValidarNumero()
    sumas = SumaSucesivas(numero)
    print("Las sumas sucesivas del numero de n hasta nnnn, es: ",sumas)
#Programa Principal
main()