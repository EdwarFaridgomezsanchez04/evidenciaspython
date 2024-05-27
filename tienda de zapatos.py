#Se requiere digitar los valores de las compras realizadas por los clientes de una tienda de
#zapatos, no se saben cuántas compras se realizaron y se deben acumular los valores
#ingresados, para así obtener el total de compra realizada. Una vez obtenido el total de
#compra realizado se debe hallar el 25% del valor, que es lo que representará las ganancias.

from os import name


def main ():

    print ("Bienviendio al programa de la tienda de zapatos ") 

comprastotales = 0



while True:       
 try:
        compra = input("Ingrese el valor de la compra del zapato (o escriba 'fin' para terminar): ")

        if compra.lower() == 'fin':

            break

        else:compra = float(compra)
        comprastotales += compra

 except : ValueError
print("Ingrese un numero valido  o 'fin' para terminar ")
   
print (f"El total de las compra final realizada es: {comprastotales: .2f}")

ganancias = comprastotales *0.25

print (f"las ganancias (25% del total) son : {ganancias: .2f}")

if name == "main" : 
    main ()
        
        

