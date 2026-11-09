"""
SERVIDOR WEB DE COMERCIO ELECTRÓNICO - ETAPA 1 (UTEM)
Plataforma: Simulación Demostrable de Tiendanube / Shopify
Asignatura: Lenguajes de Programación (Semestre 2-2026)

Este script levanta una tienda en línea 100% funcional y demostrable en http://localhost:8000
utilizando únicamente la biblioteca estándar de Python (sin dependencias externas).

Incluye:
- Frontend con Identidad Visual ("Parrilleros UTEM").
- Catálogo navegable con filtros por categoría y buscador interno inteligente.
- Carrito de compras interactivo con resumen de precios.
- Checkout con Pasarela de Pagos en MODO DE PRUEBA (Sandbox).
- API REST (/api/products) para integración aditiva con el Carrito Evento Especial.
"""

import os
import sys
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

DIRECTORIO_RAIZ = os.path.abspath(os.path.dirname(__file__))
RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
if not os.path.exists(RUTA_CATALOGO):
    RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

def cargar_catalogo():
    with open(RUTA_CATALOGO, "r", encoding="utf-8") as f:
        return json.load(f)

HTML_TIENDA = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parrilleros UTEM — Tienda Oficial (Etapa 1)</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #c92a2a;
            --primary-dark: #a61e1e;
            --dark: #1a1a1a;
            --light-bg: #f8f9fa;
            --card-bg: #ffffff;
            --border: #e9ecef;
            --text-muted: #6c757d;
            --accent: #d9480f;
            --success: #2b8a3e;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }
        body { background-color: var(--light-bg); color: var(--dark); line-height: 1.5; padding-bottom: 60px; }
        
        /* Banner superior */
        .top-banner { background: #1864ab; color: white; text-align: center; font-size: 0.85rem; padding: 8px 16px; font-weight: 600; }
        
        /* Header */
        header { background: white; border-bottom: 1px solid var(--border); position: sticky; top: 0; z-index: 100; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
        .nav-container { max-width: 1200px; margin: 0 auto; display: flex; align-items: center; justify-content: space-between; padding: 16px 24px; gap: 20px; }
        .brand { display: flex; align-items: center; gap: 12px; text-decoration: none; color: var(--dark); }
        .brand-badge { background: var(--primary); color: white; font-weight: 800; font-size: 1.1rem; padding: 6px 12px; border-radius: 8px; letter-spacing: 1px; }
        .brand-text h1 { font-size: 1.25rem; font-weight: 800; }
        .brand-text span { font-size: 0.75rem; color: var(--text-muted); display: block; font-weight: 600; }
        
        .search-box { flex: 1; max-width: 480px; position: relative; }
        .search-box input { width: 100%; padding: 10px 16px; border-radius: 999px; border: 1px solid var(--border); background: var(--light-bg); font-size: 0.9rem; outline: none; transition: all 0.2s; }
        .search-box input:focus { border-color: var(--primary); background: white; box-shadow: 0 0 0 3px rgba(201,42,42,0.1); }
        
        .cart-trigger { background: var(--light-bg); border: 1px solid var(--border); padding: 10px 18px; border-radius: 999px; font-weight: 700; cursor: pointer; display: flex; align-items: center; gap: 8px; transition: all 0.2s; font-size: 0.9rem; }
        .cart-trigger:hover { background: #e9ecef; }
        .cart-count { background: var(--primary); color: white; font-size: 0.75rem; border-radius: 999px; padding: 2px 8px; font-weight: 800; }
        
        /* Hero */
        .hero { max-width: 1200px; margin: 24px auto 0; padding: 0 24px; }
        .hero-banner { background: linear-gradient(135deg, #2b1108 0%, #7f1d1d 100%); color: white; border-radius: 20px; padding: 48px; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 10px 25px -5px rgba(127,29,29,0.3); }
        .hero-text h2 { font-size: 2.2rem; font-weight: 800; margin-bottom: 12px; line-height: 1.2; }
        .hero-text p { font-size: 1.1rem; opacity: 0.9; max-width: 540px; margin-bottom: 20px; }
        .hero-tag { display: inline-block; background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); padding: 6px 14px; border-radius: 999px; font-size: 0.85rem; font-weight: 700; }
        
        /* Navegación de categorías */
        .categories-bar { max-width: 1200px; margin: 32px auto 16px; padding: 0 24px; display: flex; gap: 12px; overflow-x: auto; }
        .cat-pill { padding: 8px 20px; border-radius: 999px; border: 1px solid var(--border); background: white; font-size: 0.9rem; font-weight: 600; cursor: pointer; transition: all 0.2s; white-space: nowrap; }
        .cat-pill.active, .cat-pill:hover { background: var(--dark); color: white; border-color: var(--dark); }
        
        /* Grid de productos */
        .main-container { max-width: 1200px; margin: 0 auto; padding: 0 24px; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 24px; margin-top: 16px; }
        .card { background: white; border-radius: 16px; border: 1px solid var(--border); overflow: hidden; display: flex; flex-direction: column; transition: transform 0.2s, box-shadow 0.2s; }
        .card:hover { transform: translateY(-4px); box-shadow: 0 12px 24px -10px rgba(0,0,0,0.08); }
        .card-img-placeholder { height: 160px; background: #f1f3f5; display: flex; align-items: center; justify-content: center; font-size: 3rem; position: relative; }
        .stock-badge { position: absolute; top: 12px; right: 12px; font-size: 0.75rem; font-weight: 700; padding: 4px 10px; border-radius: 999px; }
        .badge-low { background: #ffe3e3; color: #c92a2a; }
        .badge-ok { background: #d3f9d8; color: #2b8a3e; }
        .card-body { padding: 20px; display: flex; flex-direction: column; flex: 1; }
        .card-cat { font-size: 0.75rem; text-transform: uppercase; font-weight: 800; color: var(--text-muted); margin-bottom: 6px; }
        .card-title { font-size: 1.1rem; font-weight: 700; margin-bottom: 12px; color: var(--dark); }
        .card-price { font-size: 1.4rem; font-weight: 800; color: var(--primary); margin-bottom: 16px; }
        .card-price span { font-size: 0.85rem; color: var(--text-muted); font-weight: 500; }
        .btn-add { background: var(--dark); color: white; border: none; padding: 12px; border-radius: 10px; font-weight: 700; cursor: pointer; transition: all 0.2s; margin-top: auto; }
        .btn-add:hover { background: var(--primary); }
        
        /* Drawer del carrito */
        .cart-drawer { position: fixed; top: 0; right: -420px; width: 400px; height: 100vh; background: white; box-shadow: -10px 0 30px rgba(0,0,0,0.15); z-index: 200; display: flex; flex-direction: column; transition: right 0.3s ease; }
        .cart-drawer.open { right: 0; }
        .drawer-header { padding: 20px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }
        .drawer-header h3 { font-size: 1.2rem; font-weight: 800; }
        .btn-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-muted); }
        .drawer-items { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 16px; }
        .cart-item { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid var(--border); padding-bottom: 12px; }
        .cart-item-info h4 { font-size: 0.95rem; font-weight: 700; }
        .cart-item-info p { font-size: 0.85rem; color: var(--text-muted); }
        .cart-item-qty { display: flex; align-items: center; gap: 8px; }
        .btn-qty { width: 26px; height: 26px; border-radius: 6px; border: 1px solid var(--border); background: white; font-weight: 700; cursor: pointer; }
        .drawer-footer { padding: 20px; border-top: 1px solid var(--border); background: var(--light-bg); }
        .total-row { display: flex; justify-content: space-between; font-size: 1.2rem; font-weight: 800; margin-bottom: 16px; }
        .btn-checkout { width: 100%; background: var(--success); color: white; border: none; padding: 14px; border-radius: 12px; font-weight: 800; font-size: 1rem; cursor: pointer; transition: all 0.2s; }
        .btn-checkout:hover { background: #237032; }
        
        /* Modal de checkout sandbox */
        .modal-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.5); backdrop-filter: blur(4px); z-index: 300; display: none; align-items: center; justify-content: center; padding: 20px; }
        .modal-overlay.open { display: flex; }
        .modal { background: white; border-radius: 20px; max-width: 500px; width: 100%; padding: 32px; box-shadow: 0 20px 40px rgba(0,0,0,0.2); }
        .modal-badge { display: inline-block; background: #e7f5ff; color: #1864ab; font-size: 0.75rem; font-weight: 800; padding: 4px 12px; border-radius: 999px; margin-bottom: 12px; }
        .modal h3 { font-size: 1.4rem; font-weight: 800; margin-bottom: 8px; }
        .form-group { margin-top: 16px; }
        .form-group label { display: block; font-size: 0.85rem; font-weight: 700; margin-bottom: 6px; color: var(--dark); }
        .form-group input { width: 100%; padding: 10px 14px; border: 1px solid var(--border); border-radius: 8px; font-size: 0.95rem; }
        .btn-pay { width: 100%; background: var(--primary); color: white; border: none; padding: 14px; border-radius: 10px; font-weight: 800; font-size: 1rem; cursor: pointer; margin-top: 24px; }
        
        /* Backdrop */
        .backdrop { position: fixed; inset: 0; background: rgba(0,0,0,0.4); z-index: 150; display: none; }
        .backdrop.open { display: block; }
    </style>
</head>
<body>
    <div class="top-banner">
        🔥 ETAPA 1 OFICIAL UTEM — TIENDA EN LÍNEA OPERATIVA (MODO SANDBOX)
    </div>

    <header>
        <div class="nav-container">
            <a href="#" class="brand">
                <div class="brand-badge">UTEM</div>
                <div class="brand-text">
                    <h1>Parrilleros UTEM</h1>
                    <span>Tienda Oficial · E-commerce Académico</span>
                </div>
            </a>
            
            <div class="search-box">
                <input type="text" id="searchInput" placeholder="Buscar carnes, carbón, bebidas, insumos..." oninput="filtrarProductos()">
            </div>

            <button class="cart-trigger" onclick="toggleCart()">
                🛒 Carrito <span class="cart-count" id="cartCount">0</span>
            </button>
        </div>
    </header>

    <div class="hero">
        <div class="hero-banner">
            <div class="hero-text">
                <span class="hero-tag">Plataforma Etapa 1 Configurada</span>
                <h2>Catálogo Parrillero Oficial</h2>
                <p>Base de datos sincronizada con el Carrito Evento Especial en Python para los 3 paradigmas.</p>
            </div>
        </div>
    </div>

    <div class="categories-bar" id="categoryBar">
        <button class="cat-pill active" onclick="filtrarCategoria('todas', this)">Todas</button>
        <button class="cat-pill" onclick="filtrarCategoria('carnico', this)">🥩 Carnes</button>
        <button class="cat-pill" onclick="filtrarCategoria('vegetariano', this)">🥗 Vegetariano</button>
        <button class="cat-pill" onclick="filtrarCategoria('abarrote', this)">🪵 Abarrotes & Carbón</button>
        <button class="cat-pill" onclick="filtrarCategoria('bebida', this)">🥤 Bebidas</button>
    </div>

    <div class="main-container">
        <div class="grid" id="productGrid"></div>
    </div>

    <!-- Drawer Carrito -->
    <div class="backdrop" id="backdrop" onclick="toggleCart()"></div>
    <div class="cart-drawer" id="cartDrawer">
        <div class="drawer-header">
            <h3>Tu Carrito de Compras</h3>
            <button class="btn-close" onclick="toggleCart()">&times;</button>
        </div>
        <div class="drawer-items" id="cartItems"></div>
        <div class="drawer-footer">
            <div class="total-row">
                <span>Total a pagar:</span>
                <span id="cartTotal">$0 CLP</span>
            </div>
            <button class="btn-checkout" onclick="iniciarCheckout()">Proceder al Checkout (Prueba)</button>
        </div>
    </div>

    <!-- Modal Checkout Modo Prueba -->
    <div class="modal-overlay" id="checkoutModal">
        <div class="modal">
            <span class="modal-badge">Pasarela de Pagos en Modo de Prueba (Sandbox)</span>
            <h3>Finalizar Compra</h3>
            <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 16px;">
                Simulación oficial de checkout sin cobro real de dinero para evaluación docente.
            </p>
            
            <div class="form-group">
                <label>Nombre del Comprador</label>
                <input type="text" value="Estudiante UTEM" id="buyerName">
            </div>
            <div class="form-group">
                <label>Correo Electrónico</label>
                <input type="email" value="estudiante.utem@correo.cl" id="buyerEmail">
            </div>
            <div class="form-group">
                <label>Tarjeta de Crédito Simulada (Sandbox)</label>
                <input type="text" value="4524 •••• •••• 9999 (Aprobación Automática)" readonly>
            </div>
            <div class="form-group">
                <label>Monto a Simular</label>
                <input type="text" id="modalTotal" readonly style="font-weight: 800; color: var(--primary);">
            </div>

            <button class="btn-pay" onclick="procesarPago()">Confirmar Pago de Prueba</button>
            <button style="width: 100%; background: none; border: none; color: var(--text-muted); margin-top: 12px; cursor: pointer;" onclick="cerrarCheckout()">Cancelar</button>
        </div>
    </div>

    <script>
        let catalogo = [];
        let carrito = {};
        let categoriaActual = 'todas';
        const emojis = {
            'prod_01': '🥩', 'prod_02': '🍖', 'prod_03': '🌭',
            'prod_04': '🍔', 'prod_05': '🫑', 'prod_06': '🪵',
            'prod_07': '🧂', 'prod_08': '🥤'
        };

        async function cargarProductos() {
            try {
                const res = await fetch('/api/products');
                const data = await res.json();
                catalogo = data.productos;
                renderizarProductos();
            } catch (err) {
                console.error("Error al cargar productos:", err);
            }
        }

        function formatoCLP(monto) {
            return '$' + Math.round(monto).toLocaleString('es-CL') + ' CLP';
        }

        function renderizarProductos() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const grid = document.getElementById('productGrid');
            grid.innerHTML = '';

            const filtrados = catalogo.filter(p => {
                const matchCat = (categoriaActual === 'todas' || p.categoria === categoriaActual);
                const matchQuery = p.nombre.toLowerCase().includes(query) || p.categoria.toLowerCase().includes(query);
                return matchCat && matchQuery;
            });

            filtrados.forEach(p => {
                const card = document.createElement('div');
                card.className = 'card';
                
                const isLowStock = p.stock <= 5;
                const badgeClass = isLowStock ? 'badge-low' : 'badge-ok';
                const badgeText = isLowStock ? `⚠️ Stock Crítico: ${p.stock} ${p.unidad}` : `En Bodega: ${p.stock} ${p.unidad}`;

                card.innerHTML = `
                    <div class="card-img-placeholder">
                        ${emojis[p.id] || '📦'}
                        <span class="stock-badge ${badgeClass}">${badgeText}</span>
                    </div>
                    <div class="card-body">
                        <span class="card-cat">${p.categoria} · SKU: ${p.id}</span>
                        <h3 class="card-title">${p.nombre}</h3>
                        <div class="card-price">${formatoCLP(p.precio)} <span>/ ${p.unidad}</span></div>
                        <button class="btn-add" onclick="agregarAlCarrito('${p.id}')">Agregar al Carrito</button>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        function filtrarCategoria(cat, btn) {
            categoriaActual = cat;
            document.querySelectorAll('.cat-pill').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            renderizarProductos();
        }

        function filtrarProductos() {
            renderizarProductos();
        }

        function agregarAlCarrito(id) {
            const prod = catalogo.find(p => p.id === id);
            if (!prod) return;
            if (carrito[id]) {
                carrito[id].cantidad += 1;
            } else {
                carrito[id] = { producto: prod, cantidad: 1 };
            }
            actualizarCarritoUI();
        }

        function cambiarCantidad(id, delta) {
            if (!carrito[id]) return;
            carrito[id].cantidad += delta;
            if (carrito[id].cantidad <= 0) {
                delete carrito[id];
            }
            actualizarCarritoUI();
        }

        function actualizarCarritoUI() {
            let total = 0;
            let count = 0;
            const container = document.getElementById('cartItems');
            container.innerHTML = '';

            const items = Object.values(carrito);
            if (items.length === 0) {
                container.innerHTML = '<p style="text-align: center; color: var(--text-muted); margin-top: 40px;">Tu carrito está vacío</p>';
            }

            items.forEach(it => {
                const sub = it.cantidad * it.producto.precio;
                total += sub;
                count += it.cantidad;

                const row = document.createElement('div');
                row.className = 'cart-item';
                row.innerHTML = `
                    <div class="cart-item-info">
                        <h4>${it.producto.nombre}</h4>
                        <p>${it.cantidad} ${it.producto.unidad} x ${formatoCLP(it.producto.precio)} = <strong>${formatoCLP(sub)}</strong></p>
                    </div>
                    <div class="cart-item-qty">
                        <button class="btn-qty" onclick="cambiarCantidad('${it.producto.id}', -1)">-</button>
                        <span>${it.cantidad}</span>
                        <button class="btn-qty" onclick="cambiarCantidad('${it.producto.id}', 1)">+</button>
                    </div>
                `;
                container.appendChild(row);
            });

            document.getElementById('cartTotal').textContent = formatoCLP(total);
            document.getElementById('cartCount').textContent = count;
        }

        function toggleCart() {
            const drawer = document.getElementById('cartDrawer');
            const backdrop = document.getElementById('backdrop');
            drawer.classList.toggle('open');
            backdrop.classList.toggle('open');
        }

        function iniciarCheckout() {
            const total = Object.values(carrito).reduce((acc, it) => acc + (it.cantidad * it.producto.precio), 0);
            if (total <= 0) {
                alert("Agrega al menos un producto al carrito antes de proceder.");
                return;
            }
            document.getElementById('modalTotal').value = formatoCLP(total);
            document.getElementById('checkoutModal').classList.add('open');
        }

        function cerrarCheckout() {
            document.getElementById('checkoutModal').classList.remove('open');
        }

        function procesarPago() {
            const total = document.getElementById('modalTotal').value;
            const numOrden = Math.floor(100000 + Math.random() * 900000);
            alert(`🎉 ¡PAGO DE PRUEBA EXITOSO!\\n\\nOrden #${numOrden}\\nMonto Aprobado: ${total}\\nModo: Sandbox Test Gateway\\n\\nDemostración de checkout de Etapa 1 completada.`);
            carrito = {};
            actualizarCarritoUI();
            cerrarCheckout();
            toggleCart();
        }

        window.onload = cargarProductos;
    </script>
</body>
</html>
"""

class ManejadorTienda(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)
        
        if url.path == "/" or url.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_TIENDA.encode("utf-8"))
            
        elif url.path == "/api/products":
            datos = cargar_catalogo()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(datos, ensure_ascii=False).encode("utf-8"))
            
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Silenciamos logs repetitivos en consola para no ensuciar la salida
        pass

def iniciar_servidor(puerto=8000):
    servidor = HTTPServer(("0.0.0.0", puerto), ManejadorTienda)
    print("\n" + "═" * 72)
    print(" 🚀 SERVIDOR TIENDA EN LÍNEA OPERATIVO (ETAPA 1 UTEM)")
    print(f" URL Local Demostrable: http://localhost:{puerto}")
    print("═" * 72)
    print(" ✅ Catálogo con categorías, buscador y stock en tiempo real.")
    print(" ✅ Carrito interactivo y checkout con pasarela en modo prueba.")
    print(" ✅ API REST activa en /api/products para integración con Python.")
    print(" Presione Ctrl + C para detener el servidor.\n")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor web detenido.")

if __name__ == "__main__":
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    iniciar_servidor(puerto)
