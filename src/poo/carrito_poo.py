"""
MÓDULO DE ORQUESTACIÓN Y EJECUCIÓN - PARADIGMA ORIENTADO A OBJETOS (POO)
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

RESPONSABILIDAD DE ESTE ARCHIVO:
Transformar los datos estructurados (JSON) en un grafo de objetos en memoria,
orquestar los mensajes entre entidades (Producto, Item, Carrito) y aplicar
las reglas de negocio y promociones a través del patrón Strategy.
Incluye optimización activa por restricción presupuestaria.
"""

import os
import sys
import json
import math
from typing import Dict, Tuple, Union, Optional

# Agregamos la ruta base para imports modulares
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.poo.modelos import Producto, Carrito, ReglaComboParrillero
from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos


class PlanificadorAsadoPOO:
    """
    Servicio de Dominio encargado de coordinar la lógica de negocio del evento
    utilizando únicamente interacciones entre objetos.
    """
    def __init__(self, catalogo: Dict[str, Producto], datos_evento: dict, ruta_catalogo: str = None):
        self.catalogo = catalogo
        self.evento = datos_evento
        self.ruta_catalogo = ruta_catalogo
        self.carrito = Carrito(datos_evento["nombre_evento"])
        
        # Inyección de la estrategia de promoción (Polimorfismo / Strategy)
        self.carrito.registrar_regla_descuento(ReglaComboParrillero(porcentaje=0.10))

    @classmethod
    def construir_mapa_productos(cls, ruta_catalogo: str) -> Dict[str, Producto]:
        """Carga el catálogo JSON y lo transforma en un diccionario de entidades Producto."""
        with open(ruta_catalogo, "r", encoding="utf-8") as f_cat:
            datos_cat = json.load(f_cat)

        mapa_productos: Dict[str, Producto] = {}
        for item in datos_cat["productos"]:
            prod = Producto(
                id_prod=item["id"],
                nombre=item["nombre"],
                categoria=item["categoria"],
                precio=item["precio"],
                unidad=item["unidad"],
                stock=item["stock"],
                sustituto_id=item.get("sustituto_id")
            )
            mapa_productos[prod.id] = prod
        return mapa_productos

    @classmethod
    def desde_fuentes(
        cls, 
        ruta_catalogo: str, 
        evento_input: Union[str, dict, None] = None, 
        interactivo: bool = False
    ) -> "PlanificadorAsadoPOO":
        """Método de fábrica (Factory Method) para construir el servicio desde JSON o entrada interactiva."""
        mapa = cls.construir_mapa_productos(ruta_catalogo)

        if interactivo:
            datos_eve = solicitar_datos_interactivos("Orientado a Objetos")
        elif isinstance(evento_input, dict):
            datos_eve = evento_input
        elif isinstance(evento_input, str):
            with open(evento_input, "r", encoding="utf-8") as f_eve:
                datos_eve = json.load(f_eve)
        else:
            ruta_def = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
            with open(ruta_def, "r", encoding="utf-8") as f_eve:
                datos_eve = json.load(f_eve)

        return cls(mapa, datos_eve, ruta_catalogo)

    def planificar_carnes(self, adultos: int, ninos: int, id_corte_forzado: Optional[str] = None) -> float:
        """Calcula la demanda de carne y ejecuta la regla de quiebre de stock con sustitución."""
        kilos_necesarios = round((adultos * 0.35) + (ninos * 0.15), 2)
        if kilos_necesarios <= 0:
            return 0.0

        id_corte = id_corte_forzado or self.evento["preferencias"].get("tipo_corte_preferido", "prod_01")
        corte_preferido = self.catalogo[id_corte]

        # Consumo seguro delegando al método del objeto
        kilos_despachados = corte_preferido.consumir_stock(kilos_necesarios)

        if kilos_despachados < kilos_necesarios:
            if kilos_despachados > 0:
                self.carrito.agregar_item(
                    producto=corte_preferido,
                    cantidad=kilos_despachados,
                    nota=f"Stock agotado. Se utilizaron los {kilos_despachados} kg disponibles."
                )
            
            # Buscamos el sustituto
            kilos_pendientes = round(kilos_necesarios - kilos_despachados, 2)
            sustituto = self.catalogo.get(corte_preferido.sustituto_id)
            if sustituto:
                sustituto.consumir_stock(kilos_pendientes)
                self.carrito.agregar_item(
                    producto=sustituto,
                    cantidad=kilos_pendientes,
                    nota=f"Sustituto activado por falta de stock de {corte_preferido.nombre}."
                )
        else:
            self.carrito.agregar_item(
                producto=corte_preferido,
                cantidad=kilos_necesarios,
                nota=None
            )

        return kilos_necesarios

    def planificar_choripanes(self, adultos: int, ninos: int, packs_forzados: Optional[int] = None) -> None:
        """Calcula packs de chorizo delegando al objeto producto correspondiente."""
        carnivoros = adultos + ninos
        if carnivoros > 0:
            packs = math.ceil(carnivoros / 5.0) if packs_forzados is None else packs_forzados
            prod = self.catalogo["prod_03"]
            prod.consumir_stock(packs)
            self.carrito.agregar_item(
                producto=prod,
                cantidad=packs,
                nota=f"Calculado para {carnivoros} choripanes (packs de 5 u.)."
            )

    def planificar_vegetarianos(self, vegetarianos: int) -> None:
        """Asigna raciones vegetarianas a través de los objetos del catálogo."""
        if vegetarianos > 0:
            prod_hamb = self.catalogo["prod_04"]
            prod_pim = self.catalogo["prod_05"]

            prod_hamb.consumir_stock(vegetarianos)
            self.carrito.agregar_item(
                producto=prod_hamb,
                cantidad=vegetarianos,
                nota=f"Ración especial para {vegetarianos} comensal(es) vegetariano(s)."
            )

            prod_pim.consumir_stock(vegetarianos)
            self.carrito.agregar_item(
                producto=prod_pim,
                cantidad=vegetarianos,
                nota=None
            )

    def planificar_insumos(self, kilos_carne: float, total_personas: int) -> None:
        """Asigna carbón y sal según reglas de volumen."""
        if kilos_carne > 0:
            bolsas_carbon = math.ceil(kilos_carne / 3.0)
            prod_carbon = self.catalogo["prod_06"]
            prod_carbon.consumir_stock(bolsas_carbon)
            self.carrito.agregar_item(
                producto=prod_carbon,
                cantidad=bolsas_carbon,
                nota=f"Calculado según {kilos_carne} kg de carne (1 bolsa cada 3 kg)."
            )

        if total_personas > 5:
            prod_sal = self.catalogo["prod_07"]
            prod_sal.consumir_stock(1)
            self.carrito.agregar_item(
                producto=prod_sal,
                cantidad=1,
                nota="Requerido para eventos mayores a 5 personas."
            )

    def planificar_bebidas(self, total_personas: int, botellas_forzadas: Optional[int] = None) -> None:
        """Calcula litros y botellas de bebida requeridas."""
        if total_personas > 0:
            litros = total_personas * 0.5
            botellas = math.ceil(litros / 2.5) if botellas_forzadas is None else botellas_forzadas
            prod_bebida = self.catalogo["prod_08"]
            prod_bebida.consumir_stock(botellas)
            self.carrito.agregar_item(
                producto=prod_bebida,
                cantidad=botellas,
                nota=f"Calculado para {litros}L totales (0.5L por comensal)."
            )

    def simular_plan(self, corte_id: str, botellas: Optional[int] = None, packs_chori: Optional[int] = None) -> Tuple[dict, 'Carrito']:
        """Simula una variante de planificación reconstruyendo el grafo de objetos de forma aislada."""
        mapa_aislado = self.construir_mapa_productos(self.ruta_catalogo)
        carrito_sim = Carrito(self.evento["nombre_evento"])
        carrito_sim.registrar_regla_descuento(ReglaComboParrillero(porcentaje=0.10))

        comensales = self.evento["comensales"]
        adultos, ninos, veg = comensales["adultos"], comensales["ninos"], comensales["vegetarianos"]
        tot = adultos + ninos + veg

        # Carne
        kilos_nec = round((adultos * 0.35) + (ninos * 0.15), 2)
        if kilos_nec > 0:
            corte = mapa_aislado[corte_id]
            desp = corte.consumir_stock(kilos_nec)
            if desp < kilos_nec:
                if desp > 0:
                    carrito_sim.agregar_item(corte, desp, f"Stock agotado. Se utilizaron los {desp} kg disponibles.")
                pend = round(kilos_nec - desp, 2)
                sust = mapa_aislado.get(corte.sustituto_id)
                if sust:
                    sust.consumir_stock(pend)
                    carrito_sim.agregar_item(sust, pend, f"Sustituto activado por falta de stock de {corte.nombre}.")
            else:
                carrito_sim.agregar_item(corte, kilos_nec, None)

        # Chorizos
        if (adultos + ninos) > 0:
            p_chori = math.ceil((adultos + ninos) / 5.0) if packs_chori is None else packs_chori
            prod_c = mapa_aislado["prod_03"]
            prod_c.consumir_stock(p_chori)
            carrito_sim.agregar_item(prod_c, p_chori, f"Calculado para {adultos + ninos} choripanes (packs de 5 u.).")

        # Vegetariano
        if veg > 0:
            h = mapa_aislado["prod_04"]
            p = mapa_aislado["prod_05"]
            h.consumir_stock(veg)
            p.consumir_stock(veg)
            carrito_sim.agregar_item(h, veg, f"Ración especial para {veg} comensal(es) vegetariano(s).")
            carrito_sim.agregar_item(p, veg, None)

        # Insumos
        if kilos_nec > 0:
            b_carb = math.ceil(kilos_nec / 3.0)
            carb = mapa_aislado["prod_06"]
            carb.consumir_stock(b_carb)
            carrito_sim.agregar_item(carb, b_carb, f"Calculado según {kilos_nec} kg de carne (1 bolsa cada 3 kg).")

        if tot > 5:
            sal = mapa_aislado["prod_07"]
            sal.consumir_stock(1)
            carrito_sim.agregar_item(sal, 1, "Requerido para eventos mayores a 5 personas.")

        # Bebidas
        if tot > 0:
            litros = tot * 0.5
            b_beb = math.ceil(litros / 2.5) if botellas is None else botellas
            beb = mapa_aislado["prod_08"]
            beb.consumir_stock(b_beb)
            carrito_sim.agregar_item(beb, b_beb, f"Calculado para {litros}L totales (0.5L por comensal).")

        return carrito_sim.generar_boleta()

    def procesar(self) -> dict:
        """Punto de entrada que orquesta la ejecución completa y aplica gestión activa de presupuesto."""
        comensales = self.evento["comensales"]
        adultos, ninos, veg = comensales["adultos"], comensales["ninos"], comensales["vegetarianos"]
        tot = adultos + ninos + veg
        presupuesto_max = self.evento.get("presupuesto_maximo")
        id_corte_solicitado = self.evento["preferencias"].get("tipo_corte_preferido", "prod_01")

        kilos_carne = self.planificar_carnes(adultos, ninos)
        self.planificar_choripanes(adultos, ninos)
        self.planificar_vegetarianos(veg)
        self.planificar_insumos(kilos_carne, tot)
        self.planificar_bebidas(tot)

        boleta = self.carrito.generar_boleta()
        total_pagar = boleta["total"]
        ajustes_presupuesto = []

        # ---------------------------------------------------------------------
        # REGLA DE NEGOCIO AVANZADA: GESTIÓN ACTIVA DE PRESUPUESTO EN POO
        # ---------------------------------------------------------------------
        if presupuesto_max and total_pagar > presupuesto_max and self.ruta_catalogo:
            # Intento 1: Si pidió corte premium (prod_01), degradar a Sobrecostilla (prod_02)
            if id_corte_solicitado == "prod_01":
                boleta_t = self.simular_plan("prod_02")
                if boleta_t["total"] < total_pagar:
                    boleta = boleta_t
                    total_pagar = boleta["total"]
                    ajustes_presupuesto.append("Se degradó el corte de Lomo Vetado ($14.990) a Sobrecostilla ($9.990) para reducir costos.")

            # Intento 2: Reducir bebidas a 1 botella mínima
            if total_pagar > presupuesto_max and tot > 0:
                litros = tot * 0.5
                if math.ceil(litros / 2.5) > 1:
                    boleta_t = self.simular_plan(
                        corte_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                        botellas=1
                    )
                    if boleta_t["total"] < total_pagar:
                        boleta = boleta_t
                        total_pagar = boleta["total"]
                        ajustes_presupuesto.append("Se redujeron las bebidas a 1 botella básica para acercarse al presupuesto.")

            # Intento 3: Reducir chorizos a 1 pack esencial
            if total_pagar > presupuesto_max and (adultos + ninos) > 0:
                if math.ceil((adultos + ninos) / 5.0) > 1:
                    boleta_t = self.simular_plan(
                        corte_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                        botellas=1,
                        packs_chori=1
                    )
                    if boleta_t["total"] < total_pagar:
                        boleta = boleta_t
                        total_pagar = boleta["total"]
                        ajustes_presupuesto.append("Se redujo el embutido a 1 pack de chorizos para ajustar el gasto.")

        boleta["presupuesto_maximo"] = presupuesto_max
        boleta["ajustes_presupuesto"] = ajustes_presupuesto
        boleta["alerta_presupuesto"] = None
        if presupuesto_max and total_pagar > presupuesto_max:
            boleta["alerta_presupuesto"] = f"Incluso con ajustes mínimos, el total ({formato_moneda(total_pagar)}) excede el presupuesto ({formato_moneda(presupuesto_max)})."

        return boleta


