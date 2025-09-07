def definirDotacion(entidad):
    while True:
        dotacion = input(f"Ingrese la dotaciòn para {entidad.nombre}: ")
        try:
            dotacion = int(dotacion)  # Trato de convertir a entero
            if dotacion < 0:
                print("El valor no puede ser negativo")
            elif dotacion / entidad.areaM2 < 5:
                print("Dotaciòn muy baja para el área de la entidad")
            else:
                break  # Salir del bucle si la dotación es válida
        except ValueError:
            print("La dotaciòn debe ser un número entero positivo")  # Mensaje de error si no se puede convertir
    return dotacion


    