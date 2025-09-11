from __future__ import annotations

import json  # Este archivo es un lio, pero bueno como dijo alguien: "Si funciona, no lo toques" y "No existen mentes brillantes sin un gran desorden"
import importlib
from pathlib import Path
from typing import Any, Dict, Iterable, List


def _json_safe(value: Any) -> Any:
    """
    Convierte un valor a algo serializable por JSON.
    - dict => dict recursivo
    - list/tuple/set => list
    - primitivos => tal cual
    - otros => repr() como último recurso
    """
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, dict):
        return {k: _json_safe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_safe(v) for v in value]
    return repr(value)


def exportarDatos(dictEntidades: Dict[Any, Any], ruta: str | Path = "Datos.txt") -> None:
    """
    Exporta entidades incluyendo TODOS sus atributos específicos.
    Se guarda:
    [
      {
        "__module__": "<modulo>",
        "__class__": "<clase>",
        "attrs": { ... __dict__ completo ... }
      },
      ...
    ]
    """
    ruta = Path(ruta)
    # Armamos estructura JSON segura
    payload: List[Dict[str, Any]] = []
    for _id, entidad in dictEntidades.items():
        attrs = getattr(entidad, "__dict__", {}).copy()
        safe_attrs = _json_safe(attrs)
        payload.append(
            {
                "__module__": entidad.__class__.__module__,
                "__class__": entidad.__class__.__name__,
                "attrs": safe_attrs,
            }
        )

    # Escribimos JSON (por compatibilidad, puede seguir llamándose Datos.txt)
    ruta.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def importarDatos(ruta: str | Path = "Datos.txt") -> Dict[Any, Any]:
    """
    Importa entidades rehidratándolas según el módulo y clase guardados,
    restaurando todos los atributos específicos sin invocar __init__.
    Si el archivo no es JSON válido, intenta un fallback CSV (legacy).
    """
    ruta = Path(ruta)
    dictEntidades: Dict[Any, Any] = {}

    try:
        raw = ruta.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"El archivo en la ruta {ruta} no fue encontrado.")
        return dictEntidades
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return dictEntidades

    # Intento JSON (nuevo formato)
    try:
        data = json.loads(raw)
        if not isinstance(data, list):
            raise ValueError("El JSON no contiene una lista.")
        for item in data:
            if not isinstance(item, dict):
                continue
            mod_name = item.get("__module__")
            cls_name = item.get("__class__")
            attrs = item.get("attrs", {})

            if not mod_name or not cls_name or not isinstance(attrs, dict):
                continue

            # Import dinámico del módulo y clase
            module = importlib.import_module(mod_name)
            cls = getattr(module, cls_name)

            # Crear instancia sin llamar __init__ y rehidratar __dict__
            obj = cls.__new__(cls)
            obj.__dict__.update(attrs)

            # Usamos el 'id' del objeto como clave si existe; si no, usamos la clave original si está
            key = attrs.get("id")
            if key is None:
                # Como último recurso, generamos una clave incremental
                key = str(len(dictEntidades) + 1)

            dictEntidades[key] = obj
        print("Datos importados exitosamente.")
        return dictEntidades

    except Exception:
        # Fallback: intentar formato legacy CSV "id,nombre,areaM2,dotacion"
        try:
            for line in raw.splitlines():
                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 4:
                    continue
                id_val, nombre, areaM2, dotacion = parts
                # Construimos un objeto simple si no podemos importar la clase base
                # Esto solo preserva campos legacy; se recomienda re-exportar al nuevo formato.
                Generic = type("EntidadLegacy", (), {})
                obj = Generic()
                obj.id = id_val
                obj.nombre = nombre
                try:
                    obj.areaM2 = float(areaM2)
                except Exception:
                    obj.areaM2 = areaM2
                try:
                    obj.dotacion = int(dotacion)
                except Exception:
                    obj.dotacion = dotacion
                dictEntidades[id_val] = obj
        except Exception as e2:
            print(f"Ocurrió un error al importar los datos legacy: {e2}")

        return dictEntidades