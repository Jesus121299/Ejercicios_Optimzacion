compra = int(input("Introduzca el total de su compra:   "))

if compra>=100:

    a = (compra * 20) / 100
    descuento = compra - a
    print("Total a pagar menos el descuento: " , descuento)
    print("El descuento fue de: " , a)
    
elif compra >= 50 and compra <= 99:
        
        b = (compra * 10 ) /100
        
        descuento = compra - b
        print("Total a pagar menos el descuento: " , descuento)
        print("El descuento fue de: " , b)
        
pass
