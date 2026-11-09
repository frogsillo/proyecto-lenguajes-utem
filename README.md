# Proyecto: Carrito Evento Especial Multiparadigma en Python
**Asignatura:** Lenguajes de Programación  
**Carrera:** Ingeniería Civil en Computación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Semestre:** 2-2026  

---

## 1. Descripción del Proyecto

Este proyecto aborda el desarrollo de un componente de comercio electrónico aditivo para la gestión de un **Carrito Evento Especial ("Asado Parrillero")**, implementado bajo tres paradigmas de programación en Python:
1. **Paradigma Imperativo** (`src/imperativo/`): Control secuencial de flujo, variables acumuladoras mutables y efectos secundarios directos sobre el catálogo.
2. **Paradigma Orientado a Objetos (POO)** (`src/poo/`): Abstracción del dominio (`Producto`, `ItemCarrito`, `Carrito`), encapsulamiento de inventario y aplicación del patrón de comportamiento **Strategy** con polimorfismo para las reglas de promoción.
3. **Paradigma Funcional** (`src/funcional/`): Estructuras de datos inmutables (tuplas), funciones puras con transparencia referencial y transformaciones basadas en funciones de orden superior (`map`, `filter`, `reduce`).

### Etapa 1: Tienda en Línea Operativa
* **Plataforma:** Compatible e importable directamente en **Tiendanube** y **Shopify** mediante los archivos CSV incluidos (`data/catalogo_tiendanube.csv` y `data/catalogo_shopify.csv`).
* **Servidor Local de Demostración:** Incluye `servidor_tienda.py`, un servidor e-commerce autónomo en Python que despliega la tienda en `http://localhost:8000` con identidad visual *"Parrilleros UTEM"*, catálogo navegable con buscador, carrito interactivo y checkout con pasarela de pagos en modo de prueba (*sandbox*).

### Etapa 2: Reglas de Negocio del Carrito Evento Especial
* **Cálculo Paramétrico de Raciones:** 350g de carne por adulto, 150g por niño, 1 pack de chorizo cada 5 personas, menú vegetariano y 0.5L de bebida por persona.
* **Control de Quiebre de Stock y Sustitución Automática:** Si la demanda de carne vacuna supera el stock de bodega de *Lomo Vetado* (3.0 kg), el sistema consume el stock disponible y asigna automáticamente el corte sustituto definido en catálogo (*Sobrecostilla*).
* **Regla de Promoción 'Combo Parrillero':** Si la orden incluye simultáneamente productos cárnicos, carbón y sal, se aplica automáticamente un 10% de descuento sobre el subtotal de dichos ítems.
* **Gestión Activa de Presupuesto:** Si el total excede el presupuesto fijado por el cliente, el sistema degrada automáticamente el corte de carne y reduce extras para intentar ajustarse al límite financiero.
* **Paridad Absoluta de Resultados (Dataset Oficial):**
  * **Subtotal Neto:** \$99.809 CLP
  * **Descuento Combo:** -\$7.943 CLP
  * **Total Final a Pagar:** \$91.866 CLP

---

## 2. Requisitos y Configuración del Entorno

* **Lenguaje:** Python 3.8 o superior.
* **Dependencias Externas:** **Ninguna** (100% desarrollado sobre la biblioteca estándar de Python: `json`, `math`, `functools`, `abc`, `unittest`, `http.server`, `sys`, `os`).

---

## 3. Instrucciones de Ejecución

### 3.1. Menú Principal Multimodal
Para iniciar la aplicación ejecuta desde la terminal:

```bash
python3 main.py
```

Opciones disponibles en el menú:
* **`[1] Modo Interactivo`**: Permite al usuario ingresar por teclado el número de adultos, niños, vegetarianos, presupuesto máximo y corte preferido, evaluando las reglas de negocio y optimizando en caso de sobregiro presupuestario.
* **`[2] Modo Automático`**: Resuelve el dimensionamiento exprés del evento con solo indicar el número de asistentes (ej: *"Hazme un carrito para 10 personas"*), calculando raciones, sustituciones y presupuesto sugerido.
* **`[3] Modo Defensa Académica`**: Menú especializado para la comisión evaluadora con el dataset oficial del informe, cuadro comparativo *Side-by-Side* y ejecución de la suite de 6 pruebas unitarias.
* **`[4] Tienda Web en Vivo (Etapa 1)`**: Levanta el servidor e-commerce local en `http://localhost:8000` con catálogo, carrito y checkout sandbox demostrable.

### 3.2. Ejecución de la Tienda en Línea Local (Etapa 1)
```bash
python3 servidor_tienda.py
```
Abre en tu navegador: `http://localhost:8000`

### 3.3. Ejecución Directa de Cada Paradigma
Cada paradigma puede ser ejecutado de forma independiente por consola:
```bash
# Versión Imperativa
python3 src/imperativo/carrito_imperativo.py

# Versión Orientada a Objetos
python3 src/poo/carrito_poo.py

# Versión Funcional
python3 src/funcional/carrito_funcional.py
```

### 3.4. Ejecución de Pruebas Automatizadas de Equivalencia
Para demostrar al docente que las 3 versiones cumplen con el 100% de paridad en cálculos normales y bajo ajuste presupuestario:
```bash
python3 tests/test_equivalencia.py
```

---

## 4. Estructura del Repositorio

```text
proyecto_lenguajes/
│
├── data/
│   ├── catalogo_tienda.json          # Base de datos JSON de la tienda
│   ├── catalogo_tiendanube.csv       # Archivo listo para importar a Tiendanube
│   ├── catalogo_shopify.csv          # Archivo listo para importar a Shopify
│   └── evento_asado.json             # Parámetros oficiales del evento de prueba
│
├── src/
│   ├── imperativo/
│   │   └── carrito_imperativo.py     # Solución procedural con variables mutables y bucles
│   ├── poo/
│   │   ├── modelos.py                # Clases de dominio y Patrón Strategy
│   │   └── carrito_poo.py            # Orquestador orientado a objetos
│   ├── funcional/
│   │   └── carrito_funcional.py      # Solución pura con map, filter y reduce
│   └── utils/
│       ├── interactivo.py            # Módulo unificado de interacción y heurística
│       └── visualizador.py           # Formato de boleta común para las 3 versiones
│
├── tests/
│   └── test_equivalencia.py          # Suite de 6 pruebas unitarias (unittest)
│
├── docs/
│   ├── GUIA_MONTAJE_TIENDA.md        # Guía paso a paso para montar la tienda en la nube
│   ├── bitacora_prompts_imperativo.md # 9 prompts + errores + defensa + APA 7
│   ├── bitacora_prompts_poo.md        # 9 prompts + errores + defensa + APA 7
│   ├── bitacora_prompts_funcional.md  # 9 prompts + errores + defensa + APA 7
│   └── borrador_informe_apa7.md       # Informe académico completo (19 KB) según pauta UTEM
│
├── servidor_tienda.py                # Servidor Web E-commerce demostrable (Etapa 1)
├── REGISTRO_PROMPTS.md               # Bitácora oficial consolidada de 27 prompts
├── main.py                           # Demostrador interactivo multimodal
└── README.md                         # Guía de instalación y uso
```
