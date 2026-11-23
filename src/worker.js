// Worker de Cloudflare: sirve el sitio estático de public/ y, en la portada y en /dolar/,
// escribe las cotizaciones del momento directamente en el HTML. Así el visitante (y Google)
// ve los precios apenas abre la página, sin esperar a que cargue el JavaScript.
// Si DolarApi falla, la página sale igual que antes y el navegador las carga como siempre.

const DOLAR_API = "https://dolarapi.com/v1/dolares";
const LABEL = {
  oficial: "Oficial", blue: "Blue", bolsa: "MEP (Bolsa)", contadoconliqui: "CCL",
  mayorista: "Mayorista", cripto: "Cripto", tarjeta: "Tarjeta",
};
const RESUMEN = ["oficial", "blue", "bolsa", "tarjeta"];

const fmt = (n) =>
  typeof n === "number"
    ? n.toLocaleString("es-AR", { minimumFractionDigits: 0, maximumFractionDigits: 2 })
    : "—";
const fecha = (iso) => {
  try {
    return new Date(iso).toLocaleString("es-AR", {
      dateStyle: "short", timeStyle: "short", timeZone: "America/Argentina/Buenos_Aires",
    });
  } catch {
    return "";
  }
};
const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]);

async function cotizaciones() {
  try {
    const r = await fetch(DOLAR_API, { cf: { cacheTtl: 300, cacheEverything: true } });
    if (!r.ok) return null;
    const list = await r.json();
    return Array.isArray(list) && list.length ? list : null;
  } catch {
    return null;
  }
}

function resumenHtml(list) {
  return RESUMEN.map((casa) => {
    const d = list.find((x) => x.casa === casa);
    if (!d) return "";
    return (
      `<a class="tile" href="/dolar/"><div class="rate-name">Dólar ${LABEL[casa]}</div>` +
      `<div class="rate-val">$ ${fmt(d.venta)}</div>` +
      `<div class="rate-sub">${d.compra ? "Compra $ " + fmt(d.compra) : "Solo venta"}</div></a>`
    );
  }).join("");
}

function tarjetasHtml(list) {
  const ofi = list.find((x) => x.casa === "oficial");
  return list.map((d) => {
    const brecha = ofi && ofi.venta && d.casa !== "oficial" ? (d.venta / ofi.venta - 1) * 100 : null;
    const bTxt = brecha === null ? "" : "Brecha " + (brecha > 0 ? "+" : "") + brecha.toFixed(1).replace(".", ",") + " %";
    const nombre = "Dólar " + esc(LABEL[d.casa] || d.nombre);
    return (
      `<article class="cot"><h3 class="cot-nom">${nombre}</h3>` +
      `<dl class="cot-val"><div class="cot-c"><dt>Compra</dt><dd>${d.compra ? "$ " + fmt(d.compra) : "—"}</dd></div>` +
      `<div class="cot-v"><dt>Venta</dt><dd>$ ${fmt(d.venta)}</dd></div></dl>` +
      `<p class="cot-pie">${bTxt || (d.casa === "oficial" ? "Referencia para la brecha" : "")}` +
      `<time datetime="${esc(d.fechaActualizacion || "")}">${fecha(d.fechaActualizacion)}</time></p></article>`
    );
  }).join("");
}

function ultima(list) {
  return list.reduce((m, d) => (d.fechaActualizacion > m ? d.fechaActualizacion : m), "");
}

export default {
  async fetch(request, env) {
    const res = await env.ASSETS.fetch(request);
    const path = new URL(request.url).pathname;
    const ct = res.headers.get("content-type") || "";
    if (request.method !== "GET" || !ct.includes("text/html") || (path !== "/" && path !== "/dolar/")) return res;

    const list = await cotizaciones();
    if (!list) return res;

    const rw = new HTMLRewriter();
    if (path === "/") {
      rw.on("#dolar-summary", { element: (el) => el.setInnerContent(resumenHtml(list), { html: true }) });
    } else {
      rw.on("#dolar-cards", { element: (el) => el.setInnerContent(tarjetasHtml(list), { html: true }) });
      rw.on("#dolar-upd", {
        element: (el) => el.setInnerContent(`Actualizado el ${fecha(ultima(list))} según DolarApi.com. Cada tarjeta muestra la hora de su cotización.`),
      });
    }
    return rw.transform(res);
  },
};
