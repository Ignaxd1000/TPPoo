from app.menus.menuEntidades import menuEntidades
from app.menus.menuCalcularIngresos import menuCalcularIngresos
from app.menus.menuBuscarEntidades import menuBuscarEntidades
from app.menus.menuImportarExportar import menuExportarImportar
from app.menus.menuReportes import menuReportes

def invocarMenu(entidadesDict):
    while True:
        print("--- Sistema de Gestión de Parque ---")

        print("\n Ingrese el numero correspondiente a la accion que desea realizar:")
        print("1. Manejo de Entidades")
        print("2. Calcular ingresos")
        print("3. Buscar Entidades")
        print("4. Exportar y/o Importar Datos")
        print("5. Generar Reportes")
        print("6. Salir del Programa")
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
            menuReportes(entidadesDict)
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            return
        else:
            print("Opción no válida. Intente de nuevo.")