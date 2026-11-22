#!/usr/bin/env python3
"""Genera el sitio estático en ../public a partir de las páginas definidas acá.

Uso:  python3 src/build.py
Editá CONFIG antes de publicar.
"""
import datetime
import hashlib
import html
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from guias import GUIAS  # noqa: E402

CONFIG = {
    "SITE_NAME": "Bolsillo",
    "SITE_URL": "https://bolsillo.online",       # sin barra final
    "CONTACT_EMAIL": "contacto@bolsillo.online",  # un correo que leas de verdad
    "ADSENSE_CLIENT": "ca-pub-1697004556284286",                        # ej. "ca-pub-1234567890123456" (vacío = sin anuncios)
    "UPDATED": datetime.date.today().isoformat(),
}

OUT = pathlib.Path(__file__).resolve().parent.parent / "public"
# Versión del CSS para que los navegadores no usen una copia vieja después de cada cambio
CSS_VERSION = hashlib.sha1((OUT / "assets" / "style.css").read_bytes()).hexdigest()[:8]
JS_VERSION = hashlib.sha1((OUT / "assets" / "app.js").read_bytes()).hexdigest()[:8]

# Menú: en PC se ven las principales y el resto va en "Más"; en celular todo entra en el botón "Menú"
NAV = [
    ("/dolar/", "Dólar"),
    ("/cripto/", "Cripto"),
    ("/plazo-fijo/", "Plazo fijo"),
    ("/guias/", "Guías"),
]
NAV_MAS = [
    ("/monedas/", "Euro y real"),
    ("/aguinaldo/", "Aguinaldo"),
    ("/unidades/", "Unidades"),
    ("/porcentaje/", "% e IVA"),
]
MENU_JS = """<script>(()=>{const b=document.querySelector(".menu-btn"),m=document.getElementById("menu"),x=document.querySelector(".mas-btn"),p=document.getElementById("mas-panel");
b.addEventListener("click",()=>{const a=b.getAttribute("aria-expanded")!=="true";b.setAttribute("aria-expanded",a);m.classList.toggle("abierto",a)});
x.addEventListener("click",e=>{e.stopPropagation();const a=x.getAttribute("aria-expanded")!=="true";x.setAttribute("aria-expanded",a);p.classList.toggle("abierto",a)});
document.addEventListener("click",e=>{if(!e.target.closest(".mas")){x.setAttribute("aria-expanded","false");p.classList.remove("abierto")}});
document.addEventListener("keydown",e=>{if(e.key==="Escape"){x.setAttribute("aria-expanded","false");p.classList.remove("abierto");if(m.classList.contains("abierto")){b.click();b.focus()}}});})();</script>"""


def layout(path, title, description, body, schema=""):
    c = CONFIG
    url = c["SITE_URL"] + path
    def links(items):
        return "".join(
            f'<a href="{h}"{" aria-current=page" if h == path else ""}>{t}</a>' for h, t in items
        )

    en_mas = " actual" if any(h == path for h, _ in NAV_MAS) else ""
    nav = (
        '<button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu">'
        '<span class="menu-ico" aria-hidden="true"></span>Menú</button>'
        f'<nav class="main" id="menu" aria-label="Herramientas">{links(NAV)}'
        f'<div class="mas"><button class="mas-btn{en_mas}" type="button" aria-expanded="false" '
        f'aria-controls="mas-panel">Más</button><div class="mas-panel" id="mas-panel">{links(NAV_MAS)}</div></div>'
        f"</nav>{MENU_JS}"
    )
    ads = ""
    if c["ADSENSE_CLIENT"]:
        ads = (
            '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js'
            f'?client={c["ADSENSE_CLIENT"]}" crossorigin="anonymous"></script>'
        )
    return f"""<!DOCTYPE html>
<html lang="es-AR" class="sin-js">
<head>
<script>document.documentElement.className="js"</script>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="es_AR">
<meta name="theme-color" content="#153c4a">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@75..125,400..800&display=swap">
<link rel="stylesheet" href="/assets/style.css?v={CSS_VERSION}">
{ads}
{schema}
</head>
<body>
<header class="site"><div class="wrap">
<a class="logo" href="/"><span>&#36;</span> {c["SITE_NAME"]}</a>
{nav}
</div></header>
<main><div class="wrap">
{body}
</div></main>
<footer class="site"><div class="wrap">
<p class="foot-links"><a href="/sobre-nosotros/">Sobre nosotros</a><a href="/contacto/">Contacto</a><a href="/privacidad/">Política de privacidad</a><a href="/terminos/">Términos de uso</a></p>
<p>© <span id="year"></span> {c["SITE_NAME"]}. Las cotizaciones son de referencia y pueden diferir de las de tu banco, casa de cambio o exchange. Nada de lo publicado constituye asesoramiento financiero.</p>
</div></footer>
<script src="/assets/app.js?v={JS_VERSION}" defer></script>
</body>
</html>
"""


def faq_schema(items):
    import json
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ],
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def faq_html(items):
    return '<h2>Preguntas frecuentes</h2><div class="faq">' + "".join(
        f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items
    ) + "</div>"


PAGES = {}

