# Sistema de Gestión de Parque

Aplicación de consola para gestionar entidades de un parque tecnológico. Permite:
- Alta, modificación y baja de entidades (empresas de software, laboratorios, startups).
- Búsqueda de entidades (si el menú correspondiente está implementado).
- Exportación e importación de datos a/desde un archivo local.
- (Nuevo) Generación de reportes agregados (si se incorpora el módulo de reportes sugerido más abajo).

Este README describe supuestos, cómo ejecutar el proyecto, ejemplos de uso y cómo añadir reportes.


## Requisitos y supuestos

- Python 3.10 o superior.
- Sin dependencias externas (solo librería estándar de Python).
- Se recomienda ejecutar el proyecto desde la raíz del repositorio para que los imports funcionen correctamente.
- La dotación de personal se calcula automáticamente en el constructor de la clase base según reglas en `excepciones/dotacion.py`.

Supuestos actuales de persistencia:
- El archivo de datos por defecto es `Datos.txt` en la raíz del proyecto.
- El formato actual de exportación es CSV con columnas: `id,nombre,areaM2,dotacion`.
- Actualmente solo se persisten los atributos comunes definidos en la clase base `entidadParque` (no se guardan atributos específicos de cada subclase).
- La importación reconstruye entidades con datos base; los atributos específicos de subclase no se restauran.


## Estructura del proyecto (resumen)

- `app/menus/`
  - `menuPrincipal.py`: Menú principal de la aplicación (función `invocarMenu`).
  - `menuEntidades.py`: ABM de entidades (alta, modificación, baja).
  - Pueden existir otros menús como `menuBuscarEntidades.py`, `menuImportarExportar.py` si fueron añadidos.
- `modelos/`
  - `entidadParque.py`: Clase base abstracta para entidades del parque.
  - `subclases/`
    - `empresaSoftware.py`
    - `laboratorio.py`
    - `startup.py`
- `excepciones/`
  - `dotacion.py`: Lógica para definir/calcular dotación de personal.
- `persistencia/`
  - `manejoDeArchivos.py`: Exportación/Importación (CSV actual).
- (Propuesto) `reportes/`
  - `generadorReportes.py`: Cálculo y exportación de métricas agregadas (ver sección Reportes).


## Cómo ejecutar

Simplemente se debe correr el `main.py`, no son necesarios permisos de superusuario/administrador.

Notas:
- Ejecutá siempre desde la raíz del proyecto para que los imports absolutos funcionen.
- En el menú principal verás opciones como:
  1) Manejo de Entidades
  2) Calcular ingresos
  3) Buscar Entidades
  4) Exportar y/o Importar Datos
  5) Salir

Si alguna opción aún no está implementada, el programa lo indicará o puede no funcionar correctamente.


## Uso del Menú de Entidades (ABM)

En “Manejo de Entidades”:
- Alta: elegí tipo de entidad y completá los campos solicitados.
  - Empresa de Software: `ID`, `Nombre`, `Área (m²)`, `Número de empleados`, `Tecnologías` (separadas por coma).
  - Laboratorio: `ID`, `Nombre`, `Área (m²)`, `Especialidad`, `Número de investigadores`.
  - Startup: `ID`, `Nombre`, `Área (m²)`, `Etapa de desarrollo`, `Número de fundadores`.
- Modificación: ingresá el `ID` y ajustá los valores. Si dejás vacío un campo, se mantiene el actual.
- Eliminación: ingresá el `ID` de la entidad a borrar.

La dotación (`dotacion`) se calcula automáticamente a partir de las reglas definidas en `excepciones/dotacion.py` cuando se crea la entidad.


## Persistencia (Exportar/Importar)

Menú:
- “Exportar y/o Importar Datos” guarda o carga entidades de `Datos.txt`.

Limitaciones actuales:
- No se guardan atributos específicos de subclase.
- No se almacena el tipo concreto, por lo que al reconstruir podrían crearse instancias genéricas si se cambia la lógica.


