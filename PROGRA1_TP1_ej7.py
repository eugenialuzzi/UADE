def ContarDigitos(n2):
    resto = n2//10
    cant= 1
    while resto !=0:
        resto = resto // 10
        cant = cant +1
    return cant

def ConcatenarNumeros(n1,n2):
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
