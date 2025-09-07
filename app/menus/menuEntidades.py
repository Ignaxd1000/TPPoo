from modelos.entidades import empresaSoftware, laboratorio, startup


def menuEntidades(dictEntidades):
    while True:
        print("\n--- Menú de Manejo de Entidades ---")
        print("1. Agregar Entidad")
        print("2. Modificar Entidad")
        print("3. Eliminar Entidad")
        print("4. Volver al Menú Principal")
        opcion = input("Opción: ")
        if opcion == '1':
            print("Ingrese el numero correspondiente al tipo de entidad que desea agregar:")
            print("1. Empresa de Software")
            print("2. Laboratorio")
            print("3. Startup")
            tipo = input("Tipo de Entidad: ")
            if tipo == '1':
                id = input("ID: ")
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                dotacion = int(input("Dotación: "))
                entidad = empresaSoftware(areaM2, id, nombre, dotacion)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            elif tipo == '2':
                id = input("ID: ")
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                dotacion = int(input("Dotación: "))
                entidad = laboratorio(areaM2, id, nombre, dotacion)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            elif tipo == '3':
                id = input("ID: ")
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                dotacion = int(input("Dotación: "))
                entidad = startup(areaM2, id, nombre, dotacion)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            else:
                print("Tipo de entidad inválido.")
        elif opcion == '2':
            print("Ingrese el ID de la entidad que desea modificar:")
            id = input("ID: ")
            if id in dictEntidades:
                entidad = dictEntidades[id]
                print(f"Modificando entidad: {entidad.nombre}")
                nombre = input(f"Nuevo Nombre (actual: {entidad.nombre}): ") or entidad.nombre
                areaM2 = input(f"Nueva Área en m² (actual: {entidad.areaM2}): ")
                areaM2 = float(areaM2) if areaM2 else entidad.areaM2
                dotacion = input(f"Nueva Dotación (actual: {entidad.dotacion}): ")
                dotacion = int(dotacion) if dotacion else entidad.dotacion
                entidad.nombre = nombre
                entidad.areaM2 = areaM2
                entidad.dotacion = dotacion
                print(f"Entidad {nombre} modificada exitosamente.")
            else:
                print("Entidad no encontrada.")
        elif opcion == '3':
            print("Ingrese el ID de la entidad que desea eliminar:")
            id = input("ID: ")
            if id in dictEntidades:
                del dictEntidades[id]
                print(f"Entidad con ID {id} eliminada exitosamente.")
            else:
                print("Entidad no encontrada y/o id invalido.")
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")