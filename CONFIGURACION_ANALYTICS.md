# Configuración de Analytics para Medir Impacto

## 📊 Eventos Implementados

El sitio ahora envía automáticamente eventos a Google Analytics via DataLayer para medir el impacto de las optimizaciones.

---

## 🎯 Eventos Configurados

### 1. **Clics en Tarjetas SEO** (`click_seo_card`)

**Qué mide:** Cada clic en las tarjetas de "Más opciones de plomería"

**Parámetros enviados:**
```javascript
{
  'event': 'click_seo_card',
  'card_name': 'plomero_cerca_de_mi',    // Nombre de la tarjeta
  'card_position': '1',                    // Posición en el grid (1-5)
  'card_url': './servicios/...',          // URL destino
  'page_location': '/index.html'           // Página origen
}
```

**Tarjetas trackeadas:**
1. `plomero_cerca_de_mi` (Posición 1)
2. `plomero_24_7` (Posición 2)
3. `plomero_a_domicilio` (Posición 3)
4. `plomero_precios` (Posición 4)
5. `plomero_colonias` (Posición 5)

---

### 2. **Profundidad de Scroll** (`scroll_depth`)

**Qué mide:** Engagement del usuario con el contenido

**Triggers:**
- 25% de scroll
- 50% de scroll
- 75% de scroll
- 90% de scroll

**Parámetros enviados:**
```javascript
{
  'event': 'scroll_depth',
  'scroll_percentage': 50,          // Porcentaje alcanzado
  'page_location': '/index.html'    // Página actual
}
```

---

## 🔧 Configuración en Google Tag Manager

### Paso 1: Crear Variables Personalizadas

1. Ve a **Variables** → **Nueva**
2. Crea las siguientes variables de capa de datos:

| Variable | Nombre de Variable | Tipo |
|----------|-------------------|------|
| `card_name` | DL - Card Name | Variable de capa de datos |
| `card_position` | DL - Card Position | Variable de capa de datos |
| `card_url` | DL - Card URL | Variable de capa de datos |
| `scroll_percentage` | DL - Scroll Percentage | Variable de capa de datos |

---

### Paso 2: Crear Activadores (Triggers)

#### Activador: Clic en Tarjeta SEO
- **Nombre:** Click - SEO Card
- **Tipo:** Evento personalizado
- **Nombre del evento:** `click_seo_card`

#### Activador: Scroll Depth
- **Nombre:** Scroll Depth Milestone
- **Tipo:** Evento personalizado
- **Nombre del evento:** `scroll_depth`

---

### Paso 3: Crear Etiquetas de Google Analytics 4

#### Etiqueta 1: Evento Click SEO Card

**Configuración:**
- **Tipo de etiqueta:** Google Analytics: Evento GA4
- **ID de medición:** Tu GA4 Measurement ID
- **Nombre del evento:** `click_seo_card`
- **Parámetros del evento:**
  - `card_name`: `{{DL - Card Name}}`
  - `card_position`: `{{DL - Card Position}}`
  - `card_url`: `{{DL - Card URL}}`
- **Activación:** Click - SEO Card

#### Etiqueta 2: Evento Scroll Depth

**Configuración:**
- **Tipo de etiqueta:** Google Analytics: Evento GA4
- **ID de medición:** Tu GA4 Measurement ID
- **Nombre del evento:** `scroll_depth`
- **Parámetros del evento:**
  - `scroll_percentage`: `{{DL - Scroll Percentage}}`
- **Activación:** Scroll Depth Milestone

---

## 📈 Reportes Sugeridos en Google Analytics 4

### 1. **Análisis de Tarjetas SEO más Clickeadas**

**Exploración personalizada:**
```
Dimensiones:
- card_name
- card_position

Métricas:
- Recuento de eventos (click_seo_card)
- Usuarios únicos

Segmento:
- Página = "/" (homepage)
```

**Qué mide:**
- ¿Qué tarjeta atrae más clics?
- ¿La posición afecta el CTR?
- ¿Qué servicio genera más interés?

---

### 2. **Embudo de Conversión**

**Configurar en Análisis > Exploración de rutas:**
```
Paso 1: Visualización homepage (/)
Paso 2: Evento click_seo_card
Paso 3: Visualización de página (/servicios/...)
Paso 4: Evento de contacto (WhatsApp/teléfono)
```

