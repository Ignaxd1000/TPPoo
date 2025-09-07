from app.menus.menuEntidades import menuEntidades
# from app.menus.menuCalcularIngresos import menuCalcularIngresos
from app.menus.menuBuscarEntidades import menuBuscarEntidades
# from app.menus.menuExportarImportar import menuExportarImportar

def invocarMenu(entidadesDict):
    while True:
        print("--- Sistema de Gestión de Parque ---")

        print("\n Ingrese el numero correspondiente al submenu que desea acceder:")
        print("1. Manejo de Entidades")
        print("2. Calcular ingresos")
        print("3. Buscar Entidades")
        print("4. Exportar y/o Importar Datos")
        print("5. Salir del Programa")
        opcion = input("Opción: ")
        if opcion == '1':
            menuEntidades(entidadesDict)
        elif opcion == '2':
            menuCalcularIngresos(entidadesDict)
        elif opcion == '3':
            menuBuscarEntidades(entidadesDict)
        elif opcion == '4':
            menuExportarImportar(entidadesDict)
        elif opcion == '5':
            print("Saliendo del programa")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")