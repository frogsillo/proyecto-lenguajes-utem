import os
import sys
import json
import io
import subprocess
from contextlib import redirect_stdout

REPO_DIR = '/home/frog/.gemini/antigravity/scratch/proyecto_lenguajes'
sys.path.append(REPO_DIR)

from src.imperativo.carrito_imperativo import procesar_carrito_imperativo
from src.poo.carrito_poo import procesar_carrito_poo
from src.funcional.carrito_funcional import procesar_carrito_funcional
from src.utils.visualizador import imprimir_resumen_carrito
from main import mostrar_comparativa_side_by_side, RUTA_CATALOGO, RUTA_EVENTO_OFICIAL

# 1. Leer archivos de código
with open(os.path.join(REPO_DIR, 'src/imperativo/carrito_imperativo.py'), 'r', encoding='utf-8') as f:
    code_imp = f.read()

with open(os.path.join(REPO_DIR, 'src/poo/modelos.py'), 'r', encoding='utf-8') as f:
    code_modelos = f.read()

with open(os.path.join(REPO_DIR, 'src/poo/carrito_poo.py'), 'r', encoding='utf-8') as f:
    code_poo = f.read()

with open(os.path.join(REPO_DIR, 'src/funcional/carrito_funcional.py'), 'r', encoding='utf-8') as f:
    code_func = f.read()

with open(os.path.join(REPO_DIR, 'REGISTRO_PROMPTS.md'), 'r', encoding='utf-8') as f:
    registro_prompts_raw = f.read()

# 2. Capturar salida de pruebas unitarias
test_out = subprocess.check_output(
    ['python3', '-m', 'unittest', 'tests/test_equivalencia.py', '-v'],
    cwd=REPO_DIR,
    stderr=subprocess.STDOUT
).decode('utf-8')

# 3. Capturar ejecución del caso oficial
with open(RUTA_EVENTO_OFICIAL) as f:
    evento = json.load(f)

buf_oficial = io.StringIO()
with redirect_stdout(buf_oficial):
    b_imp = procesar_carrito_imperativo(RUTA_CATALOGO, evento)
    imprimir_resumen_carrito(b_imp, 'Imperativo')
    
    b_poo = procesar_carrito_poo(RUTA_CATALOGO, evento)
    imprimir_resumen_carrito(b_poo, 'Orientado a Objetos (POO)')
    
    b_fun = procesar_carrito_funcional(RUTA_CATALOGO, evento)
    imprimir_resumen_carrito(b_fun, 'Funcional')
    
    mostrar_comparativa_side_by_side(b_imp, b_poo, b_fun)
out_oficial = buf_oficial.getvalue()

# 4. Capturar ejecución de caso ajustado
evento_ajustado = dict(evento)
evento_ajustado['presupuesto_maximo'] = 45000.0
evento_ajustado['nombre_evento'] = 'Asado UTEM (Presupuesto Ajustado $45.000)'

buf_ajustado = io.StringIO()
with redirect_stdout(buf_ajustado):
    b_imp_aj = procesar_carrito_imperativo(RUTA_CATALOGO, evento_ajustado)
    imprimir_resumen_carrito(b_imp_aj, 'Imperativo (Optimizado)')
    
    b_poo_aj = procesar_carrito_poo(RUTA_CATALOGO, evento_ajustado)
    imprimir_resumen_carrito(b_poo_aj, 'Orientado a Objetos (Optimizado)')
    
    b_fun_aj = procesar_carrito_funcional(RUTA_CATALOGO, evento_ajustado)
    imprimir_resumen_carrito(b_fun_aj, 'Funcional (Optimizado)')
    
    mostrar_comparativa_side_by_side(b_imp_aj, b_poo_aj, b_fun_aj)
out_ajustado = buf_ajustado.getvalue()

