"""
MÓDULO DE CARRITO DE COMPRAS - PARADIGMA FUNCIONAL
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

PRINCIPIOS FUNDAMENTALES DEL PARADIGMA FUNCIONAL APLICADOS AQUÍ:
1. Funciones Puras: No producen efectos secundarios (no mutan variables ni el catálogo).
2. Inmutabilidad: Se trabaja con tuplas y estructuras no mutadas; las modificaciones
   generan nuevas estructuras de datos en lugar de alterar las existentes.
3. Funciones de Orden Superior: Uso intensivo de `map()`, `filter()` y `reduce()`.
4. Composición de Funciones: El flujo del carrito es un pipeline de transformaciones
   que toma un estado inicial inmutable y produce el reporte final.
5. Optimización Presupuestaria Pura: Evaluación de transformaciones alternativas
   para ajustar el total al presupuesto sin mutar datos.
"""

import os
import sys
import json
import math
from functools import reduce
from typing import Tuple, Dict, Any, List, Union, Optional

# Agregamos la ruta base para imports
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos


# -----------------------------------------------------------------------------
# 1. FUNCIONES PURAS DE CONSULTA Y CÁLCULO ATÓMICO (Sin Efectos Secundarios)
# -----------------------------------------------------------------------------

def obtener_producto_por_id(catalogo: Tuple[Dict[str, Any], ...], id_prod: str) -> Dict[str, Any]:
    """
    Función pura que busca un producto mediante 'filter'.
    No altera la colección original.
    """
    coincidencias = tuple(filter(lambda p: p["id"] == id_prod, catalogo))
    return coincidencias[0] if coincidencias else {}


def crear_item(producto: Dict[str, Any], cantidad: float, nota: Any = None) -> Dict[str, Any]:
    """
    Función pura constructora de un registro inmutable de línea de carrito.
    """
    cant = round(cantidad, 2)
    sub = round(cant * producto["precio"], 2)
    return {
        "id": producto["id"],
        "nombre": producto["nombre"],
        "categoria": producto["categoria"],
        "cantidad": cant,
        "unidad": producto["unidad"],
        "precio_unitario": producto["precio"],
        "subtotal": sub,
        "nota": nota
    }


# -----------------------------------------------------------------------------
# 2. TRANSFORMACIONES FUNCIONALES DE DEMANDA Y REGLAS DE NEGOCIO
# -----------------------------------------------------------------------------

def resolver_carne_con_sustitucion(
    catalogo: Tuple[Dict[str, Any], ...], 
    id_corte: str, 
    adultos: int, 
    ninos: int
) -> Tuple[Dict[str, Any], ...]:
    """
    Resuelve funcionalmente la demanda de carne y el quiebre de stock.
    Retorna una tupla de nuevos ítems sin mutar el catálogo de entrada.
    """
    kilos_necesarios = round((adultos * 0.35) + (ninos * 0.15), 2)
    if kilos_necesarios <= 0:
        return ()

    corte_preferido = obtener_producto_por_id(catalogo, id_corte)
    stock_disponible = corte_preferido.get("stock", 0.0)

    if stock_disponible < kilos_necesarios:
        kilos_cubiertos = stock_disponible
        kilos_faltantes = round(kilos_necesarios - kilos_cubiertos, 2)
        
        items_res = []
        if kilos_cubiertos > 0:
            items_res.append(crear_item(
                corte_preferido,
                kilos_cubiertos,
                f"Stock agotado. Se utilizaron los {kilos_cubiertos} kg disponibles."
            ))

        id_sustituto = corte_preferido.get("sustituto_id")
        sustituto = obtener_producto_por_id(catalogo, id_sustituto)
        if sustituto:
            items_res.append(crear_item(
                sustituto,
                kilos_faltantes,
                f"Sustituto activado por falta de stock de {corte_preferido['nombre']}."
            ))

        return tuple(items_res)
    else:
        item_preferido = crear_item(corte_preferido, kilos_necesarios, None)
        return (item_preferido,)


def resolver_choripanes(
    catalogo: Tuple[Dict[str, Any], ...], 
    carnívoros: int, 
    packs_deseados: Optional[int] = None
) -> Tuple[Dict[str, Any], ...]:
    """Genera funcionalmente los packs de choripán necesarios."""
    if carnívoros <= 0:
        return ()
    packs = math.ceil(carnívoros / 5.0) if packs_deseados is None else packs_deseados
    prod = obtener_producto_por_id(catalogo, "prod_03")
    return (crear_item(prod, packs, f"Calculado para {carnívoros} choripanes (packs de 5 u.)."),)


def resolver_vegetarianos(catalogo: Tuple[Dict[str, Any], ...], vegetarianos: int) -> Tuple[Dict[str, Any], ...]:
    """Genera las raciones vegetarianas mediante una tupla compuesta inmutable."""
    if vegetarianos <= 0:
        return ()
    prod_hamb = obtener_producto_por_id(catalogo, "prod_04")
    prod_pim = obtener_producto_por_id(catalogo, "prod_05")
    
    item_hamb = crear_item(prod_hamb, vegetarianos, f"Ración especial para {vegetarianos} comensal(es) vegetariano(s).")
    item_pim = crear_item(prod_pim, vegetarianos, None)
    return (item_hamb, item_pim)


