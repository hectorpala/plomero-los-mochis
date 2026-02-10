#!/usr/bin/env python3
"""
Actualiza lastmod de las 29 colonias que recibieron LocalBusiness schema.
"""

import re
from datetime import datetime

# Colonias modificadas (todas excepto centenario que ya tenía LocalBusiness)
colonias_modificadas = [
    "las-fuentes", "centro", "insurgentes", "guadalupe", "jiquilpan",
    "isla-del-oeste", "country-las-fuentes", "hacienda-los-huertos",
    "real-del-valle", "zona-dorada", "campestre", "santa-fe",
    "las-palmas", "nuevo-los-mochis", "infonavit-humaya", "bachigualato",
    "lomas-del-boulevard", "villa-universidad", "colinas-de-san-miguel",
    "altamira", "cumbres-las-fuentes", "bosques-del-humaya",
    "hacienda-del-valle", "portales-del-rio", "colinas-de-la-rivera",
    "jardines-del-valle", "lomas-de-san-isidro", "real-san-angel",
    "villa-bonita"
]

# Fecha actual para lastmod
new_lastmod = datetime.now().strftime("%Y-%m-%dT%H:%M:00+00:00")

sitemap_file = "sitemaps/main_sitemap.xml"

# Leer sitemap
with open(sitemap_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Actualizar lastmod para cada colonia
for colonia_slug in colonias_modificadas:
    url = f"https://plomerolosmochispro.mx/servicios/plomero-colonias-los-mochis/{colonia_slug}/"
    
    # Patrón para encontrar el bloque <url> completo de esta colonia
    pattern = f'(<loc>{re.escape(url)}</loc>\\s*<lastmod>)([^<]+)(</lastmod>)'
    
    # Reemplazar lastmod
    content = re.sub(pattern, f'\\1{new_lastmod}\\3', content)

print(f"✅ Sitemap actualizado: {len(colonias_modificadas)} colonias")
print(f"   Nueva fecha lastmod: {new_lastmod}")

# Escribir sitemap
with open(sitemap_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n📍 Colonias actualizadas:")
for colonia in colonias_modificadas[:10]:
    print(f"   • {colonia}")
print(f"   ... y {len(colonias_modificadas) - 10} más")