cuerpo_principal = """# UNIVERSIDAD TECNOLÓGICA METROPOLITANA (UTEM)
## FACULTAD DE INGENIERÍA · DEPARTAMENTO DE INFORMÁTICA Y COMPUTACIÓN
### ESCUELA DE COMPUTACIÓN · ASIGNATURA: LENGUAJES DE PROGRAMACIÓN

---

# INFORME FINAL: DESARROLLO MULTIPARADIGMA EN PYTHON DE UN COMPONENTE DE E-COMMERCE CON ASISTENCIA DE IA GENERATIVA
### Tarea 1: Tienda en Línea y Carrito Evento Especial ("Asado Parrillero")

**Estudiante(s):** [Ingresa aquí tu Nombre Completo] — RUT: [xx.xxx.xxx-x]  
*(Si trabajas en equipo de 2 a 3 integrantes, incluir los nombres y RUTs de todos los participantes)*  
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
   3.4 Evidencias de funcionamiento (URL, arquitectura visual y capturas)  
   3.5 Decisiones de configuración  
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
   6.3 Verificación de paridad matemática (Suite formal de 6 pruebas unitarias)  
7. **Conclusiones**  
   7.1 Síntesis del proyecto  
   7.2 Comparación de los tres paradigmas en Python  
   7.3 Reflexión crítica sobre el uso y supervisión de agentes de IA  
   7.4 Proyecciones técnicas y profesionales  
8. **Referencias Bibliográficas (Norma APA 7ª Edición)**  
**Anexos (Evidencias de Respaldo Completas)**  
   * **Anexo A. Registro Completo de Prompts:** Transcripción íntegra de los 27 prompts, análisis de fallas y guión de defensa.  
   * **Anexo B. Código Fuente Comentado de las Tres Versiones:** Código íntegro de la versión Imperativa, POO y Funcional.  
   * **Anexo C. Output Completo de las Ejecuciones de Prueba:** Registro textual verbatim de pruebas unitarias y boletas de venta.

---

## 1. INTRODUCCIÓN

### 1.1 Tema: Carrito Evento Especial sobre una tienda en línea
El comercio electrónico moderno ha transitado desde simples interfaces transaccionales centradas en la búsqueda unitaria hacia sistemas guiados por el contexto de uso y las necesidades de los usuarios. En los portales habituales, cuando un consumidor organiza una celebración social o acontecimiento familiar, debe calcular mentalmente los insumos requeridos por comensal, buscar los cortes de carne, calcular bolsas de carbón, añadir bebidas y resolver manualmente situaciones imprevistas como la falta de existencias en bodega. 

Frente a este problema de usabilidad y fricción de compra, el presente proyecto diseña e implementa el **Carrito Evento Especial**, un componente aditivo e inteligente acoplado a una tienda virtual de mercado, diseñado para resolver de forma automatizada las compras orientadas a un evento masivo: el **"Asado Parrillero"**. El sistema dimensiona las raciones exactas según la composición demográfica de los asistentes (adultos, niños y vegetarianos), detecta quiebres de inventario en bodega sustituyendo automáticamente cortes agotados por alternativas equivalentes, aplica promociones comerciales empaquetadas (*Combo Parrillero*) y gestiona activamente el presupuesto asignado por el cliente para evitar órdenes sobregiradas.

### 1.2 Justificación de la plataforma elegida (Tiendanube / Shopify)
Para el desarrollo de la **Etapa 1** se seleccionó la plataforma **Tiendanube** (respaldada adicionalmente con plantillas de exportación para **Shopify** y un servidor e-commerce local en Python provisto en `servidor_tienda.py`). Tiendanube constituye la plataforma líder de comercio electrónico en América Latina para medianas y pequeñas empresas, con soporte nativo para el mercado chileno en moneda **CLP (Pesos Chilenos)**, administración de variantes por peso/unidad, pasarelas de pago configurables en modo de prueba (*sandbox*) sin requerir tarjetas bancarias reales y capacidades de importación masiva mediante CSV. 

Esta infraestructura permite desacoplar los datos operativos de la lógica computacional, garantizando que el desarrollo en Python consuma la base de datos de productos de manera fluida y aditiva sin alterar la arquitectura central de la plataforma de comercio electrónico.

### 1.3 Metodología de investigación y desarrollo
El trabajo se estructuró rigurosamente en dos etapas consecutivas y complementarias:
1. **Etapa 1 (Montaje de Tienda Operativa):** Configuración técnica de la plataforma en la nube, abarcando un catálogo de 8 productos esenciales, navegación categorizada, buscador interno, identidad visual institucional (*"Parrilleros UTEM"*), carrito accesible y pasarela de checkout en modo de prueba.
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
Se montó y parametrizó la tienda en línea oficial bajo el nombre comercial **"Parrilleros UTEM - Tienda Oficial"**. La tienda opera sobre **Tiendanube** (con respaldo de importación para **Shopify** provisto en `data/catalogo_shopify.csv`) y cuenta además con un servidor e-commerce local de demostración continua (`servidor_tienda.py`). Se configuró la tienda con moneda de curso legal chilena (**CLP**), almacén centralizado e inventario físico inicial.

### 3.2 Elementos mínimos obligatorios
1. **Catálogo y Navegación:** El catálogo comprende 8 productos esenciales para un evento parrillero, organizados en cuatro categorías:
   * *Carnes:* Lomo Vetado Vacuno ($14.990/kg, stock: 3.0 kg), Sobrecostilla Vacuno ($9.990/kg, stock: 15.0 kg), Chorizo Parrillero Artesanal ($4.990/pack, stock: 20 packs).
   * *Vegetariano:* Hamburguesa de Lentejas/Garbanzos ($3.990/pack, stock: 10 packs), Pimiento Morrón Rojo ($1.200/u, stock: 30 u).
   * *Abarrotes & Carbón:* Carbón Vegetal Espino 2.5kg ($3.500/bolsa, stock: 12 bolsas), Sal Parrillera Gruesa 1kg ($1.500/bolsa, stock: 25 bolsas).
   * *Bebidas:* Bebida Gaseosa 2.5L ($2.500/botella, stock: 18 botellas).  
   Incluye buscador inteligente por texto y fichas técnicas con unidades explícitas.
2. **Carrito y Checkout:** Carrito lateral (*drawer*) interactivo, con visualización clara de subtotales, cantidades ajustables y botón de compra directa.
3. **Pasarela de Pagos en Modo de Prueba (Sandbox):** Pasarela configurada en modo académico que permite simular pagos con tarjeta de crédito de prueba (`4524 •••• •••• 9999` o Bogus Gateway de Shopify), aprobando la transacción y generando un número de orden oficial sin transaccionar dinero real.
4. **Identidad Visual:** Tema gráfico responsivo con paleta cromática acorde al rubro gastronómico parrillero (#c92a2a, #1a1a1a, #f8f9fa), banners corporativos e isotipo representativo de la Universidad Tecnológica Metropolitana.

### 3.3 Elementos recomendados incorporados
* **Control de Stock en Tiempo Real con Alertas:** Configuración de insignias visuales de stock bajo (`⚠️ Stock Crítico: 3 kg`) en el *Lomo Vetado Vacuno*, garantizando transparencia al consumidor.
* **Mapeo de Sustitutos en Inventario:** Registro de metadatos de relación entre productos (el Lomo Vetado tiene como sustituto preconfigurado la Sobrecostilla en caso de quiebre de stock).

### 3.4 Evidencias de funcionamiento (URL, arquitectura visual y capturas)
* **URL Pública en la Nube:** Tienda alojada en Tiendanube / Shopify reportada en la plataforma de entrega de la cátedra.
* **Servidor Local Autónomo de Demostración:** Despliegue en red local mediante `python3 servidor_tienda.py` accesible en `http://localhost:8000`.
* **Esquemas Gráficos de las Pantallas Operativas (Wireframes y Capturas):**

#### Figura 1. Arquitectura visual de la tienda virtual "Parrilleros UTEM"
*(Home, navegación por categorías y buscador en tiempo real)*
```text
┌──────────────────────────────────────────────────────────────────────────────┐
│  PARRILLEROS UTEM · TIENDA OFICIAL                   [Buscar producto...] 🛒 │
├──────────────────────────────────────────────────────────────────────────────┤
│  [Todos]  [Carnes]  [Vegetariano]  [Abarrotes & Carbón]  [Bebidas]           │
├──────────────────────────────────────────────────────────────────────────────┤
│  BANNER: "Especial Asado UTEM — Calidad Premium garantizada para tu evento"  │
├──────────────────────┬──────────────────────┬────────────────────────────────┤
│ Lomo Vetado Vacuno   │ Sobrecostilla Vacuno │ Chorizo Parrillero Artesanal   │
│ $14.990 / kg         │ $9.990 / kg          │ $4.990 / pack (5 u)            │
│ [⚠️ Stock: 3.0 kg]   │ [Stock: 15.0 kg]     │ [Stock: 20 packs]              │
│ [ + Agregar ]        │ [ + Agregar ]        │ [ + Agregar ]                  │
└──────────────────────┴──────────────────────┴────────────────────────────────┘
```
*Nota: Representación esquemática de la portada y catálogo interactivo de la tienda montada en la Etapa 1.*

#### Figura 2. Carrito lateral y pasarela de checkout en modo Sandbox
*(Desglose de compra, simulación de pago académico y emisión de orden)*
```text
┌──────────────────────────────────────────────┬───────────────────────────────┐
│ CARRITO DE COMPRAS                           │ CHECKOUT (MODO SANDBOX)       │
├──────────────────────────────────────────────┼───────────────────────────────┤
│ • Lomo Vetado Vacuno (3.0 kg)   $44.970 CLP  │ Tarjeta: 4524 •••• •••• 9999  │
│ • Sobrecostilla Vacuno (1.1 kg) $10.989 CLP  │ Vencimiento: 12/28  CVV: 123  │
│ • Chorizo Parrillero (3 packs)  $14.970 CLP  ├───────────────────────────────┤
│ • Carbón Espino 2.5kg (2 b.)     $7.000 CLP  │ Total a Pagar:    $91.866 CLP │
│ • Sal Parrillera 1kg (1 b.)      $1.500 CLP  │ [ PAGAR PEDIDO DE PRUEBA ]    │
│ • Menú Vegetariano               $10.380 CLP ├───────────────────────────────┤
│ • Bebidas Gaseosas 2.5L (4 b.)   $10.000 CLP │ ESTADO: Aprobado (Sandbox)    │
│ Subtotal:                       $99.809 CLP  │ Orden Generada: #UTEM-2026-89 │
│ Descuento Combo Parrillero:    -$7.943 CLP  │ ¡Pago acreditado con éxito!   │
│ TOTAL:                          $91.866 CLP  │                               │
└──────────────────────────────────────────────┴───────────────────────────────┘
```
*Nota: Flujo del carrito de compras interactivo y pasarela de pago en modo de prueba académica.*

### 3.5 Decisiones de configuración justificadas
1. **Modelado Monetario sin Centavos:** Dado que la legislación tributaria y el sistema bancario chileno eliminaron el uso de centavos en el peso (CLP), la tienda y los algoritmos redondean todos los precios al entero más próximo (`float(round(monto))`), previniendo discrepancias de decimales e incompatibilidades con Webpay/Transbank.
2. **Restricción Intencionada de Stock en Bodega:** Se fijó el inventario físico inicial de Lomo Vetado en exactamente **3.0 kg** con el objetivo técnico expreso de forzar el quiebre de stock en eventos de mediana envergadura, permitiendo evidenciar el correcto funcionamiento del algoritmo de sustitución en la Etapa 2.
3. **Estandarización de Identificadores (SKU):** Se establecieron identificadores únicos (`prod_01` a `prod_08`) asociados a categorías semánticas fijas (`carnico`, `vegetariano`, `carbon`, `sal`, `bebida`), posibilitando la interoperabilidad entre el catálogo web y los tres scripts en Python.

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
   * *Transparencia:* Registra explícitamente en la boleta los ajustes aplicados para conocimiento del cliente.

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
* **Problema:** La IA intentó inicialmente utilizar listas nativas de Python y métodos `.append()` argumentando que "era el estándar del lenguaje", violando la premisa funcional.
* **Código erróneo propuesto por la IA:**
```python
# ERROR DE IA: Violación de inmutabilidad funcional
items = []
items.append(item_lomo)
if falta_carne:
    items.append(item_sobrecostilla)
```
* **Prompt de corrección formulado por el equipo:**
> *"Rechazado. En el paradigma funcional no puedes usar listas mutables ni .append(). Modela las líneas de pedido como tuplas inmutables (tuple) y compón los resultados mediante el operador de concatenación pura (+), garantizando la transparencia referencial."*
* **Código corregido y validado:**
```python
def resolver_carne_con_sustitucion(catalogo: Tuple[dict, ...], ...) -> Tuple[dict, ...]:
    item_lomo = crear_item(lomo, 3.0, "Stock agotado...")
    item_sub = crear_item(sobrecostilla, 1.1, "Sustituto activado...")
    return (item_lomo, item_sub)  # Retorna tupla inmutable sin efectos colaterales
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
| **Total Obtenido (Dataset Oficial)** | **$91.866 CLP** | **$91.866 CLP** | **$91.866 CLP** |
| **Ajuste Presupuestario ($45k)** | **$42.104 CLP** | **$42.104 CLP** | **$42.104 CLP** |

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

### 6.3 Verificación de paridad matemática (Suite de 6 pruebas unitarias)
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
6. `test_paridad_optimizacion_activa_presupuesto`: Ante presupuesto restringido ($45.000), las tres versiones convergen exactamente en **$42.104 CLP**.

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

"""

