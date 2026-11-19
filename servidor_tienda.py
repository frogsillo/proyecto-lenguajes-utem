"""
SERVIDOR WEB DE COMERCIO ELECTRÓNICO - ETAPA 1 Y 2 (UTEM)
Plataforma: Supermercado Parrillero Retail (Inspirado en Jumbo.cl)
Asignatura: Lenguajes de Programación (Semestre 2-2026)

Este script levanta una tienda de comercio electrónico moderna, responsiva y demostrable
desplegable de forma local o en la nube gratuita (Render.com / Railway).

Características principales:
- UI/UX Retail profesional con paleta Jumbo (Verde #00843D, Neutros limpios, Acentos Parrilleros).
- Catálogo de 20 productos con fotografías reales y fallback a SVG ilustrado.
- Asistente 'Armar Asado Inteligente (IA)' con integración real al backend Python (POST /api/carrito-evento).
- Soporte en vivo de los 3 paradigmas (Imperativo, POO, Funcional).
- Carrito lateral interactivo con cálculo dinámico del Combo Parrillero (-10%).
- Checkout Sandbox con emisión de orden de compra formal (sin alertas nativas).
- Exportador de catálogo para Shopify Partners (GET /api/export/shopify.csv).
- Listo para la nube: lee la variable de entorno PORT y escucha en 0.0.0.0.
"""

import os
import sys
import json
import math
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

DIRECTORIO_RAIZ = os.path.abspath(os.path.dirname(__file__))
sys.path.append(DIRECTORIO_RAIZ)

from src.imperativo.carrito_imperativo import procesar_carrito_imperativo
from src.poo.carrito_poo import procesar_carrito_poo
from src.funcional.carrito_funcional import procesar_carrito_funcional

RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "catalogo_tienda.json")
if not os.path.exists(RUTA_CATALOGO):
    RUTA_CATALOGO = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_tienda.json")

RUTA_SHOPIFY_CSV = os.path.join(DIRECTORIO_RAIZ, "data", "catalogo_shopify.csv")


def cargar_catalogo():
    with open(RUTA_CATALOGO, "r", encoding="utf-8") as f:
        return json.load(f)


