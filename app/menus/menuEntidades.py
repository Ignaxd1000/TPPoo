from modelos.subclases.empresaSoftware import empresaSoftware
from modelos.subclases.laboratorio import laboratorio
from modelos.subclases.startup import startup
from excepciones.dotacion import definirDotacion
from excepciones.fondosInsuficientesException import fondosInsuficientesException

def menuEntidades(dictEntidades):
    while True:
        print("\n--- Menú de Manejo de Entidades ---")
        print("1. Agregar Entidad")
        print("2. Modificar Entidad")
        print("3. Asociar Entidades")
        print("4. Eliminar Entidad")
        print("5. Volver al Menú Principal")
        opcion = input("Opción: ")
        if opcion == '1':
            print("Ingrese el numero correspondiente al tipo de entidad que desea agregar:")
            print("1. Empresa de Software")
            print("2. Laboratorio")
            print("3. Startup")
            tipo = input("Tipo de Entidad: ")
            if tipo == '1':
                id = input("ID: ")
                if id in dictEntidades:
                    print("El ID ya ha sido ingresado, por favor ingrese un ID unico.")
                    continue
                if id.isalpha():
                    print("El ID no puede contener letras, por favor ingrese un ID valido.")
                    continue
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                numEmpleados = int(input("Número de Empleados: "))
                tecnologias = input("Tecnologías Utilizadas (separadas por comas): ").split(',')
                entidad = empresaSoftware(areaM2, id, nombre, numEmpleados, tecnologias)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            elif tipo == '2':
                id = input("ID: ")
                if id in dictEntidades:
                    print("El ID ya ha sido ingresado, por favor ingrese un ID unico.")
                    continue
                if id.isalpha():
                    print("El ID no puede contener letras, por favor ingrese un ID valido.")
                    continue
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                especialidad = input("Especialidad (biotecnología, física, química, etc.): ")
                numInvestigadores = int(input("Número de Investigadores: "))
                entidad = laboratorio(areaM2, id, nombre, especialidad, numInvestigadores)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            elif tipo == '3':
                id = input("ID: ")
                if id in dictEntidades:
                    print("El ID ya ha sido ingresado, por favor ingrese un ID unico.")
                    continue
                if id.isalpha():
                    print("El ID no puede contener letras, por favor ingrese un ID valido.")
                    continue
                nombre = input("Nombre: ")
                areaM2 = float(input("Área en m²: "))
                etapaDesarrollo = input("Etapa de Desarrollo: ")
                numFundadores = int(input("Número de Fundadores: "))
                entidad = startup(areaM2, id, nombre, numFundadores, etapaDesarrollo)
                dictEntidades[id] = entidad
                print(f"Entidad {nombre} agregada exitosamente.")
            else:
                print("Tipo de entidad inválido.")
        elif opcion == '2':
            print("Ingrese el ID de la entidad que desea modificar:")
            id = input("ID: ")
            if id.isalpha():
                    print("El ID no puede contener letras, por favor ingrese un ID valido.")
                    continue
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
            for id, entidad in dictEntidades.items():
                print(f"ID: {id}, Nombre: {entidad.nombre}, Tipo: {type(entidad).__name__}")
            print("Ingrese el ID de la entidad principal(Startup o Empresa de Software):")
            id1 = input("ID Entidad Principal: ")
            print("Ingrese el ID del laboratorio a asociar/colaborar:")
            id2 = input("ID Entidad a Asociar: ")
            if id1 in dictEntidades and id2 in dictEntidades:
                entidad1 = dictEntidades[id1]
                entidad2 = dictEntidades[id2]
                if isinstance(entidad1, startup) and isinstance(entidad2, laboratorio):
                    try:
                        capital = int(input(f"Ingrese el capital que la startup {entidad1.nombre} aportará para asociarse con el laboratorio {entidad2.nombre}: "))
                    except ValueError:
                        print("El capital debe ser un número entero.")
                        continue
                    try:
                        entidad1.asociarse(entidad2, capital)
                        print(f"Startup {entidad1.nombre} asociada exitosamente con el laboratorio {entidad2.nombre}.")
                    except fondosInsuficientesException as e:
                        print(e)
                elif isinstance(entidad1, empresaSoftware) and isinstance(entidad2, laboratorio):
                    entidad1.agregarColaboracion(entidad2)
                    print(f"Empresa de Software {entidad1.nombre} colaborando exitosamente con el laboratorio {entidad2.nombre}.")
                else:
                    print("Asociación/Colaboración inválida. Asegúrese de que la entidad principal sea una Startup o Empresa de Software y la otra un Laboratorio.")
        elif opcion == '4':
            print("Ingrese el ID de la entidad que desea eliminar:")
            id = input("ID: ")
            if id.isalpha():
                    print("El ID no puede contener letras, por favor ingrese un ID valido.")
                    continue
            if id in dictEntidades:
                del dictEntidades[id]
                print(f"Entidad con ID {id} eliminada exitosamente.")
            else:
                print("Entidad no encontrada y/o id invalido.")
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")