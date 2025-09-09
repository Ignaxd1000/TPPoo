from collections import defaultdict
import json
from datetime import datetime
from typing import Dict

# Importá las clases si querés usar isinstance
try:
    from modelos.subclases.empresaSoftware import empresaSoftware
    from modelos.subclases.laboratorio import laboratorio
    from modelos.subclases.startup import startup
except ImportError:
    # En caso de que se ejecute en un entorno parcial
    empresaSoftware = laboratorio = startup = tuple()

def _clasificar_tipo(entidad):
    """
    Devuelve el tipo lógico de la entidad como string.
    No rompe si no se pueden importar las clases.
    """
    cls_name = entidad.__class__.__name__
    # Normalizar nombres si hace falta
    return cls_name

def calcular_metricas_basicas(dictEntidades: Dict[str, object]) -> dict:
    total_entidades = len(dictEntidades)
    if total_entidades == 0:
        return {
            "total_entidades": 0,
            "total_area": 0.0,
            "total_dotacion": 0,
            "area_promedio": 0.0,
            "dotacion_promedio": 0.0,
            "dotacion_por_m2": 0.0,
            "por_tipo": {},
            "ranking_area": [],
            "ranking_dotacion": []
        }

    total_area = 0.0
    total_dotacion = 0
    por_tipo = defaultdict(lambda: {"cantidad": 0, "area_total": 0.0, "dotacion_total": 0})

    ranking_area_base = []
    ranking_dotacion_base = []

    for entidad in dictEntidades.values():
        area = getattr(entidad, "areaM2", 0.0)
        dotacion = getattr(entidad, "dotacion", 0)
        total_area += area
        total_dotacion += dotacion

        tipo = _clasificar_tipo(entidad)
        por_tipo[tipo]["cantidad"] += 1
        por_tipo[tipo]["area_total"] += area
        por_tipo[tipo]["dotacion_total"] += dotacion

        ranking_area_base.append((entidad.id, entidad.nombre, area))
        ranking_dotacion_base.append((entidad.id, entidad.nombre, dotacion))

    area_promedio = total_area / total_entidades if total_entidades else 0
    dotacion_promedio = total_dotacion / total_entidades if total_entidades else 0
    dotacion_por_m2 = total_dotacion / total_area if total_area else 0

    # Convertir ranking (top 5)
    ranking_area = sorted(ranking_area_base, key=lambda x: x[2], reverse=True)[:5]
    ranking_dotacion = sorted(ranking_dotacion_base, key=lambda x: x[2], reverse=True)[:5]

    # Armar resumen por tipo
    por_tipo_res = {}
    for tipo, datos in por_tipo.items():
        area_prom_tipo = datos["area_total"] / datos["cantidad"] if datos["cantidad"] else 0
        dot_prom_tipo = datos["dotacion_total"] / datos["cantidad"] if datos["cantidad"] else 0
        dot_m2_tipo = datos["dotacion_total"] / datos["area_total"] if datos["area_total"] else 0
        por_tipo_res[tipo] = {
            "cantidad": datos["cantidad"],
            "area_total": datos["area_total"],
            "dotacion_total": datos["dotacion_total"],
            "area_promedio": area_prom_tipo,
            "dotacion_promedio": dot_prom_tipo,
            "dotacion_por_m2": dot_m2_tipo
        }

    return {
        "total_entidades": total_entidades,
        "total_area": total_area,
        "total_dotacion": total_dotacion,
        "area_promedio": area_promedio,
        "dotacion_promedio": dotacion_promedio,
        "dotacion_por_m2": dotacion_por_m2,
        "por_tipo": por_tipo_res,
        "ranking_area": ranking_area,
        "ranking_dotacion": ranking_dotacion
    }

