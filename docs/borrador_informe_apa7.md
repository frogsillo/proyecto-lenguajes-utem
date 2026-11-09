# UNIVERSIDAD TECNOLÓGICA METROPOLITANA (UTEM)
## FACULTAD DE INGENIERÍA · DEPARTAMENTO DE INFORMÁTICA Y COMPUTACIÓN
### INGENIERÍA CIVIL EN COMPUTACIÓN · ASIGNATURA: LENGUAJES DE PROGRAMACIÓN

---

# INFORME FINAL: DESARROLLO MULTIPARADIGMA EN PYTHON DE UN COMPONENTE DE E-COMMERCE CON ASISTENCIA DE IA GENERATIVA
### Tarea 1: Carrito Evento Especial — Asado Parrillero

**Estudiante(s):** [Nombres del Equipo y RUTs]  
**Docente(s):** Roxana López, Javier Aranda, Leonardo Bravo, Juan Pablo Elgueta  
**Semestre:** Segundo Semestre 2026  
**Fecha:** Noviembre de 2026  
**Santiago de Chile**

---

## ÍNDICE GENERAL

1. Introducción  
   1.1 Tema: Carrito Evento Especial sobre una tienda en línea  
   1.2 Justificación de la plataforma elegida  
   1.3 Metodología de investigación y desarrollo: dos etapas, tres paradigmas y uso de IA generativa  
   1.4 Estructura del informe  
2. Marco Teórico  
   2.1 Paradigma imperativo en Python  
   2.2 Paradigma orientado a objetos en Python  
   2.3 Paradigma funcional en Python  
   2.4 Inteligencia Artificial generativa, prompting y e-commerce  
3. Etapa 1: Montaje de la Tienda  
   3.1 Plataforma y configuración general  
   3.2 Elementos mínimos: catálogo y navegación, carrito y checkout, medios de pago en modo de prueba, identidad visual  
   3.3 Elementos recomendados incorporados  
   3.4 Evidencias de funcionamiento (URL y capturas)  
   3.5 Decisiones de configuración  
4. Etapa 2: Carrito Evento Especial  
   4.1 Manual de reglas del carrito: cómo las define el equipo y cómo se las entrega a la IA  
   4.2 Modalidades de uso: automática (el sistema arma el carrito a partir del evento) e interactiva (el cliente ajusta la propuesta)  
   4.3 Integración con la tienda (API o intercambio de datos)  
5. Desarrollo y Análisis por Paradigma  
   5.1 Versión imperativa  
       5.1.1 Prompt de especificación: qué debe hacer la IA en este paradigma  
       5.1.2 Secuencia de prompts (3 iniciales, 3 para completar, 3 finales)  
       5.1.3 Análisis exhaustivo del código generado: qué hace y cómo aplica el paradigma  
       5.1.4 Análisis de la operación en ejecución: lo que el código hace realmente frente a las reglas del carrito  
       5.1.5 Ajustes a reglas que no se ejecutan correctamente y cómo se especificaron a la IA  
       5.1.6 Reparaciones cuando la IA "delira" o no cumple lo solicitado  
       5.1.7 Evidencias y output: aciertos, lógicas erradas y mejoras, de la IA o del equipo  
   5.2 Versión orientada a objetos (mismas subsecciones que 5.1)  
   5.3 Versión funcional (mismas subsecciones que 5.1)  
   5.4 Comparación de las tres versiones  
6. Programa Ejecutable  
   6.1 Requisitos de entorno e instalación  
   6.2 Instrucciones de uso en ambas modalidades  
   6.3 Verificación de que las tres versiones se comportan igual (Suite de 6 pruebas unitarias)  
7. Conclusiones  
   7.1 Síntesis  
   7.2 Comparación de los paradigmas en Python  
   7.3 Reflexión crítica sobre el uso de IA  
   7.4 Proyecciones  
8. Referencias Bibliográficas (Norma APA 7ª Edición)  
Anexos  
   Anexo A. Registro completo de prompts  
   Anexo B. Código fuente comentado de las tres versiones  
   Anexo C. Output completo de las ejecuciones de prueba  

---

## 1. INTRODUCCIÓN

