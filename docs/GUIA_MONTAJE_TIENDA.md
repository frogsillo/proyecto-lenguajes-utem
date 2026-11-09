# GUÍA DE MONTAJE DE LA TIENDA EN LÍNEA (ETAPA 1)
**Asignatura:** Lenguajes de Programación  
**Carrera:** Ingeniería Civil en Computación  
**Institución:** Universidad Tecnológica Metropolitana (UTEM)  
**Semestre:** 2-2026  

---

## 1. OBJETIVO DE LA ETAPA 1
Montar una tienda en línea funcional y demostrable sobre **Tiendanube** (o **Shopify**) con los elementos mínimos obligatorios exigidos por la pauta de evaluación:
1. **Catálogo y navegación:** Categorización (Carnes, Abarrotes, Vegetariano, Bebidas), buscador y fichas de producto con precio en CLP y stock controlado.
2. **Carrito y checkout:** Carrito accesible y editable, con cálculo de totales.
3. **Pasarela de pago en modo de prueba:** Simulación de compra sin dinero real (Sandbox).
4. **Identidad visual:** Tema gráfico coherente ("Parrilleros UTEM").

---

## 2. MONTAJE RÁPIDO EN TIENDANUBE (RECOMENDADO PARA CHILE - 10 MINUTOS)

### Paso 1: Registro gratuito
1. Ingresa a [www.tiendanube.com/cl](https://www.tiendanube.com/cl).
2. Haz clic en **"Crear tienda gratis"** o **"Probar gratis"**.
3. Nombre de la tienda: `Parrilleros UTEM` (te generará una URL como `https://parrillerosutem.mitiendanube.com`).
4. Ingresa tu correo institucional o personal y una contraseña.

### Paso 2: Importación de productos en 1 solo clic
No necesitas escribir los 8 productos a mano:
1. En el panel de control de Tiendanube, ve a **Productos** $\rightarrow$ **Importar y Exportar desde CSV**.
2. Selecciona la opción **Importar productos**.
3. Sube el archivo ubicado en tu proyecto:  
   `/data/catalogo_tiendanube.csv`
4. ¡Listo! Se crearán automáticamente los 8 productos con sus categorías, precios en pesos chilenos y sus stocks exactos (Lomo Vetado con 3.0 kg para provocar el quiebre de stock, Sobrecostilla con 15.0 kg, carbón, chorizos, etc.).

### Paso 3: Configuración del Tema e Identidad Visual
1. En el menú lateral, ve a **Mi Tiendanube** $\rightarrow$ **Diseño**.
2. Selecciona un tema gratuito moderno (ej: *Simple*, *Trend* o *Bahía*).
3. En el encabezado, coloca el nombre comercial: **Parrilleros UTEM - Tienda Oficial**.

### Paso 4: Activación de Pasarela de Pagos en Modo de Prueba
1. Ve a **Configuración** $\rightarrow$ **Medios de pago**.
2. Activa **"Pago a convenir"** o **"Transferencia bancaria de prueba"** o el **Modo Sandbox / Prueba de MercadoPago**.
3. Configura el mensaje: *"Pago de prueba académico UTEM - Sin cobro real"*.

---

## 3. MONTAJE ALTERNATIVO EN SHOPIFY

Si prefieres usar Shopify:
1. Ingresa a [www.shopify.com/es-es](https://www.shopify.com/es-es) e inicia la prueba gratuita.
2. En **Productos** $\rightarrow$ **Importar**, sube el archivo `/data/catalogo_shopify.csv`.
3. En **Configuración** $\rightarrow$ **Pagos**, en la sección de proveedores activa **"(for testing) Bogus Gateway"** (permite ingresar `1` como número de tarjeta para simular una compra aprobada).

---

## 4. SERVIDOR LOCAL RUNNABLE DE RESPALDO (`servidor_tienda.py`)

Para que tengas una garantía absoluta durante tu presentación en vivo en la universidad (por si la conexión a internet falla o el trial de la nube vence), hemos creado en el proyecto un **servidor web e-commerce autónomo en Python**:

```bash
python3 servidor_tienda.py
```

Al ejecutarlo, abre en tu navegador:  
👉 **`http://localhost:8000`**

Encontrarás:
* Interfaz visual responsiva de la tienda **"Parrilleros UTEM"**.
* Navegación por categorías (Carnes, Abarrotes, Vegetariano, Bebidas) y buscador en tiempo real.
* Carrito de compras desplegable dinámico.
* Checkout con pasarela de pago de prueba (modo sandbox con tarjeta de prueba simulada).
* **API RESTful integrada:**
  * `GET /api/products`: Devuelve el catálogo en formato JSON consumible directamente por el Carrito Evento Especial.
  * `GET /api/stock`: Permite consultar el stock en tiempo real.

---

## 5. EVIDENCIAS PARA EL INFORME FINAL (SECCIÓN 3)
En el informe final adjunta:
1. La **URL pública** de tu tienda en Tiendanube/Shopify (o captura de `servidor_tienda.py`).
2. **Captura 1:** Vista del catálogo con los productos y sus precios en CLP.
3. **Captura 2:** Vista del carrito de compras con ítems agregados.
4. **Captura 3:** Pantalla de checkout con la pasarela de pago en modo de prueba.
