"""
MÓDULO DE CARRITO DE COMPRAS - PARADIGMA IMPERATIVO
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

CARACTERÍSTICAS DEL PARADIGMA IMPERATIVO APLICADAS AQUÍ:
1. Control de flujo explícito y secuencial (paso a paso).
2. Estado mutable: variables que se reasignan y listas que crecen con .append().
3. Efectos secundarios (Side Effects): mutación directa del inventario del catálogo.
4. Acumulación manual de subtotales mediante bucles for y sentencias if/elif.
5. Gestión Activa del Presupuesto: Si el total supera el presupuesto máximo,
   aplica reglas de degradación de calidad de corte y reducción de extras.
"""

import os
import json
import math
import sys
from typing import Union, Optional

# Agregamos la ruta base para poder importar los módulos utilitarios
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos


def buscar_producto_por_id(catalogo: dict, id_producto: str):
    """
    Recorre secuencialmente la lista de productos buscando coincidencia por ID.
    Enfoque imperativo: búsqueda lineal tradicional con bucle 'for' y 'break'.
    """
    producto_encontrado = None
    for p in catalogo["productos"]:
        if p["id"] == id_producto:
            producto_encontrado = p
            break
    return producto_encontrado


def procesar_carrito_imperativo(
    ruta_catalogo: str, 
    evento_input: Union[str, dict, None] = None,
    interactivo: bool = False
) -> dict:
    """
    Ejecuta toda la lógica de negocio del carrito mediante sentencias imperativas.
    Modifica el estado del inventario y acumula resultados en variables locales mutables.
    Incluye algoritmo de optimización y ajuste activo si se sobrepasa el presupuesto.
    """
    # 1. Carga imperativa del catálogo desde el JSON
    with open(ruta_catalogo, "r", encoding="utf-8") as f_cat:
        catalogo = json.load(f_cat)

    # 2. Resolución de los datos del evento
    if interactivo:
        evento = solicitar_datos_interactivos("Imperativo")
    elif isinstance(evento_input, dict):
        evento = evento_input
    elif isinstance(evento_input, str):
        with open(evento_input, "r", encoding="utf-8") as f_eve:
            evento = json.load(f_eve)
    else:
        ruta_def = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        with open(ruta_def, "r", encoding="utf-8") as f_eve:
            evento = json.load(f_eve)

    comensales = evento["comensales"]
    adultos = comensales["adultos"]
    ninos = comensales["ninos"]
    vegetarianos = comensales["vegetarianos"]
    total_personas = adultos + ninos + vegetarianos
    presupuesto_max = evento.get("presupuesto_maximo")

    # Función interna imperativa para generar la boleta según parámetros actuales
    def calcular_propuesta(corte_vacuno_id: str, botellas_deseadas: Optional[int] = None, packs_chori_deseados: Optional[int] = None):
        items = []
        subtotal_gen = 0.0
        subtotal_combo = 0.0
        tiene_c = False
        tiene_carb = False
        tiene_s = False

        # Copia de trabajo del catálogo para no viciar recálculos
        with open(ruta_catalogo, "r", encoding="utf-8") as f:
            cat_local = json.load(f)

        # Carne vacuna
        kilos_vac = round((adultos * 0.35) + (ninos * 0.15), 2)
        corte_pref = buscar_producto_por_id(cat_local, corte_vacuno_id)

        if corte_pref and kilos_vac > 0:
            stock_disp = corte_pref["stock"]
            if stock_disp < kilos_vac:
                kilos_cub = stock_disp
                kilos_fal = round(kilos_vac - kilos_cub, 2)

                if kilos_cub > 0:
                    corte_pref["stock"] = 0.0
                    sub1 = round(kilos_cub * corte_pref["precio"], 2)
                    subtotal_gen += sub1
                    subtotal_combo += sub1
                    tiene_c = True
                    items.append({
                        "id": corte_pref["id"],
                        "nombre": corte_pref["nombre"],
                        "cantidad": kilos_cub,
                        "unidad": corte_pref["unidad"],
                        "precio_unitario": corte_pref["precio"],
                        "subtotal": sub1,
                        "nota": f"Stock agotado. Se utilizaron los {kilos_cub} kg disponibles."
                    })

                id_sust = corte_pref.get("sustituto_id")
                sust = buscar_producto_por_id(cat_local, id_sust) if id_sust else None
                if sust and sust["stock"] >= kilos_fal:
                    sust["stock"] -= kilos_fal
                    sub_sust = round(kilos_fal * sust["precio"], 2)
                    subtotal_gen += sub_sust
                    subtotal_combo += sub_sust
                    tiene_c = True
                    items.append({
                        "id": sust["id"],
                        "nombre": sust["nombre"],
                        "cantidad": kilos_fal,
                        "unidad": sust["unidad"],
                        "precio_unitario": sust["precio"],
                        "subtotal": sub_sust,
                        "nota": f"Sustituto activado por falta de stock de {corte_pref['nombre']}."
                    })
            else:
                corte_pref["stock"] -= kilos_vac
                sub = round(kilos_vac * corte_pref["precio"], 2)
                subtotal_gen += sub
                subtotal_combo += sub
                tiene_c = True
                items.append({
                    "id": corte_pref["id"],
                    "nombre": corte_pref["nombre"],
                    "cantidad": kilos_vac,
                    "unidad": corte_pref["unidad"],
                    "precio_unitario": corte_pref["precio"],
                    "subtotal": sub,
                    "nota": None
                })

        # Chorizos
        carnivoros = adultos + ninos
        if carnivoros > 0:
            packs_calc = math.ceil(carnivoros / 5.0) if packs_chori_deseados is None else packs_chori_deseados
            prod_chori = buscar_producto_por_id(cat_local, "prod_03")
            prod_chori["stock"] -= packs_calc
            sub_chori = packs_calc * prod_chori["precio"]
            subtotal_gen += sub_chori
            subtotal_combo += sub_chori

            items.append({
                "id": prod_chori["id"],
                "nombre": prod_chori["nombre"],
                "cantidad": packs_calc,
                "unidad": prod_chori["unidad"],
                "precio_unitario": prod_chori["precio"],
                "subtotal": sub_chori,
                "nota": f"Calculado para {carnivoros} choripanes (packs de 5 u.)."
            })

        # Menú Vegetariano
        if vegetarianos > 0:
            prod_hamb = buscar_producto_por_id(cat_local, "prod_04")
            prod_pim = buscar_producto_por_id(cat_local, "prod_05")
            sub_hamb = vegetarianos * prod_hamb["precio"]
            sub_pim = vegetarianos * prod_pim["precio"]
            subtotal_gen += sub_hamb + sub_pim

            items.append({
                "id": prod_hamb["id"],
                "nombre": prod_hamb["nombre"],
                "cantidad": vegetarianos,
                "unidad": prod_hamb["unidad"],
                "precio_unitario": prod_hamb["precio"],
                "subtotal": sub_hamb,
                "nota": f"Ración especial para {vegetarianos} comensal(es) vegetariano(s)."
            })
            items.append({
                "id": prod_pim["id"],
                "nombre": prod_pim["nombre"],
                "cantidad": vegetarianos,
                "unidad": prod_pim["unidad"],
                "precio_unitario": prod_pim["precio"],
                "subtotal": sub_pim,
                "nota": None
            })

        # Carbón y Sal
        if kilos_vac > 0:
            bolsas_carb = math.ceil(kilos_vac / 3.0)
            prod_carb = buscar_producto_por_id(cat_local, "prod_06")
            sub_carb = bolsas_carb * prod_carb["precio"]
            subtotal_gen += sub_carb
            subtotal_combo += sub_carb
            tiene_carb = True

            items.append({
                "id": prod_carb["id"],
                "nombre": prod_carb["nombre"],
                "cantidad": bolsas_carb,
                "unidad": prod_carb["unidad"],
                "precio_unitario": prod_carb["precio"],
                "subtotal": sub_carb,
                "nota": f"Calculado según {kilos_vac} kg de carne (1 bolsa cada 3 kg)."
            })

        if total_personas > 5:
            prod_sal = buscar_producto_por_id(cat_local, "prod_07")
            sub_sal = 1 * prod_sal["precio"]
            subtotal_gen += sub_sal
            subtotal_combo += sub_sal
            tiene_s = True

            items.append({
                "id": prod_sal["id"],
                "nombre": prod_sal["nombre"],
                "cantidad": 1,
                "unidad": prod_sal["unidad"],
                "precio_unitario": prod_sal["precio"],
                "subtotal": sub_sal,
                "nota": "Requerido para eventos mayores a 5 personas."
            })

        # Bebidas
        if total_personas > 0:
            litros = total_personas * 0.5
            botellas_calc = math.ceil(litros / 2.5) if botellas_deseadas is None else botellas_deseadas
            prod_beb = buscar_producto_por_id(cat_local, "prod_08")
            sub_beb = botellas_calc * prod_beb["precio"]
            subtotal_gen += sub_beb

            items.append({
                "id": prod_beb["id"],
                "nombre": prod_beb["nombre"],
                "cantidad": botellas_calc,
                "unidad": prod_beb["unidad"],
                "precio_unitario": prod_beb["precio"],
                "subtotal": sub_beb,
                "nota": f"Calculado para {litros}L totales (0.5L por comensal)."
            })

        # Promoción Combo Parrillero
        desc = 0.0
        det_prom = ""
        if tiene_c and tiene_carb and tiene_s:
            desc = float(round(subtotal_combo * 0.10))
            det_prom = "Combo Parrillero (10% en Carne + Carbón + Sal)"

        tot = float(round(subtotal_gen - desc))
        return items, subtotal_gen, desc, det_prom, tot

    # Cálculo de la propuesta inicial
    id_corte_solicitado = evento["preferencias"].get("tipo_corte_preferido", "prod_01")
    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = calcular_propuesta(id_corte_solicitado)

    # -------------------------------------------------------------------------
    # REGLA DE NEGOCIO AVANZADA: GESTIÓN ACTIVA DE PRESUPUESTO
    # Si el total supera el presupuesto máximo, el sistema ajusta automáticamente:
    # 1. Degrada la calidad del corte (de Lomo Vetado a Sobrecostilla).
    # 2. Si aún supera, ajusta bebidas al mínimo esencial.
    # 3. Si aún supera, ajusta chorizos a 1 pack esencial.
    # -------------------------------------------------------------------------
    ajustes_presupuesto = []
    
    if presupuesto_max and total_pagar > presupuesto_max:
        # Intento 1: Si pidió Lomo Vetado (prod_01), degradamos a Sobrecostilla (prod_02)
        if id_corte_solicitado == "prod_01":
            items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta("prod_02")
            if tot_t < total_pagar:
                items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                ajustes_presupuesto.append("Se degradó el corte de Lomo Vetado ($14.990) a Sobrecostilla ($9.990) para reducir costos.")

        # Intento 2: Si todavía supera el presupuesto, reducimos bebidas a 1 botella mínima
        if total_pagar > presupuesto_max and total_personas > 0:
            litros_totales = total_personas * 0.5
            botellas_originales = math.ceil(litros_totales / 2.5)
            if botellas_originales > 1:
                items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta(
                    corte_vacuno_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                    botellas_deseadas=1
                )
                if tot_t < total_pagar:
                    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujeron las bebidas a 1 botella básica para acercarse al presupuesto.")

        # Intento 3: Si todavía supera, reducimos chorizos a 1 pack esencial
        if total_pagar > presupuesto_max and (adultos + ninos) > 0:
            packs_originales = math.ceil((adultos + ninos) / 5.0)
            if packs_originales > 1:
                items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta(
                    corte_vacuno_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                    botellas_deseadas=1,
                    packs_chori_deseados=1
                )
                if tot_t < total_pagar:
                    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujo el embutido a 1 pack de chorizos para ajustar el gasto.")

    alerta_presupuesto = None
    if presupuesto_max and total_pagar > presupuesto_max:
        alerta_presupuesto = f"Incluso con ajustes mínimos, el total ({formato_moneda(total_pagar)}) excede el presupuesto ({formato_moneda(presupuesto_max)})."

    boleta_final = {
        "evento": evento["nombre_evento"],
        "items": items,
        "subtotal": subtotal_general,
        "descuento": descuento_total,
        "detalle_descuento": detalle_promocion,
        "total": total_pagar,
        "presupuesto_maximo": presupuesto_max,
        "ajustes_presupuesto": ajustes_presupuesto,
        "alerta_presupuesto": alerta_presupuesto
    }

    return boleta_final


if __name__ == "__main__":
    ruta_cat = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
    if not os.path.exists(ruta_cat):
        ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

    print("\n" + "═" * 68)
    print(" SISTEMA CARRITO EVENTO ESPECIAL — PARADIGMA IMPERATIVO")
    print("═" * 68)
    print(" [1] Modo Automático (Dataset oficial de prueba UTEM)")
    print(" [2] Modo Interactivo (Ingresar datos y presupuesto por teclado)")
    print("═" * 68)
    opc = input("Seleccione una opción [1 o 2, Default: 1]: ").strip()

    if opc == "2":
        boleta = procesar_carrito_imperativo(ruta_cat, interactivo=True)
    else:
        ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        boleta = procesar_carrito_imperativo(ruta_cat, ruta_eve)

    imprimir_resumen_carrito(boleta, "Imperativo")
    
    if boleta.get("ajustes_presupuesto"):
        print("\n🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
        for aj in boleta["ajustes_presupuesto"]:
            print(f"   • {aj}")
        print()

    if boleta.get("alerta_presupuesto"):
        print(f"⚠️  {boleta['alerta_presupuesto']}\n")