def generar_resumen_texto(dictEntidades: Dict[str, object]) -> str:
    met = calcular_metricas_basicas(dictEntidades)
    if met["total_entidades"] == 0:
        return "No hay entidades cargadas. No se puede generar el reporte."

    lineas = []
    lineas.append("REPORTE GENERAL DEL PARQUE")
    lineas.append(f"Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lineas.append("-" * 50)
    lineas.append(f"Total de entidades: {met['total_entidades']}")
    lineas.append(f"Total área (m2): {met['total_area']:.2f}")
    lineas.append(f"Total dotación: {met['total_dotacion']}")
    lineas.append(f"Área promedio (m2): {met['area_promedio']:.2f}")
    lineas.append(f"Dotación promedio: {met['dotacion_promedio']:.2f}")
    lineas.append(f"Dotación por m2: {met['dotacion_por_m2']:.4f}")
    lineas.append("")
    lineas.append("DESGLOSE POR TIPO:")
    for tipo, datos in met["por_tipo"].items():
        lineas.append(f"  - {tipo}: {datos['cantidad']} entidades | Área total {datos['area_total']:.2f} | Dotación {datos['dotacion_total']} | Dot/m2 {datos['dotacion_por_m2']:.4f}")
    lineas.append("")
    lineas.append("TOP 5 POR ÁREA:")
    for (id_, nombre, area) in met["ranking_area"]:
        lineas.append(f"  {id_} | {nombre} | {area:.2f} m2")
    lineas.append("")
    lineas.append("TOP 5 POR DOTACIÓN:")
    for (id_, nombre, dot) in met["ranking_dotacion"]:
        lineas.append(f"  {id_} | {nombre} | {dot} personas")
    lineas.append("-" * 50)
    return "\n".join(lineas)

def exportar_reporte_texto(dictEntidades: Dict[str, object], ruta: str = "reporte.txt") -> None:
    contenido = generar_resumen_texto(dictEntidades)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(contenido)

def exportar_reporte_json(dictEntidades: Dict[str, object], ruta: str = "reporte.json") -> None:
    met = calcular_metricas_basicas(dictEntidades)
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(met, f, ensure_ascii=False, indent=2)

def exportar_reporte_csv(dictEntidades: Dict[str, object], ruta: str = "reporte.csv") -> None:
    """
    Exporta dos bloques:
    1) Tabla de entidades (id,nombre,tipo,areaM2,dotacion)
    2) Métricas agregadas (clave,valor)
    """
    met = calcular_metricas_basicas(dictEntidades)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write("# Entidades\n")
        f.write("id,nombre,tipo,areaM2,dotacion\n")
        for entidad in dictEntidades.values():
            tipo = _clasificar_tipo(entidad)
            area = getattr(entidad, "areaM2", 0.0)
            dot = getattr(entidad, "dotacion", 0)
            f.write(f"{entidad.id},{entidad.nombre},{tipo},{area},{dot}\n")
        f.write("\n# Métricas Generales\n")
        f.write("clave,valor\n")
        f.write(f"total_entidades,{met['total_entidades']}\n")
        f.write(f"total_area,{met['total_area']}\n")
        f.write(f"total_dotacion,{met['total_dotacion']}\n")
        f.write(f"area_promedio,{met['area_promedio']}\n")
        f.write(f"dotacion_promedio,{met['dotacion_promedio']}\n")
        f.write(f"dotacion_por_m2,{met['dotacion_por_m2']}\n")
        f.write("\n# Por Tipo\n")
        f.write("tipo,cantidad,area_total,dotacion_total,area_promedio,dotacion_promedio,dotacion_por_m2\n")
        for tipo, datos in met["por_tipo"].items():
            f.write(f"{tipo},{datos['cantidad']},{datos['area_total']},{datos['dotacion_total']},{datos['area_promedio']},{datos['dotacion_promedio']},{datos['dotacion_por_m2']}\n")

def generar_markdown(dictEntidades: Dict[str, object]) -> str:
    """
    Crea un reporte en formato Markdown (opcional).
    """
    met = calcular_metricas_basicas(dictEntidades)
    if met["total_entidades"] == 0:
        return "# Reporte\nNo hay entidades."

    md = []
    md.append(f"# Reporte del Parque\n")
    md.append(f"Generado: {datetime.now().isoformat()}\n")
    md.append("## Resumen General")
    md.append(f"- Total de entidades: **{met['total_entidades']}**")
    md.append(f"- Total área (m²): **{met['total_area']:.2f}**")
    md.append(f"- Total dotación: **{met['total_dotacion']}**")
    md.append(f"- Área promedio: **{met['area_promedio']:.2f} m²**")
    md.append(f"- Dotación promedio: **{met['dotacion_promedio']:.2f}**")
    md.append(f"- Dotación por m²: **{met['dotacion_por_m2']:.4f}**\n")

    md.append("## Desglose por Tipo")
    for tipo, datos in met["por_tipo"].items():
        md.append(f"- **{tipo}**: {datos['cantidad']} entidades | Área total {datos['area_total']:.2f} | Dotación {datos['dotacion_total']} | Dot/m² {datos['dotacion_por_m2']:.4f}")

    md.append("\n## Top 5 por Área")
    for (id_, nombre, area) in met["ranking_area"]:
        md.append(f"- {id_} — {nombre}: {area:.2f} m²")

    md.append("\n## Top 5 por Dotación")
    for (id_, nombre, dot) in met["ranking_dotacion"]:
        md.append(f"- {id_} — {nombre}: {dot} personas")

    return "\n".join(md)

def exportar_markdown(dictEntidades: Dict[str, object], ruta: str = "reporte.md") -> None:
    md = generar_markdown(dictEntidades)
    with open(ruta, "w", encoding="utf-8") as f:
        f.write(md) 

# EEEE llegaste al final papu! Ahora andà a jugar Silksong.