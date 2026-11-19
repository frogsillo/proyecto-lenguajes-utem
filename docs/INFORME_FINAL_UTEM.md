# UNIVERSIDAD TECNOLÓGICA METROPOLITANA (UTEM)
## FACULTAD DE INGENIERÍA · DEPARTAMENTO DE INFORMÁTICA Y COMPUTACIÓN
### ESCUELA DE COMPUTACIÓN · ASIGNATURA: LENGUAJES DE PROGRAMACIÓN

---

# INFORME FINAL: DESARROLLO MULTIPARADIGMA EN PYTHON DE UN COMPONENTE DE E-COMMERCE CON ASISTENCIA DE IA GENERATIVA
### Tarea 1: Tienda en Línea y Carrito Evento Especial ("Asado Parrillero")

**Estudiante(s):** [Ingresa aquí tu Nombre Completo] — RUT: [xx.xxx.xxx-x]  
*(Si el proyecto fue realizado en equipo, incluir los nombres y RUTs de todos los integrantes)*  
**Docente de Cátedra:** Juan Pablo Elgueta  
**Equipo Docente de la Asignatura:** Roxana López, Javier Aranda, Leonardo Bravo, Juan Pablo Elgueta  
**Carrera:** Ingeniería Civil en Computación / Ingeniería en Informática  
**Semestre Académico:** Segundo Semestre 2026  
**Fecha de Entrega:** Domingo 29 de Noviembre de 2026  
**Santiago de Chile**

---

## PAUTA DE FORMATO INSTITUCIONAL (UTEM)
* **Estilo de Redacción:** Rigurosa tercera persona singular ("Se desarrolló", "Se observó", "El sistema calcula").
* **Tipografía oficial en Microsoft Word:** Calibri 12 pt para cuerpo de texto.
* **Interlineado:** 1,5 líneas con espaciado posterior de 6 pt.
* **Márgenes:** Estándar de 3,0 cm en los cuatro bordes (superior, inferior, izquierdo, derecho).
* **Bloques de Código Fuente:** Fuente monoespaciada Consolas o Courier New 9,5 pt con interlineado sencillo (1,0) para preservar la indentación.
* **Norma Bibliográfica:** American Psychological Association (APA), 7ª Edición (mínimo 3 citas por cada tema del Marco Teórico).
* **Estructura de Evaluación (Ponderación 40%):** Informe Final Escrito (50 puntos / 20%) y Presentación Final en Equipo con Demostración en Vivo (50 puntos / 20%).

---

## ÍNDICE GENERAL DEL INFORME

**Portada e Identificación Institucional**  
**Índice General** *(Generado con el editor de Word)*  
1. **Introducción**  
   1.1 Tema: Carrito Evento Especial sobre una tienda en línea  
   1.2 Justificación de la plataforma elegida (Tiendanube / Shopify / Render)  
   1.3 Metodología de investigación y desarrollo: dos etapas, tres paradigmas y supervisión de IA  
   1.4 Estructura del informe  
2. **Marco Teórico**  
   2.1 Paradigma imperativo en Python  
   2.2 Paradigma orientado a objetos en Python  
   2.3 Paradigma funcional en Python  
   2.4 Inteligencia Artificial generativa, prompting y e-commerce  
3. **Etapa 1: Montaje de la Tienda**  
   3.1 Plataforma y configuración general  
   3.2 Elementos mínimos: catálogo de 20 productos y navegación, carrito y checkout, medios de pago en modo de prueba, identidad visual  
   3.3 Elementos recomendados incorporados  
   3.4 Evidencias de funcionamiento (URL, arquitectura visual, marcadores y capturas)  
   3.5 Decisiones de configuración justificadas  
4. **Etapa 2: Carrito Evento Especial**  
   4.1 Manual de reglas del carrito: cómo las define el equipo y cómo se las entrega a la IA  
   4.2 Modalidades de uso: automática (dimensionamiento exprés) e interactiva (parametrización y ajuste)  
   4.3 Integración con la tienda (API REST e intercambio de datos estructurados)  
5. **Desarrollo y Análisis por Paradigma**  
   5.1 Versión Imperativa  
       5.1.1 Prompt de especificación: qué debe hacer la IA en este paradigma  
       5.1.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.1.3 Análisis exhaustivo del código generado: qué hace y cómo aplica el paradigma  
       5.1.4 Análisis de la operación en ejecución: lo que el código hace realmente frente a las reglas del carrito  
       5.1.5 Ajustes a reglas que no se ejecutan correctamente y cómo se especificaron a la IA (con código de contraste)  
       5.1.6 Reparaciones cuando la IA "delira" o no cumple lo solicitado (con código de contraste)  
       5.1.7 Evidencias y output: aciertos, lógicas erradas y mejoras  
   5.2 Versión Orientada a Objetos  
       5.2.1 Prompt de especificación  
       5.2.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.2.3 Análisis exhaustivo del código generado: abstracción, encapsulamiento y patrón Strategy  
       5.2.4 Análisis de la operación en ejecución  
       5.2.5 Ajustes a reglas que no se ejecutan correctamente (con código de contraste)  
       5.2.6 Reparaciones cuando la IA delira (dependencias circulares y fugas de encapsulamiento)  
       5.2.7 Evidencias y output  
   5.3 Versión Funcional  
       5.3.1 Prompt de especificación  
       5.3.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.3.3 Análisis exhaustivo del código generado: inmutabilidad, pureza y orden superior  
       5.3.4 Análisis de la operación en ejecución  
       5.3.5 Ajustes a reglas que no se ejecutan correctamente (con código de contraste)  
       5.3.6 Reparaciones cuando la IA delira (eliminación de métodos mutadores ocultos)  
       5.3.7 Evidencias y output  
   5.4 Comparación analítica de las tres versiones  
6. **Programa Ejecutable**  
   6.1 Requisitos de entorno e instalación  
   6.2 Instrucciones de uso en ambas modalidades (Interactiva, Automática y Modo Defensa)  
   6.3 Verificación de paridad matemática (Suite formal de 6 pruebas unitarias con unificación presupuestaria)  
7. **Conclusiones**  
   7.1 Síntesis del proyecto  
   7.2 Comparación de los tres paradigmas en Python  
   7.3 Reflexión crítica sobre el uso y supervisión de agentes de IA  
   7.4 Proyecciones técnicas y profesionales  
8. **Referencias Bibliográficas (Norma APA 7ª Edición)**  
**Anexos (Evidencias de Respaldo Completas)**  
   * **Anexo A. Registro Completo de Prompts:** Transcripción íntegra de los 27 prompts, análisis de fallas y guión de defensa.  
   * **Anexo B. Código Fuente Comentado de las Tres Versiones:** Código íntegro de la versión Imperativa, POO y Funcional corregida.  
   * **Anexo C. Output Completo de las Ejecuciones de Prueba:** Registro textual verbatim de pruebas unitarias, boletas base ($91.866 CLP) y boleta ajustada ($61.884 CLP).

---

## 1. INTRODUCCIÓN

### 1.1 Tema: Carrito Evento Especial sobre una tienda en línea
El comercio electrónico moderno ha transitado desde interfaces transaccionales tradicionales hacia sistemas guiados por el contexto de uso y las necesidades reales del consumidor. Cuando un cliente organiza una celebración social masiva, como un asado familiar o institucional, el modelo habitual de e-commerce impone una fricción considerable: el usuario debe calcular mentalmente los insumos por comensal, buscar productos dispersos en el catálogo y resolver imprevistos como quiebres de inventario o desajustes de presupuesto.

Frente a esta limitación, el presente proyecto diseña e implementa el **Carrito Evento Especial**, un componente aditivo e inteligente acoplado a una tienda virtual de mercado, diseñado para resolver de forma automatizada las compras orientadas a un evento masivo: el **"Asado Parrillero"**. El sistema dimensiona las raciones exactas según la composición demográfica de los asistentes (adultos, niños y vegetarianos), detecta quiebres de inventario en bodega sustituyendo automáticamente cortes agotados por alternativas equivalentes, aplica promociones comerciales empaquetadas (*Combo Parrillero*) y gestiona activamente el presupuesto asignado por el cliente para evitar órdenes sobregiradas.

