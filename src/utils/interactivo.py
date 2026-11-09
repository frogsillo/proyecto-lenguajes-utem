"""
MÓDULO DE INTERACCIÓN Y PARAMETRIZACIÓN DE EVENTOS
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

Proporciona:
1. Modalidad Interactiva: Lee datos detallados por consola (adultos, niños, vegetarianos, presupuesto, corte).
2. Modalidad Automática: Genera la configuración completa del evento solo a partir del número total de personas.
"""

def solicitar_datos_interactivos(paradigma_nombre: str = "") -> dict:
    """
    Solicita por teclado (input) los datos detallados del evento al usuario.
    Permite parametrizar comensales, corte de carne preferido y presupuesto máximo.
    """
    tit = f"MODO INTERACTIVO{f' - PARADIGMA {paradigma_nombre.upper()}' if paradigma_nombre else ''}"
    print("\n" + "═" * 70)
    print(f" {tit}")
    print("═" * 70)

    nombre = input("Nombre del evento [Default: Asado Familiar UTEM]: ").strip()
    if not nombre:
        nombre = "Asado Familiar UTEM"

    while True:
        try:
            raw_ad = input("Cantidad de adultos comensales [ej. 10]: ").strip()
            adultos = int(raw_ad) if raw_ad else 10
            if adultos >= 0:
                break
            print("Debe ingresar un valor mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    while True:
        try:
            raw_ni = input("Cantidad de niños comensales [ej. 4]: ").strip()
            ninos = int(raw_ni) if raw_ni else 4
            if ninos >= 0:
                break
            print("Debe ingresar un valor mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    while True:
        try:
            raw_veg = input("Cantidad de comensales vegetarianos [ej. 2]: ").strip()
            vegetarianos = int(raw_veg) if raw_veg else 2
            if vegetarianos >= 0:
                break
            print("Debe ingresar un valor mayor o igual a 0.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    while True:
        try:
            raw_pres = input("Presupuesto máximo en CLP [ej. 120000]: ").strip()
            presupuesto = float(raw_pres) if raw_pres else 120000.0
            if presupuesto > 0:
                break
            print("El presupuesto debe ser un monto positivo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número válido.")

    print("\nSeleccione el corte vacuno preferido:")
    print("  1. Lomo Vetado Vacuno ($14.990/kg - Stock en bodega: 3.0 kg)")
    print("  2. Sobrecostilla Vacuno ($9.990/kg - Stock en bodega: 15.0 kg)")
    opc = input("Opción [1 o 2, Default: 1]: ").strip()
    corte_id = "prod_02" if opc == "2" else "prod_01"

    print("═" * 70 + "\n")

    return {
        "nombre_evento": nombre,
        "comensales": {
            "adultos": adultos,
            "ninos": ninos,
            "vegetarianos": vegetarianos
        },
        "preferencias": {
            "incluir_alcohol": False,
            "tipo_corte_preferido": corte_id
        },
        "presupuesto_maximo": presupuesto
    }


def generar_evento_automatico(total_personas: int, presupuesto: float = None) -> dict:
    """
    MODALIDAD AUTOMÁTICA:
    Arma un evento coherente y parametrizado automáticamente solo con el total de personas
    (ej: 'Hazme un carrito para 10 personas').
    Distribuye los comensales considerando una composición típica y presupuesto sugerido.
    """
    if total_personas <= 0:
        total_personas = 10

    # Estimación automática: 80% adultos, 20% niños (o mínimo 1 si total >= 5)
    if total_personas >= 5:
        ninos = max(1, int(round(total_personas * 0.20)))
        adultos = total_personas - ninos
    else:
        adultos = total_personas
        ninos = 0
    
    vegetarianos = 0  # Por defecto en modo automático básico

    if presupuesto is None or presupuesto <= 0:
        # Estimación de presupuesto base ($7.500 CLP por persona)
        presupuesto = float(total_personas * 7500)

    return {
        "nombre_evento": f"Asado Exprés Automático ({total_personas} personas)",
        "comensales": {
            "adultos": adultos,
            "ninos": ninos,
            "vegetarianos": vegetarianos
        },
        "preferencias": {
            "incluir_alcohol": False,
            "tipo_corte_preferido": "prod_01"  # Prioriza corte premium para probar quiebre de stock
        },
        "presupuesto_maximo": presupuesto
    }