def resolver_insumos(
    catalogo: Tuple[Dict[str, Any], ...], 
    kilos_carne: float, 
    total_personas: int
) -> Tuple[Dict[str, Any], ...]:
    """Calcula carbón y sal sin mutación de estado."""
    items = []
    if kilos_carne > 0:
        bolsas_carbon = math.ceil(kilos_carne / 3.0)
        prod_carbon = obtener_producto_por_id(catalogo, "prod_06")
        items.append(crear_item(
            prod_carbon, 
            bolsas_carbon, 
            f"Calculado según {kilos_carne} kg de carne (1 bolsa cada 3 kg)."
        ))

    if total_personas > 5:
        prod_sal = obtener_producto_por_id(catalogo, "prod_07")
        items.append(crear_item(prod_sal, 1, "Requerido para eventos mayores a 5 personas."))
    
    return tuple(items)


def resolver_bebidas(
    catalogo: Tuple[Dict[str, Any], ...], 
    total_personas: int, 
    botellas_deseadas: Optional[int] = None
) -> Tuple[Dict[str, Any], ...]:
    """Calcula bebidas requeridas en formato funcional."""
    if total_personas <= 0:
        return ()
    litros = total_personas * 0.5
    botellas = math.ceil(litros / 2.5) if botellas_deseadas is None else botellas_deseadas
    prod_bebida = obtener_producto_por_id(catalogo, "prod_08")
    return (crear_item(prod_bebida, botellas, f"Calculado para {litros}L totales (0.5L por comensal)."),)


# -----------------------------------------------------------------------------
# 3. PIPELINE DE EVALUACIÓN DE DESCUENTOS Y AGREGACIONES CON REDUCE
# -----------------------------------------------------------------------------

def es_producto_combo(item: Dict[str, Any]) -> bool:
    """Predicado puro utilizado con 'filter' para identificar ítems afectos a promoción."""
    es_carne = item.get("categoria") == "carnico"
    es_carbon = item.get("id") == "prod_06"
    es_sal = item.get("id") == "prod_07"
    return es_carne or es_carbon or es_sal


def calcular_descuento_combo_funcional(items: Tuple[Dict[str, Any], ...]) -> Tuple[float, str]:
    """
    Aplica 'filter' y 'reduce' para evaluar la regla de descuento del combo parrillero.
    """
    tiene_carne = any(map(lambda it: it.get("categoria") == "carnico", items))
    tiene_carbon = any(map(lambda it: it.get("id") == "prod_06", items))
    tiene_sal = any(map(lambda it: it.get("id") == "prod_07", items))

    if tiene_carne and tiene_carbon and tiene_sal:
        items_combo = tuple(filter(es_producto_combo, items))
        subtotal_combo = reduce(lambda acc, it: acc + it["subtotal"], items_combo, 0.0)
        descuento = float(round(subtotal_combo * 0.10))
        return descuento, "Combo Parrillero (10% en Carne + Carbón + Sal)"

    return 0.0, ""


def calcular_pipeline_evento(
    catalogo: Tuple[Dict[str, Any], ...],
    datos_eve: dict,
    corte_id: str,
    botellas_deseadas: Optional[int] = None,
    packs_chori_deseados: Optional[int] = None
) -> Tuple[Tuple[Dict[str, Any], ...], float, float, str, float]:
    """Evalúa un pipeline funcional completo y retorna los resultados financieros."""
    comensales = datos_eve["comensales"]
    adultos = comensales["adultos"]
    ninos = comensales["ninos"]
    vegetarianos = comensales["vegetarianos"]
    carnívoros = adultos + ninos
    total_personas = adultos + ninos + vegetarianos

    items_carne = resolver_carne_con_sustitucion(catalogo, corte_id, adultos, ninos)
    kilos_carne = round((adultos * 0.35) + (ninos * 0.15), 2)
    items_chori = resolver_choripanes(catalogo, carnívoros, packs_chori_deseados)
    items_veg = resolver_vegetarianos(catalogo, vegetarianos)
    items_insumos = resolver_insumos(catalogo, kilos_carne, total_personas)
    items_bebidas = resolver_bebidas(catalogo, total_personas, botellas_deseadas)

    todos_los_items: Tuple[Dict[str, Any], ...] = (
        items_carne + items_chori + items_veg + items_insumos + items_bebidas
    )

    subtotal_general = round(
        reduce(lambda acc, it: acc + it["subtotal"], todos_los_items, 0.0),
        2
    )
    descuento, detalle_promocion = calcular_descuento_combo_funcional(todos_los_items)
    total_final = float(round(subtotal_general - descuento))

    return todos_los_items, subtotal_general, descuento, detalle_promocion, total_final


# -----------------------------------------------------------------------------
# 4. COMPOSICIÓN Y ORQUESTADOR PRINCIPAL (Pipeline Funcional)
# -----------------------------------------------------------------------------

