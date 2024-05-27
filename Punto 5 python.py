# le solicitamos el número de consumos y calcular el total de consumos al usuario
N = int(input("Porfavor, ingrese el número de consumos: "))
totalconsumos = sum(float(input("Porfavor, ingrese el monto del consumo {}: ".format(i + 1))) for i in range(N))

# ahora calculamos el descuento y el pago total con descuento
descuento = 0.10 if totalconsumos > 300000 else (0.05 if totalconsumos > 100000 else 0)
pagocondescuento = totalconsumos * (1 - descuento)

# mostrar los resultados con print
print("Total sin descuento:", totalconsumos)
print("Descuento aplicado:", descuento * 100, "%")
print("Total con descuento:", pagocondescuento)
