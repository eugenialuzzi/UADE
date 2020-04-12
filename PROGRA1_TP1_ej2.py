#Desarrollar una función que reciba tres números enteros positivos y verifique si
#corresponden a una fecha gregoriana válida (día, mes, año). Devolver True o False
#según la fecha sea correcta o no. Realizar también un programa para verificar el
#comportamiento de la función.


def IngresarPositivos():
    """ Valida si el numero es positivo o no. No recibe parametros, devuelve un
    numero positivo"""
    
    numero = int(input("Ingrese un numero positivo: "))
    while numero < 1:
        print("El numero no es positivo: ")
        numero = int(input("Ingrese un numero positivo: "))
    return numero

def esBisiesto(anio):
    """ Valida si el anio es biciesto o no. Recibe parametros el anio, devuelve
    True or False"""
    return anio % 4 == 0 or anio % 400 == 0 and anio % 100 != 0

def ValidarFecha (dia,mes,anio):
    """ Valida si una fecha es valida o no. Recibe parametros el dia, mes y anio,
    devuelve True or False"""
    
    fechaValida = True
    if dia < 1 and mes < 1 and anio <1:
        fechaValida = False
    if mes > 12:
        fechaValida = False
    if dia > 31:
        fechaValida = False
    if (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11)  and dia >30:
        fechaValida = False
    if mes == 2 and not esBisiesto(anio) and dia > 28:
        fechaValida = False
    return fechaValida

def main():
    dia = IngresarPositivos()
    mes = IngresarPositivos()
    anio = IngresarPositivos()
    
    esValida = ValidarFecha(dia,mes,anio)
    
    if esValida:
        print("La fecha ingresada es valida")
    else:
        print("La fecha ingresada no es valida")

#Programa principal
main()
