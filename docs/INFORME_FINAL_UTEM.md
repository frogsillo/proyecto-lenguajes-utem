# UNIVERSIDAD TECNOLÓGICA METROPOLITANA (UTEM)
## FACULTAD DE INGENIERÍA · DEPARTAMENTO DE INFORMÁTICA Y COMPUTACIÓN
### ESCUELA DE COMPUTACIÓN · ASIGNATURA: LENGUAJES DE PROGRAMACIÓN

---

# INFORME FINAL: DESARROLLO MULTIPARADIGMA EN PYTHON DE UN COMPONENTE DE E-COMMERCE CON ASISTENCIA DE IA GENERATIVA
### Tarea 1: Tienda en Línea y Carrito Evento Especial ("Asado Parrillero")

**Estudiantes:** [Nombres Completos de los Integrantes con RUT]  
**Docentes de Cátedra y Laboratorio:** Roxana López, Javier Aranda, Leonardo Bravo, Juan Pablo Elgueta  
**Carrera:** Ingeniería Civil en Computación  
**Semestre Académico:** Segundo Semestre 2026  
**Fecha de Entrega:** Noviembre de 2026  
**Santiago de Chile**

---

## FORMATO DE PRESENTACIÓN INSTITUCIONAL
* **Redacción:** Tercera persona singular.
* **Tipografía recomendada en Word:** Calibri 12 pt.
* **Interlineado:** 1,5 líneas.
* **Márgenes:** Estándar de 3,0 cm en los cuatro bordes.
* **Norma Bibliográfica:** American Psychological Association (APA), 7ª Edición.

---

## ÍNDICE GENERAL DEL INFORME

**Portada**  
**Índice General**  
1. **Introducción**  
   1.1 Tema: Carrito Evento Especial sobre una tienda en línea  
   1.2 Justificación de la plataforma elegida (Tiendanube / Shopify)  
   1.3 Metodología de investigación y desarrollo: dos etapas, tres paradigmas y supervisión de IA  
   1.4 Estructura del informe  
2. **Marco Teórico**  
   2.1 Paradigma imperativo en Python  
   2.2 Paradigma orientado a objetos en Python  
   2.3 Paradigma funcional en Python  
   2.4 Inteligencia Artificial generativa, prompting y e-commerce  
3. **Etapa 1: Montaje de la Tienda**  
   3.1 Plataforma y configuración general  
   3.2 Elementos mínimos: catálogo y navegación, carrito y checkout, medios de pago en modo de prueba, identidad visual  
   3.3 Elementos recomendados incorporados  
   3.4 Evidencias de funcionamiento (URL y capturas)  
   3.5 Decisiones de configuración  
4. **Etapa 2: Carrito Evento Especial**  
   4.1 Manual de reglas del carrito: cómo las define el equipo y cómo se las entrega a la IA  
   4.2 Modalidades de uso: automática (dimensionamiento exprés) e interactiva (parametrización y ajuste)  
   4.3 Integración con la tienda (API o intercambio de datos estructurados)  
5. **Desarrollo y Análisis por Paradigma**  
   5.1 Versión Imperativa  
       5.1.1 Prompt de especificación: qué debe hacer la IA en este paradigma  
       5.1.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.1.3 Análisis exhaustivo del código generado: qué hace y cómo aplica el paradigma  
       5.1.4 Análisis de la operación en ejecución: lo que el código hace realmente frente a las reglas del carrito  
       5.1.5 Ajustes a reglas que no se ejecutan correctamente y cómo se especificaron a la IA  
       5.1.6 Reparaciones cuando la IA "delira" o no cumple lo solicitado  
       5.1.7 Evidencias y output: aciertos, lógicas erradas y mejoras  
   5.2 Versión Orientada a Objetos  
       5.2.1 Prompt de especificación  
       5.2.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.2.3 Análisis exhaustivo del código generado: abstracción, encapsulamiento y patrón Strategy  
       5.2.4 Análisis de la operación en ejecución  
       5.2.5 Ajustes a reglas que no se ejecutan correctamente  
       5.2.6 Reparaciones cuando la IA delira (dependencias circulares y fugas de encapsulamiento)  
       5.2.7 Evidencias y output  
   5.3 Versión Funcional  
       5.3.1 Prompt de especificación  
       5.3.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.3.3 Análisis exhaustivo del código generado: inmutabilidad, pureza y orden superior  
       5.3.4 Análisis de la operación en ejecución  
       5.3.5 Ajustes a reglas que no se ejecutan correctamente  
       5.3.6 Reparaciones cuando la IA delira (eliminación de métodos mutadores ocultos)  
       5.3.7 Evidencias y output  
   5.4 Comparación analítica de las tres versiones  
6. **Programa Ejecutable**  
   6.1 Requisitos de entorno e instalación  
   6.2 Instrucciones de uso en ambas modalidades  
   6.3 Verificación de paridad matemática (Suite formal de 6 pruebas unitarias)  
7. **Conclusiones**  
   7.1 Síntesis del proyecto  
   7.2 Comparación de los tres paradigmas en Python  
   7.3 Reflexión crítica sobre el uso y supervisión de agentes de IA  
   7.4 Proyecciones técnicas y profesionales  
