def GastoDeViajes(viajes,tarifa):
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