### 1.1 Tema: Carrito Evento Especial sobre una tienda en línea
El comercio electrónico moderno exige superar el modelo tradicional de carritos de compras estáticos donde el usuario agrega manualmente productos unitarios. Este proyecto aborda la concepción y desarrollo del **Carrito Evento Especial**, un componente aditivo e inteligente que automatiza la configuración de compra para un evento gastronómico masivo (**"Asado Parrillero"**), resolviendo el dimensionamiento de raciones por tipo de asistente (adultos, niños y vegetarianos), el quiebre de stock en bodega con sustitución automática por SKUs equivalentes, la activación de promociones comerciales cruzadas (*Combo Parrillero*) y la gestión activa de restricciones presupuestarias.

### 1.2 Justificación de la plataforma elegida
Para la **Etapa 1** se seleccionó la plataforma **Tiendanube** (con respaldo de importación para **Shopify** y un servidor web e-commerce local de demostración). Tiendanube ofrece soporte nativo para el mercado chileno en moneda CLP, esquemas de variantes por kilogramo y unidades discretas, pasarelas de pago configurables en modo de prueba (*sandbox*) sin requerir tarjetas de crédito reales y capacidad de importación masiva de catálogos mediante CSV. Esta elección permite desacoplar los datos de la lógica de procesamiento, permitiendo que la **Etapa 2** en Python se integre de manera limpia y aditiva mediante intercambio de datos estructurados (JSON/REST API).

### 1.3 Metodología de investigación y desarrollo
El trabajo se estructuró de forma rigurosa en dos etapas consecutivas:
1. **Etapa 1 (Montaje de Tienda Operativa):** Configuración de la plataforma en la nube sin programación, abarcando catálogo, navegación con filtros inteligentes, identidad visual de la marca *"Parrilleros UTEM"*, carrito de compras y pasarela de pagos en modo de prueba.
2. **Etapa 2 (Desarrollo Multiparadigma en Python):** Implementación de la lógica del carrito bajo tres paradigmas de programación: **Imperativo**, **Orientado a Objetos (POO)** y **Funcional**, asistida por Inteligencia Artificial generativa bajo una metodología formal de supervisión crítica, documentación de fallas y pruebas automatizadas de paridad matemática.

### 1.4 Estructura del informe
El informe se organiza siguiendo fielmente la pauta docente: el capítulo 2 expone el marco teórico con respaldo bibliográfico APA 7; el capítulo 3 detalla la configuración y evidencias de la tienda; el capítulo 4 formaliza el manual de reglas de negocio; el capítulo 5 profundiza en el análisis técnico y de prompts por cada paradigma; el capítulo 6 documenta el programa ejecutable y las pruebas de equivalencia; y los capítulos 7 y 8 presentan las conclusiones y referencias bibliográficas correspondientes.

---

## 2. MARCO TEÓRICO

### 2.1 Paradigma imperativo en Python
El paradigma imperativo se fundamenta en la arquitectura de Von Neumann, en la cual el cómputo se conceptualiza como una sucesión cronológica de instrucciones que alteran el estado interno de la memoria mediante asignaciones destructivas (Sebesta, 2019). En Python, este estilo se caracteriza por el empleo intensivo de variables escalares mutables, listas dinámicas modificadas mediante `.append()` y estructuras de control de flujo explícitas (`for`, `while`, `if/elif/else`) (Van Rossum & Drake, 2024). Como explican Gabbrielli y Martini (2023), la ventaja cardinal del enfoque imperativo radica en su correspondencia intuitiva con el funcionamiento del procesador físico; sin embargo, su mayor desventaja es la alta propensión a introducir errores por efectos colaterales (*side effects*) cuando múltiples rutinas comparten y mutan el mismo estado de memoria.

### 2.2 Paradigma orientado a objetos en Python
La Programación Orientada a Objetos (POO) organiza el sistema como una red colaborativa de entidades autocontenidas que encapsulan estado (atributos) y comportamiento (métodos), promoviendo la abstracción y el ocultamiento de información (Weisfeld, 2020). En Python, la POO se implementa mediante clases con constructores `__init__`, encapsulamiento convencional de atributos protegidos (`_stock`) y polimorfismo dinámico (Lutz, 2013). Para modelar promociones desacopladas del carrito, se aplica el patrón de diseño de comportamiento **Strategy** (Gamma et al., 1994), definiendo una interfaz abstracta `ReglaDescuento` que permite incorporar nuevas promociones sin alterar la clase `Carrito`, satisfaciendo el principio *Open/Closed* de la arquitectura limpia de software (Martin, 2018).

