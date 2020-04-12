#Un comercio de electrodomésticos necesita para su línea de cajas un programa que le
#indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan dos
#números enteros, correspondientes al total de la compra y al dinero recibido.
#Informar cuántos billetes de cada denominación deben ser entregados al cliente como
#vuelto, de tal forma que se minimice la cantidad de billetes. Considerar que existen
#billetes de $500, $100, $50, $20, $10, $5 y $1. Emitir un mensaje de error si el
#dinero recibido fuera insuficiente. Ejemplo: Si la compra es de $317 y se abona con
#$500, el vuelto debe contener 1 billete de $100, 1 billete de $50, 1 billete de $20,
#1 billete de $10 y 3 billetes de $1.

def ComprobarPago(compra,pago):
    """Valida que el pago es mayor al importe de la compra
    Recibe=$compra y $ a pagar, devuelve el monto"""
    monto= pago-compra
    if monto < 0:
        print("No se puede emitir vuelto, el monto es insuficiente")
    return monto

def VueltoDeCaja(monto):
    """Dado un importe a pagar por caja, comprueba la cantidad de billedes de:
    500, 100, 50, 20, 10, 5 y 1 que la cajera debe abonar"""
    if monto > 0:
        billetes500= monto//500
        resto500 = monto%500
        billetes100 = resto500//100
        resto100 = resto500%100
        billetes50 = resto100//50
        resto50 = resto100%50
        billetes20 = resto50//20
        resto20 = resto50%20
        billetes10 = resto20//10
        resto10 = resto20%20
        billetes5 = resto10//5
        resto5 = resto10%5
        billetes1 = resto5//1
        print("Vuelto de 500:",billetes500,"Vuelto de 100:",billetes100,"Vuelto de 50:",billetes50,"Vuelto de 20:",billetes20,"Vuelto de 10:",billetes10,"Vuelto de 5:",billetes5,"Vuelto de 1:",billetes1)
    return billetes500


def main():
    venta = int(input("Ingrese el importe de la venta: "))
    pago = int(input("Ingese el pago que realizó el cliente: "))
    importe = ComprobarPago(venta,pago)
    vuelto = VueltoDeCaja(importe)
    print(vuelto)
    
#Programa Principal
main()
