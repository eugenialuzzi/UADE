#Para un número entero N menor de 100 recibido como parámetro, escribir un programa
#que utilice una función para devolver la suma de los cuadrados de aquellos números
#entre 1 y N que están separados entre si por cuatro unidades. (12 + 52 + 92 + 132 + …)

def ValidarNumero():
    """Analiza si el numero ingresado esta en el rango entre 1 y 100, no recibe 
    parametros. Devuelve un numero"""
    
    numero = int(input("Ingrese un numero entre 1 y 100: "))
    while (numero < 1) or (numero > 100):
        print("El numero ingresado no está en el rango del 1 al 100")
        numero = int(input("Ingrese un numero entre 1 y 100: "))
    return numero

def NumerosAlCuadrado(num):
    """Dado un número entre 1 y n lo suma y eleva al cuadrado separado por 4 unidades, 
    recibe un numero por parametros. Devuelve la suma de los cuadrados de aquellos números"""
        
    for i in range(1,num,4):
        num = i**2
        print(num, end=",")
    return num
        
def main():
    n = ValidarNumero()
    cuadrados = NumerosAlCuadrado(n)

#Programa principal
main()