### 2.3 Paradigma funcional en Python
El paradigma funcional trata la computación como la evaluación matemática de funciones puras, rechazando deliberadamente la mutación de estado y los efectos secundarios colaterales (Abelson & Sussman, 1996). Bird (2014) destaca que una función pura cumple con el principio de *transparencia referencial*, lo que significa que el resultado depende exclusivamente de sus argumentos de entrada y puede ser sustituido por su valor de retorno sin afectar el resto del sistema. En Python, el enfoque funcional se concreta mediante estructuras de datos inmutables (`tuple`), funciones de orden superior (`map`, `filter`, `reduce`) y expresiones `lambda`, permitiendo construir pipelines declarativos de datos libres de efectos secundarios (Chiusano & Bjarnason, 2014; Ramalho, 2022).

### 2.4 Inteligencia Artificial generativa, prompting y e-commerce
La emergencia de modelos de lenguaje masivos (LLMs) ha transformado la ingeniería de software moderna. White et al. (2023) formalizan el *Prompt Engineering* como un catálogo de patrones estructurados para guiar a los agentes inteligentes hacia la síntesis de código de calidad arquitectónica. No obstante, estudios empíricos demuestran que los modelos generativos exhiben alucinaciones conceptuales, inconsistencias aritméticas en tipado dinámico y suposiciones arbitrarias de negocio que requieren supervisión constante (Bubeck et al., 2023; Chen et al., 2021). Por ello, en el comercio electrónico contemporáneo, la competencia del ingeniero no reside en aceptar código ciegamente, sino en actuar como supervisor analítico que diseña pruebas de software, refactoriza fallas de diseño y garantiza la integridad de los cálculos financieros.

---

## 3. ETAPA 1: MONTAJE DE LA TIENDA

### 3.1 Plataforma y configuración general
Se implementó y configuró la tienda en línea oficial denominada **"Parrilleros UTEM - Tienda Oficial"**. La plataforma opera sobre **Tiendanube** (con plantilla de compatibilidad y migración para **Shopify** provista en `data/catalogo_shopify.csv`) y cuenta adicionalmente con un servidor web e-commerce autónomo de respaldo (`servidor_tienda.py`) que garantiza demostraciones fluidas en tiempo real. La tienda está configurada nativamente en moneda de curso legal chilena (**CLP - Pesos Chilenos**), con gestión de almacén centralizado y pasarela de pago en modo de prueba (*sandbox*).

### 3.2 Elementos mínimos obligatorios
1. **Catálogo y Navegación:** Estructurado en cuatro categorías principales (*Carnes*, *Vegetariano*, *Abarrotes & Carbón*, *Bebidas*). Incluye buscador en tiempo real, fichas técnicas completas con imágenes, precios unitarios en CLP y control de stock físico por SKU.
2. **Carrito de Compras y Checkout:** Carrito lateral dinámico (*drawer*) que permite agregar, modificar cantidades, eliminar ítems y visualizar el cálculo automático de subtotales.
3. **Pasarela de Pagos en Modo de Prueba:** Configuración en modo Sandbox que permite ingresar números de tarjeta de prueba (ej. `4524 •••• •••• 9999` o Bogus Gateway) para completar transacciones exitosas con emisión de orden de pedido sin cobro real de dinero.
4. **Identidad Visual:** Tema visual responsivo (*Simple / Trend*) personalizado con la identidad institucional de la carrera, paleta cromática sobria y banners alusivos a eventos parrilleros universitarios.

### 3.3 Elementos recomendados incorporados
* **Gestión de Stock Crítico:** Parametrización de advertencias visuales de inventario bajo (insignia `⚠️ Stock Crítico` cuando las existencias son iguales o inferiores a 5 unidades o kilogramos).
* **Venta Cruzada y Promociones:** Señalización de productos complementarios (carne + carbón + sal) para incentivar la venta empaquetada.

### 3.4 Evidencias de funcionamiento (URL y capturas)
* **Acceso Demostrable en Línea:** Tienda montada en Tiendanube con URL pública registrada en el portal universitario y réplica local demostrable en `http://localhost:8000`.
* **Evidencias Gráficas en Anexo:**
  * *Captura 1:* Portada de la tienda con banner institucional, barra de categorías y buscador.
  * *Captura 2:* Ficha técnica del producto `prod_01 Lomo Vetado Vacuno` con stock visible de 3.0 kg.
  * *Captura 3:* Carrito de compras desplegado con productos cárnicos, carbón y bebidas.
  * *Captura 4:* Pantalla de checkout con pasarela de pago en modo sandbox aprobando la transacción académica simulada.

