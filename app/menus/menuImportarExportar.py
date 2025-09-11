from persistencia.manejoDeArchivos import exportarDatos, importarDatos


def menuExportarImportar(entidadesDict):
    print("--- Menù de persistencia ---")
    print("\n Ingrese el numero correspondiente a la operacion que desea realizar:")
    print("1. Exportar Datos")
    print("2. Importar Datos")
    print("3. Volver al menu principal")
    opcion = input("Opción: ")
    if opcion == '1':
        exportarDatos(entidadesDict)
    elif opcion == '2':
        nuevasEntidades = importarDatos()
        entidadesDict.update(nuevasEntidades)
    elif opcion == '3':
        return
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