# ---------------------------------------------------------------- Inicio
PAGES["/"] = (
    "Conversor de dólar, cripto y unidades | " + CONFIG["SITE_NAME"],
    "Convertí dólares a pesos con la cotización oficial, blue, MEP y tarjeta, calculá el valor de Bitcoin y USDT en pesos, y convertí unidades y porcentajes al instante.",
    """
<section class="hero">
<div class="hero-txt">
<h1>Conversores rápidos y gratuitos</h1>
<p class="lead">Cotización del dólar en Argentina, precios de criptomonedas en pesos y dólares, unidades de medida y porcentajes. Sin registrarte y desde el celular.</p>
</div>
<div class="pizarra">
<h2 class="pizarra-tit">Dólar hoy, precio de venta</h2>
<div class="grid" id="dolar-summary"><p class="status">Cargando cotizaciones…</p></div>
<a class="pizarra-link" href="/dolar/">Convertir y ver todas las cotizaciones</a>
</div>
</section>
<h2>Herramientas</h2>
<div class="grid tools">
<a class="tile" href="/dolar/"><strong>Dólar a peso argentino</strong><small>Oficial, blue, MEP, CCL, tarjeta y cripto.</small></a>
<a class="tile" href="/monedas/"><strong>Euro, real y más</strong><small>EUR, BRL, CLP y UYU a pesos argentinos.</small></a>
<a class="tile" href="/plazo-fijo/"><strong>Plazo fijo</strong><small>Intereses, TEM y TEA según la TNA de tu banco.</small></a>
<a class="tile" href="/aguinaldo/"><strong>Aguinaldo</strong><small>SAC completo o proporcional, bruto y neto.</small></a>
<a class="tile" href="/cripto/"><strong>Criptomonedas</strong><small>BTC, ETH, USDT, USDC y SOL a pesos o dólares.</small></a>
<a class="tile" href="/guias/"><strong>Guías</strong><small>Dólar MEP, plazo fijo, aguinaldo, IVA y más, explicado simple.</small></a>
<a class="tile" href="/unidades/"><strong>Unidades de medida</strong><small>Longitud, peso, volumen, superficie, velocidad y temperatura.</small></a>
<a class="tile" href="/porcentaje/"><strong>Porcentajes e IVA</strong><small>Aumentos, descuentos, variaciones y cálculo de IVA.</small></a>
</div>
<h2>Por qué hay tantos “dólares” en Argentina</h2>
<p>En Argentina conviven varios tipos de cambio al mismo tiempo. El <strong>dólar oficial</strong> es el que publican los bancos y se usa como referencia para muchas operaciones reguladas. El <strong>dólar blue</strong> es el precio informal que se pacta fuera del sistema bancario. El <strong>dólar MEP</strong> (o dólar bolsa) surge de comprar un bono en pesos y venderlo en dólares dentro del mercado de capitales, y el <strong>contado con liquidación (CCL)</strong> es una operación parecida pero con los dólares acreditados en una cuenta del exterior. A eso se suma el <strong>dólar tarjeta</strong>, que es el oficial más los impuestos y percepciones que se aplican a los consumos en moneda extranjera.</p>
<p>Como cada uno tiene un precio distinto, “¿cuántos pesos son 100 dólares?” no tiene una única respuesta. Nuestro conversor te deja elegir el tipo de cambio que corresponde a tu caso y te muestra el cálculo, para que sepas exactamente de dónde sale el número.</p>
<h2>Cómo usamos los datos</h2>
<p>Las cotizaciones se obtienen de fuentes públicas (DolarApi.com para el dólar y CoinGecko para criptomonedas) y se actualizan cada pocos minutos. Son valores de referencia: el precio final que te ofrezca un banco, una casa de cambio o un exchange puede ser distinto por comisiones, horarios o impuestos. Las herramientas de unidades y porcentajes funcionan sin conexión a ningún servicio externo.</p>
""",
)

# ---------------------------------------------------------------- Dólar
DOLAR_FAQ = [
    ("¿Qué precio se usa al convertir dólares a pesos?",
     "Si tenés dólares y querés pesos, usamos el precio de compra, que es lo que te pagan por cada dólar. Si tenés pesos y querés dólares, usamos el precio de venta, que es lo que te cobran."),
    ("¿Cada cuánto se actualiza la cotización?",
     "Los datos se consultan cada pocos minutos. Debajo del conversor vas a ver la hora de la última actualización informada por la fuente."),
    ("¿Por qué el dólar tarjeta no tiene precio de compra?",
     "Porque es un tipo de cambio que solo se aplica a pagos con tarjeta en moneda extranjera: nadie te compra dólares a ese valor."),
    ("¿El dólar blue es legal?",
     "El mercado blue es informal y opera por fuera del sistema financiero regulado. Lo mostramos como referencia de precio, no como recomendación para operar en él."),
]
PAGES["/dolar/"] = (
    "Dólar hoy en Argentina: conversor de dólar blue, oficial y MEP a pesos",
    "Convertí dólares a pesos y pesos a dólares con la cotización de hoy: oficial, blue, MEP, contado con liquidación, tarjeta y cripto. Actualizado cada pocos minutos.",
    """
<h1>Conversor de dólar a peso argentino</h1>
<p class="lead">Elegí el tipo de cambio, escribí el monto y obtené el resultado al instante con la cotización de hoy.</p>
<div class="card conv-main">
<form class="conv" id="dolar-form">
<div><label for="d-amount">Monto</label><input id="d-amount" inputmode="decimal" value="100"></div>
<div><label for="d-dir">Quiero convertir</label><select id="d-dir"><option value="usd-ars">Dólares → Pesos</option><option value="ars-usd">Pesos → Dólares</option></select></div>
<div class="full"><label for="d-casa">Tipo de cambio</label><select id="d-casa"><option>Cargando…</option></select></div>
<div class="full result" id="d-result" aria-live="polite">—</div>
</form>
<p class="status" id="dolar-status"></p>
</div>
<h2>Cotizaciones de hoy</h2>
<p class="status" id="dolar-upd">Cargando cotizaciones…</p>
<div class="cot-grid" id="dolar-cards" aria-live="polite"></div>
<div class="ad-slot"></div>
<h2>Comparación con el dólar oficial</h2>
<p>La brecha indica cuánto más caro está cada dólar respecto del oficial, comparando los precios de venta.</p>
<div class="card"><table id="dolar-table"><thead><tr><th>Tipo</th><th class="num">Compra</th><th class="num">Venta</th><th class="num">Brecha</th></tr></thead><tbody><tr><td colspan="4">Cargando…</td></tr></tbody></table></div>
<h2>Evolución del dólar</h2>
<section class="card hist" id="hist" aria-labelledby="h-tit">
<div class="hist-ctrl">
<div><label for="h-casa">Tipo de cambio</label><select id="h-casa"><option value="oficial">Dólar Oficial</option><option value="blue" selected>Dólar Blue</option><option value="bolsa">Dólar MEP (Bolsa)</option><option value="contadoconliqui">Dólar CCL</option><option value="tarjeta">Dólar Tarjeta</option><option value="cripto">Dólar Cripto</option><option value="mayorista">Dólar Mayorista</option></select></div>
<div class="seg" role="group" aria-label="Período"><button type="button" data-d="30" aria-pressed="false">1 mes</button><button type="button" data-d="90" aria-pressed="true">3 meses</button><button type="button" data-d="180" aria-pressed="false">6 meses</button><button type="button" data-d="365" aria-pressed="false">1 año</button></div>
</div>
<p class="hist-tit" id="h-tit">Precio de venta</p>
<p class="hist-dato" id="h-dato"></p>
<div class="hist-chart" id="h-chart"></div>
<p class="status" id="h-status">Cargando historial…</p>
<details class="hist-tabla"><summary>Ver los datos en una tabla</summary><div id="h-tabla"></div></details>
</section>
<h2>Cómo se calcula la conversión</h2>
<p>La cuenta es simple, pero conviene saber qué precio usar. Cada tipo de cambio tiene dos valores: el de <strong>compra</strong> (lo que te pagan si vendés dólares) y el de <strong>venta</strong> (lo que pagás si comprás dólares). La diferencia entre ambos se llama <em>spread</em> y es la ganancia de quien hace la operación.</p>
<ul>
<li><strong>De dólares a pesos:</strong> monto en dólares × precio de compra. Por ejemplo, si el blue compra a $1.000, 100 dólares equivalen a $100.000.</li>
<li><strong>De pesos a dólares:</strong> monto en pesos ÷ precio de venta. Si el blue vende a $1.020, con $100.000 obtenés unos 98 dólares.</li>
</ul>
<h2>Qué tipo de cambio te conviene mirar</h2>
<h3>Dólar oficial</h3>
<p>Es el precio que publican los bancos para la compra y venta de divisas por canales formales. Se usa como base para el dólar tarjeta y como referencia para precios regulados, contratos y declaraciones.</p>
<h3>Dólar blue</h3>
<p>Es la cotización del mercado informal. Suele usarse como termómetro de las expectativas, y muchas personas lo toman como referencia para alquileres, autos usados o ahorro en efectivo.</p>
<h3>Dólar MEP o bolsa</h3>
<p>Se obtiene comprando un bono con pesos y vendiéndolo en dólares a través de un banco o una sociedad de bolsa. Es una forma legal de acceder a dólares que quedan depositados en una cuenta local.</p>
<h3>Contado con liquidación (CCL)</h3>
<p>Funciona de forma parecida al MEP, pero los dólares se acreditan en una cuenta en el exterior. Lo usan sobre todo empresas e inversores.</p>
<h3>Dólar tarjeta</h3>
<p>Es el valor que termina pagando quien consume en moneda extranjera con tarjeta (suscripciones, compras online, viajes). Se calcula como el oficial más impuestos y percepciones vigentes, que pueden cambiar según la normativa.</p>
<h3>Dólar cripto</h3>
<p>Es el precio implícito al comprar stablecoins como USDT con pesos en exchanges. Opera las 24 horas, incluso fines de semana, y por eso a veces anticipa movimientos de otras cotizaciones.</p>
""" + faq_html(DOLAR_FAQ) + """
<h2>Fuentes y metodología</h2>
<ul class="fuentes">
<li><strong>Cotizaciones del día:</strong> <a href="https://dolarapi.com" rel="nofollow noopener">DolarApi.com</a>, que reúne los precios publicados por bancos, casas de cambio y el mercado. Cada tarjeta muestra la hora que informa la fuente, y la página vuelve a consultar los datos cada 5 minutos como máximo.</li>
<li><strong>Historial:</strong> <a href="https://argentinadatos.com" rel="nofollow noopener">ArgentinaDatos</a>, con el cierre diario de cada tipo de cambio. Los fines de semana y feriados no hay datos nuevos.</li>
<li><strong>Conversión:</strong> de dólares a pesos usamos el precio de compra, y de pesos a dólares, el de venta. El dólar tarjeta solo tiene precio de venta.</li>
<li><strong>Brecha:</strong> (venta del dólar elegido ÷ venta del oficial − 1) × 100.</li>
</ul>
<p class="disclaimer">Los valores son de referencia. Verificá siempre el precio final con la entidad con la que vayas a operar.</p>
""",
    faq_schema(DOLAR_FAQ),
)