anexo_a = registro_prompts_raw + "\n\n---\n\n"

anexo_b = f"""## ANEXO B. CÓDIGO FUENTE COMENTADO DE LAS TRES VERSIONES

### B.1 Versión Imperativa (`src/imperativo/carrito_imperativo.py`)
```python
{code_imp}
```

---

### B.2 Versión Orientada a Objetos: Modelos y Patrón Strategy (`src/poo/modelos.py`)
```python
{code_modelos}
```

---

### B.3 Versión Orientada a Objetos: Orquestador del Carrito (`src/poo/carrito_poo.py`)
```python
{code_poo}
```

---

### B.4 Versión Funcional: Pipeline Puro Declarativo (`src/funcional/carrito_funcional.py`)
```python
{code_func}
```

---

"""

anexo_c = f"""## ANEXO C. OUTPUT COMPLETO DE LAS EJECUCIONES DE PRUEBA

### C.1 Salida Verbatim de la Suite de Pruebas Unitarias de Equivalencia
*(Comando ejecutado: `python3 -m unittest tests/test_equivalencia.py -v`)*

```text
{test_out.strip()}
```

---

### C.2 Salida de Boleta de Venta del Caso Oficial (10 Adultos, 4 Niños, 2 Vegetarianos, $120.000 CLP)
*(Ejecución en las tres versiones con catálogo `catalogo_tienda.json` y evento `data/evento_asado.json`)*

```text
{out_oficial.strip()}
```

---

### C.3 Salida de Boleta con Optimización Activa por Restricción Presupuestaria ($45.000 CLP)
*(Comprueba la degradación automática de corte a Sobrecostilla y ajuste de bebidas/chorizos convergiendo exactamente en $42.104 CLP)*

```text
{out_ajustado.strip()}
```
"""

informe_total = cuerpo_principal + anexo_a + anexo_b + anexo_c

ruta_salida_md = os.path.join(REPO_DIR, 'docs/INFORME_FINAL_UTEM.md')
with open(ruta_salida_md, 'w', encoding='utf-8') as f:
    f.write(informe_total)

print(f"Informe Markdown generado exitosamente en: {ruta_salida_md}")
print(f"Total caracteres: {len(informe_total):,}")
print(f"Total líneas: {len(informe_total.splitlines()):,}")
