/* Conversores — lógica del lado del cliente. Sin dependencias. */
(function () {
  "use strict";

  var DOLAR_API = "https://dolarapi.com/v1/dolares";
  var CG_API = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,usd-coin,solana&vs_currencies=usd,ars&include_24hr_change=true";
  var CACHE_MIN = 5;

  function $(s, el) { return (el || document).querySelector(s); }
  function fmt(n, dec) {
    if (n === null || n === undefined || isNaN(n)) return "—";
    if (dec === undefined) dec = Math.abs(n) >= 100 ? 2 : (Math.abs(n) >= 1 ? 4 : 8);
    return n.toLocaleString("es-AR", { minimumFractionDigits: 0, maximumFractionDigits: dec });
  }
  function parseNum(v) {
    if (typeof v !== "string") return Number(v);
    v = v.trim().replace(/\s/g, "");
    // Acepta "1.234,56" (formato AR) y "1234.56"
    if (v.indexOf(",") > -1) v = v.replace(/\./g, "").replace(",", ".");
    else if (/^-?\d{1,3}(\.\d{3})+$/.test(v)) v = v.replace(/\./g, ""); // "122.000" = 122 mil
    return parseFloat(v);
  }
  function fmtDate(iso) {
    try { return new Date(iso).toLocaleString("es-AR", { dateStyle: "short", timeStyle: "short" }); }
    catch (e) { return ""; }
  }

  function cachedFetch(url) {
    var key = "cache:" + url;
    try {
      var c = JSON.parse(localStorage.getItem(key) || "null");
      if (c && Date.now() - c.t < CACHE_MIN * 60000) return Promise.resolve(c.d);
    } catch (e) {}
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    }).then(function (d) {
      try { localStorage.setItem(key, JSON.stringify({ t: Date.now(), d: d })); } catch (e) {}
      return d;
    }).catch(function (err) {
      try {
        var c = JSON.parse(localStorage.getItem(key) || "null");
        if (c) return c.d; // último dato conocido
      } catch (e) {}
      throw err;
    });
  }

  function setStatus(el, msg, isErr) {
    if (!el) return;
    el.textContent = msg;
    el.className = "status" + (isErr ? " err" : "");
  }

  var CASA_LABEL = {
    oficial: "Oficial", blue: "Blue", bolsa: "MEP (Bolsa)", contadoconliqui: "CCL",
    mayorista: "Mayorista", cripto: "Cripto", tarjeta: "Tarjeta"
  };

  /* ---------- Resumen de dólar (inicio) ---------- */
  function initDolarSummary() {
    var box = $("#dolar-summary");
    if (!box) return;
    cachedFetch(DOLAR_API).then(function (list) {
      var want = ["oficial", "blue", "bolsa", "tarjeta"];
      box.innerHTML = "";
      want.forEach(function (casa) {
        var d = list.filter(function (x) { return x.casa === casa; })[0];
        if (!d) return;
        var a = document.createElement("a");
        a.className = "tile"; a.href = "/dolar/";
        a.innerHTML = '<div class="rate-name">Dólar ' + CASA_LABEL[casa] + '</div>' +
          '<div class="rate-val">$ ' + fmt(d.venta, 2) + '</div>' +
          '<div class="rate-sub">' + (d.compra ? 'Compra $ ' + fmt(d.compra, 2) : 'Solo venta') + '</div>';
        box.appendChild(a);
      });
    }).catch(function () {
      box.innerHTML = '<p class="status err">No pudimos cargar las cotizaciones en este momento.</p>';
    });
  }

  /* ---------- Conversor de dólar ---------- */
  function initDolar() {
    var form = $("#dolar-form");
    if (!form) return;
    var status = $("#dolar-status"), tbody = $("#dolar-table tbody"), cards = $("#dolar-cards"), upd = $("#dolar-upd"), rates = {};
    function calc() {
      var amt = parseNum($("#d-amount").value), casa = $("#d-casa").value, dir = $("#d-dir").value;
      var r = rates[casa], out = $("#d-result");
      if (!r || isNaN(amt)) { out.innerHTML = "—"; return; }
      if (dir === "usd-ars") {
        var p = r.compra || r.venta;
        out.innerHTML = "$ " + fmt(amt * p, 2) + " ARS<small>US$ " + fmt(amt, 2) + " × $ " + fmt(p, 2) + " (precio de compra, " + CASA_LABEL[casa] + ")</small>";
      } else {
        var v = r.venta;
        out.innerHTML = "US$ " + fmt(amt / v, 2) + "<small>$ " + fmt(amt, 2) + " ÷ $ " + fmt(v, 2) + " (precio de venta, " + CASA_LABEL[casa] + ")</small>";
      }
    }
    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    setStatus(status, "Cargando cotizaciones…");
    cachedFetch(DOLAR_API).then(function (list) {
      var sel = $("#d-casa"); sel.innerHTML = ""; tbody.innerHTML = "";
      if (cards) cards.innerHTML = "";
      var last = "";
      var ofi = list.filter(function (x) { return x.casa === "oficial"; })[0];
      list.forEach(function (d) {
        rates[d.casa] = d;
        var o = document.createElement("option");
        o.value = d.casa; o.textContent = "Dólar " + (CASA_LABEL[d.casa] || d.nombre);
        if (d.casa === "blue") o.selected = true;
        sel.appendChild(o);
        var tr = document.createElement("tr");
        var brecha = ofi && ofi.venta && d.casa !== "oficial" ? (d.venta / ofi.venta - 1) * 100 : null;
        var bTxt = brecha === null ? "—" : (brecha > 0 ? "+" : "") + fmt(brecha, 1) + " %";
        tr.innerHTML = "<td>" + (CASA_LABEL[d.casa] || d.nombre) + "</td><td class=num>" + (d.compra ? "$ " + fmt(d.compra, 2) : "—") +
          "</td><td class=num>$ " + fmt(d.venta, 2) + "</td><td class=num>" + bTxt + "</td>";
        tbody.appendChild(tr);
        if (cards) {
          var c = document.createElement("article");
          c.className = "cot";
          c.innerHTML = '<h3 class="cot-nom"></h3>' +
            '<dl class="cot-val"><div class="cot-c"><dt>Compra</dt><dd>' + (d.compra ? "$ " + fmt(d.compra, 2) : "—") + '</dd></div>' +
            '<div class="cot-v"><dt>Venta</dt><dd>$ ' + fmt(d.venta, 2) + '</dd></div></dl>' +
            '<p class="cot-pie">' + (brecha === null ? (d.casa === "oficial" ? "Referencia para la brecha" : "") : "Brecha " + bTxt) +
            '<time datetime="' + d.fechaActualizacion + '">' + fmtDate(d.fechaActualizacion) + '</time></p>';
          c.querySelector(".cot-nom").textContent = "Dólar " + (CASA_LABEL[d.casa] || d.nombre);
          cards.appendChild(c);
        }
        if (d.fechaActualizacion > last) last = d.fechaActualizacion;
      });
      setStatus(status, "Última actualización: " + fmtDate(last) + " · Fuente: DolarApi.com");
      setStatus(upd, "Actualizado el " + fmtDate(last) + " según DolarApi.com. Cada tarjeta muestra la hora de su cotización.");
      calc();
    }).catch(function () {
      setStatus(status, "No pudimos cargar las cotizaciones. Probá recargar la página en unos minutos.", true);
      setStatus(upd, "No pudimos cargar las cotizaciones. Probá recargar la página en unos minutos.", true);
    });
  }

  /* ---------- Historial del dólar (ArgentinaDatos) ---------- */
  var HIST_API = "https://api.argentinadatos.com/v1/cotizaciones/dolares/";
  function initHist() {
    var box = $("#hist");
    if (!box) return;
    var selCasa = $("#h-casa"), chart = $("#h-chart"), dato = $("#h-dato"), status = $("#h-status"), tabla = $("#h-tabla");
    var btns = box.querySelectorAll(".seg button"), dias = 90, serie = [], pend = 0;
    function fdia(iso) { var p = iso.split("-"); return p[2] + "/" + p[1] + "/" + p[0]; }
    function fcorto(iso) { var p = iso.split("-"); return p[2] + "/" + p[1]; }
    function cargar() {
      var casa = selCasa.value, id = ++pend;
      box.classList.add("cargando");
      setStatus(status, "Cargando historial…");
      cachedFetch(HIST_API + casa).then(function (list) {
        if (id !== pend) return;
        serie = list.filter(function (x) { return x && x.fecha && x.venta; })
          .sort(function (a, b) { return a.fecha < b.fecha ? -1 : 1; });
        dibujar();
      }).catch(function () {
        if (id !== pend) return;
        box.classList.remove("cargando");
        chart.innerHTML = ""; dato.textContent = ""; tabla.innerHTML = "";
        setStatus(status, "No pudimos cargar el historial en este momento. Probá de nuevo en unos minutos.", true);
      });
    }
    function dibujar() {
      box.classList.remove("cargando");
      if (!serie.length) { setStatus(status, "No hay datos históricos para este tipo de cambio.", true); chart.innerHTML = ""; return; }
      var fin = new Date(serie[serie.length - 1].fecha + "T12:00:00Z");
      var desde = new Date(fin.getTime() - dias * 864e5).toISOString().slice(0, 10);
      var pts = serie.filter(function (x) { return x.fecha >= desde; });
      if (pts.length < 2) { setStatus(status, "No hay suficientes datos para este período.", true); chart.innerHTML = ""; return; }
      var a = pts[0], b = pts[pts.length - 1], vari = (b.venta / a.venta - 1) * 100;
      var nombre = selCasa.options[selCasa.selectedIndex].text;
      dato.innerHTML = '<strong>$ ' + fmt(b.venta, 2) + '</strong><span>' + (vari > 0 ? "+" : "") + fmt(vari, 1) +
        ' % desde el ' + fdia(a.fecha) + ' ($ ' + fmt(a.venta, 2) + ')</span>';
      setStatus(status, nombre + ", precio de venta al cierre de cada día. Último dato: " + fdia(b.fecha) + ". Fuente: ArgentinaDatos.");
      svg(pts, nombre);
      var filas = pts.slice().reverse().map(function (x) {
        return "<tr><td>" + fdia(x.fecha) + "</td><td class=num>" + (x.compra ? "$ " + fmt(x.compra, 2) : "—") + "</td><td class=num>$ " + fmt(x.venta, 2) + "</td></tr>";
      }).join("");
      tabla.innerHTML = "<table><thead><tr><th>Fecha</th><th class=num>Compra</th><th class=num>Venta</th></tr></thead><tbody>" + filas + "</tbody></table>";
    }
    function svg(pts, nombre) {
      var W = Math.max(280, chart.clientWidth || 600), H = W < 520 ? 210 : 280;
      var m = { t: 12, r: 12, b: 28, l: W < 520 ? 58 : 70 };
      var min = Infinity, max = -Infinity;
      pts.forEach(function (x) { if (x.venta < min) min = x.venta; if (x.venta > max) max = x.venta; });
      var pad = (max - min) * 0.08 || max * 0.02; min -= pad; max += pad;
      var X = function (i) { return m.l + i * (W - m.l - m.r) / (pts.length - 1); };
      var Y = function (v) { return m.t + (max - v) * (H - m.t - m.b) / (max - min); };
      var d = pts.map(function (x, i) { return (i ? "L" : "M") + X(i).toFixed(1) + " " + Y(x.venta).toFixed(1); }).join("");
      var grid = "", n = 4;
      for (var k = 0; k <= n; k++) {
        var v = min + (max - min) * k / n, y = Y(v).toFixed(1);
        grid += '<line x1="' + m.l + '" x2="' + (W - m.r) + '" y1="' + y + '" y2="' + y + '" class="g"/>' +
          '<text x="' + (m.l - 8) + '" y="' + y + '" dy="4" text-anchor="end">$ ' + fmt(v, 0) + '</text>';
      }
      var xl = [0, Math.floor((pts.length - 1) / 2), pts.length - 1].map(function (i, j) {
        return '<text x="' + X(i).toFixed(1) + '" y="' + (H - 8) + '" text-anchor="' + ["start", "middle", "end"][j] + '">' + fcorto(pts[i].fecha) + '</text>';
      }).join("");
      var area = d + "L" + X(pts.length - 1).toFixed(1) + " " + (H - m.b) + "L" + m.l + " " + (H - m.b) + "Z";
      chart.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" width="100%" height="' + H + '" role="img" tabindex="0" aria-label="Gráfico de la evolución del ' +
        nombre + '. Usá las flechas para recorrer los datos.">' + grid + xl +
        '<path class="area" d="' + area + '"/><path class="linea" d="' + d + '"/>' +
        '<line class="cruz" y1="' + m.t + '" y2="' + (H - m.b) + '" visibility="hidden"/><circle class="punto" r="5" visibility="hidden"/>' +
        '<rect class="hit" x="' + m.l + '" y="0" width="' + (W - m.l - m.r) + '" height="' + H + '"/></svg><div class="tip" hidden></div>';
      var el = chart.querySelector("svg"), cruz = el.querySelector(".cruz"), pto = el.querySelector(".punto"), tip = chart.querySelector(".tip"), cur = -1;
      function mostrar(i) {
        cur = Math.max(0, Math.min(pts.length - 1, i));
        var x = X(cur), y = Y(pts[cur].venta), esc = chart.clientWidth / W;
        cruz.setAttribute("x1", x); cruz.setAttribute("x2", x); cruz.setAttribute("visibility", "visible");
        pto.setAttribute("cx", x); pto.setAttribute("cy", y); pto.setAttribute("visibility", "visible");
        tip.hidden = false;
        tip.innerHTML = "<strong></strong><span></span>";
        tip.firstChild.textContent = "$ " + fmt(pts[cur].venta, 2);
        tip.lastChild.textContent = fdia(pts[cur].fecha);
        var left = x * esc, w = tip.offsetWidth;
        tip.style.left = Math.max(0, Math.min(chart.clientWidth - w, left - w / 2)) + "px";
        tip.style.top = Math.max(0, y * esc - 58) + "px";
      }
      function ocultar() { cruz.setAttribute("visibility", "hidden"); pto.setAttribute("visibility", "hidden"); tip.hidden = true; }
      el.addEventListener("pointermove", function (ev) {
        var r = el.getBoundingClientRect(), px = (ev.clientX - r.left) * W / r.width;
        mostrar(Math.round((px - m.l) / ((W - m.l - m.r) / (pts.length - 1))));
      });
      el.addEventListener("pointerleave", ocultar);
      el.addEventListener("blur", ocultar);
      el.addEventListener("keydown", function (ev) {
        if (ev.key === "ArrowLeft" || ev.key === "ArrowRight") {
          ev.preventDefault(); mostrar(cur < 0 ? pts.length - 1 : cur + (ev.key === "ArrowRight" ? 1 : -1));
        }
      });
    }
    selCasa.addEventListener("change", cargar);
    Array.prototype.forEach.call(btns, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call(btns, function (o) { o.setAttribute("aria-pressed", o === b ? "true" : "false"); });
        dias = +b.getAttribute("data-d");
        if (serie.length) dibujar();
      });
    });
    var rt; window.addEventListener("resize", function () { clearTimeout(rt); rt = setTimeout(function () { if (serie.length) dibujar(); }, 200); });
    cargar();
  }

  /* ---------- Conversor de criptomonedas ---------- */
  var COINS = { bitcoin: "Bitcoin (BTC)", ethereum: "Ethereum (ETH)", tether: "Tether (USDT)", "usd-coin": "USD Coin (USDC)", solana: "Solana (SOL)" };
  var SYM = { bitcoin: "BTC", ethereum: "ETH", tether: "USDT", "usd-coin": "USDC", solana: "SOL" };
  function initCripto() {
    var form = $("#cripto-form");
    if (!form) return;
    var status = $("#cripto-status"), prices = null;
    function calc() {
      var out = $("#c-result");
      if (!prices) return;
      var amt = parseNum($("#c-amount").value), coin = $("#c-coin").value, fiat = $("#c-fiat").value, dir = $("#c-dir").value;
      var p = prices[coin] && prices[coin][fiat];
      if (!p || isNaN(amt)) { out.innerHTML = "—"; return; }
      var F = fiat.toUpperCase();
      if (dir === "coin-fiat") {
        out.innerHTML = (fiat === "ars" ? "$ " : "US$ ") + fmt(amt * p, 2) + " " + F + "<small>" + fmt(amt) + " " + SYM[coin] + " × " + fmt(p, 2) + " " + F + "</small>";
      } else {
        out.innerHTML = fmt(amt / p) + " " + SYM[coin] + "<small>" + fmt(amt, 2) + " " + F + " ÷ " + fmt(p, 2) + " " + F + "</small>";
      }
    }
    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    setStatus(status, "Cargando precios…");
    cachedFetch(CG_API).then(function (d) {
      prices = d;
      var tbody = $("#cripto-table tbody"); tbody.innerHTML = "";
      Object.keys(COINS).forEach(function (k) {
        if (!d[k]) return;
        var ch = d[k].usd_24h_change;
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + COINS[k] + "</td><td class=num>US$ " + fmt(d[k].usd, 2) + "</td><td class=num>$ " + fmt(d[k].ars, 2) +
          "</td><td class=num>" + (ch === undefined ? "—" : (ch > 0 ? "+" : "") + fmt(ch, 2) + "%") + "</td>";
        tbody.appendChild(tr);
      });
      setStatus(status, "Precios de referencia actualizados cada pocos minutos · Fuente: CoinGecko");
      calc();
    }).catch(function () {
      setStatus(status, "No pudimos cargar los precios. Probá recargar en unos minutos.", true);
    });
  }

  /* ---------- Conversor de unidades ---------- */
  var UNITS = {
    longitud: { m: ["Metros", 1], km: ["Kilómetros", 1000], cm: ["Centímetros", 0.01], mm: ["Milímetros", 0.001], mi: ["Millas", 1609.344], yd: ["Yardas", 0.9144], ft: ["Pies", 0.3048], in: ["Pulgadas", 0.0254] },
    peso: { kg: ["Kilogramos", 1], g: ["Gramos", 0.001], mg: ["Miligramos", 1e-6], t: ["Toneladas", 1000], lb: ["Libras", 0.45359237], oz: ["Onzas", 0.028349523125] },
    volumen: { l: ["Litros", 1], ml: ["Mililitros", 0.001], m3: ["Metros cúbicos", 1000], gal: ["Galones (EE.UU.)", 3.785411784], floz: ["Onzas líquidas (EE.UU.)", 0.0295735295625], taza: ["Tazas (250 ml)", 0.25] },
    superficie: { m2: ["Metros cuadrados", 1], km2: ["Kilómetros cuadrados", 1e6], ha: ["Hectáreas", 10000], cm2: ["Centímetros cuadrados", 1e-4], ft2: ["Pies cuadrados", 0.09290304], acre: ["Acres", 4046.8564224] },
    velocidad: { kmh: ["km/h", 1 / 3.6], ms: ["m/s", 1], mph: ["Millas por hora", 0.44704], kn: ["Nudos", 0.514444] },
    temperatura: { c: ["Celsius (°C)"], f: ["Fahrenheit (°F)"], k: ["Kelvin (K)"] }
  };
  function tempConv(v, from, to) {
    var c = from === "c" ? v : from === "f" ? (v - 32) * 5 / 9 : v - 273.15;
    return to === "c" ? c : to === "f" ? c * 9 / 5 + 32 : c + 273.15;
  }
  function initUnidades() {
    var form = $("#u-form");
    if (!form) return;
    var cat = $("#u-cat"), from = $("#u-from"), to = $("#u-to");
    function fill() {
      var u = UNITS[cat.value], keys = Object.keys(u);
      from.innerHTML = to.innerHTML = "";
      keys.forEach(function (k, i) {
        from.add(new Option(u[k][0], k, false, i === 0));
        to.add(new Option(u[k][0], k, false, i === 1));
      });
      calc();
    }
    function calc() {
      var v = parseNum($("#u-amount").value), out = $("#u-result"), u = UNITS[cat.value];
      if (isNaN(v)) { out.innerHTML = "—"; return; }
      var r = cat.value === "temperatura" ? tempConv(v, from.value, to.value) : v * u[from.value][1] / u[to.value][1];
      out.innerHTML = fmt(r, 6) + " " + u[to.value][0] + "<small>" + fmt(v, 6) + " " + u[from.value][0] + "</small>";
    }
    var p = new URLSearchParams(location.search);
    if (p.get("c") && UNITS[p.get("c")]) cat.value = p.get("c");
    cat.addEventListener("change", fill);
    form.addEventListener("input", function (e) { if (e.target !== cat) calc(); });
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    $("#u-swap").addEventListener("click", function () { var t = from.value; from.value = to.value; to.value = t; calc(); });
    fill();
  }

  /* ---------- Calculadora de porcentajes e IVA ---------- */
  function initPorcentaje() {
    var root = $("#pct-tools");
    if (!root) return;
    function bind(id, fn) {
      var f = $("#" + id);
      var run = function () {
        var ins = f.querySelectorAll("input"), vals = [];
        for (var i = 0; i < ins.length; i++) vals.push(parseNum(ins[i].value));
        var sel = f.querySelector("select");
        var r = fn(vals, sel ? sel.value : null);
        f.querySelector(".result").innerHTML = r;
      };
      f.addEventListener("input", run);
      f.addEventListener("submit", function (e) { e.preventDefault(); run(); });
      run();
    }
    function bad(a) { return a.some(function (x) { return isNaN(x); }); }
    bind("pct-of", function (v) { return bad(v) ? "—" : fmt(v[0] * v[1] / 100, 4) + "<small>" + fmt(v[0]) + "% de " + fmt(v[1]) + "</small>"; });
    bind("pct-change", function (v) {
      if (bad(v) || v[0] === 0) return "—";
      var c = (v[1] - v[0]) / Math.abs(v[0]) * 100;
      return (c > 0 ? "+" : "") + fmt(c, 2) + "%<small>" + (c >= 0 ? "Aumento" : "Disminución") + " de " + fmt(v[0]) + " a " + fmt(v[1]) + "</small>";
    });
    bind("pct-apply", function (v, mode) {
      if (bad(v)) return "—";
      var r = mode === "sumar" ? v[0] * (1 + v[1] / 100) : v[0] * (1 - v[1] / 100);
      return fmt(r, 2) + "<small>" + fmt(v[0]) + (mode === "sumar" ? " + " : " − ") + fmt(v[1]) + "%</small>";
    });
    bind("iva", function (v, mode) {
      if (bad(v)) return "—";
      var rate = v[1] / 100, neto, total;
      if (mode === "sumar") { neto = v[0]; total = v[0] * (1 + rate); }
      else { total = v[0]; neto = v[0] / (1 + rate); }
      return "Total $ " + fmt(total, 2) + "<small>Neto $ " + fmt(neto, 2) + " · IVA $ " + fmt(total - neto, 2) + "</small>";
    });
  }

  /* ---------- Otras monedas (EUR, BRL, CLP, UYU) ---------- */
  var MON_API = "https://dolarapi.com/v1/cotizaciones";
  var MON_LABEL = { USD: "Dólar oficial (USD)", EUR: "Euro (EUR)", BRL: "Real brasileño (BRL)", CLP: "Peso chileno (CLP)", UYU: "Peso uruguayo (UYU)" };
  function initMonedas() {
    var form = $("#m-form");
    if (!form) return;
    var status = $("#m-status"), rates = {};
    function calc() {
      var amt = parseNum($("#m-amount").value), cur = $("#m-cur").value, dir = $("#m-dir").value, r = rates[cur], out = $("#m-result");
      if (!r || isNaN(amt)) { out.innerHTML = "—"; return; }
      if (dir === "x-ars") {
        var p = r.compra || r.venta;
        out.innerHTML = "$ " + fmt(amt * p, 2) + " ARS<small>" + fmt(amt, 2) + " " + cur + " × $ " + fmt(p, 4) + " (compra)</small>";
      } else {
        out.innerHTML = fmt(amt / r.venta, 2) + " " + cur + "<small>$ " + fmt(amt, 2) + " ÷ $ " + fmt(r.venta, 4) + " (venta)</small>";
      }
    }
    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    var q = new URLSearchParams(location.search).get("m");
    setStatus(status, "Cargando cotizaciones…");
    cachedFetch(MON_API).then(function (list) {
      var sel = $("#m-cur"), tbody = $("#m-table tbody"), last = "";
      sel.innerHTML = ""; tbody.innerHTML = "";
      list.forEach(function (d) {
        if (!MON_LABEL[d.moneda]) return;
        rates[d.moneda] = d;
        sel.add(new Option(MON_LABEL[d.moneda], d.moneda, false, q ? d.moneda === q : d.moneda === "EUR"));
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + MON_LABEL[d.moneda] + "</td><td class=num>" + (d.compra ? "$ " + fmt(d.compra, 4) : "—") + "</td><td class=num>$ " + fmt(d.venta, 4) + "</td>";
        tbody.appendChild(tr);
        if (d.fechaActualizacion > last) last = d.fechaActualizacion;
      });
      setStatus(status, "Cotización oficial de referencia · Última actualización: " + fmtDate(last) + " · Fuente: DolarApi.com");
      calc();
    }).catch(function () {
      setStatus(status, "No pudimos cargar las cotizaciones. Probá recargar en unos minutos.", true);
    });
  }

  /* ---------- Plazo fijo ---------- */
  function initPlazoFijo() {
    var form = $("#pf-form");
    if (!form) return;
    function calc() {
      var cap = parseNum($("#pf-cap").value), tna = parseNum($("#pf-tna").value), dias = parseNum($("#pf-dias").value), out = $("#pf-result");
      if ([cap, tna, dias].some(isNaN) || dias <= 0) { out.innerHTML = "—"; return; }
      var interes = cap * tna / 100 * dias / 365;
      var tem = tna / 100 * 30 / 365;
      var tea = (Math.pow(1 + tna / 100 * dias / 365, 365 / dias) - 1) * 100;
      out.innerHTML = "Cobrás $ " + fmt(cap + interes, 2) + "<small>Intereses $ " + fmt(interes, 2) + " · TEM " + fmt(tem * 100, 2) + "% · TEA " + fmt(tea, 2) + "%</small>";
    }
    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    calc();
  }

  /* ---------- Aguinaldo (SAC) ---------- */
  function initAguinaldo() {
    var form = $("#ag-form");
    if (!form) return;
    function calc() {
      var sueldo = parseNum($("#ag-sueldo").value), meses = parseNum($("#ag-meses").value), out = $("#ag-result");
      if (isNaN(sueldo) || isNaN(meses)) { out.innerHTML = "—"; return; }
      meses = Math.max(0, Math.min(6, meses));
      var bruto = sueldo / 2 * meses / 6, neto = bruto * 0.83;
      out.innerHTML = "Bruto $ " + fmt(bruto, 2) + "<small>Neto aproximado $ " + fmt(neto, 2) + " (descontando 17 % de aportes)</small>";
    }
    form.addEventListener("input", calc);
    form.addEventListener("submit", function (e) { e.preventDefault(); calc(); });
    calc();
  }

  document.addEventListener("DOMContentLoaded", function () {
    initDolarSummary(); initDolar(); initHist(); initCripto(); initUnidades(); initPorcentaje(); initMonedas(); initPlazoFijo(); initAguinaldo();
    var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
  });
})();
