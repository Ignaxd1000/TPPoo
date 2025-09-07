def menuBuscarEntidades(entidadesDict):
    while True:
        print("\n--- Buscar Entidades ---")
        print("1. Listar todas las entidades")
        print("2. Buscar por ID")
        print("3. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            for id, entidad in entidadesDict.items():
                print(f"ID: {id}, Nombre: {entidad.nombre}, Tipo: {type(entidad).__name__}")
        elif opcion == '2':
            id = input("Ingrese el ID de la entidad que desea buscar: ")
            if id in entidadesDict:
                entidad = entidadesDict[id]
                print(f"ID: {id}, Nombre: {entidad.nombre}, Tipo: {type(entidad).__name__}")
            else:
                print("Entidad no encontrada y/o id incorrecto.")
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")