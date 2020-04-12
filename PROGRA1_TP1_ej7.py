#Desarrollar una función que reciba como parámetros dos números enteros y devuelva
#el número que resulte de concatenar ambos valores. Por ejemplo, si recibe 1234 y 567
#debe devolver 1234567. No se permite utilizar facilidades de Python no vistas en clase.


def ContarDigitos(n2):
    """Dado un numero la funcion comprueba la cantidad de ditos que tiene
    Recibe un numero y devuelve la cantidad de digitos"""
    
    resto = n2//10
    cant= 1
    while resto !=0:
        resto = resto // 10
        cant = cant +1
    return cant

def ConcatenarNumeros(n1,n2):
    """Al primer numero lo multiplica por la cantidad de digitos rebibidos por la
    funcion ContarDigitos y le suma el segundo numero, de esta manera lo concatena"""
    
    n = ContarDigitos(n2)
    numero = (n1 * (1*10**n))+ n2
    return numero

def main():
    numero1 = int(input("Ingrese un numero entero: "))
    numero2 = int(input("Ingrese un numero entero: "))
    concatenados = ConcatenarNumeros(numero1,numero2)
    print("El numero concatenado es: ",concatenados)
    
#Programa Principal
    
main()