**Qué mide:**
- Tasa de conversión de homepage → landing → contacto
- Dónde abandonan los usuarios
- Tiempo promedio por paso

---

### 3. **Engagement por Profundidad de Scroll**

**Exploración personalizada:**
```
Dimensiones:
- scroll_percentage
- Página

Métricas:
- Recuento de eventos
- Usuarios únicos
```

**Qué mide:**
- ¿Cuántos usuarios llegan al 90% del contenido?
- ¿La sección "Más opciones" se visualiza?
- Engagement general del homepage

---

## 🎯 KPIs a Monitorear (Primeras 2-4 Semanas)

### Antes vs Después de las Tarjetas Clickeables

| Métrica | Baseline | Objetivo | Dónde Verlo |
|---------|----------|----------|-------------|
| CTR Homepage → Landings | ? | +20% | GA4 > Exploración |
| Tiempo promedio en homepage | ? | +15% | GA4 > Páginas y pantallas |
| Profundidad de scroll (90%) | ? | +25% | Evento scroll_depth |
| Clics en tarjetas SEO | 0 | >100/semana | Evento click_seo_card |
| Tasa de rebote | ? | -10% | GA4 > Páginas y pantallas |

---

## 📊 Google Search Console

### Métricas a Revisar Semanalmente

1. **CTR de Búsqueda Orgánica**
   - Ruta: `Rendimiento > Páginas`
   - Filtrar por: `/index.html` (homepage)
   - Comparar: últimos 7 días vs 7 días anteriores

2. **Impresiones de Keywords Locales**
   - Keywords: "plomero en Los Mochis", "plomero cerca de mí", "plomería 24/7"
   - Ver tendencia semanal

3. **Posición Promedio**
   - Objetivo: mejorar posiciones para keywords long-tail
   - Ejemplo: "plomero en Centenario Los Mochis"

---

## 🔍 Análisis Recomendado (Semana 1-4)

### Semana 1-2: Baseline
- Recopilar datos sin cambios
- Establecer métricas de referencia
- Documentar CTR actual

### Semana 3-4: Post-Optimización
- Comparar con baseline
- Identificar tarjeta más popular
- Ajustar copy si es necesario

### Análisis Mensual
```
1. ¿Qué tarjeta tiene mayor CTR?
   → Priorizar ese tipo de contenido

2. ¿Usuarios llegan a scroll 90%?
   → Si no, acortar homepage

3. ¿Tiempo en página aumentó?
   → Contenido está funcionando

4. ¿Cuál es el embudo más exitoso?
   → Homepage → ¿Qué tarjeta? → Contacto
```

---

## 🚨 Alertas Configurables en GA4

**Crear alertas personalizadas:**

1. **Alerta: Caída en Clics de Tarjetas**
   - Si `click_seo_card` < 10/día
   - Notificar por email

2. **Alerta: Tasa de Rebote Alta**
   - Si tasa de rebote > 70%
   - Revisar contenido o velocidad

3. **Alerta: Scroll Depth Bajo**
   - Si scroll 50% < 30% de usuarios
   - Optimizar contenido above-the-fold

---

## 📝 Checklist de Implementación

- [x] Eventos implementados en código
- [ ] Variables creadas en GTM
- [ ] Activadores configurados en GTM
- [ ] Etiquetas GA4 creadas
- [ ] Modo Preview GTM verificado
- [ ] Eventos publicados en producción
- [ ] Dashboard GA4 configurado
- [ ] Baseline documentado (primera semana)
- [ ] Revisión semanal agendada
- [ ] Search Console conectado

---

## 🔗 Recursos Útiles

- **GTM Container ID:** `GTM-5PR5CHM7`
- **Dominio:** `plomerolosmochispro.mx`
- **Documentación GA4:** https://support.google.com/analytics/answer/9216061

---

## 📞 Próximos Pasos

1. **Inmediato:** Publicar cambios con eventos de tracking
2. **Hoy:** Configurar GTM según esta guía
3. **Esta semana:** Documentar baseline
4. **Próximas 4 semanas:** Monitorear KPIs semanalmente
5. **Mes 2:** Analizar resultados y optimizar

---

**Última actualización:** 2025-01-17
**Versión:** 1.0