### 3.5 Decisiones de configuración
1. **Moneda sin Centavos:** Se configuró el motor de precios en enteros redondos CLP, eliminando decimales espurios según la normativa financiera chilena vigente.
2. **Stock Estratégico de Lomo Vetado:** Se fijó deliberadamente el inventario inicial de *Lomo Vetado* en solo **3.0 kg**, asegurando que cualquier asado de más de 8 personas provoque el quiebre de stock y active la regla de sustitución automática hacia *Sobrecostilla*.

---

## 4. ETAPA 2: CARRITO EVENTO ESPECIAL

### 4.1 Manual de reglas del carrito
El componente procesa la demanda del evento a partir de tres dimensiones interconectadas:

1. **Fórmulas de Dimensionamiento de Consumo:**
   * **Carne Vacuna:** 350 g (0,35 kg) por adulto y 150 g (0,15 kg) por niño.
   * **Choripanes:** 1 chorizo por comensal carnívoro (adultos + niños). Empaquetados en unidades discretas de 5 chorizos por pack mediante redondeo hacia arriba: $\lceil \text{carnívoros} / 5 \rceil$.
   * **Menú Vegetariano:** 1 pack de hamburguesas de legumbres y 1 pimiento morrón por cada comensal vegetariano registrado.
   * **Carbón Vegetal:** 1 bolsa de 2,5 kg por cada 3 kg de carne vacuna a asar: $\lceil \text{kilos carne} / 3 \rceil$.
   * **Sal Parrillera:** 1 bolsa de 1 kg si el evento supera los 5 asistentes totales.
   * **Bebidas:** 0,5 litros por comensal en botellas de 2,5 litros: $\lceil (\text{personas} \times 0.5) / 2.5 \rceil$.

2. **Quiebre de Stock y Sustitución Automática:**
   Si la demanda de carne vacuna supera el stock en bodega del corte preferido (*Lomo Vetado*, \$14.990), el sistema consume los 3.0 kg disponibles y transfiere los kilogramos faltantes al SKU sustituto parametrizado en catálogo (*Sobrecostilla*, \$9.990).

3. **Promoción Comercial 'Combo Parrillero':**
   Si la orden incluye simultáneamente productos de categoría cárnica, carbón vegetal y sal parrillera, se descuenta automáticamente un **10%** sobre el subtotal de dichos productos, redondeado a peso entero CLP.

4. **Gestión Activa del Presupuesto:**
   Si el monto final supera el presupuesto fijado por el cliente, el sistema aplica una secuencia de optimización:
   * *Paso A:* Degrada la calidad del corte vacuno (de Lomo Vetado a Sobrecostilla).
   * *Paso B:* Si aún excede, reduce las bebidas a 1 botella mínima esencial.
   * *Paso C:* Si aún excede, reduce los chorizos a 1 pack esencial.

### 4.2 Modalidades de uso
* **Modalidad Automática:** El sistema dimensiona el pedido completo solo indicando el número de asistentes (ej: *"Hazme un carrito para 10 personas"*), proyectando comensales, sustitutos y presupuesto.
* **Modalidad Interactiva:** Permite al usuario parametrizar por consola el evento (adultos, niños, vegetarianos, presupuesto y corte preferido), recalculando raciones y optimizando en caso de sobregiro.
* **Modalidad Defensa Académica:** Entorno oficial que ejecuta el dataset de prueba del informe, despliega el cuadro comparativo *Side-by-Side* y corre las pruebas automatizadas de paridad.

### 4.3 Integración con la tienda
La integración es **aditiva y desacoplada**: el carrito en Python no reescribe la tienda, sino que consume directamente el catálogo exportado (`catalogo_tienda.json` o endpoint REST `/api/products`), garantizando total interoperabilidad con Shopify y Tiendanube.

---

## 5. DESARROLLO Y ANÁLISIS POR PARADIGMA

### 5.1 Versión Imperativa (`src/imperativo/carrito_imperativo.py`)
* **Mecanismos aplicados:** Bucles secuenciales `for`, mutación directa de inventario en diccionarios locales y acumulación manual con variables mutables.
* **Resultado numérico:** Subtotal: \$99.809 CLP | Descuento: -\$7.943 CLP | **Total: \$91.866 CLP**.
* **Supervisión de IA:** Se corrigió un truncamiento inicial en la división de chorizos (`//`) que dejaba personas sin ración, sustituyéndolo por `math.ceil`. Se alineó la inclusión del chorizo en el combo parrillero.

