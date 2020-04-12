def VueltoDeCaja(compra,pago):
    monto=pago-compra
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
    return monto

def main():
    venta = int(input("Ingrese el importe de la venta: "))
    pago = int(input("Ingese el pago que realizó el cliente: "))
    importe = VueltoDeCaja(venta,pago)
    print(importe)
    
#Programa Principal
main()
