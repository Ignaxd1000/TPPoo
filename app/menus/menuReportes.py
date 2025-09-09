from reportes.generadorReportes import (
    generar_resumen_texto,
    exportar_reporte_texto,
    exportar_reporte_json,
    exportar_reporte_csv,
    exportar_markdown
)

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
            print(generar_resumen_texto(entidades))
        elif op == "2":
            exportar_reporte_texto(entidades)
            print("Reporte TXT generado.")
        elif op == "3":
            exportar_reporte_json(entidades)
            print("Reporte JSON generado.")
        elif op == "4":
            exportar_reporte_csv(entidades)
            print("Reporte CSV generado.")
        elif op == "5":
            exportar_markdown(entidades)
            print("Reporte Markdown generado.")
        elif op == "6":
            break
        else:
            print("Opción inválida")