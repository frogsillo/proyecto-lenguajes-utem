"""
MÓDULO DE MODELOS DE DOMINIO - PARADIGMA ORIENTADO A OBJETOS (POO)
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

CONCEPTOS CLAVE DE POO APLICADOS:
1. Encapsulamiento: Los atributos del producto y del carrito se protegen;
   las modificaciones de stock se realizan mediante métodos internos.
2. Abstracción: Modelado de entidades del mundo real (Producto, Item, Carrito).
3. Polimorfismo y Patrón Strategy: La clase abstracta ReglaDescuento define una interfaz
   que implementa ReglaComboParrillero, permitiendo extender nuevas promociones sin
   modificar la clase Carrito (Principio Open/Closed de SOLID).
"""

from abc import ABC, abstractmethod
from typing import List, Optional, Tuple


class Producto:
    """
    Representa una entidad de catálogo en la tienda de e-commerce.
    Encapsula el stock y valida las operaciones de consumo de inventario.
    """
    def __init__(self, id_prod: str, nombre: str, categoria: str, precio: float, 
                 unidad: str, stock: float, sustituto_id: Optional[str] = None):
        self.id = id_prod
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.unidad = unidad
        self._stock = float(stock)  # Atributo protegido (encapsulamiento)
        self.sustituto_id = sustituto_id

    @property
    def stock(self) -> float:
        """Getter para consultar el stock disponible sin permitir mutación directa arbitraria."""
        return self._stock

    def tiene_stock_suficiente(self, cantidad_requerida: float) -> bool:
        """Verifica si la bodega puede satisfacer la demanda solicitada."""
        return self._stock >= cantidad_requerida

    def consumir_stock(self, cantidad: float) -> float:
        """
        Reduce el stock físico de forma segura.
        Si la cantidad solicitada supera el stock disponible, consume todo lo que queda
        y retorna la cantidad efectivamente consumida.
        """
        if cantidad <= 0:
            return 0.0

        if self._stock >= cantidad:
            self._stock = round(self._stock - cantidad, 2)
            return cantidad
        else:
            consumido = self._stock
            self._stock = 0.0
            return consumido

    def __repr__(self) -> str:
        return f"<Producto {self.nombre} (Stock: {self._stock} {self.unidad})>"


class ItemCarrito:
    """
    Representa una línea de compra en el carrito, asociando un Producto con una cantidad adquirida.
    """
    def __init__(self, producto: Producto, cantidad: float, nota: Optional[str] = None):
        self.producto = producto
        self.cantidad = round(cantidad, 2)
        self.nota = nota

    def calcular_subtotal(self) -> float:
        """Calcula el subtotal monetario de esta línea de producto."""
        return round(self.cantidad * self.producto.precio, 2)

    def to_dict(self) -> dict:
        """Exporta la línea a un diccionario estandarizado para el visualizador común."""
        return {
            "id": self.producto.id,
            "nombre": self.producto.nombre,
            "cantidad": self.cantidad,
            "unidad": self.producto.unidad,
            "precio_unitario": self.producto.precio,
            "subtotal": self.calcular_subtotal(),
            "nota": self.nota
        }


class ReglaDescuento(ABC):
    """
    Clase Base Abstracta (Interfaz) para el cálculo de descuentos.
    Aplica el patrón de diseño de comportamiento 'Strategy' (Estrategia).
    """
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_descuento(self, carrito: "Carrito") -> Tuple[float, str]:
        """
        Método polimórfico que debe implementar cada regla concreta.
        Retorna: (monto_descuento, detalle_explicativo).
        """
        pass


class ReglaComboParrillero(ReglaDescuento):
    """
    Estrategia concreta de promoción:
    Si el carrito contiene simultáneamente productos cárnicos, carbón y sal,
    aplica un 10% de descuento sobre el subtotal de dichos productos.
    """
    def __init__(self, porcentaje: float = 0.10):
        super().__init__("Combo Parrillero (10% en Carne + Carbón + Sal)")
        self.porcentaje = porcentaje

    def calcular_descuento(self, carrito: "Carrito") -> Tuple[float, str]:
        tiene_carne = False
        tiene_carbon = False
        tiene_sal = False
        subtotal_afecto = 0.0

        for item in carrito.items:
            # Identificación de elementos del combo mediante sus categorías y SKUs
            if item.producto.categoria == "carnico":
                tiene_carne = True
                subtotal_afecto += item.calcular_subtotal()
            elif item.producto.id == "prod_06":  # Carbón
                tiene_carbon = True
                subtotal_afecto += item.calcular_subtotal()
            elif item.producto.id == "prod_07":  # Sal
                tiene_sal = True
                subtotal_afecto += item.calcular_subtotal()

        # Si se cumplen las 3 condiciones de la promoción
        if tiene_carne and tiene_carbon and tiene_sal:
            monto_descuento = float(round(subtotal_afecto * self.porcentaje))
            return monto_descuento, self.nombre

        return 0.0, ""


class Carrito:
    """
    Entidad agregada raíz que encapsula la lista de ítems y las reglas comerciales.
    """
    def __init__(self, nombre_evento: str):
        self.nombre_evento = nombre_evento
        self.items: List[ItemCarrito] = []
        self.reglas_descuento: List[ReglaDescuento] = []

    def agregar_item(self, producto: Producto, cantidad: float, nota: Optional[str] = None) -> None:
        """Agrega un producto al carrito encapsulando la creación de la entidad ItemCarrito."""
        if cantidad > 0:
            item = ItemCarrito(producto, cantidad, nota)
            self.items.append(item)

    def registrar_regla_descuento(self, regla: ReglaDescuento) -> None:
        """Registra una estrategia de descuento (Inyección de dependencias / Strategy)."""
        self.reglas_descuento.append(regla)

    def calcular_subtotal_neto(self) -> float:
        """Suma polimórfica de subtotales de todos los ítems en el carrito."""
        return round(sum(item.calcular_subtotal() for item in self.items), 2)

    def aplicar_descuentos(self) -> Tuple[float, str]:
        """Ejecuta todas las reglas registradas y acumula los descuentos."""
        descuento_acumulado = 0.0
        detalles = []

        for regla in self.reglas_descuento:
            monto, detalle = regla.calcular_descuento(self)
            if monto > 0:
                descuento_acumulado += monto
                detalles.append(detalle)

        descuento_acumulado = round(descuento_acumulado, 2)
        detalle_str = " | ".join(detalles) if detalles else ""
        return descuento_acumulado, detalle_str

    def generar_boleta(self) -> dict:
        """Construye el reporte consolidado listo para ser presentado por el visualizador."""
        subtotal = self.calcular_subtotal_neto()
        descuento, detalle_desc = self.aplicar_descuentos()
        total = float(round(subtotal - descuento))

        return {
            "evento": self.nombre_evento,
            "items": [item.to_dict() for item in self.items],
            "subtotal": subtotal,
            "descuento": descuento,
            "detalle_descuento": detalle_desc,
            "total": total
        }
