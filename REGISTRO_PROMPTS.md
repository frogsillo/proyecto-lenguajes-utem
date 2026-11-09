# REGISTRO CONSOLIDADO DE PROMPTING, SUPERVISIÓN Y DEFENSA MULTIPARADIGMA
**Asignatura:** Lenguajes de Programación  
**Carrera:** Ingeniería Civil en Computación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Semestre:** 2-2026  
**Documento Oficial de Respaldo Metodológico (Pauta de Evaluación)**

---

## 1. INTRODUCCIÓN Y METODOLOGÍA DE INTERACCIÓN CON IA

De acuerdo con la pauta de evaluación de la asignatura, el presente documento certifica la supervisión crítica de código construido mediante asistencia de Inteligencia Artificial Generativa. El desarrollo no consistió en una aceptación pasiva de código autogenerado, sino en un flujo dialéctico de diseño arquitectónico, formulación de prompts progresivos, identificación de anomalías de software y corrección iterativa.

Por cada uno de los tres paradigmas implementados (**Imperativo**, **Orientado a Objetos** y **Funcional**), se documentan nueve prompts divididos cronológicamente en:
1. **Tres prompts iniciales** (especificación arquitectónica y modelado conceptual).
2. **Tres prompts de desarrollo** (reglas de negocio complejas, sustitución de stock y promociones).
3. **Tres prompts finales** (refactorización, control de presupuesto y paridad matemática).

---

## 2. PARADIGMA IMPERATIVO (`src/imperativo/carrito_imperativo.py`)

### 2.1. Secuencia de Prompts Utilizados

#### Prompts Iniciales (Diseño y Especificación)
* **Prompt 1 (Arquitectura Secuencial e Integración):**  
  > *"Actúa como desarrollador Full-Stack Senior y arquitecto de software. Necesito implementar la lógica de un Carrito Evento Especial ('Asado Parrillero') en Python siguiendo un estilo 100% imperativo. Los datos de inventario deben desacoplarse en un archivo `catalogo_tienda.json` para simular la base de datos de una tienda en Shopify/Tiendanube. Explica cómo organizarías el flujo secuencial mediante variables mutables sin recurrir a clases ni programación declarativa."*
* **Prompt 2 (Estructuración de Estado Mutable):**  
  > *"Diseña la estructura de datos para mutar directamente el inventario del catálogo a medida que se procesa el evento. ¿Cómo controlamos las cantidades de carne vacuna consumiendo el stock en caliente y acumulando los subtotales en una lista mutable `items_carrito`?"*
* **Prompt 3 (Cálculo de Raciones Lineales):**  
  > *"Escribe las fórmulas procedurales para calcular la demanda de consumo: 350g de vacuno por adulto, 150g por niño, chorizos empaquetados en packs de 5 u., raciones vegetarianas, 1 bolsa de carbón de 2.5 kg cada 3 kg de carne y 0.5L de bebida por persona en botellas de 2.5L."*

#### Prompts para Completar el Código (Reglas de Negocio)
* **Prompt 4 (Algoritmo de Quiebre de Stock y Sustitución):**  
  > *"Genera el bloque condicional imperativo `if/else` para el quiebre de stock del corte premium (`Lomo Vetado`). Si la demanda es mayor a los 3.0 kg disponibles en bodega, debe consumir todo el stock remanente, fijarlo en 0.0, buscar el SKU sustituto (`Sobrecostilla`) en el catálogo y agregar los kilos faltantes al precio del sustituto."*
* **Prompt 5 (Regla de Promoción Combo Parrillero):**  
  > *"Implementa la verificación de la promoción 'Combo Parrillero': si el carrito contiene simultáneamente productos cárnicos, carbón y sal, calcula un 10% de descuento sobre la suma de subtotales de dichos ítems usando banderas booleanas (`flags`) y variables acumuladoras."*
* **Prompt 6 (Manejo de Unidades Cerradas):**  
  > *"Asegura que los productos vendidos en packs o botellas indivisibles utilicen redondeo hacia arriba con `math.ceil` para no dejar comensales desabastecidos."*

