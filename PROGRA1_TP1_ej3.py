def ValidarNumero():
    numero = int(input("Ingrese un numero entre 1 y 100: "))
    while numero > 100:
        numero = int(input("Ingrese un numero entre 1 y 100: "))
        print("El numero debe ser mayor que 1 y menor que 100")
    return numero

def NumerosAlCuadrado(num):
    for i in range(1,num,4):
        num = i**2
        print(num, end=",")
    return num
        
def main():
    n = ValidarNumero()
    cuadrados = NumerosAlCuadrado(n)

#Programa principal
main()
