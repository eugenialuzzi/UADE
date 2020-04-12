#Utilizar la técnica de listas por comprensión para construir una lista con el doble
#del  valor de los numeros impares de un rango de números entre M y N inclusive.
#El valor de M y N se ingresa por teclado asegurando que exista un rango entre ellos.
#Mostrar la lista por pantalla.

def CargarLista(m,n):
    """La funcion crea una lista por comprension de numeros impares.
    Recibe por parametros:
    m : es el rango inicial de la lista;
    n : es el rango fina de la lista
    retorna a la lista de numeros impares"""
  
    lista = [x*2 for x in range(m,n+1) if x%2 != 0]
    return lista

def main():
    m = int(input("Ingrese el rango inicial de su lista: "))
    n = int(input("Ingrese el rango final de su lista: "))
    print()
    lista= CargarLista(m,n)
    print(lista)

#Programa Principal
main()
