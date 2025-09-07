def definirDotacion(entidad: entidadParque): # No tengo idea que es la dotaciòn, asì que voy a inventar algo
    while True:
        dotacion = input(f"Ingrese la dotaciòn para {entidad.nombre}: ") 
        try: 
            dotacion = int(dotacion) # Trato de convertir a entero, si falla tiro un error reloco
        except ValueError:
            raise ValueError("La dotaciòn debe ser un nùmero entero positivo")

        try:
            if dotacion < 0:
                raise ValueError
        except ValueError:
            raise ValueError("La dotaciòn debe ser un nùmero entero positivo")

            if dotacion/entidad.areaM2 < 5:
                raise print("La dotaciòn es baja para el area del espacio")
                return
            else:
                return dotacion

    