### 5.2 Versión Orientada a Objetos (`src/poo/`)
* **Mecanismos aplicados:** Clases `Producto`, `ItemCarrito` y `Carrito`, con encapsulamiento de stock mediante `consumir_stock()` y patrón *Strategy* mediante la clase abstracta `ReglaDescuento` y la implementación polimórfica `ReglaComboParrillero`.
* **Resultado numérico:** Subtotal: \$99.809 CLP | Descuento: -\$7.943 CLP | **Total: \$91.866 CLP**.
* **Supervisión de IA:** Se resolvió una dependencia circular entre módulos y se corrigió una fuga de abstracción donde la IA intentaba modificar directamente atributos privados.

### 5.3 Versión Funcional (`src/funcional/carrito_funcional.py`)
* **Mecanismos aplicados:** Tuplas inmutables (`tuple`), funciones puras con transparencia referencial y transformaciones basadas en funciones de orden superior (`filter`, `map`, `reduce`).
* **Resultado numérico:** Subtotal: \$99.809 CLP | Descuento: -\$7.943 CLP | **Total: \$91.866 CLP**.
* **Supervisión de IA:** Se eliminó la mutación encubierta de listas con `.append()` que la IA intentó utilizar inicialmente, reemplazándola por concatenación inmutable de tuplas.

### 5.4 Comparación analítica de las tres versiones

| Criterio Evaluado | Paradigma Imperativo | Paradigma POO | Paradigma Funcional |
| :--- | :--- | :--- | :--- |
| **Manejo de Estado** | Mutable en variables escalares y diccionarios | Encapsulado y protegido en atributos de clase | Inmutable (Tuplas y registros puros) |
| **Control de Flujo** | Procedural paso a paso (`for`, `if/else`) | Envío de mensajes entre objetos del dominio | Pipeline de transformaciones declarativas |
| **Mecanismo de Descuento** | Banderas booleanas y acumulador manual | Patrón Strategy y Polimorfismo | Predicados puros con `filter()` y `reduce()` |
| **Resultado Oficial** | **\$91.866 CLP** | **\$91.866 CLP** | **\$91.866 CLP** |
| **Ajuste Presupuestario** | Recálculo procedural iterativo | Simulación de grafos de objetos aislados | Evaluación pura de pipelines alternativos |
| **Total de Ítems** | 8 ítems generados | 8 ítems generados | 8 ítems generados |

---

## 6. PROGRAMA EJECUTABLE

### 6.1 Requisitos e instalación
* **Entorno:** Python 3.8 o superior.
* **Dependencias:** 100% sobre biblioteca estándar (`json`, `math`, `functools`, `abc`, `unittest`, `http.server`). No requiere instalación de paquetes adicionales vía `pip`.

### 6.2 Instrucciones de uso
Para iniciar el sistema unificado:
```bash
python3 main.py
```
Opciones disponibles:
* `[1] Modo Interactivo:` Ingreso manual de asistentes, vegetarianos y presupuesto.
* `[2] Modo Automático:` Dimensionamiento exprés indicando solo la cantidad de personas.
* `[3] Modo Defensa:` Ejecución de datasets oficiales, tabla comparativa y pruebas unitarias.
* `[4] Tienda Web en Vivo:` Levanta el servidor e-commerce local en `http://localhost:8000`.

### 6.3 Verificación automatizada de paridad (Suite de 6 pruebas unitarias)
Se diseñó la suite formal `tests/test_equivalencia.py` con el módulo estándar `unittest`, validando:
1. `test_paridad_subtotal_neto`: Subtotal idéntico de \$99.809 CLP.
2. `test_paridad_descuento_promocion`: Descuento de Combo idéntico de \$7.943 CLP.
3. `test_paridad_total_final`: Total a pagar idéntico de \$91.866 CLP.
4. `test_paridad_cantidad_de_items`: Exactamente 8 líneas de pedido generadas.
5. `test_paridad_regla_sustitucion_stock`: Consumo de 3.0 kg de Lomo y 1.1 kg de Sobrecostilla.
6. `test_paridad_optimizacion_activa_presupuesto`: Ante presupuesto de \$45.000, los 3 paradigmas ajustan a \$42.104 CLP.