### 1.2 Justificación de la plataforma elegida (Tiendanube / Shopify / Render)
Para el desarrollo de la **Etapa 1** se implementó una arquitectura e-commerce híbrida y flexible:
1. **Tienda Web Autónoma en Python (`servidor_tienda.py`):** Un servidor e-commerce completo con estética retail inspirada en **Jumbo.cl**, paleta verde institucional (#00843D), catálogo de 20 productos, buscador en tiempo real, carrito lateral y pasarela de pago en modo Sandbox.
2. **Compatibilidad con Shopify Partners:** El sistema genera y expone automáticamente el archivo oficial `data/catalogo_shopify.csv` (vía endpoint `GET /api/export/shopify.csv`) para importar los 20 productos a tiendas Shopify o Tiendanube en un solo clic.
3. **Despliegue Gratuito en la Nube:** El servidor backend está preparado con `Procfile`, `render.yaml` y enlace de variables de entorno (`PORT`) para su despliegue continuo en plataformas gratuitas como **Render.com** o **Railway**.

### 1.3 Metodología de investigación y desarrollo
El trabajo se estructuró rigurosamente en dos etapas consecutivas y complementarias:
1. **Etapa 1 (Montaje de Tienda Operativa):** Configuración técnica del catálogo ampliado a 20 productos esenciales, navegación categorizada, buscador instantáneo, identidad visual institucional (*"Parrilleros UTEM"*), carrito lateral accesible y pasarela de checkout en modo de prueba Sandbox.
2. **Etapa 2 (Desarrollo Multiparadigma en Python):** Programación del núcleo lógico del Carrito Evento Especial bajo tres paradigmas disímiles: **Imperativo**, **Orientado a Objetos (POO)** y **Funcional**. Dicho desarrollo se efectuó bajo supervisión analítica de Inteligencia Artificial generativa, documentando los prompts de diseño, identificando anomalías algorítmicas y verificando que las tres soluciones alcancen una paridad matemática exacta ante las mismas entradas.

### 1.4 Estructura del informe
El documento expone a continuación las bases teóricas de los paradigmas y la ingeniería de prompts (Capítulo 2); documenta la configuración, wireframes y evidencias de la tienda virtual (Capítulo 3); describe el manual de reglas de negocio del evento (Capítulo 4); desglosa el análisis técnico, iteraciones de prompting, códigos de contraste y correcciones de fallas de IA por paradigma (Capítulo 5); detalla las instrucciones del programa ejecutable y la suite de pruebas unitarias (Capítulo 6); concluye con reflexiones epistemológicas sobre el rol del ingeniero frente a la IA (Capítulo 7); presenta las referencias bibliográficas en norma APA 7 (Capítulo 8); y finaliza con los Anexos A, B y C que contienen el registro íntegro de prompts, el código fuente completo y los outputs de consola.

---

## 2. MARCO TEÓRICO

### 2.1 Paradigma imperativo en Python
El paradigma imperativo se sustenta teóricamente en la arquitectura de Von Neumann, en la cual el cómputo se modela como una sucesión determinista de instrucciones secuenciales que modifican el estado interno de la memoria a través de asignaciones destructivas (Sebesta, 2019). En el lenguaje Python, este estilo se concreta mediante el uso de variables mutables, estructuras de datos modificables en caliente (como listas y diccionarios) y mecanismos de control de flujo explícitos tales como bucles `for`, bucles condicionales `while` y bifurcaciones condicionales `if/elif/else` (Van Rossum & Drake, 2024).

Como argumentan Gabbrielli y Martini (2023), la fortaleza del paradigma imperativo radica en su transparencia conceptual y en la correspondencia directa entre las instrucciones de alto nivel y los ciclos de reloj del procesador. No obstante, su debilidad intrínseca estriba en la gestión de efectos colaterales (*side effects*): cuando múltiples subrutinas modifican estructuras de datos compartidas, la trazabilidad del estado se degrada exponencialmente, dificultando la depuración y limitando la concurrencia segura en sistemas de misión crítica.

### 2.2 Paradigma orientado a objetos en Python
La Programación Orientada a Objetos (POO) organiza el dominio del problema en una red de entidades discretas y autónomas denominadas **objetos**, los cuales encapsulan tanto su estado interno (atributos protegidos) como sus operaciones permitidas (métodos) (Weisfeld, 2020). De acuerdo con Lutz (2013), Python implementa la POO a través de clases dinámicas que soportan herencia múltiple, polimorfismo dinámico (*duck typing*) y métodos especiales de sobrecarga de operadores.

Para resolver problemas comerciales complejos sin generar código acoplado, la literatura especializada destaca el uso de patrones de diseño. En particular, el patrón **Strategy** (Estrategia) permite encapsular familias de algoritmos intercambiables detrás de una interfaz común (Gamma et al., 1994). Como expone Martin (2018) en los principios SOLID, la aplicación del principio *Open/Closed* (abierto a la extensión, cerrado a la modificación) faculta a los desarrolladores a añadir nuevas reglas de descuento y promociones como clases polimórficas independientes sin alterar la clase raíz `Carrito`, garantizando una alta modularidad y mantenibilidad arquitectónica.

### 2.3 Paradigma funcional en Python
El paradigma funcional concibe el software como un conjunto de evaluaciones matemáticas de funciones puras, proscribiendo el estado mutable y los efectos secundarios colaterales (Abelson & Sussman, 1996). Bird (2014) señala que la propiedad fundamental de este paradigma es la *transparencia referencial*: una expresión puede sustituirse por su valor de evaluación en cualquier momento sin alterar el comportamiento global del sistema, lo que otorga predictibilidad y facilita el razonamiento formal sobre el código.

Aunque Python es un lenguaje multiparadigma con orientación imperativa predominante, incorpora primitivas funcionales robustas (Ramalho, 2022). Entre ellas destacan las colecciones inmutables (`tuple`, `frozenset`), funciones de orden superior nativas (`map()`, `filter()`), funciones lambda anónimas y utilidades de plegado como `reduce()` en el módulo `functools` (Chiusano & Bjarnason, 2014). Mediante la composición de funciones puras, es posible procesar pedidos mediante *pipelines* de transformación de datos donde cada etapa genera una nueva estructura inmutable sin alterar los registros originales del catálogo.

### 2.4 Inteligencia Artificial generativa, prompting y e-commerce
La masificación de modelos de lenguaje de gran escala (LLMs) ha revolucionado los flujos de ingeniería de software. White et al. (2023) introducen el *Prompt Engineering* como un catálogo formal de patrones para orientar a los sistemas de IA hacia la generación sistemática de código limpio, pruebas y arquitecturas desacopladas. No obstante, diversas investigaciones advierten que los modelos de IA generativa adolecen de sesgos estocásticos, propensión a inventar interfaces inexistentes ("alucinaciones") y una notable dificultad para resolver restricciones sutiles de negocio sin supervisión experta (Bubeck et al., 2023; Chen et al., 2021).

En el ámbito del comercio electrónico, donde los errores aritméticos de stock o cobro conllevan pérdidas financieras directas, el rol del desarrollador muta de un simple codificador manual a un **auditor técnico y supervisor de código**. El estudiante universitario debe dominar la comprensión línea por línea del código asistido por IA, la identificación de fallas lógicas de empaquetado o tipos de datos, y el diseño de baterías automatizadas de pruebas de regresión que certifiquen la exactitud de los algoritmos.

---

## 3. ETAPA 1: MONTAJE DE LA TIENDA

### 3.1 Plataforma y configuración general
Se montó y parametrizó la tienda en línea oficial bajo el nombre comercial **"Parrilleros UTEM - Supermercado del Asado"**. La tienda opera con un catálogo ampliado de **20 productos** categorizados y cuenta con un servidor e-commerce local de demostración continua (`servidor_tienda.py`), compatible con despliegue en la nube (Render / Railway) y con exportación masiva para Shopify Partners en `data/catalogo_shopify.csv`.

Se configuró la tienda con moneda de curso legal chilena (**CLP**), almacén centralizado e inventario físico inicial.

### 3.2 Elementos mínimos obligatorios
1. **Catálogo y Navegación:** El catálogo comprende 20 productos de alta fidelidad organizados en cinco categorías principales:
   * *Carnes & Embutidos:* Lomo Vetado Vacuno ($14.990/kg, stock: 3.0 kg), Sobrecostilla Vacuno ($9.990/kg, stock: 15.0 kg), Chorizo Parrillero Artesanal ($4.990/pack, stock: 20 packs), Entraña Vacuno Nacional ($18.990/kg, stock: 8.0 kg), Punta Picana ($12.990/kg, stock: 10.0 kg), Longaniza Tradicional de Chillán ($5.490/pack, stock: 15 packs), Prietas con Nuez ($4.290/pack, stock: 12 packs).
   * *Vegetariano:* Hamburguesa de Lentejas/Garbanzos ($3.990/pack, stock: 10 packs), Pimiento Morrón Rojo ($1.200/u, stock: 30 u), Queso Provolone para Parrilla ($3.990/u, stock: 20 u), Champiñones Portobello Gigantes ($2.490/bandeja, stock: 18 b.), Choclos Dulces Selección ($1.990/malla, stock: 25 m.).
   * *Carbón & Fuego:* Carbón Vegetal Espino 2.5kg ($3.500/bolsa, stock: 12 bolsas), Carbón Quebracho Blanco 4kg ($5.990/bolsa, stock: 15 bolsas), Iniciador de Fuego Ecológico 24u ($1.990/caja, stock: 30 cajas).
   * *Sales & Abarrotes:* Sal Parrillera Gruesa 1kg ($1.500/bolsa, stock: 25 bolsas), Chimichurri Parrillero Artesanal 250ml ($2.990/frasco, stock: 22 frascos).
   * *Bebidas & Jugos:* Bebida Gaseosa 2.5L ($2.500/botella, stock: 18 botellas), Jugo Natural Naranja Plátano 1.5L ($2.990/botella, stock: 20 botellas), Agua Mineral con Gas 1.6L ($1.490/botella, stock: 35 botellas).
2. **Carrito y Checkout:** Carrito lateral (*drawer*) interactivo, con visualización de subtotales, cálculo en vivo de descuento por Combo Parrillero (-10%), cantidades ajustables y botón de compra directa.
3. **Pasarela de Pagos en Modo de Prueba (Sandbox):** Pasarela configurada en modo académico que permite simular pagos con tarjeta de crédito de prueba (`4524 •••• •••• 9999` o Bogus Gateway de Shopify), aprobando la transacción y generando un número de orden oficial `#UTEM-2026-XXXX` sin transaccionar dinero real.
4. **Identidad Visual:** Tema gráfico responsivo con paleta retail limpia inspirada en **Jumbo.cl** (#00843D, #006830, #111827, #FFFFFF, acentos en #C92A2A), banners panorámicos con contraste legible e isotipo representativo de la Universidad Tecnológica Metropolitana.

### 3.3 Elementos recomendados incorporados
* **Control de Stock en Tiempo Real con Alertas:** Configuración de insignias visuales de stock bajo (`⚠️ Stock Crítico: 3 kg`) en el *Lomo Vetado Vacuno*, garantizando transparencia al consumidor.
* **Mapeo de Sustitutos en Inventario:** Registro de metadatos de relación entre productos (el Lomo Vetado tiene como sustituto preconfigurado la Sobrecostilla en caso de quiebre de stock; la Entraña se sustituye por Sobrecostilla; la Longaniza por Chorizo; y los Champiñones por Pimiento).
* **Asistente Inteligente IA Integrado al Frontend:** Modal de cotización automática que se conecta vía `POST /api/carrito-evento` con el backend en Python para transferir la propuesta directamente al carrito web.

### 3.4 Evidencias de funcionamiento (URL, arquitectura visual y marcadores de captura)
* **URL Pública en la Nube:** Tienda alojada en Render / Railway / Tiendanube con enlace activo reportado en la plataforma CANVAS.
* **Servidor Local Autónomo:** Despliegue en red local mediante `python3 servidor_tienda.py` accesible en `http://localhost:8000`.
* **Exportador Oficial Shopify:** Endpoint activo en `http://localhost:8000/api/export/shopify.csv`.

---

#### Evidencia Visual 1: Portada Retail, Banners Panorámicos y Buscador Inteligente
*(Insértese aquí la captura de pantalla de la portada principal)*  
`[PEGAR CAPTURA 1 AQUÍ: Portada Retail, Banners Panorámicos y Buscador Inteligente en Tiempo Real]`

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  PARRILLEROS UTEM · TIENDA OFICIAL                   [Buscar producto...] 🛒 │
├──────────────────────────────────────────────────────────────────────────────┤
│  [Todos (20)]  [Carnes (6)]  [Vegetariano (5)]  [Carbón (3)]  [Bebidas (4)]  │
├──────────────────────────────────────────────────────────────────────────────┤
│  BANNER HERO: "El Mejor Asado Empieza Aquí — Especial Temporada 2026"        │
│  [ ⚡ Armar Asado Automático con IA ]   [ Ver Todo el Catálogo ]             │
└──────────────────────────────────────────────────────────────────────────────┘
```
*Figura 1: Arquitectura visual de la tienda virtual retail "Parrilleros UTEM".*

---

#### Evidencia Visual 2: Catálogo Navegable con Badges de Stock Crítico y Descuento Combo
*(Insértese aquí la captura de pantalla de la grilla de productos con stepper de cantidad)*  
`[PEGAR CAPTURA 2 AQUÍ: Catálogo Navegable de 20 Productos con Badges de Stock Crítico y Descuento Combo]`

```text
┌──────────────────────┬──────────────────────┬────────────────────────────────┐
│ Lomo Vetado Vacuno   │ Sobrecostilla Vacuno │ Chorizo Parrillero Artesanal   │
│ $14.990 / kg         │ $9.990 / kg          │ $4.990 / pack (5 u)            │
│ [⚠️ Stock: 3.0 kg]   │ [Stock: 15.0 kg]     │ [Stock: 20 packs]              │
│ [ 10% Dcto Combo ]   │ [ 10% Dcto Combo ]   │ [ 10% Dcto Combo ]             │
│ [ -  1  + ]          │ [ + Agregar ]        │ [ + Agregar ]                  │
└──────────────────────┴──────────────────────┴────────────────────────────────┘
```
*Figura 2: Grilla de productos con control interactivo de cantidad en la misma tarjeta.*

---

#### Evidencia Visual 3: Ficha Técnica Modal de Producto con Política de Sustitución
*(Insértese aquí la captura de pantalla del modal de detalle de producto)*  
`[PEGAR CAPTURA 3 AQUÍ: Ficha Técnica Modal de Producto con Política de Sustitución por Quiebre de Stock]`

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  FICHA DEL PRODUCTO: Lomo Vetado Vacuno (SKU: prod_01)                       │
├──────────────────────────────────────────────────────────────────────────────┤
│  • Marca: Carnes Selección UTEM      • Precio: $14.990 CLP / kg              │
│  • Stock Disponible: 3.0 kg en bodega central                                │
│  ⚠️ Regla de Bodega: Si las existencias en bodega se agotan (3.0 kg disp.),  │
│     el motor sustituye automáticamente por Sobrecostilla Vacuno.             │
│  [ + Agregar a mi pedido ]                                                   │
└──────────────────────────────────────────────────────────────────────────────┘
```
*Figura 3: Modal de ficha técnica con política automatizada de sustitución.*

---

#### Evidencia Visual 4: Modal del Asistente 'Armar Asado Inteligente' (Integración Python)
*(Insértese aquí la captura del modal IA ejecutando el backend Python en tiempo real)*  
`[PEGAR CAPTURA 4 AQUÍ: Modal del Asistente 'Armar Asado Inteligente' con Diagnóstico en Vivo del Backend Python]`

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  🔥 ARMAR ASADO INTELIGENTE (ASISTENTE IA CON BACKEND PYTHON)                │
├──────────────────────────────────────────────────────────────────────────────┤
│  Adultos: [10]  Niños: [4]  Vegetarianos: [2]  Presupuesto: [$120.000]       │
│  Corte: [Lomo Vetado (Stock 3kg)]   Paradigma: [POO (Strategy SOLID)]        │
│  --------------------------------------------------------------------------  │
│  ✔ Diagnóstico del Motor:                                                    │
│    • Quiebre de Stock: 3.0 kg Lomo Vetado + 1.1 kg Sobrecostilla sustituto.   │
│    • Descuento Combo Parrillero: -$7.943 CLP (10% en Carnes + Carbón + Sal)   │
│    • Total Calculado: $91.866 CLP                                            │
│  [ 🛒 Cargar esta propuesta directamente a mi Carrito ]                      │
└──────────────────────────────────────────────────────────────────────────────┘
```
*Figura 4: Integración en vivo con el motor multiparadigma Python vía POST /api/carrito-evento.*

---

#### Evidencia Visual 5: Carrito Lateral Drawer con Cálculo Dinámico del Combo Parrillero
*(Insértese aquí la captura del carrito lateral con desglose de ítems y descuento)*  
`[PEGAR CAPTURA 5 AQUÍ: Carrito Lateral Drawer con Cálculo Dinámico del 10% Descuento Combo Parrillero]`

```text
┌───────────────────────────────────────────────────────┐
│ TU CARRITO DE ASADO                               [X] │
├───────────────────────────────────────────────────────┤
│ • Lomo Vetado Vacuno (3.0 kg)             $44.970 CLP │
│ • Sobrecostilla Vacuno (1.1 kg)           $10.989 CLP │
│ • Chorizo Parrillero (3 packs)            $14.970 CLP │
│ • Hamburguesas Legumbres (2 packs)         $7.980 CLP │
│ • Pimiento Morrón Rojo (2 unidades)        $2.400 CLP │
│ • Carbón Vegetal Espino (2 bolsas)         $7.000 CLP │
│ • Sal Parrillera Gruesa (1 bolsa)          $1.500 CLP │
│ • Bebida Gaseosa 2.5L (4 botellas)        $10.000 CLP │
├───────────────────────────────────────────────────────┤
│ Subtotal Neto:                            $99.809 CLP │
│ Combo Parrillero (-10%):                  -$7.943 CLP │
│ TOTAL A PAGAR:                            $91.866 CLP │
│ [ Continuar al Pago Sandbox ➔ ]                       │
└───────────────────────────────────────────────────────┘
```
*Figura 5: Carrito lateral con cálculo automático de promociones y desglose.*

---

#### Evidencia Visual 6: Comprobante de Venta Electrónica en Modo Sandbox
*(Insértese aquí la captura del comprobante final emitido tras el pago simulado)*  
`[PEGAR CAPTURA 6 AQUÍ: Modal de Comprobante de Venta Electrónica Aprobada en Modo Sandbox (Orden #UTEM-2026-XXXX)]`

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  ✔ PAGO APROBADO (MODO SANDBOX)                                              │
│  COMPROBANTE DE VENTA ELECTRÓNICA — ORDEN #UTEM-2026-8941                    │
├──────────────────────────────────────────────────────────────────────────────┤
│  Fecha: 29/11/2026 14:32 hrs  ·  Tarjeta: 4524 •••• •••• 9999 (Sandbox)     │
│  Comercio: Parrilleros UTEM   ·  Estado: Acreditado sin transacción real     │
│  --------------------------------------------------------------------------  │
│  TOTAL PAGADO: $91.866 CLP (8 productos suministrados)                       │
│  [ 🖨️ Imprimir Boleta ]   [ Cerrar y Nuevo Pedido ]                           │
└──────────────────────────────────────────────────────────────────────────────┘
```
*Figura 6: Comprobante formal de compra sandbox generado sin recurrir a alerts nativos.*

---

### 3.5 Decisiones de configuración justificadas
1. **Modelado Monetario sin Centavos:** Dado que la legislación tributaria y el sistema bancario chileno eliminaron el uso de centavos en el peso (CLP), la tienda y los algoritmos redondean todos los precios al entero más próximo (`float(round(monto))`), previniendo discrepancias de decimales e incompatibilidades con Webpay/Transbank.
2. **Restricción Intencionada de Stock en Bodega:** Se fijó el inventario físico inicial de Lomo Vetado en exactamente **3.0 kg** con el objetivo técnico expreso de forzar el quiebre de stock en eventos de mediana envergadura, permitiendo evidenciar el correcto funcionamiento del algoritmo de sustitución en la Etapa 2.
3. **Estandarización de Identificadores (SKU):** Se establecieron identificadores únicos (`prod_01` a `prod_20`) asociados a categorías semánticas fijas (`carnico`, `vegetariano`, `carbon`, `sal`, `abarrote`, `bebida`), posibilitando la interoperabilidad entre el catálogo web y los tres scripts en Python.

---

## 4. ETAPA 2: CARRITO EVENTO ESPECIAL

### 4.1 Manual de reglas del carrito: cómo las define el equipo y cómo se las entrega a la IA
El equipo especificó el manual de reglas a la Inteligencia Artificial mediante especificaciones funcionales formales, divididas en cuatro dimensiones operativas:

1. **Dimensionamiento Paramétrico de Raciones:**
   * *Carne Vacuna:* 350 gramos (0,35 kg) por comensal adulto; 150 gramos (0,15 kg) por niño. Demanda total calculada mediante:  
     Kilos Carne = (adultos * 0.35) + (ninos * 0.15)
   * *Choripanes:* 1 chorizo por comensal carnívoro. Se comercializan en packs cerrados de 5 unidades, redondeando hacia arriba:  
     Packs Chorizo = ceil((adultos + ninos) / 5.0)
   * *Menú Vegetariano:* 1 pack de hamburguesas de legumbres y 1 pimiento morrón por cada comensal vegetariano.
   * *Carbón Vegetal:* 1 bolsa de 2,5 kg por cada 3 kg de carne vacuna a asar:  
     Bolsas Carbon = ceil(Kilos Carne / 3.0)
   * *Sal Parrillera:* 1 bolsa de 1 kg obligatoria si el evento congrega a más de 5 personas en total.
   * *Bebidas:* 0,5 litros por persona en botellas de 2,5 litros:  
     Botellas Bebida = ceil((Total Personas * 0.5) / 2.5)

2. **Quiebre de Stock y Sustitución Automática:**
   Si la demanda de carne vacuna supera el stock físico de bodega del corte preferido (*Lomo Vetado*, $14.990), el sistema consume los 3.0 kg disponibles hasta agotarlo y transfiere automáticamente los kilogramos faltantes al SKU sustituto (*Sobrecostilla*, $9.990), documentando el desglose en la boleta.

3. **Promoción Comercial 'Combo Parrillero':**
   Si la orden de compra incorpora de forma simultánea ítems de categoría cárnica, carbón vegetal y sal parrillera, se aplica un **10% de descuento** sobre el subtotal acumulado de dichos productos, redondeado al peso entero:  
   Descuento = round((Subtotal Carnico + Subtotal Carbon + Subtotal Sal) * 0.10)

4. **Gestión Activa del Presupuesto:**
   Si el total final excede el presupuesto máximo estipulado por el cliente, el sistema ejecuta una secuencia inteligente de optimización:
   * *Paso A:* Degrada la calidad del corte vacuno (de Lomo Vetado a Sobrecostilla).
   * *Paso B:* Si aún se excede el presupuesto, reduce las bebidas al mínimo esencial (1 botella).
   * *Paso C:* Si persiste el exceso, reduce los chorizos a 1 pack esencial.
   * *Transparencia:* Registra explícitamente en la boleta los ajustes aplicados para conocimiento del cliente. En el caso oficial de 10 adultos, 4 niños y 2 vegetarianos con un presupuesto restringido a $45.000 CLP, los tres paradigmas aplican los tres pasos y convergen unánimemente en **$61.884 CLP**, alertando de forma transparente la imposibilidad de reducir más sin desabastecer las raciones de alimento.

### 4.2 Modalidades de uso
* **Modalidad Automática:** Permite generar un carrito exprés con solo indicar el número total de asistentes (ej. *"Hazme un carrito para 10 personas"*). El sistema aplica una distribución representativa (80% adultos, 20% niños), proyecta un presupuesto referencial y arma el pedido optimizado.
* **Modalidad Interactiva:** Permite al usuario parametrizar por teclado la cantidad exacta de adultos, niños, vegetarianos, presupuesto límite y corte preferido, activando optimización si se sobrepasa el monto.
* **Modalidad Defensa Académica:** Entorno especializado que procesa el dataset oficial de prueba (10 adultos, 4 niños, 2 vegetarianos), imprime la tabla comparativa *Side-by-Side* y ejecuta las pruebas de equivalencia.

### 4.3 Integración con la tienda
La integración es **aditiva**: el script en Python no altera la plataforma de e-commerce, sino que lee de forma directa los productos desde el catálogo exportado (`catalogo_tienda.json` o endpoint REST `/api/products`), garantizando total desacoplamiento. Además, el frontend web invoca directamente el endpoint `POST /api/carrito-evento` para procesar la compra en tiempo real.

---

## 5. DESARROLLO Y ANÁLISIS POR PARADIGMA

### 5.1 Versión Imperativa (`src/imperativo/carrito_imperativo.py`)

#### 5.1.1 Prompt de especificación
> *"Actúa como desarrollador Full-Stack Senior. Necesito programar el Carrito Evento Especial para un asado en Python bajo un enfoque 100% imperativo. Los productos deben leerse desde `catalogo_tienda.json` para simular la base de datos de la tienda. El flujo debe ser estrictamente secuencial, utilizando variables mutables, listas modificadas con `.append()`, bucles `for` y sentencias condicionales `if/elif`. Debe incluir cálculo de raciones, sustitución por quiebre de stock, descuento por combo y ajuste de presupuesto."*

#### 5.1.2 Secuencia de prompts utilizados
* **3 Prompts Iniciales:** Prompt 1 (arquitectura secuencial e integración de datos), Prompt 2 (estructuración del inventario mutable) y Prompt 3 (fórmulas lineales de raciones).
* **3 Prompts de Desarrollo:** Prompt 4 (algoritmo condicional de sustitución por quiebre de stock), Prompt 5 (flags booleanas para Combo Parrillero) y Prompt 6 (redondeo hacia arriba con `math.ceil`).
* **3 Prompts Finales:** Prompt 7 (algoritmo iterativo de gestión de presupuesto), Prompt 8 (menú interactivo por consola) y Prompt 9 (redondeo a enteros en pesos CLP).

#### 5.1.3 Análisis exhaustivo del código generado
El código organiza la computación de forma procedural en la función `procesar_carrito_imperativo`. La mutabilidad es omnipresente: la lista `items_carrito` crece mediante invocaciones a `.append()`, el stock del catálogo local se reduce destructivamente (`corte["stock"] -= consumo`) y las variables acumuladoras (`subtotal_general += ...`) cambian de valor paso a paso.

#### 5.1.4 Análisis de la operación en ejecución
Al ejecutarse con el dataset oficial (10 adultos, 4 niños, 2 vegetarianos, presupuesto $120.000):
1. Demanda de carne: 10 * 0.35 + 4 * 0.15 = 4.10 kg.
2. Agota los 3.0 kg de Lomo Vetado ($44.970) y asigna 1.10 kg de Sobrecostilla ($10.989).
3. Asigna 3 packs de chorizos ($14.970), menú vegetariano ($10.380), carbón ($7.000), sal ($1.500) y bebidas ($10.000).
4. Subtotal neto: **$99.809 CLP**.
5. Combo parrillero (Carnes + Carbón + Sal = $79.429): Descuento 10% = **-$7.943 CLP**.
6. Total final a pagar: **$91.866 CLP**.

#### 5.1.5 Ajustes a reglas que no se ejecutaban correctamente
* **Problema:** Truncamiento indebido de packs cerrados de embutidos por división entera.
* **Código erróneo propuesto por la IA:**
```python
# ERROR DE IA: División entera trunca y desabastece a comensales
total_carnivoros = adultos + ninos
packs_chorizo = total_carnivoros // 5  # Para 14 personas: 14 // 5 = 2 packs (10 unidades)
```
* **Prompt de corrección formulado por el equipo:**
> *"El cálculo de chorizos es erróneo porque con división entera 14 // 5 da 2 packs (10 chorizos), dejando a 4 comensales sin choripán. Los packs son unidades indivisibles cerradas de 5 unidades. Aplica math.ceil((adultos + ninos) / 5.0) para asegurar que se compren 3 packs (15 unidades)."*
* **Código corregido y validado:**
```python
import math
total_carnivoros = adultos + ninos
packs_chorizo = math.ceil(total_carnivoros / 5.0)  # Para 14 personas: math.ceil(2.8) = 3 packs
```

#### 5.1.6 Reparaciones cuando la IA "delira" o no cumple lo solicitado
* **Delirio de la IA:** Exclusión de los chorizos artesanales del descuento Combo Parrillero. La IA interpretó erróneamente que "carne" se refería única y exclusivamente a los cortes vacunos, cobrando $1.497 de más en el total final ($85.363 en vez de $79.429 de base de descuento).
* **Prompt de reparación:**
> *"La regla del combo parrillero aplica un 10% de descuento sobre toda la categoría cárnica consumida en el asado, lo cual incluye expresamente al chorizo parrillero (prod_03). Modifica la lógica para sumar el subtotal de chorizos a la base imponible del combo, y redondea el descuento a entero sin decimales (CLP)."*
* **Código corregido:**
```python
subtotal_combo = subtotal_carne_vacuna + subtotal_chorizo + subtotal_carbon + subtotal_sal
descuento_combo = float(round(subtotal_combo * 0.10))
```

#### 5.1.7 Evidencias y output
Ejecución en consola verificada: Subtotal: $99.809 CLP, Descuento: -$7.943 CLP, Total: **$91.866 CLP**.

---

### 5.2 Versión Orientada a Objetos (`src/poo/`)

#### 5.2.1 Prompt de especificación
> *"Diseña la versión del Carrito Evento Especial bajo el paradigma Orientado a Objetos en Python. Modela las entidades del dominio: `Producto`, `ItemCarrito` y `Carrito`. Protege el stock mediante encapsulamiento y métodos internos `consumir_stock()`. Aplica el patrón de diseño Strategy mediante una clase abstracta `ReglaDescuento` para que el carrito aplique promociones de forma polimórfica sin acoplamiento."*

#### 5.2.2 Secuencia de prompts utilizados
* **3 Prompts Iniciales:** Prompt 10 (identificación de entidades y principios SOLID), Prompt 11 (encapsulamiento del stock en `Producto`) y Prompt 12 (entidad `ItemCarrito`).
* **3 Prompts de Desarrollo:** Prompt 13 (patrón Strategy con `ReglaDescuento(ABC)`), Prompt 14 (estrategia concreta `ReglaComboParrillero`) y Prompt 15 (servicio de dominio `PlanificadorAsadoPOO`).
* **3 Prompts Finales:** Prompt 16 (método factoría y serialización de boleta), Prompt 17 (alineación de categoría cárnica en POO) y Prompt 18 (soporte interactivo y de pruebas).

#### 5.2.3 Análisis exhaustivo del código generado
El código separa estrictamente la estructura del dominio (`modelos.py`) de la orquestación (`carrito_poo.py`). Se destaca el encapsulamiento: el mundo exterior no puede modificar arbitrariamente el stock; debe solicitarlo a través de `consumir_stock(cantidad)`, que valida si las existencias alcanzan. El patrón Strategy desacopla las promociones: la clase `Carrito` desconoce la fórmula matemática del combo; simplemente itera sobre una lista de estrategias registradas invocando `regla.calcular_descuento(self)`.

#### 5.2.4 Análisis de la operación en ejecución
El orquestador carga el catálogo JSON, construye el mapa de instancias `Producto` y planifica cada necesidad delegando en métodos de instancia. Produce exactamente el mismo desglose de 8 ítems, $99.809 de subtotal, $7.943 de descuento y **$91.866 CLP** de total final.

#### 5.2.5 Ajustes a reglas que no se ejecutaban correctamente
* **Problema:** En el ajuste presupuestario, la mutación de estado en los objetos dejaba el inventario en 0 para reintentos sucesivos.
* **Código erróneo propuesto por la IA:**
```python
# ERROR DE IA: Reintenta sobre las mismas instancias ya consumidas destructivamente
if carrito.calcular_total() > presupuesto:
    # El stock de lomo ya fue consumido a 0.0 en el primer intento; el reintento falla catastróficamente
    carrito_ajustado = planificador.armar_plan(corte_economico)
```
* **Prompt de corrección formulado por el equipo:**
> *"Al simular ajustes de presupuesto en POO, las instancias Producto mantienen su _stock mutado. Implementa el método simular_plan() en PlanificadorAsadoPOO que re-instancie un grafo limpio e independiente de objetos para cada escenario de optimización."*
* **Código corregido y validado:**
```python
def simular_plan(self, corte_preferido, reducir_bebidas=False, reducir_chorizos=False):
    # Reconstruye un mapa de productos fresco y desacoplado
    prods_frescos = self._clonar_productos()
    carrito_sim = Carrito(prods_frescos)
    # Ejecuta el plan de forma aislada
    return carrito_sim
```

#### 5.2.6 Reparaciones cuando la IA delira
* **Delirio de la IA:** Error fatal de importación circular en Python (`ImportError: cannot import name 'Carrito' from partially initialized module`). La IA intentó tipar `calcular_descuento(self, carrito: Carrito)` antes de que la clase `Carrito` estuviese definida en `modelos.py`.
* **Prompt de reparación:**
> *"Se produjo un ImportError por dependencia circular en modelos.py. No intentes importar Carrito antes de su definición; utiliza anotaciones de tipo como string 'Carrito' o importa from __future__ import annotations."*
* **Código corregido:**
```python
from __future__ import annotations
from abc import ABC, abstractmethod

class ReglaDescuento(ABC):
    @abstractmethod
    def calcular_descuento(self, carrito: "Carrito") -> Tuple[float, str]:
        pass
```

#### 5.2.7 Evidencias y output
Ejecución en consola verificada: 8 ítems generados, paridad numérica idéntica al imperativo (**$91.866 CLP**).

---

### 5.3 Versión Funcional (`src/funcional/carrito_funcional.py`)

#### 5.3.1 Prompt de especificación
> *"Implementa el Carrito Evento Especial bajo el paradigma de programación funcional en Python. Prohíbe el uso de clases con estado mutable, listas modificadas con `.append()` y bucles `for` tradicionales. Utiliza tuplas inmutables (`tuple`), funciones puras con transparencia referencial y funciones de orden superior (`filter`, `map`, `reduce`) para transformar los datos y calcular los totales."*

#### 5.3.2 Secuencia de prompts utilizados
* **3 Prompts Iniciales:** Prompt 19 (inmutabilidad y colecciones `tuple`), Prompt 20 (búsqueda pura con `filter()` y lambdas) y Prompt 21 (constructores puros `crear_item`).
* **3 Prompts de Desarrollo:** Prompt 22 (quiebre de stock puramente declarativo), Prompt 23 (evaluación con `any(map(...))` y `reduce()`) y Prompt 24 (pipeline de composición integral).
* **3 Prompts Finales:** Prompt 25 (purificación y proscripción de bucles mutables), Prompt 26 (verificación de paridad) y Prompt 27 (interoperabilidad de entrada).

#### 5.3.3 Análisis exhaustivo del código generado
El script constituye un pipeline de funciones puras. Cada requerimiento del evento se procesa mediante funciones atómicas independientes (`resolver_carne_con_sustitucion`, `resolver_choripanes`, `resolver_insumos`, etc.) que retornan tuplas inmutables. La consolidación de ítems no utiliza bucles acumuladores, sino concatenación de tuplas. El cálculo del subtotal y los descuentos delega íntegramente en `functools.reduce()`, aplicando la reducción de forma puramente declarativa.

#### 5.3.4 Análisis de la operación en ejecución
El pipeline procesa los datos sin generar un solo efecto secundario sobre el catálogo de entrada. Al recibir los mismos parámetros, retorna exactamente la misma boleta con $99.809 de subtotal, $7.943 de descuento y **$91.866 CLP** de total final.

#### 5.3.5 Ajustes a reglas que no se ejecutaban correctamente
* **Problema:** En `resolver_insumos()`, la sentencia de retorno estaba anidada dentro del condicional de personas, y se empleaban listas mutables con `.append()`.
* **Código erróneo propuesto por la IA:**
```python
# ERROR DE IA: Violación de inmutabilidad y retorno condicional fallido
items = []
if kilos_carne > 0:
    items.append(item_carbon)
if total_personas > 5:
    items.append(item_sal)
    return tuple(items)  # Falla: retorna None para <= 5 personas
```
* **Prompt de corrección formulado por el equipo:**
> *"Corrige de inmediato el error de indentación en resolver_insumos() para que siempre retorne la tupla de ítems. Además, elimina todas las listas mutables [] y llamadas a .append(). Utiliza exclusivamente tuplas inmutables y el operador de concatenación pura (+), retornando la tupla de forma garantizada."*
* **Código corregido y validado:**
```python
def resolver_insumos(catalogo: Tuple[dict, ...], kilos_carne: float, total_personas: int) -> Tuple[dict, ...]:
    items: Tuple[dict, ...] = ()
    if kilos_carne > 0:
        items = items + (item_carbon,)
    if total_personas > 5:
        items = items + (item_sal,)
    return items  # Retorno incondicional de tupla pura
```

#### 5.3.6 Reparaciones cuando la IA delira
* **Delirio de la IA:** Uso encubierto de un bucle `for` acumulador dentro de una función para calcular el subtotal, rompiendo la filosofía declarativa.
* **Prompt de reparación:**
> *"Encontré un bucle 'for item in items: total += item[subtotal]' en la función de totalización. Elimina inmediatamente el bucle procedural y reemplázalo por functools.reduce con una expresión lambda acumuladora pura."*
* **Código corregido:**
```python
import functools

subtotal_general = float(functools.reduce(
    lambda acumulador, item: acumulador + item["subtotal"], 
    items, 
    0.0
))
```

#### 5.3.7 Evidencias y output
Ejecución en consola verificada: 8 ítems inmutables generados, paridad numérica exacta (**$91.866 CLP**).

---

### 5.4 Comparación analítica de las tres versiones

| Criterio de Comparación | Paradigma Imperativo | Paradigma Orientado a Objetos (POO) | Paradigma Funcional |
| :--- | :--- | :--- | :--- |
| **Manejo de Estado** | Estado mutable en diccionarios y variables locales en caliente. | Estado protegido y encapsulado en atributos de clase (`_stock`). | Inmutabilidad estricta mediante tuplas (`tuple`) y registros puros. |
| **Control de Flujo** | Procedural paso a paso mediante bucles `for` y bifurcaciones `if/else`. | Envío polimórfico de mensajes entre objetos del dominio. | Pipeline declarativo de composición de funciones puras. |
| **Efectos Secundarios** | Frecuentes (muta destructivamente el inventario en memoria). | Controlados y restringidos al interior de cada entidad. | **Cero efectos secundarios** (transparencia referencial absoluta). |
| **Cálculo de Promociones** | Banderas booleanas (`flags`) y sumatorias manuales. | Patrón **Strategy** polimórfico (`ReglaDescuento`). | Predicados puros con `filter()` y sumatoria con `functools.reduce()`. |
| **Mantenibilidad y Extensión** | Baja (alta propensión a introducir errores al modificar el flujo). | Alta (cumple principios SOLID; cerrado a modificación, abierto a extensión). | Muy alta (código determinista, predecible y altamente paralelizable). |
| **Total Obtenido (Dataset Oficial Base)** | **$91.866 CLP** | **$91.866 CLP** | **$91.866 CLP** |
| **Total con Ajuste Presupuestario ($45k)** | **$61.884 CLP** | **$61.884 CLP** | **$61.884 CLP** |

---

## 6. PROGRAMA EJECUTABLE

### 6.1 Requisitos de entorno e instalación
* **Sistema Operativo:** Multiplataforma (Linux, Windows, macOS).
* **Entorno de Ejecución:** Python 3.8 o superior (probado en Python 3.12).
* **Dependencias Externas:** **Ninguna**. El sistema fue construido íntegramente sobre la biblioteca estándar de Python (`json`, `math`, `functools`, `abc`, `unittest`, `http.server`, `sys`, `os`), por lo que no requiere `pip install` ni configuración de entornos virtuales complejos.

### 6.2 Instrucciones de uso en ambas modalidades
Para iniciar el demostrador interactivo unificado, ejecute en la terminal:
```bash
python3 main.py
```
El sistema desplegará el menú interactivo principal:
* `[1] Modo Interactivo:` Permite parametrizar por teclado adultos, niños, vegetarianos, presupuesto y corte preferido. Aplica optimización si se excede el presupuesto y permite elegir el paradigma a ejecutar.
* `[2] Modo Automático:` Resuelve el dimensionamiento exprés indicando solo la cantidad de personas (ej: *"para 10 personas"*).
* `[3] Modo Defensa Académica:` Diseñado para la comisión docente; ejecuta el dataset oficial del informe, despliega el cuadro comparativo *Side-by-Side* y ejecuta las pruebas de equivalencia.
* `[4] Tienda Web en Vivo:` Levanta el servidor e-commerce local en `http://localhost:8000` con catálogo, carrito y checkout sandbox demostrable.
* `[0] Salir`

### 6.3 Verificación de paridad matemática (Suite de 6 pruebas unitarias con unificación presupuestaria)
Para certificar formalmente que las tres implementaciones son matemáticamente equivalentes y cumplen con las reglas de negocio, se diseñó la suite automatizada `tests/test_equivalencia.py`. Para ejecutarla directamente:
```bash
python3 -m unittest tests/test_equivalencia.py -v
```
Las 6 pruebas unitarias verifican:
1. `test_paridad_cantidad_de_items`: Las tres versiones generan exactamente 8 ítems en el caso oficial.
2. `test_paridad_subtotal_neto`: Subtotal neto idéntico de $99.809 CLP.
3. `test_paridad_descuento_promocion`: Descuento del Combo Parrillero idéntico de $7.943 CLP.
4. `test_paridad_total_final`: Total final a pagar idéntico de **$91.866 CLP**.
5. `test_paridad_regla_sustitucion_stock`: Quiebre de stock verificado (3.0 kg Lomo Vetado + 1.1 kg Sobrecostilla).
6. `test_paridad_optimizacion_activa_presupuesto`: Ante presupuesto restringido ($45.000) en el caso oficial, las tres versiones aplican degradación de corte, reducción de bebidas y embutidos, convergiendo unificadamente en **$61.884 CLP**.

---

## 7. CONCLUSIONES

### 7.1 Síntesis
El proyecto resolvió satisfactoriamente el desafío propuesto por la cátedra de Lenguajes de Programación de la Universidad Tecnológica Metropolitana, integrando con éxito una tienda de comercio electrónico funcional con un motor aditivo de Carrito Evento Especial implementado bajo tres paradigmas computacionales disímiles pero rigurosamente equivalentes.

### 7.2 Comparación de los tres paradigmas en Python
Python demostró ser un entorno multiparadigma versátil y robusto:
1. El paradigma **imperativo** resulta el más intuitivo para prototipos rápidos y scripts lineales, pero su dependencia del estado mutable lo hace vulnerable a errores sutiles de concurrencia y dificulta el mantenimiento a medida que crecen las reglas comerciales.
2. El paradigma **orientado a objetos** ofrece la mejor estructura para modelar sistemas empresariales escalables, permitiendo desacoplar reglas comerciales complejas mediante patrones de diseño formales como *Strategy*, encapsulando el inventario y facilitando el trabajo en equipos grandes.
3. El paradigma **funcional** proporciona el mayor nivel de rigor matemático y estabilidad operativa: al eliminar la mutabilidad y garantizar la transparencia referencial, previene de raíz errores imprevistos de estado, simplifica radicalmente las pruebas de software y asegura predictibilidad absoluta en cálculos financieros.

### 7.3 Reflexión crítica sobre el uso y supervisión de agentes de IA
La experiencia de desarrollo evidenció que las herramientas de IA generativa constituyen aceleradores extraordinarios de productividad, pero carecen de criterio de negocio y comprensión profunda del contexto operativo sin supervisión humana. Durante las iteraciones, la IA incurrió en fallas significativas: truncó raciones por divisiones enteras indebidas, generó dependencias circulares en clases, intentó introducir mutabilidad encubierta en funciones funcionales y descuidó la naturaleza sin centavos del peso chileno. 

La intervención analítica y experta del estudiante de ingeniería resultó estrictamente indispensable para guiar el prompting, auditar cada línea de código generado, detectar inconsistencias arquitectónicas y diseñar pruebas automatizadas que garantizaran la corrección del software. La IA asiste la escritura de código, pero la responsabilidad sobre la corrección técnica recae siempre en el ingeniero.

### 7.4 Proyecciones técnicas
Como trabajo futuro se proyecta empaquetar el motor funcional en una arquitectura de microservicios *serverless* en la nube, y conectarlo a la API de Shopify y Tiendanube mediante *Webhooks* transaccionales en tiempo real para sincronizar las compras de carritos especiales directamente en la pasarela de pago.

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

# ANEXOS (EVIDENCIAS DE RESPALDO COMPLETAS)

## ANEXO A. REGISTRO COMPLETO DE PROMPTS Y SUPERVISIÓN DE IA

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


---

## ANEXO B. CÓDIGO FUENTE COMENTADO DE LAS TRES VERSIONES

### B.1 Versión Imperativa (`src/imperativo/carrito_imperativo.py`)
```python
"""
MÓDULO DE CARRITO DE COMPRAS - PARADIGMA IMPERATIVO
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

CARACTERÍSTICAS DEL PARADIGMA IMPERATIVO APLICADAS AQUÍ:
1. Control de flujo explícito y secuencial (paso a paso).
2. Estado mutable: variables que se reasignan y listas que crecen con .append().
3. Efectos secundarios (Side Effects): mutación directa del inventario del catálogo.
4. Acumulación manual de subtotales mediante bucles for y sentencias if/elif.
5. Gestión Activa del Presupuesto: Si el total supera el presupuesto máximo,
   aplica reglas de degradación de calidad de corte y reducción de extras.
"""

import os
import json
import math
import sys
from typing import Union, Optional

# Agregamos la ruta base para poder importar los módulos utilitarios
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos


def buscar_producto_por_id(catalogo: dict, id_producto: str):
    """
    Recorre secuencialmente la lista de productos buscando coincidencia por ID.
    Enfoque imperativo: búsqueda lineal tradicional con bucle 'for' y 'break'.
    """
    producto_encontrado = None
    for p in catalogo["productos"]:
        if p["id"] == id_producto:
            producto_encontrado = p
            break
    return producto_encontrado


def procesar_carrito_imperativo(
    ruta_catalogo: str, 
    evento_input: Union[str, dict, None] = None,
    interactivo: bool = False
) -> dict:
    """
    Ejecuta toda la lógica de negocio del carrito mediante sentencias imperativas.
    Modifica el estado del inventario y acumula resultados en variables locales mutables.
    Incluye algoritmo de optimización y ajuste activo si se sobrepasa el presupuesto.
    """
    # 1. Carga imperativa del catálogo desde el JSON
    with open(ruta_catalogo, "r", encoding="utf-8") as f_cat:
        catalogo = json.load(f_cat)

    # 2. Resolución de los datos del evento
    if interactivo:
        evento = solicitar_datos_interactivos("Imperativo")
    elif isinstance(evento_input, dict):
        evento = evento_input
    elif isinstance(evento_input, str):
        with open(evento_input, "r", encoding="utf-8") as f_eve:
            evento = json.load(f_eve)
    else:
        ruta_def = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        with open(ruta_def, "r", encoding="utf-8") as f_eve:
            evento = json.load(f_eve)

    comensales = evento["comensales"]
    adultos = comensales["adultos"]
    ninos = comensales["ninos"]
    vegetarianos = comensales["vegetarianos"]
    total_personas = adultos + ninos + vegetarianos
    presupuesto_max = evento.get("presupuesto_maximo")

    # Función interna imperativa para generar la boleta según parámetros actuales
    def calcular_propuesta(corte_vacuno_id: str, botellas_deseadas: Optional[int] = None, packs_chori_deseados: Optional[int] = None):
        items = []
        subtotal_gen = 0.0
        subtotal_combo = 0.0
        tiene_c = False
        tiene_carb = False
        tiene_s = False

        # Copia de trabajo del catálogo para no viciar recálculos
        with open(ruta_catalogo, "r", encoding="utf-8") as f:
            cat_local = json.load(f)

        # Carne vacuna
        kilos_vac = round((adultos * 0.35) + (ninos * 0.15), 2)
        corte_pref = buscar_producto_por_id(cat_local, corte_vacuno_id)

        if corte_pref and kilos_vac > 0:
            stock_disp = corte_pref["stock"]
            if stock_disp < kilos_vac:
                kilos_cub = stock_disp
                kilos_fal = round(kilos_vac - kilos_cub, 2)

                if kilos_cub > 0:
                    corte_pref["stock"] = 0.0
                    sub1 = round(kilos_cub * corte_pref["precio"], 2)
                    subtotal_gen += sub1
                    subtotal_combo += sub1
                    tiene_c = True
                    items.append({
                        "id": corte_pref["id"],
                        "nombre": corte_pref["nombre"],
                        "cantidad": kilos_cub,
                        "unidad": corte_pref["unidad"],
                        "precio_unitario": corte_pref["precio"],
                        "subtotal": sub1,
                        "nota": f"Stock agotado. Se utilizaron los {kilos_cub} kg disponibles."
                    })

                id_sust = corte_pref.get("sustituto_id")
                sust = buscar_producto_por_id(cat_local, id_sust) if id_sust else None
                if sust and sust["stock"] >= kilos_fal:
                    sust["stock"] -= kilos_fal
                    sub_sust = round(kilos_fal * sust["precio"], 2)
                    subtotal_gen += sub_sust
                    subtotal_combo += sub_sust
                    tiene_c = True
                    items.append({
                        "id": sust["id"],
                        "nombre": sust["nombre"],
                        "cantidad": kilos_fal,
                        "unidad": sust["unidad"],
                        "precio_unitario": sust["precio"],
                        "subtotal": sub_sust,
                        "nota": f"Sustituto activado por falta de stock de {corte_pref['nombre']}."
                    })
            else:
                corte_pref["stock"] -= kilos_vac
                sub = round(kilos_vac * corte_pref["precio"], 2)
                subtotal_gen += sub
                subtotal_combo += sub
                tiene_c = True
                items.append({
                    "id": corte_pref["id"],
                    "nombre": corte_pref["nombre"],
                    "cantidad": kilos_vac,
                    "unidad": corte_pref["unidad"],
                    "precio_unitario": corte_pref["precio"],
                    "subtotal": sub,
                    "nota": None
                })

        # Chorizos
        carnivoros = adultos + ninos
        if carnivoros > 0:
            packs_calc = math.ceil(carnivoros / 5.0) if packs_chori_deseados is None else packs_chori_deseados
            prod_chori = buscar_producto_por_id(cat_local, "prod_03")
            prod_chori["stock"] -= packs_calc
            sub_chori = packs_calc * prod_chori["precio"]
            subtotal_gen += sub_chori
            subtotal_combo += sub_chori

            items.append({
                "id": prod_chori["id"],
                "nombre": prod_chori["nombre"],
                "cantidad": packs_calc,
                "unidad": prod_chori["unidad"],
                "precio_unitario": prod_chori["precio"],
                "subtotal": sub_chori,
                "nota": f"Calculado para {carnivoros} choripanes (packs de 5 u.)."
            })

        # Menú Vegetariano
        if vegetarianos > 0:
            prod_hamb = buscar_producto_por_id(cat_local, "prod_04")
            prod_pim = buscar_producto_por_id(cat_local, "prod_05")
            sub_hamb = vegetarianos * prod_hamb["precio"]
            sub_pim = vegetarianos * prod_pim["precio"]
            subtotal_gen += sub_hamb + sub_pim

            items.append({
                "id": prod_hamb["id"],
                "nombre": prod_hamb["nombre"],
                "cantidad": vegetarianos,
                "unidad": prod_hamb["unidad"],
                "precio_unitario": prod_hamb["precio"],
                "subtotal": sub_hamb,
                "nota": f"Ración especial para {vegetarianos} comensal(es) vegetariano(s)."
            })
            items.append({
                "id": prod_pim["id"],
                "nombre": prod_pim["nombre"],
                "cantidad": vegetarianos,
                "unidad": prod_pim["unidad"],
                "precio_unitario": prod_pim["precio"],
                "subtotal": sub_pim,
                "nota": None
            })

        # Carbón y Sal
        if kilos_vac > 0:
            bolsas_carb = math.ceil(kilos_vac / 3.0)
            prod_carb = buscar_producto_por_id(cat_local, "prod_06")
            sub_carb = bolsas_carb * prod_carb["precio"]
            subtotal_gen += sub_carb
            subtotal_combo += sub_carb
            tiene_carb = True

            items.append({
                "id": prod_carb["id"],
                "nombre": prod_carb["nombre"],
                "cantidad": bolsas_carb,
                "unidad": prod_carb["unidad"],
                "precio_unitario": prod_carb["precio"],
                "subtotal": sub_carb,
                "nota": f"Calculado según {kilos_vac} kg de carne (1 bolsa cada 3 kg)."
            })

        if total_personas > 5:
            prod_sal = buscar_producto_por_id(cat_local, "prod_07")
            sub_sal = 1 * prod_sal["precio"]
            subtotal_gen += sub_sal
            subtotal_combo += sub_sal
            tiene_s = True

            items.append({
                "id": prod_sal["id"],
                "nombre": prod_sal["nombre"],
                "cantidad": 1,
                "unidad": prod_sal["unidad"],
                "precio_unitario": prod_sal["precio"],
                "subtotal": sub_sal,
                "nota": "Requerido para eventos mayores a 5 personas."
            })

        # Bebidas
        if total_personas > 0:
            litros = total_personas * 0.5
            botellas_calc = math.ceil(litros / 2.5) if botellas_deseadas is None else botellas_deseadas
            prod_beb = buscar_producto_por_id(cat_local, "prod_08")
            sub_beb = botellas_calc * prod_beb["precio"]
            subtotal_gen += sub_beb

            items.append({
                "id": prod_beb["id"],
                "nombre": prod_beb["nombre"],
                "cantidad": botellas_calc,
                "unidad": prod_beb["unidad"],
                "precio_unitario": prod_beb["precio"],
                "subtotal": sub_beb,
                "nota": f"Calculado para {litros}L totales (0.5L por comensal)."
            })

        # Promoción Combo Parrillero
        desc = 0.0
        det_prom = ""
        if tiene_c and tiene_carb and tiene_s:
            desc = float(round(subtotal_combo * 0.10))
            det_prom = "Combo Parrillero (10% en Carne + Carbón + Sal)"

        tot = float(round(subtotal_gen - desc))
        return items, subtotal_gen, desc, det_prom, tot

    # Cálculo de la propuesta inicial
    id_corte_solicitado = evento["preferencias"].get("tipo_corte_preferido", "prod_01")
    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = calcular_propuesta(id_corte_solicitado)

    # -------------------------------------------------------------------------
    # REGLA DE NEGOCIO AVANZADA: GESTIÓN ACTIVA DE PRESUPUESTO
    # Si el total supera el presupuesto máximo, el sistema ajusta automáticamente:
    # 1. Degrada la calidad del corte (de Lomo Vetado a Sobrecostilla).
    # 2. Si aún supera, ajusta bebidas al mínimo esencial.
    # 3. Si aún supera, ajusta chorizos a 1 pack esencial.
    # -------------------------------------------------------------------------
    ajustes_presupuesto = []
    
    if presupuesto_max and total_pagar > presupuesto_max:
        # Intento 1: Si pidió Lomo Vetado (prod_01), degradamos a Sobrecostilla (prod_02)
        if id_corte_solicitado == "prod_01":
            items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta("prod_02")
            if tot_t < total_pagar:
                items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                ajustes_presupuesto.append("Se degradó el corte de Lomo Vetado ($14.990) a Sobrecostilla ($9.990) para reducir costos.")

        # Intento 2: Si todavía supera el presupuesto, reducimos bebidas a 1 botella mínima
        if total_pagar > presupuesto_max and total_personas > 0:
            litros_totales = total_personas * 0.5
            botellas_originales = math.ceil(litros_totales / 2.5)
            if botellas_originales > 1:
                items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta(
                    corte_vacuno_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                    botellas_deseadas=1
                )
                if tot_t < total_pagar:
                    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujeron las bebidas a 1 botella básica para acercarse al presupuesto.")

        # Intento 3: Si todavía supera, reducimos chorizos a 1 pack esencial
        if total_pagar > presupuesto_max and (adultos + ninos) > 0:
            packs_originales = math.ceil((adultos + ninos) / 5.0)
            if packs_originales > 1:
                items_t, sub_t, desc_t, det_t, tot_t = calcular_propuesta(
                    corte_vacuno_id="prod_02" if id_corte_solicitado == "prod_01" else id_corte_solicitado,
                    botellas_deseadas=1,
                    packs_chori_deseados=1
                )
                if tot_t < total_pagar:
                    items, subtotal_general, descuento_total, detalle_promocion, total_pagar = items_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto.append("Se redujo el embutido a 1 pack de chorizos para ajustar el gasto.")

    alerta_presupuesto = None
    if presupuesto_max and total_pagar > presupuesto_max:
        alerta_presupuesto = f"Incluso con ajustes mínimos, el total ({formato_moneda(total_pagar)}) excede el presupuesto ({formato_moneda(presupuesto_max)})."

    boleta_final = {
        "evento": evento["nombre_evento"],
        "items": items,
        "subtotal": subtotal_general,
        "descuento": descuento_total,
        "detalle_descuento": detalle_promocion,
        "total": total_pagar,
        "presupuesto_maximo": presupuesto_max,
        "ajustes_presupuesto": ajustes_presupuesto,
        "alerta_presupuesto": alerta_presupuesto
    }

    return boleta_final


if __name__ == "__main__":
    ruta_cat = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
    if not os.path.exists(ruta_cat):
        ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

    print("\n" + "═" * 68)
    print(" SISTEMA CARRITO EVENTO ESPECIAL — PARADIGMA IMPERATIVO")
    print("═" * 68)
    print(" [1] Modo Automático (Dataset oficial de prueba UTEM)")
    print(" [2] Modo Interactivo (Ingresar datos y presupuesto por teclado)")
    print("═" * 68)
    opc = input("Seleccione una opción [1 o 2, Default: 1]: ").strip()

    if opc == "2":
        boleta = procesar_carrito_imperativo(ruta_cat, interactivo=True)
    else:
        ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        boleta = procesar_carrito_imperativo(ruta_cat, ruta_eve)

    imprimir_resumen_carrito(boleta, "Imperativo")
    
    if boleta.get("ajustes_presupuesto"):
        print("\n🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
        for aj in boleta["ajustes_presupuesto"]:
            print(f"   • {aj}")
        print()

    if boleta.get("alerta_presupuesto"):
        print(f"⚠️  {boleta['alerta_presupuesto']}\n")

```

---

### B.2 Versión Orientada a Objetos: Modelos y Patrón Strategy (`src/poo/modelos.py`)
```python
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

```

---

### B.3 Versión Orientada a Objetos: Orquestador del Carrito (`src/poo/carrito_poo.py`)
```python
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

```

---

### B.4 Versión Funcional: Pipeline Puro Declarativo (`src/funcional/carrito_funcional.py`)
```python
"""
MÓDULO DE CARRITO DE COMPRAS - PARADIGMA FUNCIONAL
Asignatura: Lenguajes de Programación (UTEM)
Tema: Carrito Evento Especial (Asado Parrillero)

PRINCIPIOS FUNDAMENTALES DEL PARADIGMA FUNCIONAL APLICADOS AQUÍ:
1. Funciones Puras: No producen efectos secundarios (no mutan variables ni el catálogo).
2. Inmutabilidad: Se trabaja con tuplas y estructuras no mutadas; las modificaciones
   generan nuevas estructuras de datos en lugar de alterar las existentes.
3. Funciones de Orden Superior: Uso intensivo de `map()`, `filter()` y `reduce()`.
4. Composición de Funciones: El flujo del carrito es un pipeline de transformaciones
   que toma un estado inicial inmutable y produce el reporte final.
5. Optimización Presupuestaria Pura: Evaluación de transformaciones alternativas
   para ajustar el total al presupuesto sin mutar datos.
"""

import os
import sys
import json
import math
from functools import reduce
from typing import Tuple, Dict, Any, List, Union, Optional

# Agregamos la ruta base para imports
DIRECTORIO_RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(DIRECTORIO_RAIZ)

from src.utils.visualizador import imprimir_resumen_carrito, formato_moneda
from src.utils.interactivo import solicitar_datos_interactivos


# -----------------------------------------------------------------------------
# 1. FUNCIONES PURAS DE CONSULTA Y CÁLCULO ATÓMICO (Sin Efectos Secundarios)
# -----------------------------------------------------------------------------

def obtener_producto_por_id(catalogo: Tuple[Dict[str, Any], ...], id_prod: str) -> Dict[str, Any]:
    """
    Función pura que busca un producto mediante 'filter'.
    No altera la colección original.
    """
    coincidencias = tuple(filter(lambda p: p["id"] == id_prod, catalogo))
    return coincidencias[0] if coincidencias else {}


def crear_item(producto: Dict[str, Any], cantidad: float, nota: Any = None) -> Dict[str, Any]:
    """
    Función pura constructora de un registro inmutable de línea de carrito.
    """
    cant = round(cantidad, 2)
    sub = round(cant * producto["precio"], 2)
    return {
        "id": producto["id"],
        "nombre": producto["nombre"],
        "categoria": producto["categoria"],
        "cantidad": cant,
        "unidad": producto["unidad"],
        "precio_unitario": producto["precio"],
        "subtotal": sub,
        "nota": nota
    }


# -----------------------------------------------------------------------------
# 2. TRANSFORMACIONES FUNCIONALES DE DEMANDA Y REGLAS DE NEGOCIO
# -----------------------------------------------------------------------------

def resolver_carne_con_sustitucion(
    catalogo: Tuple[Dict[str, Any], ...], 
    id_corte: str, 
    adultos: int, 
    ninos: int
) -> Tuple[Dict[str, Any], ...]:
    """
    Resuelve funcionalmente la demanda de carne y el quiebre de stock.
    Usa exclusivamente tuplas inmutables y concatenación pura (+), sin listas mutables.
    """
    kilos_necesarios = round((adultos * 0.35) + (ninos * 0.15), 2)
    if kilos_necesarios <= 0:
        return ()

    corte_preferido = obtener_producto_por_id(catalogo, id_corte)
    stock_disponible = corte_preferido.get("stock", 0.0)

    if stock_disponible < kilos_necesarios:
        kilos_cubiertos = stock_disponible
        kilos_faltantes = round(kilos_necesarios - kilos_cubiertos, 2)
        
        items_res: Tuple[Dict[str, Any], ...] = ()
        if kilos_cubiertos > 0:
            item_agotado = crear_item(
                corte_preferido,
                kilos_cubiertos,
                f"Stock agotado. Se utilizaron los {kilos_cubiertos} kg disponibles."
            )
            items_res = items_res + (item_agotado,)

        id_sustituto = corte_preferido.get("sustituto_id")
        sustituto = obtener_producto_por_id(catalogo, id_sustituto)
        if sustituto and kilos_faltantes > 0:
            item_sustituto = crear_item(
                sustituto,
                kilos_faltantes,
                f"Sustituto activado por falta de stock de {corte_preferido['nombre']}."
            )
            items_res = items_res + (item_sustituto,)

        return items_res
    else:
        item_preferido = crear_item(corte_preferido, kilos_necesarios, None)
        return (item_preferido,)


def resolver_choripanes(
    catalogo: Tuple[Dict[str, Any], ...], 
    carnívoros: int, 
    packs_deseados: Optional[int] = None
) -> Tuple[Dict[str, Any], ...]:
    """Genera funcionalmente los packs de choripán necesarios."""
    if carnívoros <= 0:
        return ()
    packs = math.ceil(carnívoros / 5.0) if packs_deseados is None else packs_deseados
    prod = obtener_producto_por_id(catalogo, "prod_03")
    return (crear_item(prod, packs, f"Calculado para {carnívoros} choripanes (packs de 5 u.)."),)


def resolver_vegetarianos(catalogo: Tuple[Dict[str, Any], ...], vegetarianos: int) -> Tuple[Dict[str, Any], ...]:
    """Genera las raciones vegetarianas mediante una tupla compuesta inmutable."""
    if vegetarianos <= 0:
        return ()
    prod_hamb = obtener_producto_por_id(catalogo, "prod_04")
    prod_pim = obtener_producto_por_id(catalogo, "prod_05")
    
    item_hamb = crear_item(prod_hamb, vegetarianos, f"Ración especial para {vegetarianos} comensal(es) vegetariano(s).")
    item_pim = crear_item(prod_pim, vegetarianos, None)
    return (item_hamb, item_pim)


def resolver_insumos(
    catalogo: Tuple[Dict[str, Any], ...], 
    kilos_carne: float, 
    total_personas: int
) -> Tuple[Dict[str, Any], ...]:
    """
    Calcula carbón y sal mediante concatenación pura de tuplas inmutables.
    Garantiza que la tupla resultante se retorne correctamente incluso para <= 5 personas.
    """
    items: Tuple[Dict[str, Any], ...] = ()
    if kilos_carne > 0:
        bolsas_carbon = math.ceil(kilos_carne / 3.0)
        prod_carbon = obtener_producto_por_id(catalogo, "prod_06")
        if prod_carbon:
            item_carbon = crear_item(
                prod_carbon, 
                bolsas_carbon, 
                f"Calculado según {kilos_carne} kg de carne (1 bolsa cada 3 kg)."
            )
            items = items + (item_carbon,)

    if total_personas > 5:
        prod_sal = obtener_producto_por_id(catalogo, "prod_07")
        if prod_sal:
            item_sal = crear_item(
                prod_sal, 
                1, 
                "Requerido para eventos mayores a 5 personas."
            )
            items = items + (item_sal,)
    
    return items


def resolver_bebidas(
    catalogo: Tuple[Dict[str, Any], ...], 
    total_personas: int, 
    botellas_deseadas: Optional[int] = None
) -> Tuple[Dict[str, Any], ...]:
    """Calcula bebidas requeridas en formato funcional."""
    if total_personas <= 0:
        return ()
    litros = total_personas * 0.5
    botellas = math.ceil(litros / 2.5) if botellas_deseadas is None else botellas_deseadas
    prod_bebida = obtener_producto_por_id(catalogo, "prod_08")
    return (crear_item(prod_bebida, botellas, f"Calculado para {litros}L totales (0.5L por comensal)."),)


# -----------------------------------------------------------------------------
# 3. PIPELINE DE EVALUACIÓN DE DESCUENTOS Y AGREGACIONES CON REDUCE
# -----------------------------------------------------------------------------

def es_producto_combo(item: Dict[str, Any]) -> bool:
    """Predicado puro utilizado con 'filter' para identificar ítems afectos a promoción."""
    es_carne = item.get("categoria") == "carnico"
    es_carbon = item.get("id") == "prod_06"
    es_sal = item.get("id") == "prod_07"
    return es_carne or es_carbon or es_sal


def calcular_descuento_combo_funcional(items: Tuple[Dict[str, Any], ...]) -> Tuple[float, str]:
    """
    Aplica 'filter' y 'reduce' para evaluar la regla de descuento del combo parrillero.
    """
    tiene_carne = any(map(lambda it: it.get("categoria") == "carnico", items))
    tiene_carbon = any(map(lambda it: it.get("id") == "prod_06", items))
    tiene_sal = any(map(lambda it: it.get("id") == "prod_07", items))

    if tiene_carne and tiene_carbon and tiene_sal:
        items_combo = tuple(filter(es_producto_combo, items))
        subtotal_combo = reduce(lambda acc, it: acc + it["subtotal"], items_combo, 0.0)
        descuento = float(round(subtotal_combo * 0.10))
        return descuento, "Combo Parrillero (10% en Carne + Carbón + Sal)"

    return 0.0, ""


def calcular_pipeline_evento(
    catalogo: Tuple[Dict[str, Any], ...],
    datos_eve: dict,
    corte_id: str,
    botellas_deseadas: Optional[int] = None,
    packs_chori_deseados: Optional[int] = None
) -> Tuple[Tuple[Dict[str, Any], ...], float, float, str, float]:
    """Evalúa un pipeline funcional completo y retorna los resultados financieros."""
    comensales = datos_eve["comensales"]
    adultos = comensales["adultos"]
    ninos = comensales["ninos"]
    vegetarianos = comensales["vegetarianos"]
    carnívoros = adultos + ninos
    total_personas = adultos + ninos + vegetarianos

    items_carne = resolver_carne_con_sustitucion(catalogo, corte_id, adultos, ninos)
    kilos_carne = round((adultos * 0.35) + (ninos * 0.15), 2)
    items_chori = resolver_choripanes(catalogo, carnívoros, packs_chori_deseados)
    items_veg = resolver_vegetarianos(catalogo, vegetarianos)
    items_insumos = resolver_insumos(catalogo, kilos_carne, total_personas)
    items_bebidas = resolver_bebidas(catalogo, total_personas, botellas_deseadas)

    todos_los_items: Tuple[Dict[str, Any], ...] = (
        items_carne + items_chori + items_veg + items_insumos + items_bebidas
    )

    subtotal_general = round(
        reduce(lambda acc, it: acc + it["subtotal"], todos_los_items, 0.0),
        2
    )
    descuento, detalle_promocion = calcular_descuento_combo_funcional(todos_los_items)
    total_final = float(round(subtotal_general - descuento))

    return todos_los_items, subtotal_general, descuento, detalle_promocion, total_final


# -----------------------------------------------------------------------------
# 4. COMPOSICIÓN Y ORQUESTADOR PRINCIPAL (Pipeline Funcional)
# -----------------------------------------------------------------------------

def procesar_carrito_funcional(
    ruta_catalogo: str, 
    evento_input: Union[str, dict, None] = None,
    interactivo: bool = False
) -> dict:
    """
    Pipeline que carga los datos, ejecuta transformaciones puras encadenadas
    y aplica optimización activa por presupuesto sin efectos colaterales.
    """
    with open(ruta_catalogo, "r", encoding="utf-8") as f_cat:
        datos_cat = json.load(f_cat)

    if interactivo:
        datos_eve = solicitar_datos_interactivos("Funcional")
    elif isinstance(evento_input, dict):
        datos_eve = evento_input
    elif isinstance(evento_input, str):
        with open(evento_input, "r", encoding="utf-8") as f_eve:
            datos_eve = json.load(f_eve)
    else:
        ruta_def = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        with open(ruta_def, "r", encoding="utf-8") as f_eve:
            datos_eve = json.load(f_eve)

    catalogo_inmutable: Tuple[Dict[str, Any], ...] = tuple(datos_cat["productos"])
    id_corte_inicial = datos_eve["preferencias"].get("tipo_corte_preferido", "prod_01")
    presupuesto_max = datos_eve.get("presupuesto_maximo")

    # Evaluación inicial pura
    items, subtotal, descuento, detalle_prom, total = calcular_pipeline_evento(
        catalogo_inmutable, datos_eve, id_corte_inicial
    )

    ajustes_presupuesto: Tuple[str, ...] = ()
    comensales = datos_eve["comensales"]
    tot_personas = comensales["adultos"] + comensales["ninos"] + comensales["vegetarianos"]

    # -------------------------------------------------------------------------
    # GESTIÓN ACTIVA DE PRESUPUESTO EN EL PARADIGMA FUNCIONAL (INMUTABLE)
    # -------------------------------------------------------------------------
    if presupuesto_max and total > presupuesto_max:
        # Intento 1: Degradación pura de corte
        if id_corte_inicial == "prod_01":
            it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                catalogo_inmutable, datos_eve, "prod_02"
            )
            if tot_t < total:
                items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                ajustes_presupuesto = ajustes_presupuesto + ("Se degradó el corte de Lomo Vetado ($14.990) a Sobrecostilla ($9.990) para reducir costos.",)

        # Intento 2: Reducción pura de bebidas a 1 botella mínima
        if total > presupuesto_max and tot_personas > 0:
            if math.ceil((tot_personas * 0.5) / 2.5) > 1:
                it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                    catalogo_inmutable, datos_eve,
                    "prod_02" if id_corte_inicial == "prod_01" else id_corte_inicial,
                    botellas_deseadas=1
                )
                if tot_t < total:
                    items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto = ajustes_presupuesto + ("Se redujeron las bebidas a 1 botella básica para acercarse al presupuesto.",)

        # Intento 3: Reducción pura de embutidos a 1 pack esencial
        if total > presupuesto_max and (comensales["adultos"] + comensales["ninos"]) > 0:
            if math.ceil((comensales["adultos"] + comensales["ninos"]) / 5.0) > 1:
                it_t, sub_t, desc_t, det_t, tot_t = calcular_pipeline_evento(
                    catalogo_inmutable, datos_eve,
                    "prod_02" if id_corte_inicial == "prod_01" else id_corte_inicial,
                    botellas_deseadas=1,
                    packs_chori_deseados=1
                )
                if tot_t < total:
                    items, subtotal, descuento, detalle_prom, total = it_t, sub_t, desc_t, det_t, tot_t
                    ajustes_presupuesto = ajustes_presupuesto + ("Se redujo el embutido a 1 pack de chorizos para ajustar el gasto.",)

    alerta_presupuesto = None
    if presupuesto_max and total > presupuesto_max:
        alerta_presupuesto = f"Incluso con ajustes mínimos, el total ({formato_moneda(total)}) excede el presupuesto ({formato_moneda(presupuesto_max)})."

    return {
        "evento": datos_eve["nombre_evento"],
        "items": list(items),
        "subtotal": subtotal,
        "descuento": descuento,
        "detalle_descuento": detalle_prom,
        "total": total,
        "presupuesto_maximo": presupuesto_max,
        "ajustes_presupuesto": list(ajustes_presupuesto),
        "alerta_presupuesto": alerta_presupuesto
    }


if __name__ == "__main__":
    ruta_cat = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
    if not os.path.exists(ruta_cat):
        ruta_cat = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

    print("\n" + "═" * 68)
    print(" SISTEMA CARRITO EVENTO ESPECIAL — PARADIGMA FUNCIONAL")
    print("═" * 68)
    print(" [1] Modo Automático (Dataset oficial de prueba UTEM)")
    print(" [2] Modo Interactivo (Ingresar datos y presupuesto por teclado)")
    print("═" * 68)
    opc = input("Seleccione una opción [1 o 2, Default: 1]: ").strip()

    if opc == "2":
        boleta = procesar_carrito_funcional(ruta_cat, interactivo=True)
    else:
        ruta_eve = os.path.join(DIRECTORIO_RAIZ, "data", "evento_asado.json")
        boleta = procesar_carrito_funcional(ruta_cat, ruta_eve)

    imprimir_resumen_carrito(boleta, "Funcional")

    if boleta.get("ajustes_presupuesto"):
        print("\n🔧 AJUSTES APLICADOS POR LÍMITE DE PRESUPUESTO:")
        for aj in boleta["ajustes_presupuesto"]:
            print(f"   • {aj}")
        print()

    if boleta.get("alerta_presupuesto"):
        print(f"⚠️  {boleta['alerta_presupuesto']}\n")

```

---

## ANEXO C. OUTPUT COMPLETO DE LAS EJECUCIONES DE PRUEBA

### C.1 Salida Verbatim de la Suite de Pruebas Unitarias de Equivalencia
*(Comando ejecutado: `python3 -m unittest tests/test_equivalencia.py -v`)*

```text
test_paridad_cantidad_de_items (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_cantidad_de_items)
Verifica que los tres paradigmas generen exactamente las mismas 8 líneas de compra. ... ok
test_paridad_descuento_promocion (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_descuento_promocion)
Verifica que el descuento por 'Combo Parrillero' sea idéntico en las 3 versiones. ... ok
test_paridad_optimizacion_activa_presupuesto (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_optimizacion_activa_presupuesto)
Verifica que los tres paradigmas apliquen la misma optimización activa ante restricción presupuestaria ($45.000). ... ok
test_paridad_regla_sustitucion_stock (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_regla_sustitucion_stock)
Verifica que los tres paradigmas activen la sustitución de Lomo Vetado por Sobrecostilla. ... ok
test_paridad_subtotal_neto (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_subtotal_neto)
Verifica que el subtotal antes de descuentos sea idéntico en las 3 versiones. ... ok
test_paridad_total_final (tests.test_equivalencia.TestEquivalenciaMultiparadigma.test_paridad_total_final)
Verifica que el total final a pagar sea exactamente idéntico ($91.866 CLP). ... ok

----------------------------------------------------------------------
Ran 6 tests in 0.002s

OK
```

---

### C.2 Salida de Boleta de Venta del Caso Oficial Base (10 Adultos, 4 Niños, 2 Vegetarianos, $120.000 CLP)
*(Ejecución en las tres versiones con catálogo `catalogo_tienda.json` y evento `data/evento_asado.json`)*

```text
════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: IMPERATIVO
 Evento: Gran Asado Inauguración UTEM
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Lomo Vetado Vacuno                   3.0 kg    $14.990 CLP  $44.970 CLP
   ↳ [STOCK/REGLA]: Stock agotado. Se utilizaron los 3.0 kg disponibles.
Sobrecostilla Vacuno                 1.1 kg     $9.990 CLP  $10.989 CLP
   ↳ [STOCK/REGLA]: Sustituto activado por falta de stock de Lomo Vetado Vacuno.
Chorizo Parrillero Artesanal         3 pack     $4.990 CLP  $14.970 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               4 botella     $2.500 CLP  $10.000 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $99.809 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $7.943 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $91.866 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: ORIENTADO A OBJETOS (POO)
 Evento: Gran Asado Inauguración UTEM
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Lomo Vetado Vacuno                   3.0 kg    $14.990 CLP  $44.970 CLP
   ↳ [STOCK/REGLA]: Stock agotado. Se utilizaron los 3.0 kg disponibles.
Sobrecostilla Vacuno                 1.1 kg     $9.990 CLP  $10.989 CLP
   ↳ [STOCK/REGLA]: Sustituto activado por falta de stock de Lomo Vetado Vacuno.
Chorizo Parrillero Artesanal         3 pack     $4.990 CLP  $14.970 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               4 botella     $2.500 CLP  $10.000 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $99.809 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $7.943 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $91.866 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: FUNCIONAL
 Evento: Gran Asado Inauguración UTEM
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Lomo Vetado Vacuno                   3.0 kg    $14.990 CLP  $44.970 CLP
   ↳ [STOCK/REGLA]: Stock agotado. Se utilizaron los 3.0 kg disponibles.
Sobrecostilla Vacuno                 1.1 kg     $9.990 CLP  $10.989 CLP
   ↳ [STOCK/REGLA]: Sustituto activado por falta de stock de Lomo Vetado Vacuno.
Chorizo Parrillero Artesanal         3 pack     $4.990 CLP  $14.970 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               4 botella     $2.500 CLP  $10.000 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $99.809 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $7.943 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $91.866 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════════════
 CUADRO COMPARATIVO MULTIPARADIGMA — PARIDAD DE RESULTADOS (UTEM)
════════════════════════════════════════════════════════════════════════════════
Métrica / Indicador                 Imperativo             POO       Funcional
────────────────────────────────────────────────────────────────────────────────
Total de Ítems Generados                     8               8               8
Subtotal Neto                      $99.809 CLP     $99.809 CLP     $99.809 CLP
Descuento Combo Parrillero          $7.943 CLP      $7.943 CLP      $7.943 CLP
────────────────────────────────────────────────────────────────────────────────
TOTAL FINAL A PAGAR                $91.866 CLP     $91.866 CLP     $91.866 CLP
════════════════════════════════════════════════════════════════════════════════
  >>> ESTADO: [ÉXITO] Las 3 versiones producen EXACTAMENTE el mismo total. <<<
════════════════════════════════════════════════════════════════════════════════
```

---

### C.3 Salida de Boleta con Optimización Activa por Restricción Presupuestaria ($45.000 CLP -> $61.884 CLP)
*(Comprueba la degradación automática de corte a Sobrecostilla y ajuste de bebidas/chorizos convergiendo exactamente en $61.884 CLP)*

```text
════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: IMPERATIVO (OPTIMIZADO $61.884 CLP)
 Evento: Gran Asado UTEM (Presupuesto Ajustado $45.000)
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Sobrecostilla Vacuno                 4.1 kg     $9.990 CLP  $40.959 CLP
Chorizo Parrillero Artesanal         1 pack     $4.990 CLP   $4.990 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               1 botella     $2.500 CLP   $2.500 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $67.329 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $5.445 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $61.884 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: ORIENTADO A OBJETOS (OPTIMIZADO $61.884 CLP)
 Evento: Gran Asado UTEM (Presupuesto Ajustado $45.000)
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Sobrecostilla Vacuno                 4.1 kg     $9.990 CLP  $40.959 CLP
Chorizo Parrillero Artesanal         1 pack     $4.990 CLP   $4.990 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               1 botella     $2.500 CLP   $2.500 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $67.329 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $5.445 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $61.884 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════
 BOLETA DE VENTA OFICIAL — PARADIGMA: FUNCIONAL (OPTIMIZADO $61.884 CLP)
 Evento: Gran Asado UTEM (Presupuesto Ajustado $45.000)
════════════════════════════════════════════════════════════════════════
Producto                              Cant.    P. Unitario     Subtotal
────────────────────────────────────────────────────────────────────────
Sobrecostilla Vacuno                 4.1 kg     $9.990 CLP  $40.959 CLP
Chorizo Parrillero Artesanal         1 pack     $4.990 CLP   $4.990 CLP
   ↳ [STOCK/REGLA]: Calculado para 14 choripanes (packs de 5 u.).
Hamburguesa de Lentejas / G...       2 pack     $3.990 CLP   $7.980 CLP
   ↳ [STOCK/REGLA]: Ración especial para 2 comensal(es) vegetariano(s).
Pimiento Morrón Rojo               2 unidad     $1.200 CLP   $2.400 CLP
Carbón Vegetal Espino 2.5kg         2 bolsa     $3.500 CLP   $7.000 CLP
   ↳ [STOCK/REGLA]: Calculado según 4.1 kg de carne (1 bolsa cada 3 kg).
Sal Parrillera Gruesa 1kg           1 bolsa     $1.500 CLP   $1.500 CLP
   ↳ [STOCK/REGLA]: Requerido para eventos mayores a 5 personas.
Bebida Gaseosa 2.5L               1 botella     $2.500 CLP   $2.500 CLP
   ↳ [STOCK/REGLA]: Calculado para 8.0L totales (0.5L por comensal).
────────────────────────────────────────────────────────────────────────
Subtotal Neto:                                              $67.329 CLP
Descuento (Combo Parrillero (10% en Carne + Carbón + Sal)): - $5.445 CLP
════════════════════════════════════════════════════════════════════════
TOTAL FINAL A PAGAR:                                        $61.884 CLP
════════════════════════════════════════════════════════════════════════


════════════════════════════════════════════════════════════════════════════════
 CUADRO COMPARATIVO MULTIPARADIGMA — PARIDAD DE RESULTADOS (UTEM)
════════════════════════════════════════════════════════════════════════════════
Métrica / Indicador                 Imperativo             POO       Funcional
────────────────────────────────────────────────────────────────────────────────
Total de Ítems Generados                     7               7               7
Subtotal Neto                      $67.329 CLP     $67.329 CLP     $67.329 CLP
Descuento Combo Parrillero          $5.445 CLP      $5.445 CLP      $5.445 CLP
────────────────────────────────────────────────────────────────────────────────
TOTAL FINAL A PAGAR                $61.884 CLP     $61.884 CLP     $61.884 CLP
════════════════════════════════════════════════════════════════════════════════
  >>> ESTADO: [ÉXITO] Las 3 versiones producen EXACTAMENTE el mismo total. <<<
════════════════════════════════════════════════════════════════════════════════
```