# ---------------------------------------------------------------- Cripto
CRIPTO_FAQ = [
    ("¿De dónde salen los precios?",
     "Usamos el precio promedio que publica CoinGecko, que agrega datos de cientos de exchanges. El precio de un exchange puntual puede ser un poco distinto."),
    ("¿Por qué el USDT en pesos no coincide con el dólar oficial?",
     "Porque el USDT se compra con pesos en exchanges, a un precio que se forma por oferta y demanda. Por eso suele estar más cerca del dólar MEP o blue que del oficial."),
    ("¿Puedo comprar cripto desde esta página?",
     "No. Es solo una calculadora de referencia. No vendemos ni intermediamos activos."),
]
PAGES["/cripto/"] = (
    "Conversor de Bitcoin, USDT y Ethereum a pesos argentinos y dólares",
    "Calculá cuántos pesos o dólares son tus Bitcoin, Ethereum, USDT, USDC o Solana, o cuánta cripto comprás con un monto. Precios de referencia actualizados.",
    """
<h1>Conversor de criptomonedas a pesos y dólares</h1>
<p class="lead">Calculá el valor de tus BTC, ETH, USDT, USDC o SOL en pesos argentinos o en dólares, o al revés.</p>
<div class="card">
<form class="conv" id="cripto-form">
<div><label for="c-amount">Monto</label><input id="c-amount" inputmode="decimal" value="1"></div>
<div><label for="c-dir">Quiero convertir</label><select id="c-dir"><option value="coin-fiat">Cripto → Moneda</option><option value="fiat-coin">Moneda → Cripto</option></select></div>
<div><label for="c-coin">Criptomoneda</label><select id="c-coin"><option value="bitcoin">Bitcoin (BTC)</option><option value="ethereum">Ethereum (ETH)</option><option value="tether">Tether (USDT)</option><option value="usd-coin">USD Coin (USDC)</option><option value="solana">Solana (SOL)</option></select></div>
<div><label for="c-fiat">Moneda</label><select id="c-fiat"><option value="ars">Pesos argentinos (ARS)</option><option value="usd">Dólares (USD)</option></select></div>
<div class="full result" id="c-result" aria-live="polite">—</div>
</form>
<p class="status" id="cripto-status"></p>
</div>
<div class="ad-slot"></div>
<h2>Precios de referencia</h2>
<div class="card"><table id="cripto-table"><thead><tr><th>Moneda</th><th class="num">USD</th><th class="num">ARS</th><th class="num">24 h</th></tr></thead><tbody><tr><td colspan="4">Cargando…</td></tr></tbody></table></div>
<h2>Cómo leer estos precios</h2>
<p>El precio de una criptomoneda cambia todo el tiempo y varía un poco entre exchanges. Lo que ves acá es un <strong>promedio de mercado</strong>: sirve para saber cuánto vale aproximadamente lo que tenés o para comparar ofertas. Al operar, el exchange te va a mostrar su propio precio de compra y de venta, y puede sumar comisiones de trading o de retiro.</p>
<h2>Stablecoins: USDT y USDC</h2>
<p>Las stablecoins son criptomonedas diseñadas para valer siempre cerca de un dólar. En Argentina se usan mucho como forma de ahorro o para cobrar del exterior, porque se pueden comprar con pesos a cualquier hora. El precio del USDT en pesos funciona, en la práctica, como otro tipo de cambio: el llamado <em>dólar cripto</em>.</p>
<h2>Bitcoin, Ethereum y Solana</h2>
<p>A diferencia de las stablecoins, estas criptomonedas tienen precios muy volátiles: pueden subir o bajar más de un 5 % en un solo día. Por eso la columna “24 h” de la tabla te muestra la variación del último día. Si estás calculando un pago o una compra, conviene revisar el precio justo antes de operar.</p>
<h2>Ejemplo práctico</h2>
<p>Supongamos que querés saber cuántos USDT comprás con $50.000. Elegí “Moneda → Cripto”, Tether (USDT) y pesos argentinos, y escribí 50000. El conversor divide el monto por el precio de referencia del USDT en pesos. Si el exchange cobra una comisión del 0,5 %, vas a recibir un poco menos.</p>
""" + faq_html(CRIPTO_FAQ) + """
<p class="disclaimer">Las criptomonedas son activos de alto riesgo. Esta herramienta es informativa y no constituye una recomendación de inversión. Datos: CoinGecko.</p>
""",
    faq_schema(CRIPTO_FAQ),
)

