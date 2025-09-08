def menuCalcularIngresos(dictEntidades):
    while True:
        print("--- Cálculo de Ingresos ---")

        print("\nSeleccione la opción de cálculo de ingresos que desea realizar:")
        print("1. Calcular ingresos de una entidad específica")
        print("2. Calcular ingresos totales del parque")
        print("3. Volver al menú principal")
        opcion = input("Opción: ")

        if opcion == '1':
            id = input("Ingrese el ID de la entidad: ")
            if id in dictEntidades:
                entidad = dictEntidades[id]
                ingresos = entidad.calcularIngresosAnuales()
                print(f"Los ingresos de la entidad {entidad.nombre} son: {ingresos}")
            else:
                print("Entidad no encontrada.")
        elif opcion == '2':
            ingresos_totales = sum(entidad.calcularIngresosAnuales() for entidad in dictEntidades.values())
            print(f"Los ingresos totales del parque son: {ingresos_totales}")
        
        elif opcion == '3':
            print("Volviendo al menú principal.")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")
