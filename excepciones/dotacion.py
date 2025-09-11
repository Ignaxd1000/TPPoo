class capacidadExcedidaException(Exception):
    def __init__(self, message="La capacidad ha sido excedida. La dotaciòn debe ser mayor para el area disponible."):
        super().__init__(message)

def definirDotacion(entidad):
    while True:
        dotacion = input(f"Ingrese la dotación para {entidad.nombre}: ")
        try:
            dotacion = int(dotacion)
            if dotacion < 0:
                print("El valor no puede ser negativo")
                continue
            if entidad.areaM2 / dotacion < 2.5:
                raise capacidadExcedidaException("La dotación excede la capacidad permitida para el área asignada.")
            break  # Sale del while solo si todo es válido
        except ValueError:
            print("Por favor ingrese un número entero válido.")
        except capacidadExcedidaException as e:
            print(e)
    return dotacion


    