# ---------------------------------------------------------------- Unidades
PAGES["/unidades/"] = (
    "Conversor de unidades: metros, kilos, litros, grados y más",
    "Convertí unidades de longitud, peso, volumen, superficie, velocidad y temperatura: metros a pies, kilos a libras, Celsius a Fahrenheit, hectáreas a acres y más.",
    """
<h1>Conversor de unidades de medida</h1>
<p class="lead">Longitud, peso, volumen, superficie, velocidad y temperatura, con el resultado al instante.</p>
<div class="card">
<form class="conv" id="u-form">
<div class="full"><label for="u-cat">Tipo de medida</label><select id="u-cat">
<option value="longitud">Longitud</option><option value="peso">Peso</option><option value="volumen">Volumen</option>
<option value="superficie">Superficie</option><option value="velocidad">Velocidad</option><option value="temperatura">Temperatura</option></select></div>
<div class="full"><label for="u-amount">Valor</label><input id="u-amount" inputmode="decimal" value="1"></div>
<div><label for="u-from">De</label><select id="u-from"></select></div>
<div><label for="u-to">A</label><select id="u-to"></select></div>
<div class="full"><button type="button" id="u-swap">⇅ Invertir unidades</button></div>
<div class="full result" id="u-result" aria-live="polite">—</div>
</form>
</div>
<div class="ad-slot"></div>
<h2>Equivalencias más buscadas</h2>
<div class="card"><table>
<thead><tr><th>Conversión</th><th class="num">Equivalencia</th></tr></thead>
<tbody>
<tr><td>1 pulgada</td><td class="num">2,54 cm</td></tr>
<tr><td>1 pie</td><td class="num">30,48 cm</td></tr>
<tr><td>1 milla</td><td class="num">1,609 km</td></tr>
<tr><td>1 libra</td><td class="num">453,6 g</td></tr>
<tr><td>1 onza</td><td class="num">28,35 g</td></tr>
<tr><td>1 galón (EE.UU.)</td><td class="num">3,785 litros</td></tr>
<tr><td>1 hectárea</td><td class="num">10.000 m²</td></tr>
<tr><td>1 acre</td><td class="num">0,405 hectáreas</td></tr>
<tr><td>100 km/h</td><td class="num">62,1 mph</td></tr>
</tbody></table></div>
<h2>Cómo funciona la conversión</h2>
<p>Para longitud, peso, volumen, superficie y velocidad, cada unidad tiene un factor respecto de una unidad base del Sistema Internacional (el metro, el kilogramo, el litro, el metro cuadrado y el metro por segundo). El conversor pasa tu valor a la unidad base y de ahí a la unidad de destino. Por ejemplo, para pasar 5 pies a centímetros: 5 × 0,3048 = 1,524 metros, y 1,524 ÷ 0,01 = 152,4 cm.</p>
<h2>La temperatura es un caso especial</h2>
<p>Las escalas de temperatura no empiezan en el mismo cero, por eso no alcanza con multiplicar. Las fórmulas son:</p>
<ul>
<li><strong>Celsius a Fahrenheit:</strong> °F = °C × 9/5 + 32. Así, 25 °C son 77 °F.</li>
<li><strong>Fahrenheit a Celsius:</strong> °C = (°F − 32) × 5/9. Así, 100 °F son unos 37,8 °C.</li>
<li><strong>Celsius a Kelvin:</strong> K = °C + 273,15.</li>
</ul>
<h2>Usos frecuentes</h2>
<p>Las conversiones de pulgadas a centímetros sirven para comparar pantallas de televisores y celulares o medidas de ropa importada. Las de libras a kilos y de onzas a gramos son útiles para recetas y compras en tiendas de Estados Unidos. En el campo se usan mucho las hectáreas y, en documentos extranjeros, los acres. Y si viajás, pasar de millas a kilómetros o de Fahrenheit a Celsius te ayuda a entender carteles y pronósticos.</p>
<p class="disclaimer">La “taza” se toma como 250 ml, que es la medida habitual en recetas en español. Las tazas de recetas de EE.UU. son de unos 240 ml.</p>
""",
)

