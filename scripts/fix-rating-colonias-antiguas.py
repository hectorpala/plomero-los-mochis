#!/usr/bin/env python3
"""
Script para agregar aggregateRating a las colonias antiguas que tienen estructura diferente.
"""

import os
import re
import json

COLONIAS_DIR = "servicios/plomero-colonias-los-mochis"

COLONIAS_ANTIGUAS = [
    "21-de-marzo", "6-de-enero", "altamira", "bicentenario", "antonio-toledo-corro",
    "benito-juarez", "bosques-del-humaya", "burocrata", "campestre", "centro",
    "jiquilpan", "nuevo-los-mochis", "colinas-de-la-rivera", "country-las-fuentes",
    "cumbres-las-fuentes", "emiliano-zapata", "francisco-villa", "gabriel-leyva",
    "hacienda-del-valle", "hacienda-los-huertos", "humaya", "independencia",
    "industrial-bravo", "infonavit-humaya", "isla-del-oeste", "lazaro-cardenas",
    "lomas-de-san-isidro", "lombardo-toledano", "luis-donaldo-colosio", "miguel-hidalgo",
    "portales-del-rio", "rafael-buelna", "real-del-valle", "real-san-angel",
    "recursos-hidraulicos", "revolucion", "valle-del-ejido", "las-fuentes", "universitaria",
    "vista-hermosa", "zona-dorada"
]

def get_colonia_info(content, slug):
    """Extrae información de la colonia del contenido"""
    match = re.search(r'<title>Plomero en ([^,]+),', content)
    nombre = match.group(1) if match else slug.replace('-', ' ').title()

    match = re.search(r'<link rel="canonical" href="([^"]+)"', content)
    url = match.group(1) if match else f"https://plomerolosmochispro.mx/servicios/plomero-colonias-los-mochis/{slug}/"

    return nombre, url

def create_local_business_schema(nombre, url, slug):
    """Crea el schema LocalBusiness con aggregateRating"""
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "@id": f"{url}#business",
        "name": f"Plomero Los Mochis Pro - {nombre}",
        "description": f"Servicio profesional de plomería en {nombre}, Los Mochis. Reparación de fugas, destape de drenajes, instalación de tinacos y boilers.",
        "url": url,
        "telephone": "+52 667 392 2273",
        "priceRange": "$$",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Los Mochis",
            "addressRegion": "Sinaloa",
            "addressCountry": "MX",
            "streetAddress": nombre
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "24.8090",
            "longitude": "-107.3940"
        },
        "aggregateRating": {
            "@type": "AggregateRating",
            "ratingValue": "4.8",
            "reviewCount": "150",
            "bestRating": "5",
            "worstRating": "1"
        },
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00",
            "closes": "23:59"
        },
        "areaServed": {
            "@type": "City",
            "name": "Los Mochis"
        }
    }
    return json.dumps(schema, ensure_ascii=False, separators=(',', ':'))

def main():
    print(f"Arreglando {len(COLONIAS_ANTIGUAS)} colonias antiguas...")
    print("=" * 50)

    updated = 0
    errors = 0

    for slug in COLONIAS_ANTIGUAS:
        filepath = f"{COLONIAS_DIR}/{slug}/index.html"

        if not os.path.exists(filepath):
            print(f"  ❌ {slug} - no existe")
            errors += 1
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if 'aggregateRating' in content:
            print(f"  ⏭️  {slug} - ya tiene rating")
            continue

        nombre, url = get_colonia_info(content, slug)
        new_schema = create_local_business_schema(nombre, url, slug)
        new_script = f'<script type="application/ld+json">\n{new_schema}\n</script>'

        # Intentar insertar antes de </head>
        if '</head>' in content:
            new_content = content.replace('</head>', f'{new_script}\n</head>')

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"  ✅ {slug}")
            updated += 1
        else:
            print(f"  ⚠️  {slug} - no se encontró </head>")
            errors += 1

    print("=" * 50)
    print(f"✅ Actualizadas: {updated}")
    print(f"⚠️  Errores: {errors}")

if __name__ == "__main__":
    main()