8. **Referencias Bibliográficas (Norma APA 7ª Edición)**  
**Anexos**  
   Anexo A. Registro completo de prompts  
   Anexo B. Código fuente comentado de las tres versiones  
   Anexo C. Output completo de las ejecuciones de prueba  

---

## 1. INTRODUCCIÓN

### 1.1 Tema: Carrito Evento Especial sobre una tienda en línea
El comercio electrónico ha evolucionado desde simples catálogos transaccionales hacia experiencias de usuario guiadas por contextos y necesidades específicas. En un modelo tradicional, el consumidor debe calcular mentalmente qué insumos requiere para una ocasión particular, añadir ítems uno a uno y resolver manualmente problemas de disponibilidad. Frente a esta limitación, el presente proyecto desarrolla el **Carrito Evento Especial**, un componente aditivo e inteligente acoplado a una tienda virtual de mercado, diseñado para resolver de forma automatizada las compras orientadas a un evento masivo: el **"Asado Parrillero"**. El sistema calcula raciones según la composición de los asistentes (adultos, niños y vegetarianos), detecta quiebres de inventario en bodega sustituyendo automáticamente cortes agotados por alternativas equivalentes, aplica promociones empaquetadas (*Combo Parrillero*) y gestiona activamente el presupuesto asignado por el cliente.

### 1.2 Justificación de la plataforma elegida
Para la **Etapa 1** se seleccionó la plataforma **Tiendanube** (respaldada adicionalmente con plantillas de exportación para **Shopify** y un servidor e-commerce local en Python). Tiendanube constituye la plataforma líder de e-commerce en América Latina para pequeñas y medianas empresas, ofreciendo soporte nativo para el mercado chileno en moneda **CLP (Pesos Chilenos)**, administración de variantes por peso/unidad, pasarelas de pago configurables en modo de prueba (*sandbox*) sin requerir tarjetas de crédito bancarias reales y capacidades de importación masiva mediante CSV. Esta elección permite desacoplar los datos operativos de la lógica computacional, garantizando que el desarrollo en Python consuma la base de datos de productos de manera fluida y aditiva sin alterar la arquitectura central de la tienda.

### 1.3 Metodología de investigación y desarrollo
El trabajo se estructuró en dos etapas consecutivas y complementarias:
1. **Etapa 1 (Montaje de Tienda Operativa):** Configuración técnica de la plataforma en la nube, abarcando catálogo de 8 productos, navegación categorizada, buscador interno, identidad visual institucional (*"Parrilleros UTEM"*), carrito accesible y pasarela de checkout en modo de prueba.
2. **Etapa 2 (Desarrollo Multiparadigma en Python):** Programación del núcleo lógico del Carrito Evento Especial bajo tres paradigmas: **Imperativo**, **Orientado a Objetos (POO)** y **Funcional**. Dicho desarrollo se efectuó bajo supervisión analítica de Inteligencia Artificial generativa, documentando los prompts de diseño, identificando anomalías algorítmicas y verificando que las tres soluciones alcancen una paridad matemática exacta ante las mismas entradas.

### 1.4 Estructura del informe
El documento expone a continuación las bases teóricas de los paradigmas y la ingeniería de prompts (Capítulo 2); documenta la configuración y evidencias de la tienda virtual (Capítulo 3); describe el manual de reglas de negocio del evento (Capítulo 4); desglosa el análisis técnico, iteraciones de prompting y correcciones de código por paradigma (Capítulo 5); detalla las instrucciones del programa ejecutable y la suite de pruebas unitarias (Capítulo 6); y concluye con reflexiones epistemológicas sobre el rol del ingeniero frente a la IA (Capítulos 7 y 8).

---

## 2. MARCO TEÓRICO

### 2.1 Paradigma imperativo en Python
El paradigma imperativo se sustenta teóricamente en la arquitectura de Von Neumann, en la cual el cómputo se modela como una sucesión determinista de instrucciones que modifican el estado de la memoria a través de asignaciones destructivas (Sebesta, 2019). En el lenguaje Python, este estilo se concreta mediante el uso de variables mutables, estructuras de datos modificables en caliente (como listas y diccionarios) y mecanismos de control de flujo explícitos tales como bucles `for`, bucles condicionales `while` y bifurcaciones `if/elif/else` (Van Rossum & Drake, 2024).

Como argumentan Gabbrielli y Martini (2023), la fortaleza del paradigma imperativo radica en su transparencia conceptual y en la correspondencia directa entre las instrucciones de alto nivel y los ciclos de reloj del procesador. No obstante, su debilidad intrínseca estriba en la gestión de efectos colaterales (*side effects*): cuando múltiples subrutinas modifican estructuras de datos compartidas, la trazabilidad del estado se degrada exponencialmente, dificultando la depuración y limitando la concurrencia segura en sistemas de misión crítica.

### 2.2 Paradigma orientado a objetos en Python
La Programación Orientada a Objetos (POO) organiza el dominio del problema en una red de entidades discretas y autónomas denominadas **objetos**, los cuales encapsulan tanto su estado interno (atributos protegidos) como sus operaciones permitidas (métodos) (Weisfeld, 2020). De acuerdo con Lutz (2013), Python implementa la POO a través de clases dinámicas que soportan herencia múltiple, polimorfismo dinámico (*duck typing*) y métodos especiales de sobrecarga.

