"""
SUITE DE PRUEBAS DE EQUIVALENCIA MULTIPARADIGMA
Asignatura: Lenguajes de Programación (UTEM)
Tarea 1: Carrito Evento Especial (Asado Parrillero)

OBJETIVO CRÍTICO (PAUTA DE EVALUACIÓN):
Demostrar de forma automatizada que las tres implementaciones:
  1. Imperativa (src/imperativo/carrito_imperativo.py)
  2. Orientada a Objetos (src/poo/carrito_poo.py)
  3. Funcional (src/funcional/carrito_funcional.py)
producen EXACTAMENTE el mismo comportamiento, desglose de ítems, subtotales,
descuentos, total final y optimizaciones de presupuesto ante las mismas entradas.
"""

import os
import sys
import unittest

# Configuración de rutas
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.imperativo.carrito_imperativo import procesar_carrito_imperativo
from src.poo.carrito_poo import procesar_carrito_poo
from src.funcional.carrito_funcional import procesar_carrito_funcional


class TestEquivalenciaMultiparadigma(unittest.TestCase):
    """
    Test suite formal que valida la interoperabilidad y paridad numérica
    entre los tres paradigmas de programación requeridos por la UTEM.
    """

    @classmethod
    def setUpClass(cls):
        """Carga y procesa las 3 versiones una sola vez para las aserciones."""
        cls.ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")
        cls.ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")

        cls.boleta_imperativa = procesar_carrito_imperativo(cls.ruta_cat, cls.ruta_eve)
        cls.boleta_poo = procesar_carrito_poo(cls.ruta_cat, cls.ruta_eve)
        cls.boleta_funcional = procesar_carrito_funcional(cls.ruta_cat, cls.ruta_eve)

    def test_paridad_subtotal_neto(self):
        """Verifica que el subtotal antes de descuentos sea idéntico en las 3 versiones."""
        sub_imp = self.boleta_imperativa["subtotal"]
        sub_poo = self.boleta_poo["subtotal"]
        sub_fun = self.boleta_funcional["subtotal"]

        self.assertEqual(sub_imp, sub_poo, f"Discrepancia Imperativo ({sub_imp}) vs POO ({sub_poo})")
        self.assertEqual(sub_poo, sub_fun, f"Discrepancia POO ({sub_poo}) vs Funcional ({sub_fun})")
        self.assertEqual(sub_imp, 99809.0, f"El subtotal neto esperado es 99809.0, obtenido {sub_imp}")

    def test_paridad_descuento_promocion(self):
        """Verifica que el descuento por 'Combo Parrillero' sea idéntico en las 3 versiones."""
        desc_imp = self.boleta_imperativa["descuento"]
        desc_poo = self.boleta_poo["descuento"]
        desc_fun = self.boleta_funcional["descuento"]

        self.assertEqual(desc_imp, desc_poo, f"Discrepancia en descuento: Imperativo ({desc_imp}) vs POO ({desc_poo})")
        self.assertEqual(desc_poo, desc_fun, f"Discrepancia en descuento: POO ({desc_poo}) vs Funcional ({desc_fun})")
        self.assertEqual(desc_imp, 7943.0, f"El descuento esperado es 7943.0, obtenido {desc_imp}")

    def test_paridad_total_final(self):
        """Verifica que el total final a pagar sea exactamente idéntico ($91.866 CLP)."""
        tot_imp = self.boleta_imperativa["total"]
        tot_poo = self.boleta_poo["total"]
        tot_fun = self.boleta_funcional["total"]

        self.assertEqual(tot_imp, tot_poo, f"Total disímil entre Imperativo ({tot_imp}) y POO ({tot_poo})")
        self.assertEqual(tot_poo, tot_fun, f"Total disímil entre POO ({tot_poo}) y Funcional ({tot_fun})")
        self.assertEqual(tot_imp, 91866.0, f"El total a pagar esperado es 91866.0, obtenido {tot_imp}")

    def test_paridad_cantidad_de_items(self):
        """Verifica que los tres paradigmas generen exactamente las mismas 8 líneas de compra."""
        len_imp = len(self.boleta_imperativa["items"])
        len_poo = len(self.boleta_poo["items"])
        len_fun = len(self.boleta_funcional["items"])

        self.assertEqual(len_imp, 8, "El carrito debe contener 8 ítems procesados.")
        self.assertEqual(len_imp, len_poo)
        self.assertEqual(len_poo, len_fun)

    def test_paridad_regla_sustitucion_stock(self):
        """Verifica que los tres paradigmas activen la sustitución de Lomo Vetado por Sobrecostilla."""
        for nombre_vers, boleta in [
            ("Imperativa", self.boleta_imperativa),
            ("POO", self.boleta_poo),
            ("Funcional", self.boleta_funcional)
        ]:
            item_lomo = next((it for it in boleta["items"] if it["id"] == "prod_01"), None)
            item_sobrecostilla = next((it for it in boleta["items"] if it["id"] == "prod_02"), None)

            self.assertIsNotNone(item_lomo, f"Falta Lomo Vetado en versión {nombre_vers}")
            self.assertEqual(item_lomo["cantidad"], 3.0, f"Lomo en {nombre_vers} debe consumir los 3.0 kg disponibles")

            self.assertIsNotNone(item_sobrecostilla, f"Falta sustituto Sobrecostilla en {nombre_vers}")
            self.assertEqual(item_sobrecostilla["cantidad"], 1.1, f"Sobrecostilla en {nombre_vers} debe cubrir 1.1 kg faltantes")

    def test_paridad_optimizacion_activa_presupuesto(self):
        """Verifica que los tres paradigmas apliquen la misma optimización activa ante restricción presupuestaria."""
        evento_ajustado = {
            "nombre_evento": "Asado Ajuste Presupuesto",
            "comensales": {"adultos": 5, "ninos": 2, "vegetarianos": 1},
            "preferencias": {
                "incluir_alcohol": False,
                "tipo_corte_preferido": "prod_01"
            },
            "presupuesto_maximo": 45000.0
        }
        b_imp = procesar_carrito_imperativo(self.ruta_cat, evento_input=evento_ajustado)
        b_poo = procesar_carrito_poo(self.ruta_cat, evento_input=evento_ajustado)
        b_fun = procesar_carrito_funcional(self.ruta_cat, evento_input=evento_ajustado)

        # Verificación de que los tres llegaron al mismo total ajustado ($42.104 CLP)
        self.assertEqual(b_imp["total"], b_poo["total"], "Discrepancia en ajuste de presupuesto: Imperativo vs POO")
        self.assertEqual(b_poo["total"], b_fun["total"], "Discrepancia en ajuste de presupuesto: POO vs Funcional")
        self.assertEqual(b_imp["total"], 42104.0, f"Esperado $42.104 CLP, obtenido {b_imp['total']}")
        
        # Verificación de que todos registraron ajustes
        self.assertTrue(len(b_imp["ajustes_presupuesto"]) > 0)
        self.assertEqual(len(b_imp["ajustes_presupuesto"]), len(b_poo["ajustes_presupuesto"]))
        self.assertEqual(len(b_poo["ajustes_presupuesto"]), len(b_fun["ajustes_presupuesto"]))


if __name__ == "__main__":
    print("\n" + "═" * 70)
    print(" EJECUTANDO SUITE DE PRUEBAS DE EQUIVALENCIA MULTIPARADIGMA (UTEM)")
    print("═" * 70 + "\n")
    unittest.main(verbosity=2)
