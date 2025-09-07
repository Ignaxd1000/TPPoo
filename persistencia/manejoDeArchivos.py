from excepciones.dotacion import definirDotacion 
from modelos.entidadParque import entidadParque 

def exportarDatos(dictEntidades, ruta):
    with open(ruta, 'w') as archivo:
        for id, entidad in dictEntidades.items():
            linea = f"{entidad.id},{entidad.nombre},{entidad.areaM2},{definirDotacion(entidad.dotacion)}\n"
            archivo.write(linea)

def importarDatos(ruta):
    dictEntidades = {}
    try:
        with open(ruta, 'r') as archivo:
            for linea in archivo:
                id, nombre, areaM2, dotacion = linea.strip().split(',')
                entidad = entidadParque(id, nombre, float(areaM2), int(dotacion))
                dictEntidades[id] = entidad
    except FileNotFoundError:
        print(f"El archivo en la ruta {ruta} no fue encontrado.")
    except Exception as e:
        print(f"Ocurrió un error al importar los datos: {e}")
    return dictEntidades