#### Prompts Finales (Ajuste Presupuestario y Menú Interactivo)
* **Prompt 7 (Gestión Activa del Presupuesto):**  
  > *"Si el total final supera el presupuesto fijado por el usuario, no te limites a emitir un aviso en texto. Diseña una regla de ajuste iterativo que degrade automáticamente el corte de carne (de Lomo Vetado a Sobrecostilla), reduzca bebidas al mínimo (1 botella) y ajuste chorizos a 1 pack esencial hasta intentar estar bajo el presupuesto."*
* **Prompt 8 (Entrada Amigable por Teclado):**  
  > *"Reemplaza las preguntas confusas por un menú directo al ejecutar el script: `[1] Modo Automático (Prueba)` y `[2] Modo Interactivo (Ingresar datos)` que solicite invitados, vegetarianos y presupuesto."*
* **Prompt 9 (Paridad y Moneda CLP):**  
  > *"Ajusta el redondeo financiero a pesos enteros CLP (`round(..., 0)`) dado que la moneda chilena no posee centavos, garantizando la compatibilidad con pasarelas de pago reales."*

---

## 3. PARADIGMA ORIENTADO A OBJETOS (`src/poo/`)

### 3.1. Secuencia de Prompts Utilizados

#### Prompts Iniciales (Modelado de Clases y Abstracción)
* **Prompt 10 (Diseño de Dominio):**  
  > *"Actúa como diseñador orientado a objetos. Modela el Carrito Evento Especial identificando las clases del dominio: `Producto`, `ItemCarrito` y `Carrito`. Define claramente qué atributos y métodos corresponden a cada entidad respetando el Principio de Responsabilidad Única (SRP)."*
* **Prompt 11 (Encapsulamiento del Inventario):**  
  > *"En la clase `Producto`, encapsula el atributo `_stock` como protegido y expón el método `consumir_stock(cantidad)`. Debe validar si hay disponibilidad suficiente y retornar la cantidad efectivamente despachada, evitando que entidades externas alteren arbitrariamente el stock."*
* **Prompt 12 (Entidad ItemCarrito):**  
  > *"Crea la clase `ItemCarrito` que asocie una instancia de `Producto` con una cantidad adquirida y un método interno `calcular_subtotal()`, exportable a un formato estándar para el visualizador."*

#### Prompts para Completar el Código (Patrón Strategy y Servicios)
* **Prompt 13 (Polimorfismo con Patrón Strategy):**  
  > *"Aplica el patrón de comportamiento Strategy mediante la biblioteca `abc` de Python. Define la clase abstracta `ReglaDescuento` con el método abstracto `calcular_descuento(carrito) -> Tuple[float, str]` para que el Carrito no dependa de sentencias condicionales acopladas a promociones específicas."*
* **Prompt 14 (Estrategia Concreta Combo Parrillero):**  
  > *"Implementa la subclase `ReglaComboParrillero` evaluando polimórficamente la categoría `carnico`, carbón y sal para aplicar el 10% de descuento sobre el subtotal de dichos productos."*
* **Prompt 15 (Servicio Planificador POO):**  
  > *"Crea la clase `PlanificadorAsadoPOO` con un método de fábrica `desde_fuentes()` que cargue los JSONs, instancie los objetos y orqueste la planificación de carnes, choripanes, menú vegetariano, carbón y bebidas."*

#### Prompts Finales (Interoperabilidad y Control Presupuestario)
* **Prompt 16 (Serialización y Exportación de Boleta):**  
  > *"Implementa en la clase `Carrito` el método `generar_boleta() -> dict` con una firma de salida idéntica a la versión imperativa para que el visualizador común funcione de forma transparente."*
* **Prompt 17 (Detección de Discrepancias de Categoría):**  
  > *"Al comparar POO con Imperativo, POO incluyó los chorizos en el descuento porque su categoría era 'carnico', mientras que Imperativo los había omitido. Analiza cuál comportamiento refleja mejor el negocio y alinea ambas versiones."*
