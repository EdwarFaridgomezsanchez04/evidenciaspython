
print(f"Estoy pensando en un número entre 1 y 5.")
numero_secreto = 3  

while True:
    print("Intenta adivinar el numero.")
    cercania = int(input())

    if cercania < numero_secreto:
        print("El numero es mas alto.")
    elif cercania > numero_secreto:
        print("El numero es mas bajo.")
    else:
        print(f"Felicitaciones el {cercania} es correcto")
        break