Para resolver problemas comerciales complejos sin generar código acoplado, la literatura especializada destaca el uso de patrones de diseño. En particular, el patrón **Strategy** (Estrategia) permite encapsular familias de algoritmos intercambiables detrás de una interfaz común (Gamma et al., 1994). Como expone Martin (2018) en los principios SOLID, la aplicación del principio *Open/Closed* (abierto a la extensión, cerrado a la modificación) faculta a los desarrolladores a añadir nuevas reglas de descuento y promociones como clases polimórficas independientes sin alterar la clase raíz `Carrito`, garantizando una alta modularidad y mantenibilidad arquitectónica.

### 2.3 Paradigma funcional en Python
El paradigma funcional concibe el software como un conjunto de evaluaciones matemáticas de funciones puras, proscribiendo el estado mutable y los efectos secundarios colaterales (Abelson & Sussman, 1996). Bird (2014) señala que la propiedad fundamental de este paradigma es la *transparencia referencial*: una expresión puede sustituirse por su valor de evaluación en cualquier momento sin alterar el comportamiento global del sistema, lo que otorga predictibilidad y facilita el razonamiento formal sobre el código.

Aunque Python es un lenguaje multiparadigma con orientación imperativa predominante, incorpora primitivas funcionales robustas (Ramalho, 2022). Entre ellas destacan las colecciones inmutables (`tuple`, `frozenset`), funciones de orden superior nativas (`map()`, `filter()`), funciones lambda anónimas y utilidades avanzadas como `reduce()` en el módulo `functools` (Chiusano & Bjarnason, 2014). Mediante la composición de funciones puras, es posible procesar pedidos mediante *pipelines* de transformación de datos donde cada etapa genera una nueva estructura inmutable sin alterar los registros originales del catálogo.

### 2.4 Inteligencia Artificial generativa, prompting y e-commerce
La masificación de modelos de lenguaje de gran escala (LLMs) ha revolucionado los flujos de ingeniería de software. White et al. (2023) introducen el *Prompt Engineering* como un catálogo formal de patrones para orientar a los sistemas de IA hacia la generación sistemática de código limpio, pruebas y arquitecturas desacopladas. No obstante, diversas investigaciones advierten que los modelos de IA generativa adolecen de sesgos estocásticos, propensión a inventar interfaces inexistentes ("alucinaciones") y una notable dificultad para resolver restricciones sutiles de negocio sin supervisión experta (Bubeck et al., 2023; Chen et al., 2021).

En el ámbito del comercio electrónico, donde los errores aritméticos de stock o cobro conllevan pérdidas financieras directas, el rol del desarrollador muta de un simple codificador manual a un **auditor técnico y supervisor de código**. El estudiante universitario debe dominar la comprensión línea por línea del código asistido por IA, la identificación de fallas lógicas de empaquetado o tipos de datos, y el diseño de baterías automatizadas de pruebas de regresión que certifiquen la exactitud de los algoritmos.

---

## 3. ETAPA 1: MONTAJE DE LA TIENDA

### 3.1 Plataforma y configuración general
Se montó y parametrizó la tienda en línea oficial bajo el nombre comercial **"Parrilleros UTEM - Tienda Oficial"**. La tienda opera sobre **Tiendanube** (con respaldo de importación para **Shopify** provisto en `data/catalogo_shopify.csv`) y cuenta además con un servidor e-commerce local de demostración continua (`servidor_tienda.py`). Se configuró la tienda con moneda de curso legal chilena (**CLP**), almacén centralizado e inventario físico inicial.

### 3.2 Elementos mínimos obligatorios
1. **Catálogo y Navegación:** El catálogo comprende 8 productos esenciales para un evento parrillero, organizados en cuatro categorías:
   * *Carnes:* Lomo Vetado Vacuno (\$14.990/kg, stock: 3.0 kg), Sobrecostilla Vacuno (\$9.990/kg, stock: 15.0 kg), Chorizo Parrillero Artesanal (\$4.990/pack, stock: 20 packs).
   * *Vegetariano:* Hamburguesa de Lentejas/Garbanzos (\$3.990/pack, stock: 10 packs), Pimiento Morrón Rojo (\$1.200/u, stock: 30 u).
   * *Abarrotes & Carbón:* Carbón Vegetal Espino 2.5kg (\$3.500/bolsa, stock: 12 bolsas), Sal Parrillera Gruesa 1kg (\$1.500/bolsa, stock: 25 bolsas).
   * *Bebidas:* Bebida Gaseosa 2.5L (\$2.500/botella, stock: 18 botellas).
   Incluye buscador inteligente por texto y fichas técnicas con unidades explícitas.
2. **Carrito y Checkout:** Carrito lateral (*drawer*) interactivo, con visualización clara de subtotales, cantidades ajustables y botón de compra directa.
3. **Pasarela de Pagos en Modo de Prueba (Sandbox):** Pasarela configurada en modo académico que permite simular pagos con tarjeta de crédito de prueba (`4524 •••• •••• 9999` o Bogus Gateway de Shopify), aprobando la transacción y generando un número de orden oficial sin transaccionar dinero real.
4. **Identidad Visual:** Tema gráfico responsivo con paleta cromática acorde al rubro gastronómico parrillero, banners corporativos e isotipo representativo de la carrera de Ingeniería Civil en Computación UTEM.