* **Prompt 18 (Soporte Multimodal en POO):**  
  > *"Permite que `PlanificadorAsadoPOO` se ejecute tanto interactivamente por consola como desde diccionarios de eventos para pruebas automatizadas."*

---

## 4. PARADIGMA FUNCIONAL (`src/funcional/carrito_funcional.py`)

### 4.1. Secuencia de Prompts Utilizados

#### Prompts Iniciales (Filosofía Declarativa e Inmutabilidad)
* **Prompt 19 (Diseño sin Estado Mutable):**  
  > *"Actúa como especialista en programación funcional en Python. Diseña el Carrito Evento Especial bajo un modelo declarativo puro. Explica cómo representar el catálogo y las líneas del pedido utilizando tuplas inmutables (`tuple`) sin alterar variables ni recurrir a métodos mutadores como `.append()`."*
* **Prompt 20 (Consultas Puras con `filter`):**  
  > *"Implementa la función pura `obtener_producto_por_id` utilizando la función de orden superior `filter()` y expresiones `lambda` sobre una tupla inmutable de productos, sin usar bucles tradicionales ni `break`."*
* **Prompt 21 (Constructores Puros):**  
  > *"Define la función constructora pura `crear_item(producto, cantidad, nota)` que retorne un nuevo registro inmutable con el subtotal calculado, satisfaciendo el principio de transparencia referencial."*

#### Prompts para Completar el Código (Funciones de Orden Superior y Composición)
* **Prompt 22 (Resolución Funcional de Quiebre de Stock):**  
  > *"Escribe la función pura `resolver_carne_con_sustitucion()`. Si la demanda supera el stock disponible del corte preferido, debe devolver una tupla inmutable con dos nuevos ítems (corte preferido agotado y sustituto con el saldo restante) sin mutar la tupla original del catálogo."*
* **Prompt 23 (Evaluación de Promociones con `filter` y `reduce`):**  
  > *"Diseña `calcular_descuento_combo_funcional()` utilizando `any(map(...))` para verificar las condiciones del combo, `filter()` para aislar los ítems afectos y `functools.reduce()` para sumar los subtotales y calcular el 10% de descuento."*
* **Prompt 24 (Pipeline Declarativo Integral):**  
  > *"Construye la función principal `procesar_carrito_funcional()` como una composición de transformaciones donde las tuplas de carnes, chorizos, vegetarianos, insumos y bebidas se concatenan de forma inmutable y se totalizan mediante `reduce()`."*

#### Prompts Finales (Garantía de Paridad y Validación)
* **Prompt 25 (Eliminación de Acumuladores Ocultos):**  
  > *"Inspecciona el código funcional para asegurar que no queden bucles acumuladores residuales (`total += subtotal`) y que toda reducción se realice con funciones de orden superior."*
* **Prompt 26 (Paridad Numérica Exacta):**  
  > *"Valida que ante los datos oficiales de prueba, la versión funcional retorne exactamente Subtotal: \$99.809 CLP, Descuento: -\$7.943 CLP y Total: \$91.866 CLP."*
* **Prompt 27 (Modularidad de Entrada):**  
  > *"Adapta la función para admitir parámetros directos o el flujo interactivo sin comprometer la pureza de las funciones internas de cálculo."*

---

## 5. ERRORES IDENTIFICADOS EN LA GENERACIÓN POR IA Y CORRECCIONES EN EQUIPO

La supervisión humana del código generado por IA permitió detectar y subsanar fallas graves que habrían invalidado la entrega universitaria:

1. **Truncamiento indebido en compras por pack (División Entera):**  
   * *Falla de la IA:* Inicialmente, la IA calculó los chorizos como `comensales // 5`. Para 14 carnívoros, `14 // 5 = 2 packs` (10 unidades), dejando a 4 personas sin comida.  
   * *Corrección aplicada:* Se intervino el algoritmo reemplazándolo por `math.ceil(comensales / 5.0)` (3 packs = 15 unidades), satisfaciendo la demanda real.