def procesar_carrito_poo(
    ruta_catalogo: str, 
    evento_input: Union[str, dict, None] = None, 
    interactivo: bool = False
) -> dict:
    """Función interfaz para pruebas y ejecución unificada."""
    planificador = PlanificadorAsadoPOO.desde_fuentes(ruta_catalogo, evento_input, interactivo)
    return planificador.procesar()


if __name__ == "__main__":
    ruta_cat = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
    if not os.path.exists(ruta_cat):
        ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

    print("\n" + "═" * 68)
    print(" SISTEMA CARRITO EVENTO ESPECIAL — PARADIGMA ORIENTADO A OBJETOS")
    print("═" * 68)
    print(" [1] Modo Automático (Dataset oficial de prueba UTEM)")
    print(" [2] Modo Interactivo (Ingresar datos y presupuesto por teclado)")
    print("═" * 68)
    opc = input("Seleccione una opción [1 o 2, Default: 1]: ").strip()

    if opc == "2":
        boleta = procesar_carrito_poo(ruta_cat, interactivo=True)
    else:
        ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        boleta = procesar_carrito_poo(ruta_cat, ruta_eve)

    imprimir_resumen_carrito(boleta, "Orientado a Objetos")

    if boleta.get("ajustes_presupuesto"):
        print("\n🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
        for aj in boleta["ajustes_presupuesto"]:
            print(f"   • {aj}")
        print()

    if boleta.get("alerta_presupuesto"):
        print(f"⚠️  {boleta['alerta_presupuesto']}\n")
