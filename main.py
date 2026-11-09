"""
PROGRAMA PRINCIPAL Y DEMOSTRADOR MULTIMODAL (CLI)
Asignatura: Lenguajes de Programación (UTEM)
Proyecto: Carrito Evento Especial — Asado Parrillero

MODALIDADES SOPORTADAS SEGÚN LA PAUTA:
1. Modo Interactivo: El usuario ingresa por teclado invitados, vegetarianos y presupuesto.
2. Modo Automático: El sistema dimensiona el pedido completo solo con ingresar 'N personas'.
3. Modo Defensa Académica: Demostrador para la comisión evaluadora y pruebas automatizadas.
4. Tienda Web Demostrable (Etapa 1): Servidor e-commerce local en http://localhost:8000.
"""

import os
import sys
import unittest
import webbrowser

# Directorio raíz del proyecto
DIRECTORIO_RAIZ = os.path.abspath(os.path.dirname(__file__))
sys.path.append(DIRECTORIO_RAIZ)

from src.imperativo.carrito_imperativo import procesar_carrito_imperativo
from src.poo.carrito_poo import procesar_carrito_poo
from src.funcional.carrito_funcional import procesar_carrito_funcional
from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos, generar_evento_automatico
from tests.test_equivalencia import TestEquivalenciaMultiparadigma
from servidor_tienda import iniciar_servidor

RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
if not os.path.exists(RUTA_CATALOGO):
    RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

RUTA_EVENTO_OFICIAL = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")


def mostrar_comparativa_side_by_side(boleta_imp, boleta_poo, boleta_fun):
    """Muestra una tabla resumen de comparación directa entre los 3 paradigmas."""
    ancho = 80
    sep = "═" * ancho
    sub_sep = "─" * ancho

    print("\n" + sep)
    print(" CUADRO COMPARATIVO MULTIPARADIGMA — PARIDAD DE RESULTADOS (UTEM)")
    print(sep)
    print(f"{'Métrica / Indicador':<30} {'Imperativo':>15} {'POO':>15} {'Funcional':>15}")
    print(sub_sep)
    
    # Líneas de ítems
    print(f"{'Total de Ítems Generados':<30} {len(boleta_imp['items']):>15} {len(boleta_poo['items']):>15} {len(boleta_fun['items']):>15}")
    
    # Subtotal
    sub_i = formato_moneda(boleta_imp['subtotal'])
    sub_p = formato_moneda(boleta_poo['subtotal'])
    sub_f = formato_moneda(boleta_fun['subtotal'])
    print(f"{'Subtotal Neto':<30} {sub_i:>15} {sub_p:>15} {sub_f:>15}")

    # Descuento
    desc_i = formato_moneda(boleta_imp['descuento'])
    desc_p = formato_moneda(boleta_poo['descuento'])
    desc_f = formato_moneda(boleta_fun['descuento'])
    print(f"{'Descuento Combo Parrillero':<30} {desc_i:>15} {desc_p:>15} {desc_f:>15}")

    # Total
    tot_i = formato_moneda(boleta_imp['total'])
    tot_p = formato_moneda(boleta_poo['total'])
    tot_f = formato_moneda(boleta_fun['total'])
    print(sub_sep)
    print(f"{'TOTAL FINAL A PAGAR':<30} {tot_i:>15} {tot_p:>15} {tot_f:>15}")
    print(sep)

    coinciden = (boleta_imp['total'] == boleta_poo['total'] == boleta_fun['total'])
    if coinciden:
        print("  >>> ESTADO: [ÉXITO] Las 3 versiones producen EXACTAMENTE el mismo total. <<<")
    else:
        print("  >>> ESTADO: [DISCREPANCIA] Hay diferencias en los cálculos. <<<")
    print(sep + "\n")