2. **Discrepancia en la definición de negocio del Combo Parrillero:**  
   * *Falla de la IA:* En la versión imperativa, la IA sumó al combo solo el corte vacuno, carbón y sal (descuento \$6.446 CLP). En POO, evaluó `item.categoria == 'carnico'`, incluyendo los chorizos artesanales (descuento \$7.943 CLP).  
   * *Corrección aplicada:* Se determinó que los embutidos pertenecen a la categoría cárnica de un asado; se alineó la versión imperativa y funcional para incluir los chorizos, logrando una paridad matemática perfecta en \$91.866 CLP.
3. **Pérdida de inmutabilidad en el paradigma funcional:**  
   * *Falla de la IA:* La IA utilizó listas tradicionales y métodos `.append()` dentro de la versión funcional, argumentando falsamente que "en Python las listas son la forma estándar".  
   * *Corrección aplicada:* Se rechazó la solución y se exigió el uso riguroso de tuplas inmutables (`Tuple[Dict, ...]`), concatenación pura y funciones `map`, `filter` y `reduce`.
4. **Manejo de flotantes en moneda nacional (IEEE 754):**  
   * *Falla de la IA:* Las operaciones aritméticas arrojaban centavos como `91866.10000000001 CLP`. En Chile, el peso no tiene centavos.  
   * *Corrección aplicada:* Se forzó el redondeo a peso entero `float(round(monto))` en todas las versiones.
5. **Gestión pasiva versus activa del presupuesto:**  
   * *Falla de la IA:* Al superar el presupuesto, la IA solo imprimía una cadena de texto advirtiendo el problema.  
   * *Corrección aplicada:* Se diseñó un algoritmo de optimización que degrada activamente el corte y reduce extras para respetar el tope financiero del cliente.

---

## 6. EXPLICACIÓN CONCEPTUAL DEL ALUMNO (DEFENSA ORAL)

> *"El proyecto demuestra que un mismo problema de ingeniería de software puede resolverse con tres filosofías de diseño distintas:  
> 1. En el **Paradigma Imperativo**, pensamos en secuencias cronológicas de pasos que modifican la memoria del computador en caliente, utilizando variables acumuladoras y bucles tradicionales.  
> 2. En el **Paradigma Orientado a Objetos (POO)**, modelamos el negocio mediante entidades (`Producto`, `Carrito`) que encapsulan su propio estado y utilizamos el patrón **Strategy** con polimorfismo para que los descuentos no estén 'quemados' en el carrito, cumpliendo los principios SOLID.  
> 3. En el **Paradigma Funcional**, no existe el estado mutable ni los efectos secundarios: concebimos el sistema como un pipeline matemático de transformaciones donde los datos fluyen a través de funciones puras (`filter`, `map`, `reduce`) sobre colecciones inmutables.  
> Las tres versiones están integradas de forma aditiva sobre el catálogo de la tienda y pasan la suite de pruebas unitarias demostrando un comportamiento 100% equivalente."*

---

## 7. REFERENCIAS BIBLIOGRÁFICAS (NORMA APA 7ª EDICIÓN)

* Abelson, H., y Sussman, G. J. (1996). *Structure and interpretation of computer programs* (2a ed.). MIT Press.
* Bird, R. (2014). *Thinking functionally with Haskell*. Cambridge University Press. https://doi.org/10.1017/CBO9781316092415
* Gamma, E., Helm, R., Johnson, R., y Vlissides, J. (1994). *Design patterns: elements of reusable object-oriented software*. Addison-Wesley.
* Martin, R. C. (2018). *Clean architecture: a craftsman's guide to software structure and design*. Prentice Hall.
* Ramalho, L. (2022). *Fluent Python: clear, concise, and effective programming* (2a ed.). O'Reilly Media.
* Sebesta, R. W. (2019). *Concepts of programming languages* (12a ed.). Pearson Education.
* Van Rossum, G., y Drake, F. L. (2024). *Python 3.12 reference manual*. Python Software Foundation. https://docs.python.org/3/reference/
* Weisfeld, M. (2020). *The object-oriented thought process* (5a ed.). Addison-Wesley Professional.
* White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., y Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *ArXiv*. https://doi.org/10.48550/arXiv.2302.11382
