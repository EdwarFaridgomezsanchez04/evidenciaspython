def dete(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

numero_ingresado = int(input("Por favor, ingrese un número: "))

dete(numero_ingresado)
