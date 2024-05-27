
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1
print(f"Los números ingresados son {num1} y {num2}, organizados son {menor}, {mayor}")
