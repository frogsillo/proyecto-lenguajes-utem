# Bitácora de Interacción con IA y Análisis Técnico: Paradigma Funcional
**Asignatura:** Lenguajes de Programación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Proyecto:** Carrito Evento Especial — Asado Parrillero  
**Entrega:** Etapa 2 — Versión Funcional  

---

## 1. Registro Metodológico de Prompts (Pauta UTEM)

### 1.1. Prompts Iniciales (Filosofía Declarativa e Inmutabilidad)
* **Prompt 1 (Modelado sin Efectos Secundarios):**  
  > *"Actúa como especialista en programación funcional en Python. Necesito rediseñar el Carrito Evento Especial (Asado) para que opere bajo una arquitectura puramente declarativa y libre de efectos secundarios. Explica cómo representar el catálogo y los ítems del carrito utilizando tuplas inmutables en lugar de diccionarios mutables o clases con estado."*
* **Prompt 2 (Búsqueda Declarativa con `filter`):**  
  > *"Crea una función pura `obtener_producto_por_id(catalogo: Tuple[dict, ...], id_prod: str) -> dict` que busque un producto dentro de una tupla inmutable utilizando la función de orden superior `filter()` y expresiones `lambda`, sin utilizar bucles `for` tradicionales ni sentencias `break`."*
* **Prompt 3 (Constructores de Datos Puros):**  
  > *"Define la función pura `crear_item(producto, cantidad, nota)` que reciba un producto inmutable y retorne un nuevo registro inmutable con el subtotal precalculado, asegurando que ninguna variable externa sea modificada durante el proceso."*

### 1.2. Prompts para Completar el Código (Composición de Funciones y Reducción)
* **Prompt 4 (Resolución Funcional de Quiebre de Stock):**  
  > *"Implementa la función pura `resolver_carne_con_sustitucion(...)`. Si el stock disponible de la carne preferida es inferior a la demanda, la función debe retornar una tupla con dos nuevos ítems (el producto preferido hasta agotar stock y el sustituto con el saldo restante) sin mutar el inventario del catálogo de entrada."*
* **Prompt 5 (Evaluación de Reglas con `filter` y `reduce`):**  
  > *"Diseña la función `calcular_descuento_combo_funcional(items: Tuple[dict, ...]) -> Tuple[float, str]`. Debe utilizar `any(map(...))` para verificar la presencia simultánea de carnes, carbón y sal, `filter()` para aislar los ítems afectos y `reduce()` de `functools` para calcular la sumatoria de subtotales y el 10% de descuento."*
* **Prompt 6 (Pipeline de Transformación Declarativo):**  
  > *"Construye la función orquestadora `procesar_carrito_funcional(ruta_cat, ruta_eve)` como un pipeline de datos donde las demandas de carnes, choripanes, vegetarianos, insumos y bebidas se resuelvan como tuplas independientes que se concatenan en una única estructura inmutable, calculando el subtotal general mediante `reduce`."*

### 1.3. Prompts Finales (Equivalencia Numérica y Pureza)
* **Prompt 7 (Garantía de Paridad Matemática):**  
  > *"Revisa exhaustivamente que las fórmulas matemáticas y el orden de evaluación en la versión funcional arrojen exactamente Subtotal: \$99.809 CLP, Descuento: \$7.943 CLP y Total: \$91.866 CLP, coincidiendo al 100% con las versiones Imperativa y POO."*
* **Prompt 8 (Eliminación de Acumuladores Foráneos):**  
  > *"Inspecciona el código funcional para asegurar que no existan variables contadoras globales ni métodos mutadores como `.append()` o reasignaciones `total += subtotal`."*
* **Prompt 9 (Documentación de Funciones de Orden Superior):**  
  > *"Añade type hinting riguroso (`Tuple`, `Dict`, `Any`) y comentarios didácticos explicando cómo opera cada función de orden superior (`map`, `filter`, `reduce`) para la defensa oral del examen."*

---

## 2. Errores Identificados en la Generación por IA y Correcciones Realizadas

1. **Mutación encubierta de colecciones (Efecto Colateral Oculto):**  
   * *Problema de la IA:* Inicialmente, la IA utilizó listas estándar de Python y ejecutó `items.extend(...)` dentro de las funciones de cálculo, violando el principio de inmutabilidad del paradigma funcional.  
   * *Corrección aplicada:* Se sustituyeron todas las listas mutables por tuplas inmutables (`tuple`), y la agregación se implementó mediante la operación de concatenación pura `tupla1 + tupla2`, lo que garantiza que las estructuras originales permanezcan inalteradas en memoria.
2. **Uso de bucle `for` tradicional en lugar de `reduce` (Estilo Declarativo):**  
   * *Problema de la IA:* Al calcular el subtotal general, la IA propuso un bucle `for item in items: total += item['subtotal']`, lo cual es imperativo.  
   * *Corrección aplicada:* Se refactorizó usando `functools.reduce(lambda acc, it: acc + it['subtotal'], items, 0.0)`, cumpliendo rigurosamente con los estándares de la programación funcional evaluados por la UTEM.
3. **Pérdida de inmutabilidad en la lectura de JSON:**  
   * *Problema de la IA:* `json.load()` retorna diccionarios y listas mutables nativas.  
   * *Corrección aplicada:* Se forzó la conversión del catálogo a una tupla inmutable de registros en el punto de entrada (`tuple(datos_cat['productos'])`).

---

## 3. Explicación Conceptual y Defensa del Paradigma Funcional

> **En palabras del estudiante (para la defensa oral ante el profesor):**  
> *"El paradigma funcional trata la computación como la evaluación de funciones matemáticas puras y evita deliberadamente el estado mutable y los efectos secundarios. En `carrito_funcional.py`, las funciones son de 'transparencia referencial': para los mismos argumentos de entrada, siempre retornan la misma salida sin alterar variables externas ni mutar el catálogo original. En lugar de instrucciones secuenciales con bucles acumuladores, empleamos un pipeline declarativo donde los datos fluyen a través de funciones de orden superior: `filter()` para discriminar productos por ID o categoría, `map()` para verificar condiciones booleanas y `reduce()` para colapsar la lista de ítems en los montos de subtotal y descuento. Esto aporta enormes ventajas de robustez, ausencia de 'bugs' por estado compartido y alta facilidad para pruebas unitarias y concurrencia."*

---

## 4. Referencias Bibliográficas (Norma APA 7ª Edición)

* Abelson, H., y Sussman, G. J. (1996). *Structure and interpretation of computer programs* (2a ed.). MIT Press.
* Bird, R. (2014). *Thinking functionally with Haskell*. Cambridge University Press. https://doi.org/10.1017/CBO9781316092415
* Chiusano, P., y Bjarnason, R. (2014). *Functional programming in Scala*. Manning Publications.