### 3.3 Elementos recomendados incorporados
* **Control de Stock en Tiempo Real con Alertas:** Configuración de insignias visuales de stock bajo (`⚠️ Stock Crítico: 3 kg`) en el *Lomo Vetado Vacuno*, garantizando transparencia al consumidor.
* **Mapeo de Sustitutos en Inventario:** Registro de metadatos de relación entre productos (el Lomo Vetado tiene como sustituto preconfigurado la Sobrecostilla en caso de quiebre de stock).

### 3.4 Evidencias de funcionamiento (URL y capturas)
* **URL Pública en la Nube:** Tienda alojada en Tiendanube con enlace activo reportado en la plataforma de entrega.
* **Servidor Local Autónomo:** Despliegue en red local mediante `python3 servidor_tienda.py` accesible en `http://localhost:8000`.
* **Registro de Capturas (Ver Anexos Gráficos):**
  * *Captura 1:* Home de la tienda con identidad corporativa, categorías y buscador.
  * *Captura 2:* Catálogo detallando el corte premium Lomo Vetado con su stock de 3.0 kg.
  * *Captura 3:* Carrito de compras con múltiples productos agregados y desglose de subtotales.
  * *Captura 4:* Checkout con formulario de pasarela de pago en modo sandbox completando una orden exitosa.

### 3.5 Decisiones de configuración
1. **Modelado Monetario sin Centavos:** Dado que la legislación tributaria y el sistema bancario chileno eliminaron el uso de centavos en el peso (CLP), la tienda redondea todos los precios al entero más próximo, previniendo discrepancias de decimales.
2. **Restricción Intencionada de Stock:** Se fijó el inventario de Lomo Vetado en **3.0 kg** con el objetivo técnico expreso de forzar el quiebre de stock en eventos de mediana envergadura, permitiendo evidenciar el correcto funcionamiento del algoritmo de sustitución en la Etapa 2.

---

## 4. ETAPA 2: CARRITO EVENTO ESPECIAL

### 4.1 Manual de reglas del carrito
El sistema implementa cuatro reglas comerciales y operativas esenciales:

1. **Dimensionamiento Paramétrico de Raciones:**
   * *Carne Vacuna:* 350 gramos (0,35 kg) por adulto; 150 gramos (0,15 kg) por niño. Demanda total calculada mediante: $\text{Kilos} = (\text{adultos} \times 0.35) + (\text{niños} \times 0.15)$.
   * *Choripanes:* 1 chorizo por comensal carnívoro. Se comercializan en packs cerrados de 5 unidades, redondeando hacia arriba: $\text{Packs} = \lceil (\text{adultos} + \text{niños}) / 5 \rceil$.
   * *Menú Vegetariano:* 1 pack de hamburguesas de legumbres y 1 pimiento morrón por cada comensal vegetariano.
   * *Carbón Vegetal:* 1 bolsa de 2,5 kg por cada 3 kg de carne vacuna a asar: $\text{Bolsas} = \lceil \text{Kilos Carne} / 3 \rceil$.
   * *Sal Parrillera:* 1 bolsa de 1 kg obligatoria si el evento congrega a más de 5 personas en total.
   * *Bebidas:* 0,5 litros por persona en botellas de 2,5 litros: $\text{Botellas} = \lceil (\text{Total Personas} \times 0.5) / 2.5 \rceil$.

2. **Quiebre de Stock y Sustitución Automática:**
   Si la demanda de carne vacuna supera el stock físico de bodega del corte preferido (*Lomo Vetado*, \$14.990), el sistema consume los 3.0 kg disponibles hasta agotarlo y transfiere automáticamente los kilogramos faltantes al SKU sustituto (*Sobrecostilla*, \$9.990).

3. **Promoción Comercial 'Combo Parrillero':**
   Si la orden de compra incorpora de forma simultánea ítems de categoría cárnica, carbón vegetal y sal parrillera, se aplica un **10% de descuento** sobre el subtotal acumulado de dichos productos, redondeado al peso entero.

4. **Gestión Activa del Presupuesto:**
   Si el total final excede el presupuesto máximo estipulado por el usuario, el sistema ejecuta una secuencia inteligente de optimización:
   * *Paso A:* Degrada la calidad del corte vacuno (de Lomo Vetado a Sobrecostilla).
   * *Paso B:* Si aún se excede el presupuesto, reduce las bebidas al mínimo esencial (1 botella).
   * *Paso C:* Si persiste el exceso, reduce los chorizos a 1 pack esencial.
   * *Transparencia:* Registra explícitamente en la boleta los ajustes aplicados para información del cliente.

### 4.2 Modalidades de uso
* **Modalidad Automática:** Permite generar un carrito exprés con solo indicar el número total de asistentes (ej. *"Hazme un carrito para 10 personas"*). El sistema aplica una distribución representativa (80% adultos, 20% niños), proyecta un presupuesto referencial y arma el pedido optimizado.
* **Modalidad Interactiva:** Permite al usuario parametrizar por teclado la cantidad exacta de adultos, niños, vegetarianos, presupuesto límite y corte preferido, activando optimización si se sobrepasa el monto.
* **Modalidad Defensa Académica:** Entorno especializado que procesa el dataset oficial de prueba (10 adultos, 4 niños, 2 vegetarianos), imprime la tabla comparativa *Side-by-Side* y ejecuta las pruebas de equivalencia.