## Ejemplos rápidos

Alta por menú (flujo típico):
1. “1. Manejo de Entidades”
2. “1. Agregar Entidad”
3. “1. Empresa de Software”
4. Completar:
   - ID: `E001`
   - Nombre: `Soft SA`
   - Área en m²: `250`
   - Número de Empleados: `12`
   - Tecnologías Utilizadas: `Python,SQL,FastAPI`

Exportar por menú:
- “4. Exportar y/o Importar Datos” y elegí “Exportar”.


## Reportes (Nuevo / Propuesto)

Se propone añadir un módulo de reportes para obtener métricas agregadas del parque:

Métricas generales:
- Total de entidades
- Área total (m²)
- Dotación total
- Área promedio
- Dotación promedio
- Dotación por m²

Por tipo de entidad:
- Cantidad
- Área total
- Dotación total
- Área promedio
- Dotación promedio
- Dotación por m²

Rankings:
- Top 5 por área
- Top 5 por dotación

Formatos de salida sugeridos:
- Texto plano (consola / archivo .txt)
- CSV (tabla de entidades + métricas)
- JSON (estructura completa para integraciones)
- Markdown (reporte legible)

### Estructura propuesta del módulo
```
reportes/
  generadorReportes.py
```

### Ejemplo de uso (una vez creado el módulo)
```python
from reportes.generadorReportes import (
    generar_resumen_texto,
    exportar_reporte_texto,
    exportar_reporte_json,
    exportar_reporte_csv,
    exportar_markdown
)

# dictEntidades es el diccionario principal ya cargado en memoria
print(generar_resumen_texto(dictEntidades))
exportar_reporte_texto(dictEntidades, "reporte.txt")
exportar_reporte_json(dictEntidades, "reporte.json")
exportar_reporte_csv(dictEntidades, "reporte.csv")
exportar_markdown(dictEntidades, "reporte.md")
```

### Integración de menú (ejemplo)
```python
def menuReportes(entidades):
    while True:
        print("\n=== Menú Reportes ===")
        print("1) Ver resumen en consola")
        print("2) Exportar TXT")
        print("3) Exportar JSON")
        print("4) Exportar CSV")
        print("5) Exportar Markdown")
        print("6) Volver")
        op = input("Opción: ").strip()
        if op == "1":
            from reportes.generadorReportes import generar_resumen_texto
            print(generar_resumen_texto(entidades))
        elif op == "2":
            from reportes.generadorReportes import exportar_reporte_texto
            exportar_reporte_texto(entidades)
            print("Reporte TXT generado.")
        elif op == "3":
            from reportes.generadorReportes import exportar_reporte_json
            exportar_reporte_json(entidades)
            print("Reporte JSON generado.")
        elif op == "4":
            from reportes.generadorReportes import exportar_reporte_csv
            exportar_reporte_csv(entidades)
            print("Reporte CSV generado.")
        elif op == "5":
            from reportes.generadorReportes import exportar_markdown
            exportar_markdown(entidades)
            print("Reporte Markdown generado.")
        elif op == "6":
            break
        else:
            print("Opción inválida")
```

### Posibles mejoras futuras
- Serializar también tipo y atributos específicos (migrar a JSON).
- Añadir filtros por rango de área o dotación.
- Gráficos (matplotlib / seaborn) si se permiten dependencias externas.
- Exportación a PDF (ReportLab o HTML+wkhtmltopdf).
- Cache de métricas si el volumen crece.


## Roadmap de mejoras (ideas)
- Persistir tipo de entidad y atributos específicos.
- Validaciones más robustas de entrada de usuario.
- Tests unitarios para lógica de cálculo de dotación y reportes.
- Refactor para usar una capa de repositorio y facilitar cambios de persistencia (CSV -> JSON/SQLite).


## Licencia
(Si aplica, agregar aquí el tipo de licencia del proyecto.)

---
Si necesitás que también agregue el archivo del módulo de reportes al repositorio, pedímelo y preparo el cambio.