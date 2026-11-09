"""
Módulo de visualización y formateo de boletas de compra.
Garantiza un formato de salida estandarizado e idéntico para los tres paradigmas
(Imperativo, Orientado a Objetos y Funcional).
"""

def formato_moneda(monto: float) -> str:
    """
    Formatea un número a representación monetaria en Pesos Chilenos (CLP).
    Ejemplo: 14990 -> $14.990 CLP
    """
    monto_redondeado = int(round(monto))
    # Formateo con separador de miles
    cadena_formateada = f"${monto_redondeado:,}".replace(",", ".")
    return f"{cadena_formateada} CLP"


def imprimir_resumen_carrito(boleta: dict, nombre_paradigma: str) -> None:
    """
    Imprime en consola el desglose ordenado y profesional de la compra.
    
    Parámetros:
        boleta (dict): Diccionario con la estructura canónica:
            - 'evento': str
            - 'items': list of dicts (nombre, cantidad, unidad, precio_unitario, subtotal, nota)
            - 'subtotal': float
            - 'descuento': float
            - 'detalle_descuento': str
            - 'total': float
        nombre_paradigma (str): Nombre del paradigma ejecutado (ej: 'IMPERATIVO').
    """
    separador_principal = "═" * 72
    separador_secundario = "─" * 72

    print("\n" + separador_principal)
    print(f" BOLETA DE VENTA OFICIAL — PARADIGMA: {nombre_paradigma.upper()}")
    print(f" Evento: {boleta.get('evento', 'Evento Especial')}")
    print(separador_principal)
    print(f"{'Producto':<32} {'Cant.':>10} {'P. Unitario':>14} {'Subtotal':>12}")
    print(separador_secundario)

    for item in boleta.get("items", []):
        nombre = item["nombre"]
        if len(nombre) > 30:
            nombre = nombre[:27] + "..."

        cant_str = f"{item['cantidad']} {item.get('unidad', '')}".strip()
        p_unit_str = formato_moneda(item["precio_unitario"])
        sub_str = formato_moneda(item["subtotal"])

        print(f"{nombre:<32} {cant_str:>10} {p_unit_str:>14} {sub_str:>12}")
        
        # Muestra avisos pedagógicos (sustituciones por falta de stock)
        if item.get("nota"):
            print(f"   ↳ [STOCK/REGLA]: {item['nota']}")

    print(separador_secundario)
    print(f"{'Subtotal Neto:':<58} {formato_moneda(boleta['subtotal']):>12}")

    if boleta.get("descuento", 0) > 0:
        detalle = boleta.get("detalle_descuento", "Descuento Promoción")
        desc_str = f"- {formato_moneda(boleta['descuento'])}"
        print(f"{'Descuento (' + detalle + '):':<58} {desc_str:>12}")

    print(separador_principal)
    print(f"{'TOTAL FINAL A PAGAR:':<58} {formato_moneda(boleta['total']):>12}")
    print(separador_principal + "\n")