def procesar_carrito_funcional(
    ruta_catalogo: str, 
    evento_input: Union[str, dict, None] = None,
    interactivo: bool = False
) -> dict:
    """
    Pipeline que carga los datos, ejecuta transformaciones puras encadenadas
    y aplica optimización activa por presupuesto sin efectos colaterales.
    """
    with open(ruta_catalogo, "r", encoding="utf-8") as f_cat:
        datos_cat = json.load(f_cat)

    if interactivo:
        datos_eve = solicitar_datos_interactivos("Funcional")
    elif isinstance(evento_input, dict):
        datos_eve = evento_input
    elif isinstance(evento_input, str):
        with open(evento_input, "r", encoding="utf-8") as f_eve:
            datos_eve = json.load(f_eve)
    else:
        ruta_def = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        with open(ruta_def, "r", encoding="utf-8") as f_eve:
            datos_eve = json.load(f_eve)

    catalogo_inmutable: Tuple[Dict[str, Any], ...] = tuple(datos_cat["productos"])
    id_corte_inicial = datos_eve["preferencias"].get("tipo_corte_preferido", "prod_01")
    presupuesto_max = datos_eve.get("presupuesto_maximo")

    # Evaluación inicial pura
    items, subtotal, descuento, detalle_prom, total = calcular_pipeline_evento(
        catalogo_inmutable, datos_eve, id_corte_inicial
    )

    ajustes_presupuesto = []
    comensales = datos_eve["comensales"]
    tot_personas = comensales["adultos"] + comensales["ninos"] + comensales["vegetarianos"]

    # -------------------------------------------------------------------------
    # GESTIÓN ACTIVA DE PRESUPUESTO EN EL PARADIGMA FUNCIONAL
    # -------------------------------------------------------------------------
    if presupuesto_max and total > presupuesto_max:
        # Intento 1: Degradación pura de corte
        if id_corte_inicial == "prod_01":
            it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                catalogo_inmutable, datos_eve, "prod_02"
            )
            if tot_t < total:
                items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                ajustes_presupuesto.append("Se degradó el corte de Lomo Vetado ($14.990) a Sobrecostilla ($9.990) para reducir costos.")

        # Intento 2: Reducción pura de bebidas a 1 botella mínima
        if total > presupuesto_max and tot_personas > 0:
            if math.ceil((tot_personas * 0.5) / 2.5) > 1:
                it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                    catalogo_inmutable, datos_eve,
                    "prod_02" if id_corte_inicial == "prod_01" else id_corte_inicial,
                    botellas_deseadas=1
                )
                if tot_t < total:
                    items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujeron las bebidas a 1 botella básica para acercarse al presupuesto.")

        # Intento 3: Reducción pura de embutidos a 1 pack esencial
        if total > presupuesto_max and (comensales["adultos"] + comensales["ninos"]) > 0:
            if math.ceil((comensales["adultos"] + comensales["ninos"]) / 5.0) > 1:
                it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                    catalogo_inmutable, datos_eve,
                    "prod_02" if id_corte_inicial == "prod_01" else id_corte_inicial,
                    botellas_deseadas=1,
                    packs_chori_deseados=1
                )
                if tot_t < total:
                    items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujo el embutido a 1 pack de chorizos para ajustar el gasto.")

    alerta_presupuesto = None
    if presupuesto_max and total > presupuesto_max:
        alerta_presupuesto = f"Incluso con ajustes mínimos, el total ({formato_moneda(total)}) excede el presupuesto ({formato_moneda(presupuesto_max)})."

    return {
        "evento": datos_eve["nombre_evento"],
        "items": list(items),
        "subtotal": subtotal,
        "descuento": descuento,
        "detalle_descuento": detalle_prom,
        "total": total,
        "presupuesto_maximo": presupuesto_max,
        "ajustes_presupuesto": ajustes_presupuesto,
        "alerta_presupuesto": alerta_presupuesto
    }


if __name__ == "__main__":
    ruta_cat = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
    if not os.path.exists(ruta_cat):
        ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

    print("\n" + "═" * 68)
    print(" SISTEMA CARRITO EVENTO ESPECIAL — PARADIGMA FUNCIONAL")
    print("═" * 68)
    print(" [1] Modo Automático (Dataset oficial de prueba UTEM)")
    print(" [2] Modo Interactivo (Ingresar datos y presupuesto por teclado)")
    print("═" * 68)
    opc = input("Seleccione una opción [1 o 2, Default: 1]: ").strip()

    if opc == "2":
        boleta = procesar_carrito_funcional(ruta_cat, interactivo=True)
    else:
        ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        boleta = procesar_carrito_funcional(ruta_cat, ruta_eve)

    imprimir_resumen_carrito(boleta, "Funcional")

    if boleta.get("ajustes_presupuesto"):
        print("\n🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
        for aj in boleta["ajustes_presupuesto"]:
            print(f"   • {aj}")
        print()

    if boleta.get("alerta_presupuesto"):
        print(f"⚠️  {boleta['alerta_presupuesto']}\n")