# ---------------------------------------------------------------- Porcentajes e IVA
PCT_FAQ = [
    ("¿Cómo calculo un aumento del 20 %?",
     "Multiplicá el valor por 1,20. Por ejemplo, $10.000 con un 20 % de aumento son $12.000."),
    ("¿Cómo saco el IVA de un precio final?",
     "Dividí el precio final por 1,21 para obtener el neto. La diferencia entre el final y el neto es el IVA."),
    ("¿Si algo sube 50 % y después baja 50 % vuelve al mismo precio?",
     "No. Si $100 suben 50 % pasan a $150, y si bajan 50 % quedan en $75. Los porcentajes se aplican sobre el valor del momento."),
]
PAGES["/porcentaje/"] = (
    "Calculadora de porcentajes, aumentos, descuentos e IVA",
    "Calculá el porcentaje de un número, la variación porcentual entre dos valores, aumentos y descuentos, y sumá o sacá el IVA del 21 % o 10,5 % de un precio.",
    """
<h1>Calculadora de porcentajes e IVA</h1>
<p class="lead">Cuatro calculadoras en una: porcentaje de un número, variación entre dos valores, aumentos o descuentos, e IVA.</p>
<div id="pct-tools">
<div class="card"><h2 style="margin-top:0">¿Cuánto es X % de Y?</h2>
<form class="conv" id="pct-of">
<div><label for="p1a">Porcentaje (%)</label><input id="p1a" inputmode="decimal" value="15"></div>
<div><label for="p1b">Del número</label><input id="p1b" inputmode="decimal" value="20000"></div>
<div class="full result" aria-live="polite">—</div></form></div>

<div class="card"><h2 style="margin-top:0">Variación porcentual entre dos valores</h2>
<form class="conv" id="pct-change">
<div><label for="p2a">Valor inicial</label><input id="p2a" inputmode="decimal" value="1000"></div>
<div><label for="p2b">Valor final</label><input id="p2b" inputmode="decimal" value="1250"></div>
<div class="full result" aria-live="polite">—</div></form></div>

<div class="ad-slot"></div>

<div class="card"><h2 style="margin-top:0">Aplicar un aumento o un descuento</h2>
<form class="conv" id="pct-apply">
<div><label for="p3a">Precio</label><input id="p3a" inputmode="decimal" value="50000"></div>
<div><label for="p3b">Porcentaje (%)</label><input id="p3b" inputmode="decimal" value="10"></div>
<div class="full"><label for="p3m">Operación</label><select id="p3m"><option value="sumar">Aumento (+)</option><option value="restar">Descuento (−)</option></select></div>
<div class="full result" aria-live="polite">—</div></form></div>

<div class="card"><h2 style="margin-top:0">Calculadora de IVA</h2>
<form class="conv" id="iva">
<div><label for="p4a">Monto ($)</label><input id="p4a" inputmode="decimal" value="10000"></div>
<div><label for="p4b">Alícuota (%)</label><input id="p4b" inputmode="decimal" value="21"></div>
<div class="full"><label for="p4m">El monto es</label><select id="p4m"><option value="sumar">Neto (sin IVA): sumar IVA</option><option value="restar">Final (con IVA): sacar IVA</option></select></div>
<div class="full result" aria-live="polite">—</div></form></div>
</div>
<h2>Fórmulas que usa cada calculadora</h2>
<ul>
<li><strong>Porcentaje de un número:</strong> resultado = número × porcentaje ÷ 100.</li>
<li><strong>Variación porcentual:</strong> (valor final − valor inicial) ÷ valor inicial × 100. Sirve para medir cuánto subió un precio, un sueldo o una cotización.</li>
<li><strong>Aumento:</strong> precio × (1 + porcentaje ÷ 100). <strong>Descuento:</strong> precio × (1 − porcentaje ÷ 100).</li>
<li><strong>IVA:</strong> para sumarlo, neto × (1 + alícuota ÷ 100). Para sacarlo de un precio final, final ÷ (1 + alícuota ÷ 100).</li>
</ul>
<h2>Alícuotas de IVA en Argentina</h2>
<p>La alícuota general del IVA es del <strong>21 %</strong>. Algunos bienes y servicios tienen una alícuota reducida del <strong>10,5 %</strong> (por ejemplo, ciertos alimentos y la medicina prepaga), y otros, como algunos servicios públicos para empresas, tienen una alícuota del 27 %. Podés escribir cualquier alícuota en la calculadora. Ante dudas sobre un caso puntual, consultá con tu contador o en el sitio de ARCA.</p>
<h2>Un error común con los descuentos</h2>
<p>Dos descuentos sucesivos no se suman. Un 20 % de descuento seguido de otro 10 % no es un 30 %: primero pagás el 80 % del precio y después el 90 % de eso, es decir, el 72 % del precio original, un descuento total del 28 %. Lo mismo pasa con los aumentos mensuales: tres subas del 5 % equivalen a un 15,76 % acumulado, no a un 15 %.</p>
""" + faq_html(PCT_FAQ),
    faq_schema(PCT_FAQ),
)

# ---------------------------------------------------------------- Otras monedas
MON_FAQ = [
    ("¿Qué cotización del euro se muestra?",
     "La cotización oficial de referencia que publican los bancos. En casas de cambio o en el mercado informal el precio puede ser distinto."),
    ("¿Cómo paso reales a pesos?",
     "Elegí Real brasileño, la opción “Moneda → Pesos” y escribí el monto. El conversor lo multiplica por el precio de compra del real."),
    ("¿Sirve para calcular gastos de viaje?",
     "Sirve como referencia. Si pagás con tarjeta argentina en el exterior, el cargo final se calcula con el dólar tarjeta, que incluye impuestos."),
]
PAGES["/monedas/"] = (
    "Euro, real, peso chileno y uruguayo a pesos argentinos hoy",
    "Convertí euros, reales, pesos chilenos y pesos uruguayos a pesos argentinos (y al revés) con la cotización oficial de hoy. Actualizado cada pocos minutos.",
    """
<h1>Conversor de euro, real y otras monedas a pesos</h1>
<p class="lead">Calculá cuántos pesos argentinos son tus euros, reales, pesos chilenos o uruguayos, o cuánta moneda extranjera comprás con tus pesos.</p>
<div class="card">
<form class="conv" id="m-form">
<div><label for="m-amount">Monto</label><input id="m-amount" inputmode="decimal" value="100"></div>
<div><label for="m-dir">Quiero convertir</label><select id="m-dir"><option value="x-ars">Moneda → Pesos</option><option value="ars-x">Pesos → Moneda</option></select></div>
<div class="full"><label for="m-cur">Moneda</label><select id="m-cur"><option>Cargando…</option></select></div>
<div class="full result" id="m-result" aria-live="polite">—</div>
</form>
<p class="status" id="m-status"></p>
</div>
<div class="ad-slot"></div>
<h2>Cotizaciones oficiales de hoy</h2>
<div class="card"><table id="m-table"><thead><tr><th>Moneda</th><th class="num">Compra</th><th class="num">Venta</th></tr></thead><tbody><tr><td colspan="3">Cargando…</td></tr></tbody></table></div>
<h2>Las monedas más consultadas desde Argentina</h2>
<h3>Euro</h3>
<p>Es la moneda de buena parte de la Unión Europea y la segunda más usada en el mundo. Se consulta mucho para viajes, estudios y compras en tiendas europeas. Su precio en pesos depende de la cotización del euro contra el dólar y del dólar contra el peso.</p>
<h3>Real brasileño</h3>
<p>Brasil es el principal socio comercial de Argentina y uno de los destinos turísticos más elegidos. Por eso la conversión de reales a pesos es una de las más buscadas, sobre todo antes del verano.</p>
<h3>Peso chileno y peso uruguayo</h3>
<p>Chile y Uruguay son destinos habituales de compras y vacaciones. El peso chileno tiene un valor unitario muy bajo (hace falta una gran cantidad de pesos chilenos para un dólar), por eso en la tabla mostramos más decimales.</p>
<h2>Cómo se calcula</h2>
<p>Igual que con el dólar: si tenés moneda extranjera y querés pesos, se usa el precio de <strong>compra</strong>; si tenés pesos y querés moneda extranjera, se usa el precio de <strong>venta</strong>. Por ejemplo, si el euro compra a $1.300, 100 euros son $130.000.</p>
""" + faq_html(MON_FAQ) + """
<p class="disclaimer">Valores de referencia del mercado oficial (fuente: DolarApi.com). Consultá el precio final con tu banco o casa de cambio.</p>
""",
    faq_schema(MON_FAQ),
)