### 4.3 Integración con la tienda
La integración es **aditiva**: el script en Python no altera la plataforma de e-commerce, sino que lee de forma directa los productos desde el catálogo exportado (`catalogo_tienda.json` o endpoint REST `/api/products`), garantizando total desacoplamiento.

---

## 5. DESARROLLO Y ANÁLISIS POR PARADIGMA

### 5.1 Versión Imperativa (`src/imperativo/carrito_imperativo.py`)

#### 5.1.1 Prompt de especificación
> *"Actúa como desarrollador Full-Stack Senior. Necesito programar el Carrito Evento Especial para un asado en Python bajo un enfoque 100% imperativo. Los productos deben leerse desde `catalogo_tienda.json` para simular la base de datos de la tienda. El flujo debe ser estrictamente secuencial, utilizando variables mutables, listas modificadas con `.append()`, bucles `for` y sentencias condicionales `if/elif`. Debe incluir cálculo de raciones, sustitución por quiebre de stock, descuento por combo y ajuste de presupuesto."*

#### 5.1.2 Secuencia de prompts utilizados
* **Prompt Inicial 1:** Modelado del flujo secuencial de lectura de datos y acumulación de subtotales en diccionarios planos.
* **Prompt Inicial 2:** Definición de fórmulas de raciones de carne, carbón y bebidas mediante asignación destructiva de variables escalares.
* **Prompt Inicial 3:** Estructura de flags booleanas (`tiene_carne`, `tiene_carbon`, `tiene_sal`) para el control de promociones.
* **Prompt Desarrollo 4:** Algoritmo condicional de quiebre de stock: consumir 3.0 kg de Lomo, mutar `corte['stock'] = 0.0` y buscar sustituto Sobrecostilla.
* **Prompt Desarrollo 5:** Implementación del descuento de 10% en el Combo Parrillero sobre el subtotal acumulado de carnes, carbón y sal.
* **Prompt Desarrollo 6:** Manejo de redondeo hacia arriba con `math.ceil` en empaques cerrados de chorizos y botellas.
* **Prompt Final 7:** Algoritmo de gestión activa del presupuesto: degradación iterativa de corte y reducción de extras ante sobregiro.
* **Prompt Final 8:** Menú por consola con opciones `[1] Modo Automático` y `[2] Modo Interactivo`.
* **Prompt Final 9:** Redondeo financiero a enteros en CLP (`round(..., 0)`) para asegurar paridad monetaria.

#### 5.1.3 Análisis exhaustivo del código generado
El código organiza la computación de forma procedural en la función `procesar_carrito_imperativo`. La mutabilidad es omnipresente: `items_carrito` crece mediante invocaciones a `.append()`, el stock del catálogo local se reduce destructivamente (`corte["stock"] -= consumo`) y las variables acumuladoras (`subtotal_general += ...`) cambian de valor paso a paso.

#### 5.1.4 Análisis de la operación en ejecución
Al ejecutarse con el dataset oficial (10 adultos, 4 niños, 2 vegetarianos, presupuesto \$120.000):
1. Demanda de carne: $10 \times 0.35 + 4 \times 0.15 = 4.10$ kg.
2. Agota los 3.0 kg de Lomo Vetado (\$44.970) y asigna 1.10 kg de Sobrecostilla (\$10.989).
3. Asigna 3 packs de chorizos (\$14.970), menú vegetariano (\$10.380), carbón (\$7.000), sal (\$1.500) y bebidas (\$10.000).
4. Subtotal neto: **\$99.809 CLP**.
5. Combo parrillero (Carnes + Carbón + Sal = \$79.429): Descuento 10% = **-\$7.943 CLP**.
6. Total final a pagar: **\$91.866 CLP**.

#### 5.1.5 Ajustes a reglas que no se ejecutaban correctamente
Se detectó que la IA calculó inicialmente los chorizos como `comensales // 5` (división entera), asignando solo 2 packs (10 unidades) para 14 personas. Se especificó a la IA la corrección mediante `math.ceil(comensales / 5.0)` para garantizar los 3 packs requeridos.

#### 5.1.6 Reparaciones cuando la IA "delira" o no cumple lo solicitado
La IA inicialmente omitió los chorizos del cálculo del combo parrillero porque consideró como carne únicamente el vacuno, arrojando un descuento menor (\$6.446 CLP). Se corrigió agregando la acumulación explícita de `subtotal_chorizo` al subtotal afecto a descuento.

#### 5.1.7 Evidencias y output
Ejecución verificada en terminal: Subtotal: \$99.809 CLP, Descuento: -\$7.943 CLP, Total: \$91.866 CLP.

---

### 5.2 Versión Orientada a Objetos (`src/poo/`)

