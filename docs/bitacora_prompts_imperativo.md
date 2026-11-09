# Bitácora de Interacción con IA y Análisis Técnico: Paradigma Imperativo
**Asignatura:** Lenguajes de Programación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Proyecto:** Carrito Evento Especial — Asado Parrillero  
**Entrega:** Etapa 2 — Versión Imperativa  

---

## 1. Registro Metodológico de Prompts (Pauta UTEM)

Para cumplir con la pauta de evaluación, se documenta la secuencia evolutiva de interacción con el asistente de IA dividida en tres etapas cronológicas:

### 1.1. Prompts Iniciales (Diseño y Modelado)
* **Prompt 1 (Definición de Arquitectura):**  
  > *"Actúa como arquitecto de software. Necesito diseñar un carrito de compras en Python para un evento especial ('Asado') utilizando un enfoque 100% imperativo. Los datos deben provenir de archivos JSON externos (`catalogo_tienda.json` y `evento_asado.json`) para desacoplar datos de la lógica. Explica cómo estructurarías el flujo secuencial sin usar clases ni programación funcional."*
* **Prompt 2 (Estructura de Datos Mutable):**  
  > *"¿Cómo modelamos el inventario de la tienda para que el stock se modifique en caliente a medida que se procesan los cortes de carne y abarrotes? Necesito que el diccionario del catálogo sea directamente mutable durante el bucle de procesamiento."*
* **Prompt 3 (Especificación de Comensales):**  
  > *"Define las fórmulas matemáticas lineales para calcular la demanda de carne vacuna (350g por adulto, 150g por niño), chorizos (1 por comensal carnívoro agrupado en packs de 5), menú vegetariano, carbón (1 bolsa cada 3 kg de carne) y bebidas (0.5L por persona), utilizando asignación directa de variables escalares."*

### 1.2. Prompts para Completar el Código (Reglas de Negocio Complejas)
* **Prompt 4 (Algoritmo de Quiebre de Stock y Sustitución):**  
  > *"Genera el bloque condicional `if/else` imperativo para manejar el quiebre de stock del corte preferido (`Lomo Vetado`). Si el evento requiere 4.1 kg y solo hay 3.0 kg en bodega, debe agotar los 3.0 kg, modificar el stock a 0.0, buscar el `sustituto_id` (`Sobrecostilla`) y consumir los 1.1 kg faltantes al precio del sustituto."*
* **Prompt 5 (Regla de Descuento 'Combo Parrillero'):**  
  > *"Escribe la lógica imperativa usando banderas booleanas (`tiene_carne`, `tiene_carbon`, `tiene_sal`) y un acumulador de subtotales para aplicar un 10% de descuento exclusivamente sobre la suma de esos tres productos si los tres están presentes en el carrito."*
* **Prompt 6 (Manejo de Unidades Discretas):**  
  > *"Asegura que los productos que se venden por unidades cerradas (packs de chorizos y botellas de bebida) utilicen redondeo hacia arriba con `math.ceil` en lugar de divisiones truncadas, actualizando el stock restante del catálogo."*

### 1.3. Prompts Finales (Refactorización y Estandarización)
* **Prompt 7 (Estandarización de Salida):**  
  > *"Ajusta el diccionario de retorno `boleta_final` para que contenga llaves idénticas (`evento`, `items`, `subtotal`, `descuento`, `detalle_descuento`, `total`) que permitan conectarse al formateador visual común sin discrepancias de tipos."*
* **Prompt 8 (Control de Precisión Flotante):**  
  > *"Aplica `round(..., 2)` en todas las operaciones aritméticas intermedias para evitar el arrastre de decimales espurios del estándar IEEE 754 de coma flotante en Python."*
* **Prompt 9 (Modularización Ejecutable):**  
  > *"Envuelve todo en una función principal `procesar_carrito_imperativo(ruta_cat, ruta_eve)` con bloque `if __name__ == '__main__':` para permitir pruebas unitarias y ejecución por consola."*

---

## 2. Errores Identificados en la Generación por IA y Correcciones Realizadas

Durante el proceso asistido con IA, se identificaron y corrigieron los siguientes defectos de software:

1. **Error de truncamiento en compras por pack (Lógica de Negocio):**  
   * *Problema de la IA:* Inicialmente, la IA calculó los packs de chorizos usando división entera (`14 // 5 = 2 packs`), lo que dejaba a 4 personas sin comer (solo 10 unidades para 14 comensales).  
   * *Corrección aplicada:* Se intervino el código sustituyéndolo por `math.ceil(comensales / 5.0)`, garantizando 3 packs (15 unidades) y cubriendo la demanda real.
2. **Inconsistencia de tipos en mutación de stock (Tipado dinámico):**  
   * *Problema de la IA:* Al restar flotantes (`4.1 - 3.0`), Python arrojaba `1.0999999999999996` en lugar de `1.10`, afectando el precio final por redondeo de moneda.  
   * *Corrección aplicada:* Se forzó el redondeo explícito `round(kilos_faltantes, 2)` antes de consultar el catálogo del sustituto.
3. **Omisión del sustituto por retorno prematuro (Flujo de Control):**  
   * *Problema de la IA:* En la primera propuesta, la IA lanzaba una excepción `ValueError("Stock insuficiente")` en lugar de ejecutar la regla aditiva de sustitución.  
   * *Corrección aplicada:* Se rediseñó el flujo condicional para que el quiebre de stock no detenga la ejecución, sino que transfiera la demanda residual al SKU sustituto.

---

## 3. Explicación Conceptual y Defensa del Paradigma Imperativo

> **En palabras del estudiante (para la defensa oral ante el profesor):**  
> *"El paradigma imperativo resuelve el problema mediante una secuencia explícita de instrucciones que transforman el estado de la máquina paso a paso. En nuestro script `carrito_imperativo.py`, el estado mutable se evidencia en la manipulación directa del diccionario del catálogo en memoria, donde los valores de stock disminuyen a medida que se recorren las necesidades del asado. El control de flujo es completamente procedural: utilizamos estructuras selectivas (`if/elif/else`) para bifurcar la toma de decisiones (por ejemplo, si el stock es suficiente o si debemos acudir a un producto sustituto) y variables acumuladoras que van sumando subtotales y encendiendo banderas lógicas (`flags`). Esta forma de programar refleja de manera transparente cómo opera la arquitectura subyacente del computador (modelo de Von Neumann), aunque tiene como desventaja que el estado compartido puede ser difícil de depurar a gran escala debido a los efectos secundarios colaterales."*

---

## 4. Referencias Bibliográficas (Norma APA 7ª Edición)

* Gabbrielli, M., y Martini, S. (2023). *Programming languages: principles and paradigms* (2a ed.). Springer. https://doi.org/10.1007/978-3-031-34144-1
* Sebesta, R. W. (2019). *Concepts of programming languages* (12a ed.). Pearson Education.
* Van Rossum, G., y Drake, F. L. (2024). *Python 3.12 reference manual*. Python Software Foundation. https://docs.python.org/3/reference/
