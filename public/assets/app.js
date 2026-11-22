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
    var status = $("#dolar-status"), tbody = $("#dolar-table tbody"), rates = {};
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
      var last = "";
      list.forEach(function (d) {
        rates[d.casa] = d;
        var o = document.createElement("option");
        o.value = d.casa; o.textContent = "Dólar " + (CASA_LABEL[d.casa] || d.nombre);
        if (d.casa === "blue") o.selected = true;
        sel.appendChild(o);
        var tr = document.createElement("tr");
        tr.innerHTML = "<td>" + (CASA_LABEL[d.casa] || d.nombre) + "</td><td class=num>" + (d.compra ? "$ " + fmt(d.compra, 2) : "—") +
          "</td><td class=num>$ " + fmt(d.venta, 2) + "</td>";
        tbody.appendChild(tr);
        if (d.fechaActualizacion > last) last = d.fechaActualizacion;
      });
      setStatus(status, "Última actualización: " + fmtDate(last) + " · Fuente: DolarApi.com");
      calc();
    }).catch(function () {
      setStatus(status, "No pudimos cargar las cotizaciones. Probá recargar la página en unos minutos.", true);
    });
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

  document.addEventListener("DOMContentLoaded", function () {
    initDolarSummary(); initDolar(); initCripto(); initUnidades(); initPorcentaje();
    var y = $("#year"); if (y) y.textContent = new Date().getFullYear();
  });
})();
