#Una persona desea llevar el control de los gastos realizados al viajar en el
#subterráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un
#esquema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita
#desarrollar una función que reciba como parámetro la cantidad de viajes realizados
#en un determinado mes y devuelva el total gastado en viajes. Realizar también un
#programa para verificar el comportamiento de la función

def GastoDeViajes(viajes,tarifa):
    """Dada una cantidad de viajes y una tarifa, si los viajes están entre 1 y 20, no tiene
    descuento, si están entre 21 y 30 tienen un 20% de descuento en la tarifa,
    si están entre 31 y 40 un 30% y superior a 40 un 40%. La funcion recibe:
    Viajes y tarifa; y devueve el monto mensual"""
    
    tarifa30 = tarifa-(tarifa*0.2)
    tarifa40 = tarifa-(tarifa*0.3)
    tarifamas = tarifa-(tarifa*0.4)
    if viajes <= 0:
        total=0
    elif viajes <= 20:
        total= viajes*tarifa
    elif viajes <=30:
        total = 20*tarifa + (viajes-20)*tarifa30
    elif viajes <=40:
        total = 20*tarifa + 10*tarifa30 + (viajes-30)*tarifa40
    elif viajes > 40:
        total = 20*tarifa + 10*tarifa30 + 30*tarifa40 + (viajes-40)*tarifamas
    return total

def main():
    viajes = int(input("Ingrese el total de viajes: "))
    tarifa = int(input("Ingrese la tarifa diaria de su viaje: "))
    importeViajes = GastoDeViajes(viajes,tarifa)
    print("El importe mensual que paga es: ",importeViajes)

main()