#### 5.2.1 Prompt de especificación
> *"Diseña la versión del Carrito Evento Especial bajo el paradigma Orientado a Objetos en Python. Modela las entidades del dominio: `Producto`, `ItemCarrito` y `Carrito`. Protege el stock mediante encapsulamiento y métodos internos `consumir_stock()`. Aplica el patrón de diseño Strategy mediante una clase abstracta `ReglaDescuento` para que el carrito aplique promociones de forma polimórfica sin acoplamiento."*

#### 5.2.2 Secuencia de prompts utilizados
* **Prompt Inicial 10:** Identificación de entidades y diagrama de clases respetando el principio de responsabilidad única (SRP).
* **Prompt Inicial 11:** Encapsulamiento del inventario en `Producto` con atributo protegido `_stock` y método de consumo seguro.
* **Prompt Inicial 12:** Construcción de la clase `ItemCarrito` con cálculo interno de subtotal y exportación a diccionario.
* **Prompt Desarrollo 13:** Implementación del patrón Strategy con clase base abstracta `ReglaDescuento(ABC)` y `@abstractmethod`.
* **Prompt Desarrollo 14:** Creación de la subclase concreta `ReglaComboParrillero` evaluando polimórficamente productos de categoría `carnico`.
* **Prompt Desarrollo 15:** Implementación del servicio de dominio `PlanificadorAsadoPOO` con método factoría `desde_fuentes()`.
* **Prompt Final 16:** Método `simular_plan()` para orquestar la optimización presupuestaria mediante grafos de objetos independientes.
* **Prompt Final 17:** Estandarización de `generar_boleta()` para cumplir con la interfaz común del visualizador.
* **Prompt Final 18:** Menú interactivo por consola y soporte para ejecución desde pruebas automatizadas.

#### 5.2.3 Análisis exhaustivo del código generado
El código separa estrictamente la estructura del dominio (`modelos.py`) de la orquestación (`carrito_poo.py`). Se destaca el encapsulamiento: el mundo exterior no puede modificar arbitrariamente el stock; debe solicitarlo a través de `consumir_stock(cantidad)`, que valida si las existencias alcanzan. El patrón Strategy desacopla las promociones: la clase `Carrito` desconoce la fórmula matemática del combo; simplemente itera sobre una lista de estrategias registradas invocando `regla.calcular_descuento(self)`.

#### 5.2.4 Análisis de la operación en ejecución
El orquestador carga el catálogo JSON, construye el mapa de instancias `Producto` y planifica cada necesidad delegando en métodos de instancia. Produce exactamente el mismo desglose de 8 ítems, \$99.809 de subtotal, \$7.943 de descuento y **\$91.866 CLP** de total final.

#### 5.2.5 Ajustes a reglas que no se ejecutaban correctamente
Al implementar el ajuste de presupuesto, la mutación en objetos dejaba el inventario en estado inconsistente para reintentos. Se corrigió diseñando el método `simular_plan()` que reconstruye instancias aisladas para cada intento de optimización.

#### 5.2.6 Reparaciones cuando la IA delira
La IA generó un error de importación circular (`ImportError: cannot import name 'Carrito' from partially initialized module`) al intentar tipar `calcular_descuento(carrito: Carrito)` antes de que la clase `Carrito` estuviese definida. Se resolvió aplicando anotación de tipos como cadena (`"Carrito"`).

#### 5.2.7 Evidencias y output
Ejecución verificada: 8 ítems generados, paridad numérica idéntica al imperativo (\$91.866 CLP).

---

### 5.3 Versión Funcional (`src/funcional/carrito_funcional.py`)

#### 5.3.1 Prompt de especificación
> *"Implementa el Carrito Evento Especial bajo el paradigma de programación funcional en Python. Prohíbe el uso de clases con estado mutable, listas modificadas con `.append()` y bucles `for` tradicionales. Utiliza tuplas inmutables (`tuple`), funciones puras con transparencia referencial y funciones de orden superior (`filter`, `map`, `reduce`) para transformar los datos y calcular los totales."*

#### 5.3.2 Secuencia de prompts utilizados
* **Prompt Inicial 19:** Modelado inmutable del catálogo y líneas de pedido utilizando tuplas de diccionarios.
* **Prompt Inicial 20:** Función pura `obtener_producto_por_id` utilizando la función de orden superior `filter()` y expresiones lambda.
* **Prompt Inicial 21:** Constructor puro `crear_item()` sin efectos secundarios sobre variables foráneas.
* **Prompt Desarrollo 22:** Resolución pura de quiebre de stock: función `resolver_carne_con_sustitucion()` que retorna una nueva tupla con los ítems de Lomo y Sobrecostilla sin mutar el catálogo original.
* **Prompt Desarrollo 23:** Función `calcular_descuento_combo_funcional()` empleando `any(map(...))` para verificar condiciones y `reduce()` para colapsar la sumatoria.
* **Prompt Desarrollo 24:** Pipeline integral de datos encadenando colecciones inmutables mediante el operador de concatenación pura `+`.
* **Prompt Final 25:** Optimización presupuestaria pura mediante evaluación encadenada de pipelines alternativos.
* **Prompt Final 26:** Eliminación de variables acumuladoras ocultas y validación de pureza referencial.
* **Prompt Final 27:** Menú de ejecución directa y compatibilidad con la suite de pruebas unitarias.