# ---------------------------------------------------------------- Plazo fijo
PF_FAQ = [
    ("¿Qué es la TNA?",
     "Es la tasa nominal anual que informa el banco. Los intereses de un plazo fijo de 30 días se calculan como capital × TNA × 30 ÷ 365."),
    ("¿Qué diferencia hay entre TNA y TEA?",
     "La TEA (tasa efectiva anual) supone que renovás el plazo fijo con capital e intereses durante un año. Por el interés compuesto, siempre es mayor que la TNA."),
    ("¿Cuál es el plazo mínimo?",
     "En general 30 días para plazos fijos tradicionales. Algunos bancos ofrecen plazos fijos precancelables o UVA con otras condiciones."),
    ("¿Un plazo fijo le gana a la inflación?",
     "Depende del momento. Compará la TEM (tasa efectiva mensual) que te da la calculadora con la inflación mensual publicada por el INDEC."),
]
PAGES["/plazo-fijo/"] = (
    "Calculadora de plazo fijo: cuánto gano con mi plata",
    "Calculá cuánto ganás con un plazo fijo en pesos según la TNA de tu banco y los días. Te mostramos los intereses, la TEM y la TEA al instante.",
    """
<h1>Calculadora de plazo fijo</h1>
<p class="lead">Escribí cuánto querés invertir, la tasa que te ofrece tu banco y el plazo. Te mostramos cuánto vas a cobrar.</p>
<div class="card">
<form class="conv" id="pf-form">
<div class="full"><label for="pf-cap">Capital ($)</label><input id="pf-cap" inputmode="decimal" value="1.000.000"></div>
<div><label for="pf-tna">TNA (%)</label><input id="pf-tna" inputmode="decimal" value="30"></div>
<div><label for="pf-dias">Plazo (días)</label><input id="pf-dias" inputmode="numeric" value="30"></div>
<div class="full result" id="pf-result" aria-live="polite">—</div>
</form>
<p class="status">La tasa del ejemplo es ilustrativa. Usá la TNA que figure en el home banking de tu banco.</p>
</div>
<div class="ad-slot"></div>
<h2>Cómo se calculan los intereses</h2>
<p>Los bancos informan la <strong>TNA</strong> (tasa nominal anual). Para un plazo fijo tradicional, los intereses son:</p>
<p class="card">Intereses = Capital × TNA ÷ 100 × Días ÷ 365</p>
<p>Por ejemplo, con $1.000.000 a una TNA del 30 % durante 30 días: 1.000.000 × 0,30 × 30 ÷ 365 = $24.657. Al vencimiento cobrás $1.024.657.</p>
<h2>TEM y TEA: para comparar</h2>
<p>La <strong>TEM</strong> (tasa efectiva mensual) es lo que rinde tu plata en un mes. Es útil para compararla con la inflación mensual. La <strong>TEA</strong> (tasa efectiva anual) es lo que ganarías si renovaras el plazo fijo todo un año, sumando los intereses al capital cada vez. Como los intereses también generan intereses, la TEA es mayor que la TNA.</p>
<h2>Plazo fijo tradicional, UVA y precancelable</h2>
<ul>
<li><strong>Tradicional:</strong> tasa fija conocida de antemano. Es el que calcula esta herramienta.</li>
<li><strong>UVA:</strong> el capital se ajusta por inflación (a través de las UVA) y además paga una tasa pequeña. Suele exigir un plazo mínimo más largo.</li>
<li><strong>Precancelable:</strong> te permite retirar la plata antes, a cambio de una tasa menor si lo cancelás anticipadamente.</li>
</ul>
<h2>Antes de invertir</h2>
<p>Los depósitos a plazo fijo en pesos en bancos argentinos están cubiertos por el Sistema de Seguro de Garantía de los Depósitos hasta un monto máximo por persona y por banco, que se actualiza periódicamente. Comparar tasas entre bancos y billeteras virtuales puede marcar una diferencia importante en lo que cobrás.</p>
""" + faq_html(PF_FAQ) + """
<p class="disclaimer">Cálculo informativo. No incluye impuestos ni condiciones particulares de cada banco y no constituye asesoramiento financiero.</p>
""",
    faq_schema(PF_FAQ),
)

