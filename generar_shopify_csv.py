import csv
import json
import os

REPO_DIR = '/home/frog/.gemini/antigravity/scratch/proyecto_lenguajes'

with open(os.path.join(REPO_DIR, 'data/catalogo_tienda.json'), 'r', encoding='utf-8') as f:
    catalogo = json.load(f)

csv_path = os.path.join(REPO_DIR, 'data/catalogo_shopify.csv')

headers = [
    "Handle", "Title", "Body (HTML)", "Vendor", "Type", "Tags", "Published",
    "Option1 Name", "Option1 Value", "Variant SKU", "Variant Grams",
    "Variant Inventory Tracker", "Variant Inventory Qty", "Variant Inventory Policy",
    "Variant Fulfillment Service", "Variant Price", "Variant Compare At Price",
    "Variant Requires Shipping", "Variant Taxable", "Variant Barcode",
    "Image Src", "Image Position", "Image Alt Text", "Gift Card",
    "SEO Title", "SEO Description", "Google Shopping / Google Product Category",
    "Google Shopping / Gender", "Google Shopping / Age Group",
    "Google Shopping / MPN", "Google Shopping / AdWords Grouping",
    "Google Shopping / AdWords Labels", "Google Shopping / Condition",
    "Google Shopping / Custom Product", "Google Shopping / Custom Label 0",
    "Google Shopping / Custom Label 1", "Google Shopping / Custom Label 2",
    "Google Shopping / Custom Label 3", "Google Shopping / Custom Label 4",
    "Variant Image", "Variant Weight Unit", "Variant Tax Code", "Cost per item", "Status"
]

rows = []
for p in catalogo["productos"]:
    handle = p["nombre"].lower().replace(" ", "-").replace("/", "").replace("ñ", "n").replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("---", "-").replace("--", "-")
    desc_html = f"<p>{p.get('descripcion', '')}</p><p><strong>Categoría:</strong> {p['categoria'].capitalize()} | <strong>Unidad:</strong> {p['unidad']}</p>"
    if p.get("sustituto_id"):
        desc_html += f"<p><em>Aviso de Stock: Producto con regla de sustitución automática por quiebre de inventario.</em></p>"
    
    tags = f"asado, {p['categoria']}, utem, parrilla"
    if p["categoria"] in ["carnico", "carbon", "sal"]:
        tags += ", combo-parrillero"
    if p["id"] == "prod_01":
        tags += ", stock-critico"

    row = {
        "Handle": handle,
        "Title": p["nombre"],
        "Body (HTML)": desc_html,
        "Vendor": p.get("marca", "Parrilleros UTEM"),
        "Type": p["categoria"].capitalize(),
        "Tags": tags,
        "Published": "true",
        "Option1 Name": "Formato",
        "Option1 Value": p["unidad"],
        "Variant SKU": p["id"],
        "Variant Grams": "1000",
        "Variant Inventory Tracker": "shopify",
        "Variant Inventory Qty": str(int(p["stock"])),
        "Variant Inventory Policy": "deny",
        "Variant Fulfillment Service": "manual",
        "Variant Price": str(p["precio"]),
        "Variant Compare At Price": str(int(p["precio"] * 1.15)) if p["categoria"] in ["carnico", "carbon"] else "",
        "Variant Requires Shipping": "true",
        "Variant Taxable": "true",
        "Variant Barcode": "",
        "Image Src": p.get("imagen_url", ""),
        "Image Position": "1",
        "Image Alt Text": p["nombre"],
        "Gift Card": "false",
        "SEO Title": f"{p['nombre']} - Parrilleros UTEM",
        "SEO Description": p.get("descripcion", ""),
        "Google Shopping / Google Product Category": "",
        "Google Shopping / Gender": "",
        "Google Shopping / Age Group": "",
        "Google Shopping / MPN": "",
        "Google Shopping / AdWords Grouping": "",
        "Google Shopping / AdWords Labels": "",
        "Google Shopping / Condition": "new",
        "Google Shopping / Custom Product": "false",
        "Google Shopping / Custom Label 0": "",
        "Google Shopping / Custom Label 1": "",
        "Google Shopping / Custom Label 2": "",
        "Google Shopping / Custom Label 3": "",
        "Google Shopping / Custom Label 4": "",
        "Variant Image": "",
        "Variant Weight Unit": "kg" if p["unidad"] == "kg" else "g",
        "Variant Tax Code": "",
        "Cost per item": str(int(p["precio"] * 0.7)),
        "Status": "active"
    }
    rows.append(row)

with open(csv_path, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows)

print(f"Shopify CSV generado exitosamente en: {csv_path} ({len(rows)} productos)")
