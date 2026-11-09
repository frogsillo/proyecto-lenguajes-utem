# Bitácora de Interacción con IA y Análisis Técnico: Paradigma Orientado a Objetos (POO)
**Asignatura:** Lenguajes de Programación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Proyecto:** Carrito Evento Especial — Asado Parrillero  
**Entrega:** Etapa 2 — Versión Orientada a Objetos  

---

## 1. Registro Metodológico de Prompts (Pauta UTEM)

### 1.1. Prompts Iniciales (Abstracción y Modelado de Clases)
* **Prompt 1 (Identificación de Entidades y Responsabilidades):**  
  > *"Actúa como arquitecto de software. A partir del problema del Carrito Evento Especial (Asado), identifica las entidades del dominio para modelarlas bajo el paradigma orientado a objetos en Python. Define qué atributos y métodos pertenecen a `Producto`, `ItemCarrito` y `Carrito` respetando el Principio de Responsabilidad Única (SRP)."*
* **Prompt 2 (Encapsulamiento del Inventario):**  
  > *"Diseña la clase `Producto` de modo que el stock no sea accesible para modificación arbitraria desde el exterior. Implementa un método `consumir_stock(cantidad: float)` que descuente únicamente lo que hay disponible y devuelva la cantidad efectivamente despachada, permitiendo detectar quiebres de inventario."*
* **Prompt 3 (Modelado de Ítems del Carrito):**  
  > *"Crea la clase `ItemCarrito` que asocie una instancia de `Producto` con una cantidad adquirida y un atributo opcional de notas. Implementa un método `calcular_subtotal()` dentro de la clase para evitar cálculos externos."*

### 1.2. Prompts para Completar el Código (Patrón Strategy y Reglas de Negocio)
* **Prompt 4 (Polimorfismo para Promociones y Descuentos):**  
  > *"Aplica el patrón de diseño de comportamiento 'Strategy' en Python utilizando el módulo `abc`. Crea la clase abstracta `ReglaDescuento` con el método abstracto `calcular_descuento(carrito: Carrito) -> Tuple[float, str]` para desacoplar las promociones de la clase Carrito."*
* **Prompt 5 (Implementación Concreta del Combo Parrillero):**  
  > *"Crea la subclase `ReglaComboParrillero(ReglaDescuento)` que evalúe si el carrito contiene productos de categoría 'carnico', carbón y sal. Debe calcular el 10% de descuento exclusivamente sobre la suma de los subtotales de dichos productos."*
* **Prompt 6 (Servicio de Orquestación del Evento):**  
  > *"Crea la clase de servicio `PlanificadorAsadoPOO` con un método de fábrica `desde_archivos(ruta_cat, ruta_eve)` que transforme los datos crudos del JSON en un catálogo de objetos `Producto`, instancie el `Carrito`, registre la regla de descuento y calcule las cantidades según el número de personas."*

### 1.3. Prompts Finales (Detección de Discrepancias y Paridad)
* **Prompt 7 (Estandarización del Método `generar_boleta`):**  
  > *"Implementa en la clase `Carrito` el método `generar_boleta() -> dict` para que serialice los objetos internos en la estructura canónica requerida por el módulo `visualizador.py`."*
* **Prompt 8 (Resolución de Discrepancia de Categorías en Promociones):**  
  > *"Al comparar la ejecución de POO con la versión imperativa, POO arrojó un descuento mayor (\$7.943 CLP vs \$6.446 CLP). Analiza si los chorizos artesanales deben incluirse en la categoría 'carnico' del combo y cómo afecta esto a la coherencia de negocio."*
* **Prompt 9 (Refactorización y Verificación de Tipado):**  
  > *"Agrega type hints (`typing.List`, `Tuple`, `Optional`) y docstrings pedagógicos a cada método para facilitar la explicación y defensa del código en la presentación final."*

---

## 2. Errores Identificados en la Generación por IA y Correcciones Realizadas

1. **Ambigüedad de Categoría en Reglas de Promoción (Lógica de Dominio):**  
   * *Problema de la IA:* Al implementar `ReglaComboParrillero`, la IA evaluó productos cárnicos filtrando únicamente por IDs específicos (`prod_01` y `prod_02`), ignorando que los embutidos (`prod_03 Chorizo`) pertenecían a la misma categoría semántica (`carnico`). Esto provocó una discordancia inicial con la especificación de negocio del combo parrillero.  
   * *Corrección aplicada:* Se refactorizó la regla para evaluar `item.producto.categoria == "carnico"`, aprovechando el polimorfismo del objeto y alineando la regla en ambas versiones a \$91.866 CLP.
2. **Dependencia circular y acoplamiento (Arquitectura de Clases):**  
   * *Problema de la IA:* En la primera iteración, la clase `ReglaDescuento` requería importar la clase `Carrito`, mientras que `Carrito` importaba `ReglaDescuento`, generando un error de `ImportError: cannot import name 'Carrito' from partially initialized module` en Python.  
   * *Corrección aplicada:* Se utilizó anotación de tipos como cadena (`"Carrito"`) y se modularizó la jerarquía dentro de `modelos.py` antes de la definición de `Carrito`.
3. **Fuga de Abstracción en Modificación de Stock:**  
   * *Problema de la IA:* El método `planificar_carnes` accedía directamente a `corte._stock -= cantidad`.  
   * *Corrección aplicada:* Se reforzó el principio de encapsulamiento exigiendo el uso estricto de `corte.consumir_stock(cantidad)`.

---

## 3. Explicación Conceptual y Defensa del Paradigma Orientado a Objetos

> **En palabras del estudiante (para la defensa oral ante el profesor):**  
> *"El paradigma orientado a objetos estructura el sistema como un conjunto de componentes colaborativos que encapsulan estado y comportamiento. En nuestra solución, la clase `Producto` protege el stock bajo el atributo `_stock`, garantizando que ninguna operación externa altere el inventario sin pasar por el método de control `consumir_stock`. Además, para resolver las promociones aplicamos el patrón Strategy: la clase `Carrito` no contiene sentencias condicionales 'hardcodeadas' para calcular descuentos; en su lugar, delega esa responsabilidad de forma polimórfica a cualquier objeto que implemente la interfaz `ReglaDescuento`. Esto respeta el principio Open/Closed (abierto a extensión, cerrado a modificación), lo que permite que una tienda agregue nuevas campañas de marketing simplemente creando una nueva clase de regla sin alterar el núcleo del carrito."*

---

## 4. Referencias Bibliográficas (Norma APA 7ª Edición)

* Gamma, E., Helm, R., Johnson, R., y Vlissides, J. (1994). *Design patterns: elements of reusable object-oriented software*. Addison-Wesley.
* Martin, R. C. (2018). *Clean architecture: a craftsman's guide to software structure and design*. Prentice Hall.
* Weisfeld, M. (2020). *The object-oriented thought process* (5a ed.). Addison-Wesley Professional.