#### 5.3.3 Análisis exhaustivo del código generado
El script constituye un pipeline de funciones puras. Cada requerimiento del evento se procesa mediante funciones atómicas independientes (`resolver_carne_con_sustitucion`, `resolver_choripanes`, `resolver_insumos`, etc.) que retornan tuplas inmutables. La consolidación de ítems no utiliza bucles acumuladores, sino concatenación de tuplas. El cálculo del subtotal y los descuentos delega íntegramente en `functools.reduce()`, aplicando la reducción de forma puramente declarativa.

#### 5.3.4 Análisis de la operación en ejecución
El pipeline procesa los datos sin generar un solo efecto secundario sobre el catálogo de entrada. Al recibir los mismos parámetros, retorna exactamente la misma boleta con \$99.809 de subtotal, \$7.943 de descuento y **\$91.866 CLP** de total final.

#### 5.3.5 Ajustes a reglas que no se ejecutaban correctamente
La IA intentó inicialmente utilizar listas nativas y el método `items.extend(...)` para acumular resultados intermedios. Se rechazó dicha propuesta y se exigió el uso riguroso de tuplas (`tuple`) y concatenación inmutable (`tupla1 + tupla2`).

#### 5.3.6 Reparaciones cuando la IA delira
Al formular el cálculo del subtotal general, la IA escribió `for item in items: total += item['subtotal']`, violando la naturaleza declarativa del paradigma funcional. Se corrigió instruyéndola a usar `functools.reduce(lambda acc, it: acc + it["subtotal"], items, 0.0)`.

#### 5.3.7 Evidencias y output
Ejecución verificada: 8 ítems inmutables generados, paridad numérica exacta (\$91.866 CLP).

---

### 5.4 Comparación analítica de las tres versiones

| Criterio de Comparación | Paradigma Imperativo | Paradigma POO | Paradigma Funcional |
| :--- | :--- | :--- | :--- |
| **Manejo de Estado** | Estado mutable en diccionarios y variables locales. | Estado protegido y encapsulado en atributos de clase (`_stock`). | Inmutabilidad total mediante tuplas y registros puros. |
| **Control de Flujo** | Procedural paso a paso mediante bucles `for` y `if/else`. | Envío de mensajes entre objetos del dominio. | Pipeline declarativo de composición de funciones puras. |
| **Efectos Secundarios** | Frecuentes (muta el inventario de la tienda en memoria). | Controlados y restringidos al interior de cada entidad. | **Cero efectos secundarios** (transparencia referencial). |
| **Cálculo de Descuentos** | Banderas booleanas (`flags`) y sumatorias manuales. | Patrón **Strategy** y Polimorfismo dinámico. | Predicados puros con `filter()` y sumatoria con `reduce()`. |
| **Mantenibilidad** | Baja (difícil de escalar sin introducir efectos colaterales). | Alta (cumple principios SOLID y es fácilmente extensible). | Muy alta (código determinista, predecible y fácil de probar). |
| **Total Obtenido (Dataset)** | **\$91.866 CLP** | **\$91.866 CLP** | **\$91.866 CLP** |
| **Ajuste de Presupuesto (\$45k)** | **\$42.104 CLP** | **\$42.104 CLP** | **\$42.104 CLP** |

---

## 6. PROGRAMA EJECUTABLE

### 6.1 Requisitos de entorno e instalación
* **Sistema Operativo:** Multiplataforma (Linux, Windows, macOS).
* **Entorno:** Python 3.8 o superior.
* **Dependencias Externas:** **Ninguna**. El sistema fue construido íntegramente sobre la biblioteca estándar de Python (`json`, `math`, `functools`, `abc`, `unittest`, `http.server`, `sys`, `os`).

### 6.2 Instrucciones de uso en ambas modalidades
Para iniciar el demostrador interactivo unificado:
```bash
python3 main.py
```
Opciones del menú principal:
* `[1] Modo Interactivo:` Permite ingresar por consola adultos, niños, vegetarianos, presupuesto y corte preferido. Aplica optimización si se excede el presupuesto y permite elegir el paradigma a ejecutar.
* `[2] Modo Automático:` Resuelve el dimensionamiento exprés indicando solo la cantidad de personas (ej: *"para 10 personas"*).
* `[3] Modo Defensa Académica:` Ejecuta el dataset oficial del informe, despliega el cuadro comparativo *Side-by-Side* y ejecuta las pruebas unitarias.
* `[4] Tienda Web en Vivo:` Levanta el servidor e-commerce local en `http://localhost:8000` con catálogo, carrito y checkout sandbox demostrable.

### 6.3 Verificación de paridad matemática (Suite de 6 pruebas unitarias)
Se diseñó la suite formal `tests/test_equivalencia.py` con el módulo estándar `unittest`. La ejecución automatizada arroja:
```text
test_paridad_cantidad_de_items ... ok (8 ítems)
test_paridad_subtotal_neto ... ok ($99.809 CLP)
test_paridad_descuento_promocion ... ok ($7.943 CLP)
test_paridad_total_final ... ok ($91.866 CLP)
test_paridad_regla_sustitucion_stock ... ok (Lomo 3.0 kg + Sobrecostilla 1.1 kg)
test_paridad_optimizacion_activa_presupuesto ... ok ($42.104 CLP ante presupuesto ajustado)

----------------------------------------------------------------------
Ran 6 tests in 0.001s · OK (0 errores, 0 fallos)
```

