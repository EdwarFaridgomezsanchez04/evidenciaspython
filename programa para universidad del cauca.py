
#en este programa se escriben los nombres de los estudiantes mediante un ciclo hasta que el 
#usuario escriba 'salir' aquello a esto nos dice si aprobo o reprobo



def calcularnotadefinitiva(primerparcial, segundoparcial, final):
    return primerparcial * 0.35 + segundoparcial * 0.35 + final * 0.30

def main():
    estudiantes = []

    # Captura de datos de los estudiantes
    while True:
        nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
        if nombre.lower() == 'salir':
            break
        
        codigo = input("Ingrese el código del estudiante: ")
        
        primerparcial = float(input("Ingrese la nota del primer parcial: "))
        if primerparcial < 0.0 or primerparcial > 5.0:
            print("Nota inválida. Debe estar entre 0.0 y 5.0.")
            continue
        
        segundoparcial = float(input("Ingrese la nota del segundo parcial: "))
        if segundoparcial < 0.0 or segundoparcial > 5.0:
            print("Nota inválida. Debe estar entre 0.0 y 5.0.")
            continue
        
        final = float(input("Ingrese la nota del examen final: "))
        if final < 0.0 or final > 5.0:
            print("Nota inválida. Debe estar entre 0.0 y 5.0.")
            continue
        
        notadefinitiva = calcularnotadefinitiva(primerparcial, segundoparcial, final)
        
        estudiante = {
            "nombre": nombre,
            "codigo": codigo,
            "notadefinitiva": notadefinitiva
        }
        
        estudiantes.append(estudiante)
    
    # Presentación de resultados
    for estudiante in estudiantes:
        print(f"Estudiante: {estudiante['nombre']}, Código: {estudiante['codigo']}")
        if estudiante["nota_definitiva"] >= 3.5:
            print( "Aprobó" )
                
        else:
            print("Reprobó")

if __name__ == "__main__":
    main()