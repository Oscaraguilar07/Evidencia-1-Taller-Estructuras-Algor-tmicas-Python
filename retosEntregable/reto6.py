from random import randint
a=randint(1,4)

cont=0 #definir variable numerica e inicializar antes del ciclo

total=0

for i in range(0,5,1):
    #qui instrucciones que se deasea repetir
    price=int(input("ingrese el precio del producto:"))
    cantidad=int(input("ingrese la cantidad del producto:"))
    cont=cont+1 #iniciar el contador dentro del ciclo
    subtotal=price*cantidad
    total=total+subtotal

compra = total

if compra >= 50000:
  if a==1:
   print("Felicidades, sacaste bolita roja. Tienes un descuento del 10%")
   compra = (compra / 100) * 10
   print()
   print("Tu descuento es de: ", compra)
    
  if a==2:
    print("Felicidades, sacaste bolita AZUL. Tienes un descuento del 30%")
    compra = (compra / 100) * 30
    print()
    print("Tu descuento es de: ", compra)
    
  if a==3:
    print("Felicidades, sacaste bolita AMARILLA. Tienes un descuento del 50%")
    compra = (compra / 100) * 50
    print()
    print("Tu descuento es de: ", compra)
    
  if a==4:
    print("Felicidades, sacaste bolita BLANCA. Te llevas la compra gratis!")
    compra = compra - compra
    print()
    print("Osea, tienes que pagar: ", compra)

    print("su total a pagar es",total)

    pago=int(input("digite la cantidad con la que desea pagar:"))
    cambio=pago-total
    print("su cambio es:",cambio)

else:
  print()
  print("******¡Gracias por comprar con nosotros!*******")