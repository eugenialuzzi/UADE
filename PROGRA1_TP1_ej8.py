#Escribir una función que reciba como parámetro número del 1 al 9 y devuelva el
#resultado de sumar n + nn + nnn + nnnn, donde n corresponde al número recibido.
#Por ejemplo, si se ingresa 3 debe devolver 3702 (3+33+333+3333).
#Escribir también un programa para verificar el comportamiento de la función. No se
#permite utilizar facilidades de Python no vistas en clase.


def ValidarNumero():
    """Valida si el numero ingresado esta entre 1 y 9 inclusive"""
    
    n = int(input("Ingrese un numero del 1 a 9: "))
    while (n < 1) or (n > 9):
        print("El numero ingresado no está en el rango del 1 al 9")
        n = int(input("Ingrese nuevamente un numero del 1 a 9: "))
    return n

def SumaSucesivas (n):
    """Dado el numero ingresado lo suma sucesivamente hasta 4 digitos,
    Recibe un numero y devuelve la suma sucesiva del mismo"""
    
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