# ---------------------------------------------------------------- Aguinaldo
AG_FAQ = [
    ("¿Cuándo se cobra el aguinaldo?",
     "En dos cuotas: la primera hasta el 30 de junio y la segunda hasta el 18 de diciembre. Hay cuatro días hábiles adicionales de plazo para el pago."),
    ("¿Qué sueldo se toma para el cálculo?",
     "La mejor remuneración mensual bruta del semestre, incluyendo horas extra y conceptos remunerativos."),
    ("¿Cómo se calcula si trabajé menos de seis meses?",
     "Se paga en forma proporcional: la mitad del mejor sueldo multiplicada por los meses trabajados y dividida por seis. Para mayor precisión, se puede hacer por días trabajados."),
]
PAGES["/aguinaldo/"] = (
    "Calculadora de aguinaldo (SAC): cuánto cobro bruto y neto",
    "Calculá tu aguinaldo de junio o diciembre: medio aguinaldo completo o proporcional según los meses trabajados, en bruto y neto aproximado.",
    """
<h1>Calculadora de aguinaldo</h1>
<p class="lead">Calculá el sueldo anual complementario (SAC) de junio o diciembre, completo o proporcional.</p>
<div class="card">
<form class="conv" id="ag-form">
<div><label for="ag-sueldo">Mejor sueldo bruto del semestre ($)</label><input id="ag-sueldo" inputmode="decimal" value="800.000"></div>
<div><label for="ag-meses">Meses trabajados en el semestre</label><input id="ag-meses" inputmode="decimal" value="6"></div>
<div class="full result" id="ag-result" aria-live="polite">—</div>
</form>
</div>
<div class="ad-slot"></div>
<h2>Cómo se calcula el aguinaldo</h2>
<p>El aguinaldo, o sueldo anual complementario (SAC), equivale a medio sueldo por semestre. Se calcula como el <strong>50 % de la mejor remuneración mensual bruta</strong> del semestre (enero a junio, o julio a diciembre).</p>
<p class="card">Aguinaldo = Mejor sueldo bruto ÷ 2 × Meses trabajados ÷ 6</p>
<p>Si trabajaste los seis meses, cobrás la mitad del mejor sueldo. Si entraste a trabajar en marzo, por ejemplo, cobrás la parte proporcional a cuatro meses.</p>
<h2>Del bruto al neto</h2>
<p>Al aguinaldo se le aplican los mismos descuentos que al sueldo: 11 % de jubilación, 3 % de PAMI (ley 19.032) y 3 % de obra social, en total un 17 % para la mayoría de los trabajadores en relación de dependencia. Según tus ingresos, también puede corresponder una retención de impuesto a las ganancias, que esta calculadora no incluye.</p>
<h2>Ejemplo</h2>
<p>Si tu mejor sueldo bruto del semestre fue de $800.000 y trabajaste los seis meses, el aguinaldo bruto es de $400.000. Descontando el 17 % de aportes, cobrás alrededor de $332.000.</p>
""" + faq_html(AG_FAQ) + """
<p class="disclaimer">Cálculo orientativo. Ante dudas sobre tu caso, consultá tu recibo de sueldo, a tu empleador o a un contador.</p>
""",
    faq_schema(AG_FAQ),
)


# ---------------------------------------------------------------- Guías
def article_schema(g, url):
    import json
    data = {
        "@context": "https://schema.org", "@type": "Article", "headline": g["titulo"],
        "description": g["desc"], "datePublished": CONFIG["UPDATED"], "dateModified": CONFIG["UPDATED"],
        "inLanguage": "es-AR", "mainEntityOfPage": url,
        "author": {"@type": "Organization", "name": CONFIG["SITE_NAME"]},
        "publisher": {"@type": "Organization", "name": CONFIG["SITE_NAME"]},
    }
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


for _g in GUIAS:
    _path = f"/guias/{_g['slug']}/"
    _others = [o for o in GUIAS if o is not _g][:3]
    PAGES[_path] = (
        _g["titulo"] + " | " + CONFIG["SITE_NAME"],
        _g["desc"],
        f"""<p class="status"><a href="/guias/">Guías</a> › {_g['titulo']}</p>
<h1>{_g['titulo']}</h1>
<p class="lead">{_g['desc']}</p>
<p class="status">Actualizado: {CONFIG['UPDATED']}</p>
<p><a class="tile tool-link" href="{_g['tool'][0]}"><strong>{_g['tool'][1]}</strong></a></p>
{_g['body']}
<div class="ad-slot"></div>
<h2>Seguí leyendo</h2>
<div class="grid">""" + "".join(
            f'<a class="tile" href="/guias/{o["slug"]}/"><strong>{o["titulo"]}</strong></a>' for o in _others
        ) + "</div>",
        article_schema(_g, CONFIG["SITE_URL"] + _path),
    )

PAGES["/guias/"] = (
    "Guías de finanzas personales para Argentina | " + CONFIG["SITE_NAME"],
    "Guías simples sobre dólar MEP, dólar tarjeta, plazo fijo, aguinaldo, USDT, tasas de interés, inflación e IVA en Argentina.",
    """<h1>Guías</h1>
<p class="lead">Explicaciones claras y con ejemplos sobre dólar, ahorro, sueldo e impuestos en Argentina.</p>
<div class="grid tools">""" + "".join(
        f'<a class="tile" href="/guias/{g["slug"]}/"><strong>{g["titulo"]}</strong><small>{g["desc"]}</small></a>' for g in GUIAS
    ) + "</div>",
)

# ---------------------------------------------------------------- Páginas institucionales
PAGES["/sobre-nosotros/"] = (
    "Sobre nosotros | " + CONFIG["SITE_NAME"],
    "Quiénes somos y por qué creamos " + CONFIG["SITE_NAME"] + ", un sitio de conversores gratuitos.",
    f"""
<h1>Sobre nosotros</h1>
<p>{CONFIG["SITE_NAME"]} es un proyecto independiente hecho en Argentina. Lo creamos porque todos los días necesitamos responder preguntas simples, como cuántos pesos son 100 dólares, cuánto vale un USDT o cuánto es un 15 % de aumento, y la mayoría de las páginas que lo resuelven están llenas de distracciones o no explican de dónde sale el número.</p>
<h2>Nuestro enfoque</h2>
<ul>
<li><strong>Rápido:</strong> las páginas son livianas y funcionan bien en el celular.</li>
<li><strong>Transparente:</strong> cada conversor muestra el cálculo que hace y la fuente de los datos.</li>
<li><strong>Gratuito:</strong> no hace falta registrarse. El sitio se sostiene con publicidad.</li>
</ul>
<h2>Fuentes de datos</h2>
<p>Las cotizaciones del dólar provienen de DolarApi.com y los precios de criptomonedas de CoinGecko. Son valores de referencia y pueden diferir de los que te ofrezca cada entidad. Las conversiones de unidades y porcentajes se calculan directamente en tu navegador.</p>
<h2>Contacto</h2>
<p>Si encontrás un error o querés sugerir una herramienta nueva, escribinos desde la página de <a href="/contacto/">contacto</a>.</p>
""",
)

PAGES["/contacto/"] = (
    "Contacto | " + CONFIG["SITE_NAME"],
    "Escribinos para reportar errores, sugerir herramientas o hacer consultas sobre " + CONFIG["SITE_NAME"] + ".",
    f"""
<h1>Contacto</h1>
<p>¿Encontraste un error en algún cálculo, querés proponer un conversor nuevo o tenés una consulta sobre publicidad? Escribinos a:</p>
<p class="card" style="font-size:1.2rem"><a href="mailto:{CONFIG["CONTACT_EMAIL"]}">{CONFIG["CONTACT_EMAIL"]}</a></p>
<p>Respondemos en general dentro de las 48 horas hábiles. No brindamos asesoramiento financiero ni realizamos operaciones de cambio.</p>
""",
)

