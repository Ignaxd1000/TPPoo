# Sistema de Gestión de Parque

Aplicación de consola para gestionar entidades de un parque tecnológico. Permite:
- Alta, modificación y baja de entidades (empresas de software, laboratorios, startups).
- Búsqueda de entidades (si el menú correspondiente está implementado).
- Exportación e importación de datos a/desde un archivo local.

Este README describe supuestos, cómo ejecutar el proyecto, y ejemplos de uso.



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



## Cómo ejecutar

Simplemente se debe correr el main.py, no son necesarios permisos de superusuario/administrador.

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