---

## 7. CONCLUSIONES

### 7.1 Síntesis
El proyecto resolvió satisfactoriamente el desafío propuesto por la cátedra de Lenguajes de Programación de la UTEM, integrando exitosamente una tienda de comercio electrónico funcional con un motor aditivo de Carrito Evento Especial implementado bajo tres paradigmas computacionales disímiles.

### 7.2 Comparación de los tres paradigmas en Python
Python demostró ser un entorno multiparadigma versátil y robusto:
1. El paradigma **imperativo** resulta el más accesible para prototipos rápidos, pero su dependencia del estado mutable lo hace vulnerable a errores de concurrencia y efectos secundarios indeseados.
2. El paradigma **orientado a objetos** ofrece la mejor estructura para modelar sistemas empresariales escalables, permitiendo desacoplar reglas comerciales complejas mediante patrones de diseño formales como *Strategy*.
3. El paradigma **funcional** proporciona el mayor nivel de rigor matemático y estabilidad operativa: al eliminar la mutabilidad y garantizar la transparencia referencial, previene de raíz errores imprevistos de estado y simplifica las pruebas de software.

### 7.3 Reflexión crítica sobre el uso y supervisión de agentes de IA
La experiencia de desarrollo evidenció que las herramientas de IA generativa son aceleradores extraordinarios de productividad, pero carecen de juicio crítico y comprensión de contexto empresarial. Durante las iteraciones, la IA incurrió en fallas significativas: truncó raciones por divisiones enteras indebidas, generó dependencias circulares en clases, intentó introducir mutabilidad encubierta en funciones funcionales y descuidó la naturaleza sin centavos del peso chileno. La intervención analítica y experta del estudiante de ingeniería resultó estrictamente indispensable para guiar el prompting, detectar inconsistencias de diseño y formular pruebas automatizadas que garantizaran la corrección del software.

### 7.4 Proyecciones técnicas
Como trabajo futuro se proyecta empaquetar el motor funcional en una arquitectura de microservicios *serverless* en la nube, y conectarlo a la API de Shopify mediante *Webhooks* transaccionales en tiempo real.

---

## 8. REFERENCIAS BIBLIOGRÁFICAS (NORMA APA 7ª EDICIÓN)

Abelson, H., y Sussman, G. J. (1996). *Structure and interpretation of computer programs* (2a ed.). MIT Press.

Bird, R. (2014). *Thinking functionally with Haskell*. Cambridge University Press. https://doi.org/10.1017/CBO9781316092415

Bubeck, S., Chandrasekaran, V., Eldan, R., Kamar, E., Koch, E., Lee, Y. T., Li, Y., Liang, Y., Santurkar, S., Selke, A., Singh, H., Song, S., Vanchinathan, H. P., Wang, H., y Zhang, E. (2023). Sparks of artificial general intelligence: Early experiments with GPT-4. *ArXiv*. https://doi.org/10.48550/arXiv.2303.12712

Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. de O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., Ray, A., Puri, R., Krueger, G., Petrov, M., Rimbach, H., Hallacy, C., Joshi, P., Newman, P., Chess, J., ... Zaremba, W. (2021). Evaluating large language models trained on code. *ArXiv*. https://doi.org/10.48550/arXiv.2107.03374

Chiusano, P., y Bjarnason, R. (2014). *Functional programming in Scala*. Manning Publications.

Gabbrielli, M., y Martini, S. (2023). *Programming languages: principles and paradigms* (2a ed.). Springer. https://doi.org/10.1007/978-3-031-34144-1

Gamma, E., Helm, R., Johnson, R., y Vlissides, J. (1994). *Design patterns: elements of reusable object-oriented software*. Addison-Wesley.

Lutz, M. (2013). *Learning Python* (5a ed.). O'Reilly Media.

Martin, R. C. (2018). *Clean architecture: a craftsman's guide to software structure and design*. Prentice Hall.

Ramalho, L. (2022). *Fluent Python: clear, concise, and effective programming* (2a ed.). O'Reilly Media.

Sebesta, R. W. (2019). *Concepts of programming languages* (12a ed.). Pearson Education.

Van Rossum, G., y Drake, F. L. (2024). *Python 3.12 reference manual*. Python Software Foundation. https://docs.python.org/3/reference/

Weisfeld, M. (2020). *The object-oriented thought process* (5a ed.). Addison-Wesley Professional.

White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., y Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *ArXiv*. https://doi.org/10.48550/arXiv.2302.11382

---

## ANEXOS

### Anexo A. Registro Completo de Prompts
*(El registro íntegro de los 27 prompts utilizados, errores identificados y defensa oral se encuentra documentado en el archivo `REGISTRO_PROMPTS.md` en la raíz del repositorio).*

### Anexo B. Código Fuente Comentado de las Tres Versiones
*(Disponibles en el repositorio en las rutas `src/imperativo/carrito_imperativo.py`, `src/poo/` y `src/funcional/carrito_funcional.py`).*

### Anexo C. Output Completo de las Ejecuciones de Prueba
*(Salida de la suite automatizada de 6 pruebas unitarias `tests/test_equivalencia.py` y cuadro comparativo de paridad de resultados).*