PAGES["/privacidad/"] = (
    "Política de privacidad | " + CONFIG["SITE_NAME"],
    "Cómo " + CONFIG["SITE_NAME"] + " trata la información de quienes visitan el sitio, uso de cookies y publicidad de Google.",
    f"""
<h1>Política de privacidad</h1>
<p>Última actualización: {CONFIG["UPDATED"]}</p>
<p>En {CONFIG["SITE_NAME"]} ({CONFIG["SITE_URL"]}) respetamos tu privacidad. Esta política explica qué información se recopila cuando visitás el sitio y cómo se usa.</p>
<h2>Información que recopilamos</h2>
<p>No pedimos registro ni datos personales para usar los conversores. Los montos que escribís se procesan en tu navegador y no se envían a nuestros servidores. Para mostrar cotizaciones, tu navegador consulta directamente a servicios públicos de datos (DolarApi.com y CoinGecko), que pueden registrar datos técnicos como tu dirección IP según sus propias políticas. Guardamos en tu navegador (almacenamiento local) una copia temporal de las cotizaciones para que la página cargue más rápido.</p>
<p>Si nos escribís por correo electrónico, usaremos tu dirección únicamente para responderte.</p>
<h2>Cookies y publicidad</h2>
<p>Este sitio utiliza Google AdSense para mostrar anuncios. Google y sus socios utilizan cookies para mostrar anuncios basados en las visitas anteriores de una persona a este sitio web o a otros sitios web.</p>
<ul>
<li>El uso de cookies de publicidad permite a Google y a sus socios mostrar anuncios a los usuarios en función de sus visitas a este sitio y a otros sitios de Internet.</li>
<li>Podés inhabilitar la publicidad personalizada en la <a href="https://adssettings.google.com" rel="nofollow">Configuración de anuncios de Google</a>, o desactivar las cookies de terceros para publicidad personalizada en <a href="https://www.aboutads.info/choices/" rel="nofollow">www.aboutads.info</a>.</li>
<li>Más información sobre cómo Google usa los datos: <a href="https://policies.google.com/technologies/partner-sites" rel="nofollow">Cómo utiliza Google la información de sitios que usan sus servicios</a>.</li>
</ul>
<p>Cuando corresponda según tu ubicación, se te mostrará un aviso para que aceptes o rechaces el uso de cookies publicitarias.</p>
<h2>Tus derechos</h2>
<p>De acuerdo con la Ley 25.326 de Protección de Datos Personales de Argentina, podés solicitar el acceso, la rectificación o la supresión de tus datos personales escribiendo a <a href="mailto:{CONFIG["CONTACT_EMAIL"]}">{CONFIG["CONTACT_EMAIL"]}</a>. La Agencia de Acceso a la Información Pública es el órgano de control de esa ley.</p>
<h2>Menores de edad</h2>
<p>El sitio no está dirigido a menores de 13 años y no recopilamos a sabiendas información de ellos.</p>
<h2>Cambios en esta política</h2>
<p>Podemos actualizar esta política. La fecha de la última actualización figura al principio de esta página.</p>
""",
)

PAGES["/terminos/"] = (
    "Términos de uso | " + CONFIG["SITE_NAME"],
    "Condiciones de uso de los conversores y calculadoras de " + CONFIG["SITE_NAME"] + ".",
    f"""
<h1>Términos de uso</h1>
<p>Al usar {CONFIG["SITE_NAME"]} aceptás estas condiciones.</p>
<h2>Carácter informativo</h2>
<p>Las cotizaciones, precios y resultados que muestra el sitio son de referencia. Pueden tener demoras o diferir de los valores de bancos, casas de cambio o exchanges. No constituyen asesoramiento financiero, impositivo ni de inversión, ni una oferta de compra o venta.</p>
<h2>Responsabilidad</h2>
<p>Hacemos nuestro mejor esfuerzo para que los cálculos sean correctos, pero no garantizamos que la información esté libre de errores. No nos responsabilizamos por decisiones tomadas en base a los resultados del sitio. Verificá siempre los valores con la entidad con la que vayas a operar.</p>
<h2>Servicios de terceros</h2>
<p>El sitio usa datos de DolarApi.com y CoinGecko, y publicidad de Google. Cada uno tiene sus propios términos y políticas.</p>
<h2>Contacto</h2>
<p>Consultas sobre estos términos: <a href="mailto:{CONFIG["CONTACT_EMAIL"]}">{CONFIG["CONTACT_EMAIL"]}</a>.</p>
""",
)


def build():
    for path, page in PAGES.items():
        title, desc, body, *rest = page
        related = [g for g in GUIAS if g["tool"][0] == path]
        if related:
            body += "<h2>Guías relacionadas</h2><ul>" + "".join(
                f'<li><a href="/guias/{g["slug"]}/">{g["titulo"]}</a></li>' for g in related) + "</ul>"
        schema = rest[0] if rest else ""
        target = OUT / path.strip("/") / "index.html" if path != "/" else OUT / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(layout(path, title, desc, body, schema), encoding="utf-8")

    # 404
    (OUT / "404.html").write_text(layout("/404.html", "Página no encontrada", "La página no existe.",
        '<h1>Página no encontrada</h1><p>Volvé al <a href="/">inicio</a> para usar los conversores.</p>'), encoding="utf-8")

    # sitemap y robots
    urls = "".join(
        f"<url><loc>{CONFIG['SITE_URL']}{p}</loc><lastmod>{CONFIG['UPDATED']}</lastmod></url>" for p in PAGES
    )
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        + urls + "</urlset>", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {CONFIG['SITE_URL']}/sitemap.xml\n", encoding="utf-8")

    # ads.txt (solo si hay ID de AdSense)
    if CONFIG["ADSENSE_CLIENT"]:
        pub = CONFIG["ADSENSE_CLIENT"].replace("ca-", "")
        (OUT / "ads.txt").write_text(f"google.com, {pub}, DIRECT, f08c47fec0942fa0\n", encoding="utf-8")

    (OUT / "favicon.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="32" fill="#153c4a"/>'
        '<text x="32" y="44" font-size="34" text-anchor="middle" fill="#7fd8c3" font-family="Arial" font-weight="700">$</text></svg>',
        encoding="utf-8")
    print("Sitio generado en", OUT)


if __name__ == "__main__":
    build()