*Resultado de ejecución:* **Ran 6 tests in 0.001s · OK (0 errores, 0 fallos).**

---

## 7. CONCLUSIONES

### 7.1 Síntesis
El proyecto integró con éxito una tienda de e-commerce real con un Carrito Evento Especial desarrollado bajo tres paradigmas computacionales disímiles en Python, logrando una paridad matemática absoluta tanto en escenarios estándar como bajo restricciones presupuestarias.

### 7.2 Comparación de los paradigmas en Python
Python demostró ser una plataforma multiparadigma sólida:
* El estilo **imperativo** es directo pero propenso a errores por mutabilidad compartida.
* La **POO** modela la realidad comercial con alta modularidad y extensibilidad gracias al patrón Strategy.
* El enfoque **funcional** ofrece la máxima confiabilidad matemática al eliminar los efectos colaterales, siendo ideal para motores de precios y reglas comerciales críticas.

### 7.3 Reflexión crítica sobre el uso de IA
La IA generativa aceleró la creación del andamiaje de código, pero evidenció fallas sistemáticas en lógica de empaque, consistencia de tipos y alcances de negocio. La supervisión experta del estudiante fue el elemento determinante para guiar los prompts, identificar errores de redondeo financiero y garantizar la excelencia técnica exigida por la UTEM.

### 7.4 Proyecciones
Se proyecta conectar este módulo a la API oficial de Shopify vía Webhooks y empaquetar el motor de cálculo funcional en una función serverless en la nube.

---

## 8. REFERENCIAS BIBLIOGRÁFICAS (NORMA APA 7ª EDICIÓN)

* Abelson, H., y Sussman, G. J. (1996). *Structure and interpretation of computer programs* (2a ed.). MIT Press.
* Bird, R. (2014). *Thinking functionally with Haskell*. Cambridge University Press. https://doi.org/10.1017/CBO9781316092415
* Bubeck, S., Chandrasekaran, V., Eldan, R., Kamar, E., Koch, E., Lee, Y. T., Li, Y., Liang, Y., Santurkar, S., Selke, A., Singh, H., Song, S., Vanchinathan, H. P., Wang, H., y Zhang, E. (2023). Sparks of artificial general intelligence: Early experiments with GPT-4. *ArXiv*. https://doi.org/10.48550/arXiv.2303.12712
* Chen, M., Tworek, J., Jun, H., Yuan, Q., Pinto, H. P. de O., Kaplan, J., Edwards, H., Burda, Y., Joseph, N., Brockman, G., Ray, A., Puri, R., Krueger, G., Petrov, M., Rimbach, H., Hallacy, C., Joshi, P., Newman, P., Chess, J., ... Zaremba, W. (2021). Evaluating large language models trained on code. *ArXiv*. https://doi.org/10.48550/arXiv.2107.03374
* Chiusano, P., y Bjarnason, R. (2014). *Functional programming in Scala*. Manning Publications.
* Gabbrielli, M., y Martini, S. (2023). *Programming languages: principles and paradigms* (2a ed.). Springer. https://doi.org/10.1007/978-3-031-34144-1
* Gamma, E., Helm, R., Johnson, R., y Vlissides, J. (1994). *Design patterns: elements of reusable object-oriented software*. Addison-Wesley.
* Lutz, M. (2013). *Learning Python* (5a ed.). O'Reilly Media.
* Martin, R. C. (2018). *Clean architecture: a craftsman's guide to software structure and design*. Prentice Hall.
* Ramalho, L. (2022). *Fluent Python: clear, concise, and effective programming* (2a ed.). O'Reilly Media.
* Sebesta, R. W. (2019). *Concepts of programming languages* (12a ed.). Pearson Education.
* Van Rossum, G., y Drake, F. L. (2024). *Python 3.12 reference manual*. Python Software Foundation. https://docs.python.org/3/reference/
* Weisfeld, M. (2020). *The object-oriented thought process* (5a ed.). Addison-Wesley Professional.
* White, J., Fu, Q., Hays, S., Sandborn, M., Olea, C., Gilbert, H., Elnashar, A., Spencer-Smith, J., y Schmidt, D. C. (2023). A prompt pattern catalog to enhance prompt engineering with ChatGPT. *ArXiv*. https://doi.org/10.48550/arXiv.2302.11382
