# Bolsillo (bolsillo.online): sitio de conversores para AdSense

Sitio estático (HTML + CSS + JS, sin servidor ni base de datos), en español de Argentina.

## Qué incluye

| Página | Ruta | Datos |
|---|---|---|
| Inicio con resumen del dólar | `/` | DolarApi.com |
| Conversor dólar ↔ peso (oficial, blue, MEP, CCL, tarjeta, cripto) | `/dolar/` | DolarApi.com |
| Conversor cripto (BTC, ETH, USDT, USDC, SOL) ↔ ARS/USD | `/cripto/` | CoinGecko |
| Unidades (longitud, peso, volumen, superficie, velocidad, temperatura) | `/unidades/` | local |
| Porcentajes, aumentos, descuentos e IVA | `/porcentaje/` | local |
| Sobre nosotros, Contacto, Privacidad, Términos | `/sobre-nosotros/` etc. | — |

Además: `sitemap.xml`, `robots.txt`, `404.html`, favicon, metadatos SEO, datos estructurados de preguntas frecuentes, y `ads.txt` automático cuando cargues tu ID de AdSense.

Las cotizaciones se guardan 5 minutos en el navegador para no saturar las APIs. Si una API falla, se muestra el último valor conocido o un aviso.

## Paso 1: personalizar

Abrí `src/build.py` y cambiá `CONFIG`:

- `SITE_NAME`: el nombre del sitio (ya configurado: Bolsillo).
- `SITE_URL`: tu dominio, por ejemplo `https://cambioclaro.com.ar`.
- `CONTACT_EMAIL`: un correo que revises.
- `ADSENSE_CLIENT`: dejalo vacío hasta que AdSense te dé el ID `ca-pub-…`.

Después corré `python3 src/build.py` (regenera la carpeta `public/`).

## Paso 2: publicar gratis (Cloudflare Pages, recomendado)

1. Creá un repositorio en GitHub y subí esta carpeta.
2. En dash.cloudflare.com → Workers & Pages → Create → Pages → conectá el repositorio.
3. Build command: *(vacío)*. Output directory: `public`.
4. Te da una URL `*.pages.dev`. Probala.

Alternativas: Vercel o Netlify (misma idea, carpeta `public`). GitHub Pages también sirve, pero solo con dominio propio, porque las rutas empiezan con `/`.

## Paso 3: dominio propio (necesario para AdSense)

AdSense no acepta subdominios gratuitos como `*.pages.dev`. Comprá un dominio:

- `.com.ar` en NIC Argentina (nic.ar): barato, se paga en pesos, requiere clave fiscal.
- `.com` en Cloudflare Registrar o Namecheap: unos 10 a 12 USD por año.

Conectalo en Cloudflare Pages → Custom domains, y volvé a generar el sitio con ese `SITE_URL`.

## Paso 4: Google Search Console

1. search.google.com/search-console → agregá tu dominio y verificalo.
2. Enviá `https://tu-dominio/sitemap.xml`.
3. Esperá a que Google indexe las páginas (días a semanas).

## Paso 5: solicitar AdSense

Recomendado esperar a tener contenido indexado y algo de tráfico (aunque no hay un mínimo oficial).

1. adsense.google.com → registrate con tu cuenta de Google, agregá el sitio.
2. Copiá tu ID `ca-pub-…` en `ADSENSE_CLIENT`, regenerá y publicá: eso agrega el script en todas las páginas y crea `ads.txt`.
3. En AdSense, configurá el mensaje de consentimiento (Privacidad y mensajes) si vas a recibir tráfico de Europa.
4. La revisión tarda de días a unas semanas. Si te rechazan, el motivo más común es “contenido de poco valor”: sumá más páginas con texto útil y volvé a pedir.
5. Una vez aprobado, activá **Anuncios automáticos** (Auto ads) en AdSense: no hace falta tocar el código. Los `<div class="ad-slot">` marcan lugares donde podés poner bloques manuales más adelante.

Para cobrar: AdSense paga cuando llegás a 100 USD. Desde Argentina se cobra por transferencia a una cuenta bancaria en pesos o en dólares, según lo que permita tu banco; revisá la opción de pago en tu cuenta.

## Expectativas realistas

- **Aprobación**: los sitios de herramientas con poco texto a veces se rechazan. Por eso cada página trae explicación original. Ayuda sumar más contenido propio con el tiempo.
- **Tráfico**: “dólar blue hoy” es una búsqueda enorme pero dominada por medios grandes (Ámbito, La Nación, Infobae, DolarHoy). Un sitio nuevo tarda meses en posicionar, si lo logra. Las búsquedas más chicas (por ejemplo “calcular IVA 10,5”, “cuántos USDT son 50000 pesos”) son más alcanzables.
- **Ingresos**: el tráfico de Argentina paga poco por publicidad, típicamente entre 0,3 y 1,5 USD cada 1.000 visitas. Con 30.000 visitas por mes serían del orden de 10 a 45 USD por mes. Llegar a 100 USD mensuales suele requerir cientos de miles de visitas.
- **Lo que más ayuda**: muchas páginas específicas (una por conversión popular), compartir el sitio en redes y grupos, y paciencia.

## Ideas para crecer

- Páginas dedicadas: “100 dólares a pesos”, “dólar MEP hoy”, “USDT a pesos”, “calculadora de plazo fijo”, “calculadora de inflación”, “conversor euro a peso”, “real a peso”.
- Histórico de cotizaciones con gráfico.
- Calculadora de sueldo neto o de aguinaldo.
