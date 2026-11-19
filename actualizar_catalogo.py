import json
import os

REPO_DIR = '/home/frog/.gemini/antigravity/scratch/proyecto_lenguajes'

productos_20 = [
    {
        "id": "prod_01",
        "nombre": "Lomo Vetado Vacuno",
        "marca": "Carnes Selección UTEM",
        "categoria": "carnico",
        "precio": 14990,
        "unidad": "kg",
        "stock": 3.0,
        "sustituto_id": "prod_02",
        "descripcion": "Corte parrillero premium por excelencia con veteado de grasa infiltrada que garantiza terneza y máxima jugosidad a las brasas.",
        "imagen_url": "https://images.unsplash.com/photo-1558030006-450675393462?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_02",
        "nombre": "Sobrecostilla Vacuno",
        "marca": "Tradición Ganadera",
        "categoria": "carnico",
        "precio": 9990,
        "unidad": "kg",
        "stock": 15.0,
        "sustituto_id": None,
        "descripcion": "Corte vacuno versátil de gran sabor parrillero. Sustituto oficial de alto rendimiento ante quiebre de stock de cortes premium.",
        "imagen_url": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_03",
        "nombre": "Chorizo Parrillero Artesanal",
        "marca": "Embutidos Don Juan",
        "categoria": "carnico",
        "precio": 4990,
        "unidad": "pack",
        "stock": 20.0,
        "sustituto_id": None,
        "descripcion": "Pack de 5 chorizos artesanales aliñados al estilo campestre chileno. Indispensable para los clásicos choripanes con pebre.",
        "imagen_url": "https://images.unsplash.com/photo-1597393353415-b3730f3719fe?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_04",
        "nombre": "Hamburguesa de Lentejas / Garbanzos",
        "marca": "GreenParrilla Veggie",
        "categoria": "vegetariano",
        "precio": 3990,
        "unidad": "pack",
        "stock": 10.0,
        "sustituto_id": None,
        "descripcion": "Pack de 4 hamburguesas 100% vegetales ricas en proteína. Textura firme y especiado suave ideal para cocinar a la plancha o rejilla.",
        "imagen_url": "https://images.unsplash.com/photo-1520072959219-c595dc870360?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_05",
        "nombre": "Pimiento Morrón Rojo",
        "marca": "Huerto del Maipo",
        "categoria": "vegetariano",
        "precio": 1200,
        "unidad": "unidad",
        "stock": 30.0,
        "sustituto_id": None,
        "descripcion": "Pimiento fresco de pulpa gruesa y dulce. Perfecto para asar al rescoldo relleno con huevo o queso provolone.",
        "imagen_url": "https://images.unsplash.com/photo-1563565375-f3fdfdbefa83?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_06",
        "nombre": "Carbón Vegetal Espino 2.5kg",
        "marca": "Fuego Noble",
        "categoria": "carbon",
        "precio": 3500,
        "unidad": "bolsa",
        "stock": 12.0,
        "sustituto_id": None,
        "descripcion": "Bolsa de 2.5 kg de carbón vegetal seleccionado. Brasa constante, encendido parejo y duración prolongada para asados familiares.",
        "imagen_url": "https://images.unsplash.com/photo-1527661591475-527312dd65f5?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_07",
        "nombre": "Sal Parrillera Gruesa 1kg",
        "marca": "Salinas de Cáhuil",
        "categoria": "sal",
        "precio": 1500,
        "unidad": "bolsa",
        "stock": 25.0,
        "sustituto_id": None,
        "descripcion": "Sal marina gruesa de grano uniforme extraída artesanalmente. Realza los jugos naturales de la carne sin sobre-salar.",
        "imagen_url": "https://images.unsplash.com/photo-1518110903495-cd99c129f45f?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_08",
        "nombre": "Bebida Gaseosa 2.5L",
        "marca": "Embonor Clásica",
        "categoria": "bebida",
        "precio": 2500,
        "unidad": "botella",
        "stock": 18.0,
        "sustituto_id": None,
        "descripcion": "Botella familiar de 2.5 litros retornable de refresco gaseoso. Máximo rendimiento para compartir con todos los comensales.",
        "imagen_url": "https://images.unsplash.com/photo-1622483767028-3f66f32aef97?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_09",
        "nombre": "Entraña Vacuno Nacional",
        "marca": "Carnes Ñuble",
        "categoria": "carnico",
        "precio": 18990,
        "unidad": "kg",
        "stock": 8.0,
        "sustituto_id": "prod_02",
        "descripcion": "Corte de cocción rápida y sabor supremo. Se cocina a fuego vivo con piel crocante o limpia a gusto del parrillero.",
        "imagen_url": "https://images.unsplash.com/photo-1603048588665-791ca8aea617?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_10",
        "nombre": "Punta Picana Vacuno",
        "marca": "Pampa Mía",
        "categoria": "carnico",
        "precio": 12990,
        "unidad": "kg",
        "stock": 10.0,
        "sustituto_id": "prod_02",
        "descripcion": "Corte triangular con capa de grasa exterior que protege la carne y concentra los aromas durante asados prolongados.",
        "imagen_url": "https://images.unsplash.com/photo-1546964124-0cce460f38ef?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_11",
        "nombre": "Longaniza Tradicional de Chillán",
        "marca": "Don Teo Artesanal",
        "categoria": "carnico",
        "precio": 5490,
        "unidad": "pack",
        "stock": 15.0,
        "sustituto_id": "prod_03",
        "descripcion": "Pack de 5 longanizas ahumadas con madera nativa y aliño criollo con orégano y comino característico del Valle de Ñuble.",
        "imagen_url": "https://images.unsplash.com/photo-1585325701165-351af916e581?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_12",
        "nombre": "Prietas Artesanales con Nuez",
        "marca": "Tradición Sureña",
        "categoria": "carnico",
        "precio": 4290,
        "unidad": "pack",
        "stock": 12.0,
        "sustituto_id": None,
        "descripcion": "Pack de 4 unidades aliñadas al punto con cebolla sofrita y nueces del Valle de Aconcagua. Textura cremosa inigualable.",
        "imagen_url": "https://images.unsplash.com/photo-1599921841143-819065a55cc6?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_13",
        "nombre": "Queso Provolone Hilado para Parrilla",
        "marca": "Santa Rosa",
        "categoria": "vegetariano",
        "precio": 3990,
        "unidad": "unidad",
        "stock": 20.0,
        "sustituto_id": None,
        "descripcion": "Rodaja de 200g de provolone seleccionado. Se dora directamente sobre la parrilla hasta formar una costra dorada crocante.",
        "imagen_url": "https://images.unsplash.com/photo-1452195100486-9cc805987862?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_14",
        "nombre": "Champiñones Portobello Gigantes",
        "marca": "Fungi Del Valle",
        "categoria": "vegetariano",
        "precio": 2490,
        "unidad": "bandeja",
        "stock": 18.0,
        "sustituto_id": "prod_05",
        "descripcion": "Bandeja de 300g con 4 unidades grandes. Ideales para rellenar con queso azul, espinaca o mantequilla de hierbas.",
        "imagen_url": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_15",
        "nombre": "Choclos Dulces Selección",
        "marca": "AgroFresco Central",
        "categoria": "vegetariano",
        "precio": 1990,
        "unidad": "malla",
        "stock": 25.0,
        "sustituto_id": None,
        "descripcion": "Malla de 3 unidades tiernas y dulces. Aptos para asar enteros en su chala o pincelados con mantequilla con sal.",
        "imagen_url": "https://images.unsplash.com/photo-1551754655-cd27e38d2076?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_16",
        "nombre": "Carbón Quebracho Blanco 4kg",
        "marca": "Fuego Sureño Premium",
        "categoria": "carbon",
        "precio": 5990,
        "unidad": "bolsa",
        "stock": 15.0,
        "sustituto_id": "prod_06",
        "descripcion": "Carbón denso de quebracho blanco de altísimo poder calórico. Genera brasas incandescentes de más de 3 horas de duración.",
        "imagen_url": "https://images.unsplash.com/photo-1542838132-92c53300491e?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_17",
        "nombre": "Iniciador de Fuego Ecológico 24u",
        "marca": "PyroEco Chile",
        "categoria": "carbon",
        "precio": 1990,
        "unidad": "caja",
        "stock": 30.0,
        "sustituto_id": None,
        "descripcion": "Bloques ecológicos de viruta y cera vegetal prensada. Encienden sin humo negro ni olores que alteren el sabor de los alimentos.",
        "imagen_url": "https://images.unsplash.com/photo-1508873696983-2df5293cb32f?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_18",
        "nombre": "Chimichurri Parrillero Artesanal 250ml",
        "marca": "El Quincho Gourmet",
        "categoria": "abarrote",
        "precio": 2990,
        "unidad": "frasco",
        "stock": 22.0,
        "sustituto_id": None,
        "descripcion": "Receta clásica macerada en aceite de oliva con ajo chilote, ají cacho de cabra, perejil y vinagre de manzana.",
        "imagen_url": "https://images.unsplash.com/photo-1472476443507-c7a5948772fc?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_19",
        "nombre": "Jugo Natural Naranja Plátano 1.5L",
        "marca": "Guallarauco",
        "categoria": "bebida",
        "precio": 2990,
        "unidad": "botella",
        "stock": 20.0,
        "sustituto_id": "prod_08",
        "descripcion": "Jugo 100% fruta natural prensada en frío sin azúcar añadida ni conservantes artificiales. Envase familiar de 1.5L.",
        "imagen_url": "https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": "prod_20",
        "nombre": "Agua Mineral con Gas 1.6L",
        "marca": "Vital Manantial",
        "categoria": "bebida",
        "precio": 1490,
        "unidad": "botella",
        "stock": 35.0,
        "sustituto_id": "prod_08",
        "descripcion": "Agua de vertiente cordillerana con burbuja fina y gasificación refrescante, ideal para acompañar cortes a la parrilla.",
        "imagen_url": "https://images.unsplash.com/photo-1548839140-29a749e1bc4e?auto=format&fit=crop&w=600&q=80"
    }
]

catalogo_completo = {
    "tienda": "Parrilleros UTEM - Tienda Oficial Retail",
    "moneda": "CLP",
    "productos": productos_20
}

# Guardar en data/catalogo_tienda.json y catalogo_tienda.json
rutas = [
    os.path.join(REPO_DIR, 'data/catalogo_tienda.json'),
    os.path.join(REPO_DIR, 'catalogo_tienda.json')
]

for r in rutas:
    with open(r, 'w', encoding='utf-8') as f:
        json.dump(catalogo_completo, f, indent=2, ensure_ascii=False)
    print(f"Catálogo actualizado en: {r} (20 productos)")