def ejecutar_modo_interactivo():
    """Ejecuta el flujo interactivo donde el usuario personaliza el evento."""
    evento = solicitar_datos_interactivos("Configuración Personalizada")

    print("\n¿En qué paradigma desea procesar el carrito?")
    print("  1. Imperativo")
    print("  2. Orientado a Objetos (POO)")
    print("  3. Funcional")
    print("  4. Comparativa Triple Simultánea (Los 3 paradigmas)")
    sub_opc = input("Seleccione opción [1-4, Default: 4]: ").strip() or "4"

    def imprimir_ajustes(b):
        if b.get("ajustes_presupuesto"):
            print("🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
            for aj in b["ajustes_presupuesto"]:
                print(f"   • {aj}")
            print()
        if b.get("alerta_presupuesto"):
            print(f"⚠️  {b['alerta_presupuesto']}\n")

    if sub_opc == "1":
        b = procesar_carrito_imperativo(RUTA_CATALOGO, evento_input=evento)
        imprimir_resumen_carrito(b, "Imperativo")
        imprimir_ajustes(b)
    elif sub_opc == "2":
        b = procesar_carrito_poo(RUTA_CATALOGO, evento_input=evento)
        imprimir_resumen_carrito(b, "Orientado a Objetos")
        imprimir_ajustes(b)
    elif sub_opc == "3":
        b = procesar_carrito_funcional(RUTA_CATALOGO, evento_input=evento)
        imprimir_resumen_carrito(b, "Funcional")
        imprimir_ajustes(b)
    else:
        b1 = procesar_carrito_imperativo(RUTA_CATALOGO, evento_input=evento)
        b2 = procesar_carrito_poo(RUTA_CATALOGO, evento_input=evento)
        b3 = procesar_carrito_funcional(RUTA_CATALOGO, evento_input=evento)
        imprimir_resumen_carrito(b2, "Orientado a Objetos (Consolidado)")
        imprimir_ajustes(b2)
        mostrar_comparativa_side_by_side(b1, b2, b3)


def ejecutar_modo_automatico():
    """Arma el carrito solo indicando 'N personas' (ej: 'Hazme un carrito para 10 personas')."""
    print("\n" + "─" * 68)
    print(" MODALIDAD AUTOMÁTICA: DIMENSIONAMIENTO EXPRÉS DE CARRITO")
    print("─" * 68)
    
    while True:
        try:
            raw_p = input("Ingrese para cuántas personas es el evento [ej. 10]: ").strip()
            total_p = int(raw_p) if raw_p else 10
            if total_p > 0:
                break
            print("Debe ser mayor a 0.")
        except ValueError:
            print("Ingrese un número entero válido.")

    evento_auto = generar_evento_automatico(total_p)
    print(f"\n[OK] Generado automáticamente: {evento_auto['nombre_evento']}")
    print(f"     Comensales: {evento_auto['comensales']['adultos']} adultos, {evento_auto['comensales']['ninos']} niños.")
    print(f"     Presupuesto estimado: {formato_moneda(evento_auto['presupuesto_maximo'])}")

    # Procesa en los 3 paradigmas
    b_imp = procesar_carrito_imperativo(RUTA_CATALOGO, evento_input=evento_auto)
    b_poo = procesar_carrito_poo(RUTA_CATALOGO, evento_input=evento_auto)
    b_fun = procesar_carrito_funcional(RUTA_CATALOGO, evento_input=evento_auto)

    imprimir_resumen_carrito(b_poo, "Automático - Orquestado")
    mostrar_comparativa_side_by_side(b_imp, b_poo, b_fun)


def ejecutar_modo_defensa():
    """Submenú específico con los datos fijos del informe y suite de pruebas para el profesor."""
    while True:
        print("\n" + "┌────────────────────────────────────────────────────────────────────┐")
        print("│   MODO DEFENSA ACADÉMICA (EVALUACIÓN DOCENTE UTEM)                 │")
        print("├────────────────────────────────────────────────────────────────────┤")
        print("│ 1. Ejecutar Versión Imperativa (Dataset oficial del informe)        │")
        print("│ 2. Ejecutar Versión Orientada a Objetos (Dataset oficial)          │")
        print("│ 3. Ejecutar Versión Funcional (Dataset oficial)                    │")
        print("│ 4. Comparativa Triple Simultánea (Side-by-Side)                    │")
        print("│ 5. Ejecutar Suite de Pruebas Unitarias de Equivalencia (6 tests)   │")
        print("│ 0. Volver al Menú Principal                                        │")
        print("└────────────────────────────────────────────────────────────────────┘")

        opc = input("Seleccione una opción [0-5]: ").strip()
        if opc == "1":
            b = procesar_carrito_imperativo(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            imprimir_resumen_carrito(b, "Imperativo")
        elif opc == "2":
            b = procesar_carrito_poo(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            imprimir_resumen_carrito(b, "Orientado a Objetos")
        elif opc == "3":
            b = procesar_carrito_funcional(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            imprimir_resumen_carrito(b, "Funcional")
        elif opc == "4":
            b_imp = procesar_carrito_imperativo(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            b_poo = procesar_carrito_poo(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            b_fun = procesar_carrito_funcional(RUTA_CATALOGO, RUTA_EVENTO_OFICIAL)
            mostrar_comparativa_side_by_side(b_imp, b_poo, b_fun)
        elif opc == "5":
            suite = unittest.TestLoader().loadTestsFromTestCase(TestEquivalenciaMultiparadigma)
            unittest.TextTestRunner(verbosity=2).run(suite)
        elif opc == "0":
            break
        else:
            print("Opción inválida.")


def menu_principal():
    """Menú raíz de la aplicación."""
    while True:
        print("╔════════════════════════════════════════════════════════════════════╗")
        print("║   SISTEMA DE E-COMMERCE: CARRITO EVENTO ESPECIAL (UTEM)            ║")
        print("║   Asignatura: Lenguajes de Programación · Semestre 2-2026          ║")
        print("╠════════════════════════════════════════════════════════════════════╣")
        print("║ 1. Modo Interactivo (Ingreso por teclado de invitados y montos)    ║")
        print("║ 2. Modo Automático  (Armado exprés solo indicando 'N personas')    ║")
        print("║ 3. Modo Defensa     (Demostrador oficial para la comisión docente) ║")
        print("║ 4. Tienda Web en Vivo (Levantar servidor local en puerto 8000)     ║")
        print("║ 0. Salir                                                           ║")
        print("╚════════════════════════════════════════════════════════════════════╝")

        opc = input("Seleccione una opción [0-4]: ").strip()

        if opc == "1":
            ejecutar_modo_interactivo()
        elif opc == "2":
            ejecutar_modo_automatico()
        elif opc == "3":
            ejecutar_modo_defensa()
        elif opc == "4":
            iniciar_servidor(8000)
        elif opc == "0":
            print("\n¡Gracias por utilizar el Carrito Evento Especial! Éxito en tu presentación.\n")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.\n")


if __name__ == "__main__":
    menu_principal()