HTML_TIENDA = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Parrilleros UTEM — Supermercado Parrillero Oficial</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --jumbo-green: #00843D;
            --jumbo-green-dark: #006830;
            --jumbo-green-light: #e6f4ea;
            --primary-red: #c92a2a;
            --dark: #111827;
            --gray-700: #374151;
            --gray-500: #6B7280;
            --gray-200: #E5E7EB;
            --gray-100: #F3F4F6;
            --bg-body: #F4F6F8;
            --card-bg: #FFFFFF;
            --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
            --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
            --shadow-lg: 0 12px 28px rgba(0,0,0,0.15);
            --radius-md: 10px;
            --radius-lg: 16px;
        }

        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
        body { background-color: var(--bg-body); color: var(--dark); line-height: 1.5; padding-bottom: 80px; }

        /* Top Bar */
        .top-bar {
            background-color: var(--jumbo-green-dark);
            color: #ffffff;
            font-size: 0.82rem;
            padding: 8px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 500;
        }
        .top-bar a { color: #d1fae5; text-decoration: underline; margin-left: 8px; }
        .engine-badge {
            background-color: rgba(255, 255, 255, 0.18);
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.78rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }
        .engine-dot { width: 8px; height: 8px; background-color: #34d399; border-radius: 50%; box-shadow: 0 0 6px #34d399; }

        /* Header Sticky */
        header {
            background: #ffffff;
            border-bottom: 1px solid var(--gray-200);
            position: sticky;
            top: 0;
            z-index: 90;
            box-shadow: var(--shadow-sm);
        }
        .header-content {
            max-width: 1280px;
            margin: 0 auto;
            padding: 14px 24px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 20px;
        }
        .brand {
            display: flex;
            align-items: center;
            gap: 12px;
            text-decoration: none;
            color: var(--dark);
        }
        .brand-logo {
            width: 44px;
            height: 44px;
            background: linear-gradient(135deg, var(--jumbo-green), #047857);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 800;
            font-size: 1.3rem;
            box-shadow: 0 3px 8px rgba(0, 132, 61, 0.3);
        }
        .brand-text h1 { font-size: 1.25rem; font-weight: 800; letter-spacing: -0.02em; color: var(--dark); }
        .brand-text p { font-size: 0.75rem; color: var(--jumbo-green); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }

        /* Search Bar */
        .search-container {
            flex: 1;
            max-width: 540px;
            position: relative;
        }
        .search-input {
            width: 100%;
            padding: 12px 18px 12px 42px;
            background-color: var(--gray-100);
            border: 1px solid transparent;
            border-radius: 24px;
            font-size: 0.95rem;
            outline: none;
            transition: all 0.2s ease;
        }
        .search-input:focus {
            background-color: #ffffff;
            border-color: var(--jumbo-green);
            box-shadow: 0 0 0 3px rgba(0, 132, 61, 0.15);
        }
        .search-icon {
            position: absolute;
            left: 15px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--gray-500);
            font-size: 1.1rem;
        }

        /* Action Buttons */
        .header-actions { display: flex; align-items: center; gap: 14px; }
        .btn-ia {
            background: linear-gradient(135deg, #c92a2a, #e03131);
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 24px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 8px;
            box-shadow: 0 4px 12px rgba(201, 42, 42, 0.3);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }
        .btn-ia:hover {
            transform: translateY(-1px);
            box-shadow: 0 6px 16px rgba(201, 42, 42, 0.4);
        }
        .btn-cart {
            background-color: var(--jumbo-green);
            color: white;
            border: none;
            padding: 10px 18px;
            border-radius: 24px;
            font-weight: 700;
            font-size: 0.9rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 10px;
            transition: background-color 0.15s;
        }
        .btn-cart:hover { background-color: var(--jumbo-green-dark); }
        .cart-badge {
            background-color: #ffffff;
            color: var(--jumbo-green-dark);
            border-radius: 50%;
            width: 22px;
            height: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: 800;
        }

        /* Hero Banner */
        .hero {
            background: linear-gradient(rgba(17, 24, 39, 0.75), rgba(17, 24, 39, 0.8)),
                        url('https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=1600&q=80') center/cover no-repeat;
            color: white;
            padding: 50px 24px;
            text-align: left;
            position: relative;
        }
        .hero-inner {
            max-width: 1280px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 24px;
        }
        .hero-text { max-width: 720px; }
        .hero-tag {
            background-color: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(4px);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            display: inline-block;
            margin-bottom: 12px;
            color: #d1fae5;
        }
        .hero-text h2 { font-size: 2.2rem; font-weight: 800; line-height: 1.2; margin-bottom: 12px; }
        .hero-text p { font-size: 1.05rem; color: #e5e7eb; margin-bottom: 20px; max-width: 620px; }
        .hero-btns { display: flex; gap: 12px; flex-wrap: wrap; }
        .btn-hero-primary {
            background-color: #c92a2a;
            color: white;
            border: none;
            padding: 12px 22px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.95rem;
            cursor: pointer;
            box-shadow: 0 4px 14px rgba(201, 42, 42, 0.4);
        }
        .btn-hero-secondary {
            background-color: transparent;
            color: white;
            border: 2px solid white;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 0.95rem;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
        }
        .btn-hero-secondary:hover { background-color: rgba(255,255,255,0.15); }

        /* Container & Categories */
        .main-container { max-width: 1280px; margin: 30px auto; padding: 0 24px; }
        
        .controls-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            margin-bottom: 24px;
            background: white;
            padding: 14px 20px;
            border-radius: var(--radius-md);
            box-shadow: var(--shadow-sm);
        }
        .category-pills { display: flex; gap: 8px; flex-wrap: wrap; }
        .cat-pill {
            background: var(--gray-100);
            border: 1px solid transparent;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--gray-700);
            cursor: pointer;
            transition: all 0.15s;
        }
        .cat-pill:hover { background: #e5e7eb; }
        .cat-pill.active {
            background: var(--jumbo-green);
            color: white;
        }
        .sort-select {
            padding: 8px 14px;
            border-radius: 8px;
            border: 1px solid var(--gray-200);
            background: white;
            font-size: 0.88rem;
            font-weight: 500;
            outline: none;
            color: var(--gray-700);
        }

        /* Product Grid */
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
            gap: 20px;
        }
        .product-card {
            background: white;
            border-radius: var(--radius-md);
            border: 1px solid var(--gray-200);
            overflow: hidden;
            box-shadow: var(--shadow-sm);
            display: flex;
            flex-direction: column;
            transition: transform 0.15s, box-shadow 0.15s;
            position: relative;
        }
        .product-card:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-md);
        }
        .card-img-wrap {
            position: relative;
            width: 100%;
            height: 200px;
            background-color: #f3f4f6;
            overflow: hidden;
        }
        .card-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s ease;
        }
        .product-card:hover .card-img { transform: scale(1.04); }
        
        .badge-stock {
            position: absolute;
            top: 10px;
            left: 10px;
            background: #ef4444;
            color: white;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
            text-transform: uppercase;
        }
        .badge-combo {
            position: absolute;
            top: 10px;
            right: 10px;
            background: var(--jumbo-green);
            color: white;
            font-size: 0.72rem;
            font-weight: 700;
            padding: 4px 8px;
            border-radius: 4px;
        }

        .card-body {
            padding: 16px;
            display: flex;
            flex-direction: column;
            flex: 1;
        }
        .card-brand {
            font-size: 0.75rem;
            text-transform: uppercase;
            font-weight: 700;
            color: var(--gray-500);
            margin-bottom: 4px;
        }
        .card-title {
            font-size: 0.98rem;
            font-weight: 700;
            color: var(--dark);
            margin-bottom: 8px;
            line-height: 1.3;
            min-height: 2.6em;
        }
        .card-price-box {
            margin-top: auto;
            margin-bottom: 12px;
            display: flex;
            align-items: baseline;
            gap: 6px;
        }
        .card-price {
            font-size: 1.35rem;
            font-weight: 800;
            color: var(--dark);
        }
        .card-unit {
            font-size: 0.85rem;
            color: var(--gray-500);
        }
        
        .card-actions {
            display: flex;
            gap: 8px;
        }
        .btn-detail {
            background: var(--gray-100);
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--gray-700);
            cursor: pointer;
        }
        .btn-detail:hover { background: #e5e7eb; }
        .btn-add {
            flex: 1;
            background: var(--jumbo-green);
            color: white;
            border: none;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 700;
            cursor: pointer;
            transition: background 0.15s;
        }
        .btn-add:hover { background: var(--jumbo-green-dark); }

        .qty-stepper {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--jumbo-green-light);
            border: 1px solid var(--jumbo-green);
            border-radius: 6px;
            padding: 2px 4px;
            flex: 1;
        }
        .btn-step {
            background: white;
            border: 1px solid var(--jumbo-green);
            color: var(--jumbo-green-dark);
            width: 28px;
            height: 28px;
            border-radius: 4px;
            font-weight: 800;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .step-val {
            font-weight: 700;
            color: var(--jumbo-green-dark);
            font-size: 0.9rem;
        }

        /* Cart Drawer */
        .drawer-overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 100;
            display: none;
        }
        .cart-drawer {
            position: fixed;
            top: 0; right: -450px;
            width: 100%;
            max-width: 440px;
            height: 100%;
            background: white;
            z-index: 101;
            box-shadow: var(--shadow-lg);
            display: flex;
            flex-direction: column;
            transition: right 0.25s ease-out;
        }
        .cart-drawer.open { right: 0; }
        .drawer-header {
            padding: 20px;
            border-bottom: 1px solid var(--gray-200);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .drawer-title { font-size: 1.2rem; font-weight: 800; }
        .btn-close {
            background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--gray-500);
        }
        .drawer-items {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }
        .cart-item-row {
            display: flex;
            gap: 12px;
            align-items: center;
            padding-bottom: 14px;
            border-bottom: 1px solid var(--gray-100);
        }
        .cart-item-img {
            width: 56px;
            height: 56px;
            object-fit: cover;
            border-radius: 6px;
            background: var(--gray-100);
        }
        .cart-item-info { flex: 1; }
        .cart-item-name { font-weight: 700; font-size: 0.9rem; line-height: 1.2; }
        .cart-item-price { font-size: 0.85rem; color: var(--gray-500); }
        .cart-item-sub { font-weight: 800; font-size: 0.95rem; color: var(--dark); margin-top: 4px; }
        
        .drawer-footer {
            padding: 20px;
            background: var(--gray-100);
            border-top: 1px solid var(--gray-200);
        }
        .summary-row {
            display: flex;
            justify-content: space-between;
            font-size: 0.92rem;
            margin-bottom: 8px;
            color: var(--gray-700);
        }
        .summary-row.discount { color: var(--jumbo-green); font-weight: 700; }
        .summary-row.total {
            font-size: 1.25rem;
            font-weight: 800;
            color: var(--dark);
            margin-top: 10px;
            padding-top: 10px;
            border-top: 2px dashed #cbd5e1;
        }
        .btn-checkout {
            width: 100%;
            background: var(--jumbo-green);
            color: white;
            border: none;
            padding: 14px;
            border-radius: 8px;
            font-weight: 800;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 14px;
            box-shadow: 0 4px 12px rgba(0, 132, 61, 0.3);
        }
        .btn-checkout:hover { background: var(--jumbo-green-dark); }

        /* Modals */
        .modal {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: rgba(0,0,0,0.6);
            backdrop-filter: blur(4px);
            z-index: 120;
            display: none;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .modal-content {
            background: white;
            width: 100%;
            max-width: 620px;
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-lg);
            display: flex;
            flex-direction: column;
            max-height: 90vh;
        }
        .modal-header {
            padding: 20px;
            background: var(--gray-100);
            border-bottom: 1px solid var(--gray-200);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .modal-body {
            padding: 24px;
            overflow-y: auto;
        }

        /* Form elements inside modal */
        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px;
        }
        .form-group {
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 14px;
        }
        .form-group.full { grid-column: span 2; }
        .form-group label {
            font-weight: 600;
            font-size: 0.88rem;
            color: var(--gray-700);
        }
        .form-input, .form-select {
            padding: 10px 14px;
            border: 1px solid var(--gray-200);
            border-radius: 8px;
            font-size: 0.95rem;
            outline: none;
        }
        .form-input:focus, .form-select:focus {
            border-color: var(--jumbo-green);
        }
        .alert-box {
            background: #fffbeb;
            border-left: 4px solid #f59e0b;
            padding: 12px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
            color: #92400e;
            margin: 14px 0;
        }
        .alert-box.success {
            background: #ecfdf5;
            border-color: var(--jumbo-green);
            color: #065f46;
        }
        .result-card {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
        }

        /* Comprobante de Pago */
        .voucher-header { text-align: center; margin-bottom: 20px; }
        .voucher-stamp {
            display: inline-block;
            background: #ecfdf5;
            color: var(--jumbo-green);
            border: 2px solid var(--jumbo-green);
            font-weight: 800;
            font-size: 0.9rem;
            padding: 6px 16px;
            border-radius: 30px;
            margin-bottom: 10px;
            text-transform: uppercase;
        }
        .voucher-meta { font-size: 0.85rem; color: var(--gray-500); }
        .voucher-table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 0.9rem; }
        .voucher-table th, .voucher-table td { padding: 8px 10px; border-bottom: 1px solid #e2e8f0; text-align: left; }
        .voucher-table th { background: #f1f5f9; color: var(--gray-700); font-weight: 700; }
        .voucher-table .text-right { text-align: right; }

        @media (max-width: 768px) {
            .header-content { flex-direction: column; align-items: stretch; gap: 12px; }
            .search-container { max-width: 100%; }
            .form-grid { grid-template-columns: 1fr; }
            .form-group.full { grid-column: span 1; }
            .hero-text h2 { font-size: 1.7rem; }
        }
    </style>
</head>
<body>

    <!-- Top Bar -->
    <div class="top-bar">
        <div>
            <span>🚚 Despacho programado en Santiago · Retiro en Tienda Campus UTEM</span>
            <a href="/api/export/shopify.csv" target="_blank">📥 Exportar Catálogo Shopify CSV</a>
        </div>
        <div class="engine-badge">
            <span class="engine-dot"></span>
            <span>Motor Python 3.12 · 3 Paradigmas Operativos</span>
        </div>
    </div>

    <!-- Header Sticky -->
    <header>
        <div class="header-content">
            <a href="/" class="brand">
                <div class="brand-logo">P</div>
                <div class="brand-text">
                    <h1>Parrilleros UTEM</h1>
                    <p>Supermercado del Asado</p>
                </div>
            </a>

            <div class="search-container">
                <span class="search-icon">🔍</span>
                <input type="text" id="searchInput" class="search-input" placeholder="Buscar carne, carbón, embutidos, vegetales o bebidas..." onkeyup="filtrarCatalogo()">
            </div>

            <div class="header-actions">
                <button class="btn-ia" onclick="abrirModalIA()">
                    <span>🔥 Armar Asado Inteligente (IA)</span>
                </button>
                <button class="btn-cart" onclick="toggleCartDrawer()">
                    <span>🛒</span>
                    <span id="cartCountBadge" class="cart-badge">0</span>
                    <span id="cartTotalHeader">$0</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Hero Banner -->
    <section class="hero">
        <div class="hero-inner">
            <div class="hero-text">
                <span class="hero-tag">Especial Temporada Parrillera 2026</span>
                <h2>El Mejor Asado Empieza Aquí</h2>
                <p>Cortes vacunos premium, carbón vegetal de espino, embutidos artesanales y alternativas veganas. Deja que nuestro asistente IA calcule las porciones exactas para tu evento sin desperdicios ni sobrecostos.</p>
                <div class="hero-btns">
                    <button class="btn-hero-primary" onclick="abrirModalIA()">⚡ Armar Asado Automático con IA</button>
                    <a href="#catalogoSeccion" class="btn-hero-secondary">Ver Todo el Catálogo</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content -->
    <main class="main-container" id="catalogoSeccion">
        <!-- Controls Bar -->
        <div class="controls-bar">
            <div class="category-pills">
                <button class="cat-pill active" onclick="filtrarCategoria('todos', this)">Todos (20)</button>
                <button class="cat-pill" onclick="filtrarCategoria('carnico', this)">Carnes & Embutidos (6)</button>
                <button class="cat-pill" onclick="filtrarCategoria('vegetariano', this)">Vegetariano (5)</button>
                <button class="cat-pill" onclick="filtrarCategoria('carbon', this)">Carbón & Fuego (3)</button>
                <button class="cat-pill" onclick="filtrarCategoria('sal', this)">Sales & Abarrotes (2)</button>
                <button class="cat-pill" onclick="filtrarCategoria('bebida', this)">Bebidas & Jugos (4)</button>
            </div>
            <div>
                <select id="sortSelect" class="sort-select" onchange="ordenarCatalogo()">
                    <option value="relevancia">Ordenar por: Relevancia</option>
                    <option value="menor-precio">Menor precio</option>
                    <option value="mayor-precio">Mayor precio</option>
                    <option value="nombre">Nombre A-Z</option>
                </select>
            </div>
        </div>

        <!-- Products Grid -->
        <div class="products-grid" id="productsGrid">
            <!-- Renderizado dinámico vía JavaScript -->
        </div>
    </main>

    <!-- Cart Drawer -->
    <div id="drawerOverlay" class="drawer-overlay" onclick="toggleCartDrawer()"></div>
    <aside id="cartDrawer" class="cart-drawer">
        <div class="drawer-header">
            <h3 class="drawer-title">Tu Carrito de Asado</h3>
            <button class="btn-close" onclick="toggleCartDrawer()">&times;</button>
        </div>
        <div class="drawer-items" id="cartDrawerItems">
            <!-- Items del carrito -->
        </div>
        <div class="drawer-footer">
            <div class="summary-row">
                <span>Subtotal Neto:</span>
                <span id="drawerSubtotal">$0 CLP</span>
            </div>
            <div class="summary-row discount" id="rowComboDiscount" style="display: none;">
                <span>Combo Parrillero (-10%):</span>
                <span id="drawerDiscount">-$0 CLP</span>
            </div>
            <div class="summary-row total">
                <span>TOTAL A PAGAR:</span>
                <span id="drawerTotal">$0 CLP</span>
            </div>
            <button class="btn-checkout" onclick="iniciarCheckoutSandbox()">Continuar al Pago Sandbox ➔</button>
        </div>
    </aside>

    <!-- Modal Ficha Técnica de Producto -->
    <div id="modalProducto" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 id="modalProdTitle" style="font-size: 1.2rem; font-weight: 800;">Ficha del Producto</h3>
                <button class="btn-close" onclick="cerrarModal('modalProducto')">&times;</button>
            </div>
            <div class="modal-body" id="modalProdBody">
                <!-- Contenido dinámico -->
            </div>
        </div>
    </div>

    <!-- Modal Asistente Inteligente IA -->
    <div id="modalIA" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <div>
                    <h3 style="font-size: 1.25rem; font-weight: 800; color: #c92a2a;">🔥 Armar Carrito Evento con IA</h3>
                    <p style="font-size: 0.8rem; color: var(--gray-500);">Dimensiona raciones, quiebre de stock y presupuesto con Python.</p>
                </div>
                <button class="btn-close" onclick="cerrarModal('modalIA')">&times;</button>
            </div>
            <div class="modal-body">
                <form id="formAsadoIA" onsubmit="procesarAsadoIA(event)">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Adultos Comensales (350g c/u):</label>
                            <input type="number" id="iaAdultos" class="form-input" value="10" min="1" required>
                        </div>
                        <div class="form-group">
                            <label>Niños Comensales (150g c/u):</label>
                            <input type="number" id="iaNinos" class="form-input" value="4" min="0" required>
                        </div>
                        <div class="form-group">
                            <label>Vegetarianos (Hamburguesa + Morrón):</label>
                            <input type="number" id="iaVegetarianos" class="form-input" value="2" min="0" required>
                        </div>
                        <div class="form-group">
                            <label>Presupuesto Máximo (CLP):</label>
                            <input type="number" id="iaPresupuesto" class="form-input" value="120000" min="10000" step="1000" required>
                        </div>
                        <div class="form-group">
                            <label>Corte Vacuno Preferido:</label>
                            <select id="iaCorte" class="form-select">
                                <option value="prod_01">Lomo Vetado ($14.990 - Stock Crítico 3.0 kg)</option>
                                <option value="prod_02">Sobrecostilla ($9.990 - Stock 15.0 kg)</option>
                                <option value="prod_09">Entraña Vacuno ($18.990 - Stock 8.0 kg)</option>
                                <option value="prod_10">Punta Picana ($12.990 - Stock 10.0 kg)</option>
                            </select>
                        </div>
                        <div class="form-group">
                            <label>Paradigma Backend Python:</label>
                            <select id="iaParadigma" class="form-select">
                                <option value="imperativo">1. Imperativo (Procedural con Stock Mutation)</option>
                                <option value="poo" selected>2. Orientado a Objetos (Patrón Strategy SOLID)</option>
                                <option value="funcional">3. Funcional (Pipeline Puro e Inmutable)</option>
                            </select>
                        </div>
                    </div>
                    <button type="submit" class="btn-checkout" style="margin-top: 10px; background: #c92a2a;">
                        ⚡ Calcular Carrito con el Motor Seleccionado
                    </button>
                </form>

                <div id="resultadoIABox" style="display: none; margin-top: 20px;">
                    <!-- Resultado del backend Python -->
                </div>
            </div>
        </div>
    </div>

    <!-- Modal Comprobante Sandbox -->
    <div id="modalComprobante" class="modal">
        <div class="modal-content">
            <div class="modal-header">
                <h3 style="font-weight: 800;">Orden de Compra Finalizada</h3>
                <button class="btn-close" onclick="cerrarModal('modalComprobante')">&times;</button>
            </div>
            <div class="modal-body" id="modalComprobanteBody">
                <!-- Contenido dinámico del comprobante -->
            </div>
        </div>
    </div>

    <script>
        // ESTADO GLOBAL DE LA APLICACIÓN
        let catalogoProductos = [];
        let carrito = {}; // id -> { producto, cantidad }
        let categoriaActiva = 'todos';
        let resultadoIAActual = null;

        // CARGA INICIAL DESDE LA API
        async function cargarProductos() {
            try {
                const res = await fetch('/api/products');
                const data = await res.json();
                catalogoProductos = data.productos;
                renderizarGrid(catalogoProductos);
            } catch (err) {
                console.error("Error al cargar catálogo:", err);
            }
        }

        // RENDERIZADO DEL CATÁLOGO
        function renderizarGrid(productos) {
            const grid = document.getElementById('productsGrid');
            if (!productos || productos.length === 0) {
                grid.innerHTML = '<p style="grid-column: 1/-1; text-align: center; color: var(--gray-500); padding: 40px;">No se encontraron productos coincidentes.</p>';
                return;
            }

            grid.innerHTML = productos.map(p => {
                const enCarrito = carrito[p.id] ? carrito[p.id].cantidad : 0;
                
                // Badges
                let stockBadge = '';
                if (p.id === 'prod_01') {
                    stockBadge = '<span class="badge-stock">⚠️ Stock Crítico: 3.0 kg</span>';
                }
                
                let comboBadge = '';
                if (['carnico', 'carbon', 'sal'].includes(p.categoria)) {
                    comboBadge = '<span class="badge-combo">10% Dcto Combo</span>';
                }

                // Botón o Stepper
                let actionBtn = `
                    <button class="btn-detail" onclick="verFicha('${p.id}')">Ver Detalle</button>
                    <button class="btn-add" onclick="agregarAlCarrito('${p.id}')">+ Agregar</button>
                `;
                if (enCarrito > 0) {
                    actionBtn = `
                        <button class="btn-detail" onclick="verFicha('${p.id}')">Ver Detalle</button>
                        <div class="qty-stepper">
                            <button class="btn-step" onclick="modificarCantidad('${p.id}', -1)">-</button>
                            <span class="step-val">${enCarrito}</span>
                            <button class="btn-step" onclick="modificarCantidad('${p.id}', 1)">+</button>
                        </div>
                    `;
                }

                return `
                    <div class="product-card" id="card-${p.id}">
                        <div class="card-img-wrap">
                            <img src="${p.imagen_url}" alt="${p.nombre}" class="card-img" onerror="this.src='data:image/svg+xml;utf8,<svg xmlns=\\'http://www.w3.org/2000/svg\\' width=\\'300\\' height=\\'200\\' viewBox=\\'0 0 300 200\\'><rect fill=\\'%23f3f4f6\\' width=\\'300\\' height=\\'200\\'/><text fill=\\'%239ca3af\\' font-family=\\'sans-serif\\' font-size=\\'14\\' dy=\\'10.5\\' font-weight=\\'bold\\' x=\\'50%\\' y=\\'50%\\' text-anchor=\\'middle\\'>${p.nombre}</text></svg>'">
                            ${stockBadge}
                            ${comboBadge}
                        </div>
                        <div class="card-body">
                            <div class="card-brand">${p.marca || 'Parrilleros UTEM'}</div>
                            <h4 class="card-title">${p.nombre}</h4>
                            <div class="card-price-box">
                                <span class="card-price">$${p.precio.toLocaleString('es-CL')}</span>
                                <span class="card-unit">/ ${p.unidad}</span>
                            </div>
                            <div class="card-actions" id="actions-${p.id}">
                                ${actionBtn}
                            </div>
                        </div>
                    </div>
                `;
            }).join('');
        }

        // FILTRADO POR CATEGORÍA Y BUSCADOR
        function filtrarCategoria(cat, btn) {
            categoriaActiva = cat;
            document.querySelectorAll('.cat-pill').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');
            filtrarCatalogo();
        }

        function filtrarCatalogo() {
            const query = document.getElementById('searchInput').value.toLowerCase().trim();
            let filtrados = catalogoProductos.filter(p => {
                const matchCat = categoriaActiva === 'todos' || p.categoria === categoriaActiva;
                const matchText = p.nombre.toLowerCase().includes(query) || 
                                  (p.marca && p.marca.toLowerCase().includes(query)) ||
                                  p.categoria.toLowerCase().includes(query);
                return matchCat && matchText;
            });
            ordenarArray(filtrados);
            renderizarGrid(filtrados);
        }

        function ordenarCatalogo() {
            filtrarCatalogo();
        }

        function ordenarArray(lista) {
            const criterio = document.getElementById('sortSelect').value;
            if (criterio === 'menor-precio') {
                lista.sort((a, b) => a.precio - b.precio);
            } else if (criterio === 'mayor-precio') {
                lista.sort((a, b) => b.precio - a.precio);
            } else if (criterio === 'nombre') {
                lista.sort((a, b) => a.nombre.localeCompare(b.nombre));
            }
        }

        // GESTIÓN DEL CARRITO
        function agregarAlCarrito(idProducto, cantidad = 1) {
            const producto = catalogoProductos.find(p => p.id === idProducto);
            if (!producto) return;

            if (!carrito[idProducto]) {
                carrito[idProducto] = { producto, cantidad: 0 };
            }
            carrito[idProducto].cantidad += cantidad;
            actualizarEstadoCarrito();
        }

        function modificarCantidad(idProducto, delta) {
            if (!carrito[idProducto]) return;
            carrito[idProducto].cantidad += delta;
            if (carrito[idProducto].cantidad <= 0) {
                delete carrito[idProducto];
            }
            actualizarEstadoCarrito();
        }

        function actualizarEstadoCarrito() {
            let totalItems = 0;
            let subtotalNeto = 0;

            let tieneCarnico = false;
            let tieneCarbon = false;
            let tieneSal = false;
            let subtotalAfectoCombo = 0;

            for (const id in carrito) {
                const item = carrito[id];
                totalItems += item.cantidad;
                const subItem = item.cantidad * item.producto.precio;
                subtotalNeto += subItem;

                if (item.producto.categoria === 'carnico') {
                    tieneCarnico = true;
                    subtotalAfectoCombo += subItem;
                } else if (item.producto.categoria === 'carbon') {
                    tieneCarbon = true;
                    subtotalAfectoCombo += subItem;
                } else if (item.producto.categoria === 'sal') {
                    tieneSal = true;
                    subtotalAfectoCombo += subItem;
                }
            }

            // Descuento Combo Parrillero: 10% si tiene Carne + Carbón + Sal
            let descuentoCombo = 0;
            if (tieneCarnico && tieneCarbon && tieneSal) {
                descuentoCombo = Math.round(subtotalAfectoCombo * 0.10);
            }

            const totalFinal = Math.max(0, subtotalNeto - descuentoCombo);

            // Actualizar Badges y Header
            document.getElementById('cartCountBadge').innerText = totalItems;
            document.getElementById('cartTotalHeader').innerText = `$${totalFinal.toLocaleString('es-CL')}`;

            // Actualizar Drawer
            renderizarDrawerItems();
            document.getElementById('drawerSubtotal').innerText = `$${subtotalNeto.toLocaleString('es-CL')} CLP`;
            
            const rowDiscount = document.getElementById('rowComboDiscount');
            if (descuentoCombo > 0) {
                rowDiscount.style.display = 'flex';
                document.getElementById('drawerDiscount').innerText = `-$${descuentoCombo.toLocaleString('es-CL')} CLP`;
            } else {
                rowDiscount.style.display = 'none';
            }

            document.getElementById('drawerTotal').innerText = `$${totalFinal.toLocaleString('es-CL')} CLP`;

            // Refrescar las tarjetas de producto en el grid
            filtrarCatalogo();
        }

        function renderizarDrawerItems() {
            const cont = document.getElementById('cartDrawerItems');
            const ids = Object.keys(carrito);

            if (ids.length === 0) {
                cont.innerHTML = '<p style="text-align: center; color: var(--gray-500); padding: 50px 0;">Tu carrito está vacío.</p>';
                return;
            }

            cont.innerHTML = ids.map(id => {
                const item = carrito[id];
                const sub = item.cantidad * item.producto.precio;
                return `
                    <div class="cart-item-row">
                        <img src="${item.producto.imagen_url}" class="cart-item-img" onerror="this.style.display='none'">
                        <div class="cart-item-info">
                            <div class="cart-item-name">${item.producto.nombre}</div>
                            <div class="cart-item-price">$${item.producto.precio.toLocaleString('es-CL')} x ${item.producto.unidad}</div>
                            <div class="cart-item-sub">$${sub.toLocaleString('es-CL')} CLP</div>
                        </div>
                        <div class="qty-stepper" style="max-width: 100px;">
                            <button class="btn-step" onclick="modificarCantidad('${id}', -1)">-</button>
                            <span class="step-val">${item.cantidad}</span>
                            <button class="btn-step" onclick="modificarCantidad('${id}', 1)">+</button>
                        </div>
                    </div>
                `;
            }).join('');
        }

        function toggleCartDrawer() {
            const drawer = document.getElementById('cartDrawer');
            const overlay = document.getElementById('drawerOverlay');
            if (drawer.classList.contains('open')) {
                drawer.classList.remove('open');
                overlay.style.display = 'none';
            } else {
                drawer.classList.add('open');
                overlay.style.display = 'block';
            }
        }

        // MODAL DETALLE DE PRODUCTO
        function verFicha(idProducto) {
            const p = catalogoProductos.find(x => x.id === idProducto);
            if (!p) return;

            let sustitutoHtml = '';
            if (p.sustituto_id) {
                const sub = catalogoProductos.find(x => x.id === p.sustituto_id);
                const nombreSub = sub ? sub.nombre : p.sustituto_id;
                sustitutoHtml = `
                    <div class="alert-box">
                        <strong>⚠️ Regla de Bodega (Quiebre de Stock):</strong>
                        Si las existencias en bodega se agotan (${p.stock} ${p.unidad} disponibles), el motor sustituye automáticamente por <strong>${nombreSub}</strong>.
                    </div>
                `;
            }

            const body = document.getElementById('modalProdBody');
            body.innerHTML = `
                <div style="display: flex; gap: 20px; flex-wrap: wrap;">
                    <img src="${p.imagen_url}" style="width: 100%; max-width: 240px; height: 220px; object-fit: cover; border-radius: 8px;">
                    <div style="flex: 1; min-width: 260px;">
                        <span style="font-size: 0.8rem; font-weight: 700; color: var(--gray-500); text-transform: uppercase;">${p.marca || 'Parrilleros UTEM'} · SKU: ${p.id}</span>
                        <h2 style="font-size: 1.4rem; font-weight: 800; margin: 4px 0 10px;">${p.nombre}</h2>
                        <div style="font-size: 1.6rem; font-weight: 800; color: var(--jumbo-green); margin-bottom: 10px;">
                            $${p.precio.toLocaleString('es-CL')} <span style="font-size: 0.9rem; color: var(--gray-500);">/ ${p.unidad}</span>
                        </div>
                        <p style="font-size: 0.92rem; color: var(--gray-700); margin-bottom: 14px;">${p.descripcion || 'Producto fresco seleccionado bajo estándares UTEM.'}</p>
                        <p style="font-size: 0.85rem; color: var(--gray-500); margin-bottom: 14px;"><strong>Stock en bodega:</strong> ${p.stock} ${p.unidad}</p>
                        ${sustitutoHtml}
                        <button class="btn-checkout" onclick="agregarAlCarrito('${p.id}'); cerrarModal('modalProducto'); toggleCartDrawer();">
                            + Agregar a mi pedido
                        </button>
                    </div>
                </div>
            `;
            document.getElementById('modalProducto').style.display = 'flex';
        }

        // MODAL INTELIGENTE (IA BACKEND INTEGRATION)
        function abrirModalIA() {
            document.getElementById('modalIA').style.display = 'flex';
        }

        async function procesarAsadoIA(event) {
            event.preventDefault();
            const btn = event.target.querySelector('button[type="submit"]');
            btn.disabled = true;
            btn.innerText = 'Calculando con motor Python...';

            const payload = {
                adultos: parseInt(document.getElementById('iaAdultos').value),
                ninos: parseInt(document.getElementById('iaNinos').value),
                vegetarianos: parseInt(document.getElementById('iaVegetarianos').value),
                presupuesto_maximo: parseFloat(document.getElementById('iaPresupuesto').value),
                tipo_corte_preferido: document.getElementById('iaCorte').value,
                paradigma: document.getElementById('iaParadigma').value
            };

            try {
                const res = await fetch('/api/carrito-evento', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(payload)
                });
                const boleta = await res.json();
                resultadoIAActual = boleta;
                mostrarResultadoIA(boleta, payload.paradigma);
            } catch (err) {
                alert("Error al comunicarse con el backend Python: " + err);
            } finally {
                btn.disabled = false;
                btn.innerText = '⚡ Calcular Carrito con el Motor Seleccionado';
            }
        }

        function mostrarResultadoIA(boleta, paradigma) {
            const box = document.getElementById('resultadoIABox');
            box.style.display = 'block';

            let reglasHtml = '';
            if (boleta.items.some(it => it.nota && it.nota.includes('Sustituto activado'))) {
                reglasHtml += '<div class="alert-box"><strong>🔄 Quiebre de Stock Activado:</strong> Se agotaron los 3.0 kg de Lomo Vetado y se sustituyó automáticamente por Sobrecostilla.</div>';
            }
            if (boleta.descuento > 0) {
                reglasHtml += `<div class="alert-box success"><strong>🎉 Combo Parrillero Aplicado:</strong> Ahorraste $${Math.round(boleta.descuento).toLocaleString('es-CL')} CLP (10% en Carnes + Carbón + Sal).</div>`;
            }
            if (boleta.ajustes_presupuesto && boleta.ajustes_presupuesto.length > 0) {
                reglasHtml += `<div class="alert-box" style="background:#fef2f2; border-color:#ef4444; color:#991b1b;">
                    <strong>⚖️ Optimización Presupuestaria Activa:</strong>
                    <ul>${boleta.ajustes_presupuesto.map(a => `<li>${a}</li>`).join('')}</ul>
                </div>`;
            }

            const itemsRows = boleta.items.map(it => `
                <div style="display:flex; justify-content:space-between; padding:4px 0; border-bottom:1px dashed #e2e8f0; font-size:0.88rem;">
                    <span>${it.nombre} (${it.cantidad} ${it.unidad})</span>
                    <strong>$${Math.round(it.subtotal).toLocaleString('es-CL')} CLP</strong>
                </div>
            `).join('');

            box.innerHTML = `
                <div class="result-card">
                    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                        <span style="font-weight:800; font-size:1.05rem;">Diagnóstico del Motor (${paradigma.toUpperCase()}):</span>
                        <span class="engine-badge" style="background:var(--jumbo-green); color:white;">Validado</span>
                    </div>
                    ${reglasHtml}
                    <div style="margin: 12px 0;">
                        ${itemsRows}
                    </div>
                    <div style="display:flex; justify-content:space-between; font-weight:800; font-size:1.2rem; margin:10px 0; padding-top:10px; border-top:2px solid #cbd5e1;">
                        <span>TOTAL CALCULADO:</span>
                        <span style="color:var(--jumbo-green);">$${Math.round(boleta.total).toLocaleString('es-CL')} CLP</span>
                    </div>
                    <button class="btn-checkout" onclick="cargarItemsIAlCarrito()">
                        🛒 Cargar esta propuesta directamente a mi Carrito
                    </button>
                </div>
            `;
        }

        function cargarItemsIAlCarrito() {
            if (!resultadoIAActual || !resultadoIAActual.items) return;
            // Limpiamos carrito previo o sobreescribimos
            carrito = {};
            resultadoIAActual.items.forEach(it => {
                const prod = catalogoProductos.find(p => p.id === it.id);
                if (prod) {
                    carrito[it.id] = {
                        producto: prod,
                        cantidad: it.cantidad
                    };
                }
            });
            actualizarEstadoCarrito();
            cerrarModal('modalIA');
            toggleCartDrawer();
        }

        // CHECKOUT SANDBOX CON EMISIÓN DE BOLETA
        function iniciarCheckoutSandbox() {
            const ids = Object.keys(carrito);
            if (ids.length === 0) {
                alert("Tu carrito está vacío. Agrega productos para pagar.");
                return;
            }
            toggleCartDrawer();

            let subtotal = 0;
            let descuento = 0;
            let subtotalAfecto = 0;
            let tieneCarnico = false, tieneCarbon = false, tieneSal = false;

            for (const id in carrito) {
                const item = carrito[id];
                const sub = item.cantidad * item.producto.precio;
                subtotal += sub;
                if (item.producto.categoria === 'carnico') { tieneCarnico = true; subtotalAfecto += sub; }
                if (item.producto.categoria === 'carbon') { tieneCarbon = true; subtotalAfecto += sub; }
                if (item.producto.categoria === 'sal') { tieneSal = true; subtotalAfecto += sub; }
            }

            if (tieneCarnico && tieneCarbon && tieneSal) {
                descuento = Math.round(subtotalAfecto * 0.10);
            }
            const total = Math.max(0, subtotal - descuento);

            const numOrden = "UTEM-2026-" + Math.floor(1000 + Math.random() * 9000);
            const fechaHora = new Date().toLocaleString('es-CL');

            const modalBody = document.getElementById('modalComprobanteBody');
            modalBody.innerHTML = `
                <div class="voucher-header">
                    <div class="voucher-stamp">✔ Pago Aprobado (Modo Sandbox)</div>
                    <h2 style="font-weight: 800; font-size: 1.4rem;">Comprobante de Venta Electrónica</h2>
                    <div class="voucher-meta">Orden #${numOrden} · ${fechaHora}</div>
                    <div class="voucher-meta">Comercio: Parrilleros UTEM · Pasarela Académica</div>
                </div>

                <div style="background:#f8fafc; padding:12px; border-radius:8px; margin-bottom:14px; font-size:0.88rem;">
                    <strong>Método de Pago:</strong> Tarjeta Crédito Sandbox (4524 •••• •••• 9999)<br>
                    <strong>Tipo de Entrega:</strong> Retiro Express Campus Macul UTEM
                </div>

                <table class="voucher-table">
                    <thead>
                        <tr>
                            <th>Producto</th>
                            <th class="text-right">Cant.</th>
                            <th class="text-right">Unitario</th>
                            <th class="text-right">Subtotal</th>
                        </tr>
                    </thead>
                    <tbody>
                        ${Object.keys(carrito).map(id => {
                            const it = carrito[id];
                            return `
                                <tr>
                                    <td>${it.producto.nombre}</td>
                                    <td class="text-right">${it.cantidad} ${it.producto.unidad}</td>
                                    <td class="text-right">$${it.producto.precio.toLocaleString('es-CL')}</td>
                                    <td class="text-right">$${(it.cantidad * it.producto.precio).toLocaleString('es-CL')}</td>
                                </tr>
                            `;
                        }).join('')}
                    </tbody>
                </table>

                <div style="text-align: right; font-size: 0.92rem; line-height: 1.6;">
                    <div>Subtotal: $${subtotal.toLocaleString('es-CL')} CLP</div>
                    ${descuento > 0 ? `<div style="color:var(--jumbo-green); font-weight:700;">Dcto. Combo Parrillero: -$${descuento.toLocaleString('es-CL')} CLP</div>` : ''}
                    <div style="font-size: 1.3rem; font-weight: 800; color: var(--dark); margin-top: 6px;">
                        TOTAL PAGADO: $${total.toLocaleString('es-CL')} CLP
                    </div>
                </div>

                <div style="margin-top: 20px; display: flex; gap: 10px;">
                    <button class="btn-checkout" style="background:#2563eb;" onclick="window.print()">🖨️ Imprimir Boleta</button>
                    <button class="btn-checkout" style="background:var(--gray-700);" onclick="vaciarCarritoYSalir()">Cerrar y Nuevo Pedido</button>
                </div>
            `;
            document.getElementById('modalComprobante').style.display = 'flex';
        }

        function vaciarCarritoYSalir() {
            carrito = {};
            actualizarEstadoCarrito();
            cerrarModal('modalComprobante');
        }

        function cerrarModal(idModal) {
            document.getElementById(idModal).style.display = 'none';
        }

        // INICIALIZACIÓN
        cargarProductos();
    </script>
</body>
</html>
"""


class ManejadorTienda(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urllib.parse.urlparse(self.path)

        if url.path in ["/", "/index.html"]:
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

        elif url.path == "/api/export/shopify.csv":
            if os.path.exists(RUTA_SHOPIFY_CSV):
                with open(RUTA_SHOPIFY_CSV, "rb") as f_csv:
                    contenido_csv = f_csv.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/csv; charset=utf-8")
                self.send_header("Content-Disposition", 'attachment; filename="catalogo_shopify_utem.csv"')
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(contenido_csv)
            else:
                self.send_response(404)
                self.end_headers()

        elif url.path == "/api/health":
            resp = {"status": "ok", "app": "Parrilleros UTEM Retail", "engine": "Python 3.12"}
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(resp).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        url = urllib.parse.urlparse(self.path)

        if url.path == "/api/carrito-evento":
            longitud = int(self.headers.get("Content-Length", 0))
            cuerpo = self.rfile.read(longitud).decode("utf-8")
            
            try:
                datos_req = json.loads(cuerpo)
            except Exception:
                self.send_response(400)
                self.end_headers()
                return

            adultos = int(datos_req.get("adultos", 10))
            ninos = int(datos_req.get("ninos", 4))
            vegetarianos = int(datos_req.get("vegetarianos", 2))
            presupuesto = float(datos_req.get("presupuesto_maximo", 120000.0))
            corte = datos_req.get("tipo_corte_preferido", "prod_01")
            paradigma = datos_req.get("paradigma", "poo").lower()

            evento_input = {
                "nombre_evento": f"Asado Asistido por IA ({adultos + ninos + vegetarianos} comensales)",
                "comensales": {
                    "adultos": adultos,
                    "ninos": ninos,
                    "vegetarianos": vegetarianos
                },
                "preferencias": {
                    "incluir_alcohol": False,
                    "tipo_corte_preferido": corte
                },
                "presupuesto_maximo": presupuesto
            }

            # Enrutamiento según el paradigma seleccionado
            if paradigma == "imperativo":
                boleta = procesar_carrito_imperativo(RUTA_CATALOGO, evento_input)
            elif paradigma == "funcional":
                boleta = procesar_carrito_funcional(RUTA_CATALOGO, evento_input)
            else: # poo default
                boleta = procesar_carrito_poo(RUTA_CATALOGO, evento_input)

            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(boleta, ensure_ascii=False).encode("utf-8"))

        else:
            self.send_response(404)
            self.end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def log_message(self, format, *args):
        # Silenciamos logs en consola
        pass


def iniciar_servidor(puerto=None, host="0.0.0.0"):
    if puerto is None:
        puerto = int(os.environ.get("PORT", 8000))
    servidor = HTTPServer((host, puerto), ManejadorTienda)
    print("\n" + "═" * 74)
    print(" 🚀 SERVIDOR SUPERMERCADO RETAIL OPERATIVO (UTEM - LENGUAJES)")
    print(f" URL Local: http://localhost:{puerto}")
    print(f" Host de Red: {host}:{puerto} (Compatible con Render.com / Railway)")
    print("═" * 74)
    print(" ✅ Catálogo de 20 productos con fotografías reales y fallback SVG.")
    print(" ✅ POST /api/carrito-evento conectado a los 3 paradigmas Python.")
    print(" ✅ GET /api/export/shopify.csv disponible para Shopify Partners.")
    print(" ✅ Checkout Sandbox estilizado con emisión de orden académica.")
    print(" Presione Ctrl + C para detener el servidor.\n")
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor web detenido.")


if __name__ == "__main__":
    puerto = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8000))
    iniciar_servidor(puerto)
