"""Guías (artículos) del sitio. Cada guía: slug, título, descripción, herramienta relacionada, cuerpo HTML."""

GUIAS = [
    {
        "slug": "como-comprar-dolar-mep",
        "titulo": "Cómo comprar dólar MEP paso a paso",
        "desc": "Guía simple para comprar dólar MEP desde el home banking o una cuenta comitente: qué necesitás, qué bono se usa, cuánto tarda y qué costos tiene.",
        "tool": ("/dolar/", "Ver la cotización del dólar MEP hoy"),
        "body": """
<p>El dólar MEP (Mercado Electrónico de Pagos), también llamado dólar bolsa, es una forma legal de pasar pesos a dólares usando el mercado de capitales. En lugar de comprar dólares directamente, comprás un bono con pesos y lo vendés en dólares. La diferencia entre ambos precios es lo que se conoce como cotización del MEP.</p>
<h2>Qué necesitás</h2>
<ul>
<li>Una <strong>cuenta bancaria en pesos y otra en dólares</strong> a tu nombre. Casi todos los bancos abren la caja de ahorro en dólares desde la app.</li>
<li>Una <strong>cuenta comitente</strong>, que es la cuenta para operar títulos. Muchos bancos la ofrecen dentro del home banking, y también la podés abrir en una sociedad de bolsa (ALyC) de forma online.</li>
<li>Estar al día con tus datos personales y, en algunos casos, completar un perfil de inversor.</li>
</ul>
<h2>Paso a paso</h2>
<ol>
<li><strong>Transferí pesos</strong> a tu cuenta comitente (si es en el mismo banco, suele estar vinculada).</li>
<li><strong>Comprá un bono en pesos</strong>. Los más usados para esta operación son los bonos soberanos más líquidos, como el AL30 o el GD30. Tu banco o ALyC suele indicarlo.</li>
<li><strong>Esperá el plazo de tenencia, si corresponde</strong>. Según la normativa vigente puede existir un plazo mínimo entre la compra y la venta (el llamado <em>parking</em>). Consultá en tu banco o ALyC si aplica a tu caso.</li>
<li><strong>Vendé el mismo bono en su especie en dólares</strong> (por ejemplo, AL30D). El resultado se acredita en dólares en tu cuenta comitente.</li>
<li><strong>Transferí los dólares</strong> a tu caja de ahorro en dólares.</li>
</ol>
<p>Muchos bancos ya tienen una opción “Comprar dólar MEP” que hace todos estos pasos de forma automática. Si la ves, es la manera más simple.</p>
<h2>Cuánto cuesta</h2>
<p>Además de la diferencia de precio, pagás <strong>comisiones</strong> de compra y venta del bono y, a veces, derechos de mercado. En total suelen sumar menos del 1 %, pero varían mucho entre bancos y ALyC. Vale la pena comparar.</p>
<h2>MEP, blue y oficial: cuál conviene</h2>
<p>El MEP es legal, queda registrado en el sistema bancario y los dólares quedan depositados a tu nombre. El blue es informal y en efectivo. El oficial puede estar sujeto a límites o impuestos según la normativa del momento. Antes de decidir, compará las cotizaciones del día en nuestro <a href="/dolar/">conversor de dólar</a>.</p>
<h2>Errores comunes</h2>
<ul>
<li>Vender el bono en la especie equivocada (por ejemplo, en la especie de dólar cable en lugar de la de dólar MEP).</li>
<li>No tener en cuenta el horario del mercado: las operaciones se hacen en días hábiles y en horario bursátil.</li>
<li>Olvidar las comisiones al calcular cuántos dólares vas a recibir.</li>
</ul>
""",
    },
    {
        "slug": "dolar-tarjeta-como-se-calcula",
        "titulo": "Dólar tarjeta: cómo se calcula y cómo pagar menos",
        "desc": "Qué es el dólar tarjeta, cómo se calcula a partir del oficial, qué impuestos incluye y qué opciones hay para pagar consumos en el exterior.",
        "tool": ("/dolar/", "Ver el dólar tarjeta de hoy"),
        "body": """
<p>Cuando pagás con una tarjeta argentina en una moneda extranjera (una suscripción a una plataforma, una compra en una tienda del exterior o un gasto en un viaje), el consumo no se convierte al dólar oficial a secas. Se aplica el llamado <strong>dólar tarjeta</strong>, que es el oficial más impuestos y percepciones.</p>
<h2>Cómo se calcula</h2>
<p>La fórmula general es:</p>
<p class="card">Dólar tarjeta = Dólar oficial (venta) × (1 + suma de impuestos y percepciones vigentes)</p>
<p>Los porcentajes dependen de la normativa de cada momento y cambiaron muchas veces en los últimos años. Lo más práctico es mirar el valor actualizado en nuestro <a href="/dolar/">conversor</a>, donde aparece como “Tarjeta”.</p>
<h2>Las percepciones no son un gasto perdido (a veces)</h2>
<p>Parte de lo que pagás como percepción puede funcionar como un adelanto de impuestos. Si estás inscripto en ganancias o en bienes personales, podés computarlo; si no, en muchos casos se puede pedir la devolución ante ARCA al año siguiente. Revisá las condiciones vigentes o consultá con un contador.</p>
<h2>Cómo pagar menos</h2>
<ul>
<li><strong>Pagar el resumen con dólares propios.</strong> Si tenés dólares en una cuenta bancaria, muchos bancos te permiten cancelar el saldo en dólares de la tarjeta con ellos. En ese caso, en general no se aplican las percepciones sobre ese pago.</li>
<li><strong>Comparar con el MEP.</strong> Si el dólar MEP está más barato que el dólar tarjeta, puede convenir comprar MEP y pagar el resumen en dólares. Mirá la <a href="/guias/como-comprar-dolar-mep/">guía para comprar dólar MEP</a>.</li>
<li><strong>Revisar la moneda del cobro.</strong> Algunos comercios del exterior te ofrecen cobrarte en pesos con su propio tipo de cambio. Suele ser más caro: elegí pagar en la moneda local del comercio.</li>
</ul>
<h2>Ejemplo</h2>
<p>Si una suscripción cuesta 10 dólares y el dólar tarjeta está a $1.400, el cargo en pesos será de unos $14.000. Si en cambio pagás esos 10 dólares con dólares que compraste en el MEP a $1.200, te cuesta unos $12.000 más las comisiones de la compra.</p>
<p>¿Comprás juegos en Steam, PlayStation o Xbox? En <a href="https://juegos.bolsillo.online/ofertas/">Bolsillo Gamer</a> ves las ofertas del día con el precio ya pasado a pesos con el dólar tarjeta.</p>
""",
    },
    {
        "slug": "plazo-fijo-o-billetera-virtual",
        "titulo": "Plazo fijo o billetera virtual: qué conviene",
        "desc": "Comparamos el plazo fijo tradicional con las cuentas remuneradas y fondos de las billeteras virtuales: rendimiento, liquidez, riesgos y cuándo conviene cada uno.",
        "tool": ("/plazo-fijo/", "Calcular cuánto rinde un plazo fijo"),
        "body": """
<p>Hoy hay dos formas muy populares de hacer rendir los pesos sin complicarse: el plazo fijo tradicional y la plata que queda “rindiendo” en una billetera virtual o cuenta remunerada. Las dos son simples, pero funcionan distinto.</p>
<h2>Plazo fijo</h2>
<ul>
<li><strong>Tasa fija</strong>: sabés desde el primer día cuánto vas a cobrar.</li>
<li><strong>Plazo mínimo</strong>: en general 30 días. No podés sacar la plata antes, salvo en los precancelables.</li>
<li><strong>Garantía</strong>: los depósitos en bancos tienen cobertura del seguro de depósitos hasta un monto máximo por persona y por banco.</li>
</ul>
<h2>Billeteras virtuales y cuentas remuneradas</h2>
<ul>
<li><strong>Liquidez inmediata</strong>: podés usar la plata cuando quieras.</li>
<li><strong>Tasa variable</strong>: el rendimiento cambia día a día y puede bajar sin aviso.</li>
<li><strong>Qué hay detrás</strong>: en muchas billeteras, la plata se invierte en un fondo común de inversión (FCI) de mercado de dinero. Un FCI no es un depósito bancario y no tiene la cobertura del seguro de depósitos, aunque suele ser de bajo riesgo.</li>
<li><strong>Cuentas remuneradas bancarias</strong>: son depósitos a la vista en un banco que pagan interés. Combinan liquidez con la cobertura del seguro.</li>
</ul>
<h2>Cómo compararlas</h2>
<p>El error más común es comparar tasas distintas. Las billeteras suelen informar la TNA, igual que los bancos, pero como el rendimiento se acredita todos los días, el efecto del interés compuesto es mayor. Para comparar en serio, pasá todo a <strong>TEM</strong> (tasa efectiva mensual). Lo explicamos en la guía <a href="/guias/tna-tem-tea-diferencias/">TNA, TEM y TEA</a>, y nuestra <a href="/plazo-fijo/">calculadora de plazo fijo</a> te muestra la TEM al instante.</p>
<h2>Cuándo conviene cada uno</h2>
<ul>
<li><strong>Plazo fijo</strong>: si sabés que no vas a necesitar esa plata por un mes o más y la tasa es mejor que la de la billetera.</li>
<li><strong>Billetera o cuenta remunerada</strong>: para el fondo de emergencia o la plata que vas a usar pronto.</li>
<li><strong>Combinación</strong>: muchas personas dejan una parte líquida en la billetera y el resto en plazo fijo.</li>
</ul>
<h2>Y la inflación</h2>
<p>Lo que importa no es cuánto ganás en pesos sino si le ganás a la inflación. Compará la TEM con el último dato mensual del INDEC. Si la TEM es menor, tu plata pierde poder de compra aunque “rinda”.</p>
""",
    },
    {
        "slug": "cuando-se-cobra-el-aguinaldo",
        "titulo": "Aguinaldo de diciembre 2026: cuándo se cobra y cómo se calcula",
        "actualizado": "2026-11-23",
        "desc": "Fechas de pago del aguinaldo en Argentina, quiénes lo cobran, cómo se calcula el medio aguinaldo y el proporcional, y qué descuentos tiene.",
        "tool": ("/aguinaldo/", "Calcular mi aguinaldo"),
        "body": """
<p>El aguinaldo, o <strong>sueldo anual complementario (SAC)</strong>, es un pago extra que reciben todos los trabajadores en relación de dependencia. Equivale a un sueldo por año y se cobra en dos cuotas.</p>
<h2>Cuándo se cobra</h2>
<ul>
<li><strong>Primera cuota</strong>: corresponde al semestre enero a junio. Vence el 30 de junio.</li>
<li><strong>Segunda cuota</strong>: corresponde al semestre julio a diciembre. Vence el 18 de diciembre.</li>
</ul>
<p>La ley da un plazo adicional de cuatro días hábiles para el pago, así que muchas empresas lo depositan en los primeros días de julio o en la última semana de diciembre.</p>
<h2>Aguinaldo de diciembre 2026</h2>
<p>La segunda cuota de 2026 vence el <strong>viernes 18 de diciembre de 2026</strong>. Con los cuatro días hábiles de tolerancia, el último día para pagarla cae en la semana de Navidad. Los jubilados y pensionados de ANSES lo cobran junto con el haber de diciembre, según el calendario de pagos por terminación de documento.</p>
<p>Corresponde al semestre de julio a diciembre: si trabajaste todo el semestre, cobrás la mitad del mejor sueldo bruto de esos meses. Para saber cuánto te toca, usá la <a href="/aguinaldo/">calculadora de aguinaldo</a>.</p>
<h2>Quiénes lo cobran</h2>
<p>Lo cobran los trabajadores registrados en relación de dependencia, incluido el personal de casas particulares, los jubilados y los pensionados. Los monotributistas y autónomos no cobran aguinaldo.</p>
<h2>Cómo se calcula</h2>
<p>Cada cuota es el <strong>50 % de la mejor remuneración mensual bruta</strong> del semestre. Se incluyen los conceptos remunerativos como horas extra, comisiones y adicionales.</p>
<p class="card">Aguinaldo = Mejor sueldo bruto ÷ 2</p>
<p>Si no trabajaste el semestre completo, se paga en forma <strong>proporcional</strong>: mejor sueldo ÷ 2 × días trabajados ÷ días del semestre. En la práctica, se aproxima con los meses trabajados dividido seis. Podés hacer la cuenta en nuestra <a href="/aguinaldo/">calculadora de aguinaldo</a>.</p>
<h2>Descuentos</h2>
<p>El aguinaldo tiene los mismos aportes que el sueldo: 11 % de jubilación, 3 % de PAMI y 3 % de obra social. Según el nivel de ingresos, también puede tener retención del impuesto a las ganancias.</p>
<h2>Ejemplo</h2>
<p>Ana trabajó de enero a junio y su mejor sueldo bruto fue de $900.000 en mayo. Su medio aguinaldo bruto es de $450.000 y, después de los aportes del 17 %, cobra unos $373.500.</p>
<p>Juan empezó a trabajar el 1 de abril, con un sueldo bruto de $700.000. Trabajó tres meses del semestre, así que su aguinaldo proporcional es de $700.000 ÷ 2 × 3 ÷ 6 = $175.000 bruto.</p>
<h2>Si te despiden o renunciás</h2>
<p>En la liquidación final se paga el aguinaldo proporcional a lo trabajado en el semestre, y en caso de despido también se calcula el SAC sobre algunos rubros indemnizatorios, como las vacaciones no gozadas.</p>
""",
    },
    {
        "slug": "que-es-usdt",
        "titulo": "Qué es USDT y por qué se usa tanto en Argentina",
        "desc": "Qué es la stablecoin USDT, cómo mantiene su valor en un dólar, cómo se compra con pesos y qué riesgos tiene frente a otras formas de ahorrar en dólares.",
        "tool": ("/cripto/", "Convertir USDT a pesos"),
        "body": """
<p>USDT (Tether) es una <strong>stablecoin</strong>: una criptomoneda diseñada para valer siempre aproximadamente un dólar estadounidense. A diferencia de Bitcoin, su precio no sube ni baja con el mercado, porque la empresa que la emite dice respaldar cada token con reservas en dólares y activos equivalentes.</p>
<h2>Por qué es tan popular en Argentina</h2>
<ul>
<li><strong>Se compra con pesos en minutos</strong>, desde una app y a cualquier hora, incluidos fines de semana y feriados.</li>
<li><strong>No tiene los límites de compra</strong> que muchas veces tuvo el dólar oficial.</li>
<li>Sirve para <strong>cobrar trabajos del exterior</strong> o enviar dinero a otros países con costos bajos.</li>
<li>Algunas plataformas pagan un pequeño rendimiento por mantener USDT.</li>
</ul>
<h2>El dólar cripto</h2>
<p>El precio de USDT en pesos se forma por oferta y demanda en los exchanges, y se lo conoce como <em>dólar cripto</em>. Suele moverse cerca del dólar MEP y del blue. Podés ver su valor actualizado en nuestro <a href="/cripto/">conversor de criptomonedas</a> o en la fila “Cripto” del <a href="/dolar/">conversor de dólar</a>.</p>
<h2>Cómo se compra</h2>
<ol>
<li>Abrí una cuenta en un exchange que opere en Argentina y validá tu identidad.</li>
<li>Transferí pesos desde tu cuenta bancaria.</li>
<li>Comprá USDT en el mercado del exchange o en la sección P2P.</li>
<li>Si querés, retiralos a tu propia billetera. Revisá bien la <strong>red</strong> que elegís al enviar (por ejemplo, TRON o Ethereum): si la red no coincide, los fondos se pueden perder.</li>
</ol>
<h2>Riesgos a tener en cuenta</h2>
<ul>
<li><strong>Riesgo del emisor</strong>: el valor depende de que Tether efectivamente tenga las reservas que declara.</li>
<li><strong>Riesgo de la plataforma</strong>: si dejás los USDT en un exchange y este tiene problemas, podés perder acceso a tus fondos.</li>
<li><strong>No hay seguro de depósitos</strong>: a diferencia de los dólares en un banco argentino.</li>
<li><strong>Errores de envío</strong>: las transacciones en blockchain no se pueden revertir.</li>
</ul>
<h2>USDT, USDC y dólares en el banco</h2>
<p>USDC es otra stablecoin muy usada, emitida por Circle, que publica auditorías periódicas de sus reservas. Los dólares en un banco argentino tienen la cobertura del seguro de depósitos pero menos flexibilidad. Muchas personas combinan ambas opciones según para qué necesiten el dinero.</p>
<p class="disclaimer">Esta guía es informativa y no es una recomendación de inversión.</p>
""",
    },
    {
        "slug": "tna-tem-tea-diferencias",
        "titulo": "TNA, TEM y TEA: qué son y cómo compararlas",
        "desc": "Explicación simple de la tasa nominal anual, la tasa efectiva mensual y la tasa efectiva anual, con fórmulas y ejemplos para comparar inversiones y préstamos.",
        "tool": ("/plazo-fijo/", "Calcular TEM y TEA"),
        "body": """
<p>Cuando un banco, una billetera o una tarjeta te informan una tasa, casi siempre aparecen tres siglas: TNA, TEM y TEA. Entenderlas es la única forma de saber qué opción conviene de verdad.</p>
<h2>TNA: tasa nominal anual</h2>
<p>Es la tasa “de cartel”. Sirve para calcular los intereses de un período, pero no tiene en cuenta que los intereses se pueden reinvertir. Para un plazo de 30 días:</p>
<p class="card">Interés = Capital × TNA ÷ 100 × 30 ÷ 365</p>
<h2>TEM: tasa efectiva mensual</h2>
<p>Es lo que efectivamente rinde (o cuesta) tu plata en un mes:</p>
<p class="card">TEM = TNA × 30 ÷ 365</p>
<p>Con una TNA del 36 %, la TEM es de 2,96 %. La TEM es la mejor tasa para comparar con la <strong>inflación mensual</strong>.</p>
<h2>TEA: tasa efectiva anual</h2>
<p>Supone que cada mes reinvertís capital más intereses. Por el interés compuesto, la TEA siempre es mayor que la TNA:</p>
<p class="card">TEA = (1 + TEM)<sup>12</sup> − 1 (aproximadamente)</p>
<p>Con una TNA del 36 %, la TEA ronda el 42 %.</p>
<h2>Cuál usar para comparar</h2>
<ul>
<li><strong>Dos plazos fijos</strong>: alcanza con comparar la TNA si tienen el mismo plazo.</li>
<li><strong>Plazo fijo contra billetera virtual</strong>: compará la TEM o la TEA, porque la billetera capitaliza todos los días.</li>
<li><strong>Inversión contra inflación</strong>: TEM contra inflación mensual.</li>
<li><strong>Préstamos y tarjetas</strong>: mirá el <strong>CFT</strong> (costo financiero total), que suma la tasa, los impuestos y los gastos. Es el número que realmente pagás.</li>
</ul>
<h2>Ejemplo</h2>
<p>Un banco ofrece un plazo fijo con TNA del 30 % y una billetera paga una TNA del 29 % con capitalización diaria. La TEM del plazo fijo es de 2,47 %. La de la billetera, con capitalización diaria, es de alrededor de 2,41 %. A igualdad de tasa nominal, la billetera rinde un poco más por capitalizar todos los días, pero en este caso el plazo fijo sigue ganando por tener una tasa mayor.</p>
<p>Podés probar tus propios números en la <a href="/plazo-fijo/">calculadora de plazo fijo</a>.</p>
""",
    },
    {
        "slug": "como-calcular-aumento-de-sueldo-inflacion",
        "titulo": "Cómo saber si tu aumento de sueldo le ganó a la inflación",
        "desc": "Cómo calcular el porcentaje de aumento de tu sueldo, compararlo con la inflación acumulada y saber si ganaste o perdiste poder de compra.",
        "tool": ("/porcentaje/", "Calcular el porcentaje de aumento"),
        "body": """
<p>Recibir un aumento no siempre significa ganar más. Si los precios subieron más que tu sueldo, en realidad podés comprar menos cosas que antes. Para saberlo hacen falta dos números: tu aumento porcentual y la inflación del mismo período.</p>
<h2>Paso 1: calculá tu aumento</h2>
<p class="card">Aumento % = (Sueldo nuevo − Sueldo anterior) ÷ Sueldo anterior × 100</p>
<p>Si cobrabas $800.000 y ahora cobrás $920.000, tu aumento fue del 15 %. Podés hacer la cuenta en la calculadora de <a href="/porcentaje/">variación porcentual</a>.</p>
<h2>Paso 2: calculá la inflación acumulada</h2>
<p>La inflación mensual no se suma: se <strong>acumula</strong>. Tres meses de 4 % no son 12 %, sino:</p>
<p class="card">1,04 × 1,04 × 1,04 − 1 = 12,49 %</p>
<p>Los datos oficiales de inflación los publica el INDEC todos los meses. Tomá los meses que pasaron entre tu sueldo anterior y el nuevo.</p>
<h2>Paso 3: compará correctamente</h2>
<p>Tampoco alcanza con restar los porcentajes. La variación real del sueldo se calcula así:</p>
<p class="card">Variación real = (1 + aumento) ÷ (1 + inflación) − 1</p>
<p>Con un aumento del 15 % y una inflación del 12,49 %: 1,15 ÷ 1,1249 − 1 = 2,23 %. Tu sueldo ganó un 2,23 % de poder de compra.</p>
<h2>Ejemplo cuando se pierde</h2>
<p>Si el aumento hubiera sido del 10 % con la misma inflación: 1,10 ÷ 1,1249 − 1 = −2,21 %. Aunque cobres más pesos, podés comprar un 2,21 % menos que antes.</p>
<h2>Cuánto aumento necesitás para empatar</h2>
<p>Para no perder, tu aumento tiene que ser igual a la inflación acumulada. En el ejemplo, 12,49 %. Con la calculadora de <a href="/porcentaje/">aumentos</a> podés ver cuánto debería ser tu nuevo sueldo: $800.000 + 12,49 % = $899.920.</p>
<h2>Consejos</h2>
<ul>
<li>Compará siempre sueldos <strong>brutos con brutos</strong> o <strong>netos con netos</strong>.</li>
<li>No mezcles meses: la inflación tiene que corresponder al mismo período del aumento.</li>
<li>Si cobrás bonos o sumas no remunerativas, calculá con y sin ellos.</li>
</ul>
""",
    },
    {
        "slug": "como-calcular-el-iva",
        "titulo": "Cómo calcular el IVA: sumar, sacar y alícuotas",
        "desc": "Cómo sumarle el IVA a un precio neto, cómo sacar el IVA de un precio final, qué alícuotas existen en Argentina y errores frecuentes al facturar.",
        "tool": ("/porcentaje/", "Usar la calculadora de IVA"),
        "body": """
<p>El IVA (impuesto al valor agregado) es el impuesto que más se paga en Argentina, porque está incluido en casi todo lo que compramos. Saber calcularlo sirve tanto para quien factura como para entender un precio.</p>
<h2>Las alícuotas</h2>
<ul>
<li><strong>21 %</strong>: la alícuota general. Se aplica a la mayoría de los bienes y servicios.</li>
<li><strong>10,5 %</strong>: alícuota reducida para algunos productos y servicios, como ciertos alimentos, la construcción de vivienda y la medicina prepaga, entre otros.</li>
<li><strong>27 %</strong>: para algunos servicios públicos (como luz, gas y telecomunicaciones) cuando el cliente es una empresa o un responsable inscripto.</li>
<li><strong>Exento</strong>: algunos bienes y servicios no pagan IVA, como ciertos servicios educativos o el agua para consumo familiar, según la ley.</li>
</ul>
<h2>Sumar el IVA a un precio neto</h2>
<p class="card">Precio final = Neto × (1 + alícuota ÷ 100)</p>
<p>Un servicio de $50.000 más IVA del 21 % cuesta $60.500. El IVA es de $10.500.</p>
<h2>Sacar el IVA de un precio final</h2>
<p>Acá está el error más común: <strong>no se resta el 21 % al precio final</strong>. Hay que dividir:</p>
<p class="card">Neto = Precio final ÷ (1 + alícuota ÷ 100)</p>
<p>De $60.500 con IVA, el neto es 60.500 ÷ 1,21 = $50.000. Si restaras el 21 % de $60.500, te daría $47.795, que es incorrecto.</p>
<h2>¿Y los monotributistas?</h2>
<p>Los monotributistas no discriminan IVA en sus facturas (emiten factura C) y el impuesto está incluido en la cuota mensual del monotributo. Si comprás a un monotributista, no podés computar ese IVA como crédito fiscal.</p>
<h2>Ver el IVA en los tickets</h2>
<p>Por la ley de transparencia fiscal, los tickets y facturas a consumidores finales muestran cuánto IVA y otros impuestos nacionales están incluidos en el precio. Es una buena forma de ver cuánto de lo que pagás son impuestos.</p>
<p>Hacé tus cuentas en la <a href="/porcentaje/">calculadora de IVA</a>, donde podés elegir cualquier alícuota.</p>
<p class="disclaimer">Información general. Para casos puntuales de facturación, consultá a un contador o el sitio de ARCA.</p>
""",
    },
    {
        "slug": "dolar-para-viajar-brasil-chile-uruguay",
        "titulo": "Viajar a Brasil, Chile o Uruguay: cómo pagar y qué dólar conviene",
        "actualizado": "2026-11-23",
        "desc": "Tarjeta, efectivo o billetera virtual: cómo conviene pagar en las vacaciones de verano en Brasil, Chile y Uruguay, y cómo calcular cuánto te sale en pesos.",
        "tool": ("/monedas/", "Pasar reales, pesos chilenos y uruguayos a pesos"),
        "body": """
<p>Cada verano se repite la misma duda: ¿llevo dólares, pago con tarjeta o uso una billetera? No hay una respuesta única, porque depende de cuánto estén el dólar tarjeta y el MEP ese día. Lo que sí podés hacer es comparar las opciones con números antes de salir.</p>
<h2>Las tres formas de pagar</h2>
<ul>
<li><strong>Tarjeta de crédito argentina.</strong> El consumo se convierte al dólar tarjeta, que es el oficial más impuestos y percepciones. Es cómodo y seguro, pero suele ser la opción más cara si no pagás el resumen con dólares propios.</li>
<li><strong>Tarjeta de débito con dólares propios.</strong> Si tenés dólares en tu caja de ahorro, muchos bancos debitan el gasto directamente de ahí. En general no se aplican las percepciones sobre ese pago, así que el costo real es el precio al que compraste esos dólares (por ejemplo, en el MEP).</li>
<li><strong>Efectivo.</strong> Llevar dólares y cambiarlos allá. En Uruguay se aceptan dólares en muchos comercios; en Brasil y Chile vas a tener que cambiarlos a moneda local, y la casa de cambio se queda con una diferencia.</li>
</ul>
<h2>Billeteras virtuales y QR</h2>
<p>Algunas billeteras y bancos argentinos ya permiten pagar con QR en el exterior, por ejemplo con Pix en Brasil. Antes de viajar, revisá si la tuya lo ofrece, a qué tipo de cambio convierte y si cobra comisión. A veces convierte a un valor cercano al MEP, lo que puede salir más barato que la tarjeta de crédito.</p>
<h2>Cómo comparar en dos minutos</h2>
<ol>
<li>Mirá el precio en moneda local (reales, pesos chilenos o uruguayos).</li>
<li>Pasalo a pesos con nuestro <a href="/monedas/">conversor de monedas</a>.</li>
<li>Compará con el <a href="/dolar/">dólar tarjeta y el MEP de hoy</a>: la diferencia entre los dos te dice cuánto te ahorrás pagando con dólares propios.</li>
</ol>
<h2>Ejemplo</h2>
<p>Una cena de 200 reales en Florianópolis. Si el real equivale a unos 0,18 dólares, son 36 dólares. Con un dólar tarjeta de $1.900 te cuesta unos $68.400; con dólares comprados en el MEP a $1.500, unos $54.000. Son valores de ejemplo: hacé la cuenta con las cotizaciones del día.</p>
<h2>Consejos para el viaje</h2>
<ul>
<li>Si un comercio te ofrece cobrarte en pesos argentinos, decí que no: casi siempre usa un tipo de cambio peor. Pagá en la moneda del país.</li>
<li>Avisá a tu banco que vas a viajar y revisá los límites de compra en el exterior.</li>
<li>Llevá un poco de efectivo en moneda local para gastos chicos, peajes o lugares que no aceptan tarjeta.</li>
</ul>
<p class="disclaimer">Las condiciones de bancos y billeteras cambian seguido. Confirmá con tu entidad antes de viajar.</p>
""",
    },
    {
        "slug": "como-calcular-aumento-de-alquiler",
        "titulo": "Aumento de alquiler: cómo se calcula con IPC o ICL",
        "actualizado": "2026-11-23",
        "desc": "Cómo saber cuánto aumenta tu alquiler según el índice y la frecuencia de tu contrato, con ejemplos y una calculadora que usa la inflación oficial.",
        "tool": ("/alquiler/", "Calcular el aumento de mi alquiler"),
        "body": """
<p>Desde fines de 2023, cuando se derogó la ley de alquileres, el índice y la frecuencia de actualización se pactan libremente en cada contrato. Por eso lo primero es leer tu contrato: ahí dice cada cuántos meses aumenta y con qué índice.</p>
<h2>Los índices más usados</h2>
<ul>
<li><strong>IPC (inflación del INDEC).</strong> Es el más común en los contratos nuevos. El alquiler sube lo mismo que subieron los precios en los meses del período.</li>
<li><strong>ICL (Índice para Contratos de Locación).</strong> Lo publica el Banco Central y se usa en los contratos firmados con la ley anterior (entre julio de 2020 y diciembre de 2023), que se ajustan una vez por año.</li>
<li><strong>Porcentaje fijo.</strong> Algunos contratos fijan un aumento conocido de antemano, por ejemplo 10 % cada cuatro meses.</li>
</ul>
<h2>Cómo se calcula con IPC</h2>
<p>Se acumula la inflación de los meses del período. No se suman los porcentajes: se multiplican.</p>
<p class="card">Nuevo alquiler = Alquiler actual × (1 + IPC mes 1) × (1 + IPC mes 2) × … × (1 + IPC último mes)</p>
<p>Por ejemplo, un alquiler de $500.000 que se actualiza cada tres meses, con inflación de 2 %, 1,8 % y 2,2 %: 500.000 × 1,02 × 1,018 × 1,022 = $530.602. El aumento es de 6,12 %, un poco más que la suma simple (6 %).</p>
<h2>Qué meses se toman</h2>
<p>Normalmente se usan los últimos meses publicados antes del mes del aumento. Como el INDEC publica la inflación a mediados del mes siguiente, a veces el último dato todavía no salió. Muchos contratos aclaran qué hacer en ese caso; si el tuyo no dice nada, lo habitual es usar los últimos meses disponibles.</p>
<p>La <a href="/alquiler/">calculadora de alquiler</a> toma automáticamente la inflación oficial y te muestra qué meses usó.</p>
<h2>Si tu contrato usa ICL</h2>
<p>El aumento anual es el cociente entre el ICL del día de inicio del nuevo año de contrato y el del inicio del anterior. El valor diario del ICL se publica en el sitio del Banco Central.</p>
<p class="disclaimer">Información general. Ante dudas sobre tu contrato, consultá con un abogado o con el colegio de martilleros de tu provincia.</p>
""",
    },
    {
        "slug": "como-actualizar-un-monto-por-inflacion",
        "titulo": "Cómo actualizar un monto por inflación",
        "actualizado": "2026-11-23",
        "desc": "Cómo saber cuánto equivale hoy una plata de hace meses o años usando la inflación oficial del INDEC, con la fórmula y ejemplos.",
        "tool": ("/inflacion/", "Actualizar un monto por inflación"),
        "body": """
<p>¿Cuánto serían hoy los $100.000 que cobrabas hace un año? ¿Una deuda de 2024 vale lo mismo ahora? Para responderlo hay que actualizar el monto por inflación, es decir, ajustarlo por cuánto subieron los precios en el medio.</p>
<h2>La fórmula</h2>
<p>Se multiplica el monto por la inflación de cada mes del período:</p>
<p class="card">Monto actualizado = Monto × (1 + inflación mes 1) × (1 + inflación mes 2) × …</p>
<p>Si los precios subieron 3 % un mes y 2 % el siguiente, $100.000 pasan a ser 100.000 × 1,03 × 1,02 = $105.060.</p>
<h2>Para qué sirve</h2>
<ul>
<li>Saber si tu sueldo de hoy alcanza para lo mismo que hace un año (mirá también la guía sobre <a href="/guias/como-calcular-aumento-de-sueldo-inflacion/">aumento de sueldo e inflación</a>).</li>
<li>Comparar precios de distintos años sin que te engañe la inflación.</li>
<li>Calcular cuánto debería valer una cuota, un alquiler o un presupuesto viejo.</li>
</ul>
<h2>De dónde salen los datos</h2>
<p>Usamos el índice de precios al consumidor (IPC) del INDEC, que se publica cada mes. La <a href="/inflacion/">calculadora de inflación</a> los trae solos: solo elegís el monto y los meses.</p>
<p class="disclaimer">La inflación oficial es un promedio: tus gastos pueden haber subido más o menos según lo que consumas.</p>
""",
    },
    {
        "slug": "cuotas-o-contado-que-conviene",
        "titulo": "¿Cuotas o contado? Cómo saber qué conviene",
        "actualizado": "2026-11-23",
        "desc": "Cómo comparar un precio en cuotas con el precio de contado teniendo en cuenta la inflación, con ejemplos y una calculadora simple.",
        "tool": ("/cuotas/", "Comparar cuotas y contado"),
        "body": """
<p>Con inflación, pagar en cuotas fijas puede convenir aunque el total sea más alto que el precio de contado. La razón es simple: las cuotas de más adelante las pagás con pesos que valen menos.</p>
<h2>La idea</h2>
<p>Para comparar, hay que llevar cada cuota a “pesos de hoy”. Si la inflación es de 2 % por mes, una cuota de $10.000 dentro de un mes equivale a unos $9.804 de hoy, y la del mes siguiente, a $9.612.</p>
<p class="card">Valor de hoy de las cuotas = Cuota ÷ (1 + i) + Cuota ÷ (1 + i)² + … + Cuota ÷ (1 + i)ⁿ</p>
<p>Donde <em>i</em> es la inflación mensual que esperás y <em>n</em> la cantidad de cuotas. Si ese total es menor que el precio de contado, conviene pagar en cuotas.</p>
<h2>Ejemplo</h2>
<p>Una heladera cuesta $900.000 de contado o 6 cuotas de $160.000 (total $960.000). Con una inflación esperada de 2 % mensual, las 6 cuotas valen hoy unos $896.000. Es casi lo mismo que el contado, así que la diferencia es mínima. Si la inflación fuera más alta, las cuotas ganarían; si fuera más baja, convendría el contado.</p>
<h2>Lo que también hay que mirar</h2>
<ul>
<li><strong>Descuento por pago en efectivo o transferencia.</strong> Muchos comercios hacen un 10 % o más. Usá ese precio como “contado”.</li>
<li><strong>Costo financiero total (CFT).</strong> Si las cuotas tienen interés, el CFT figura en la publicidad y en el resumen. Las cuotas “sin interés” igual pueden tener un precio de lista más alto.</li>
<li><strong>Dónde tenés la plata mientras tanto.</strong> Si guardás el contado en una cuenta que rinde, podés usar ese rendimiento mensual en lugar de la inflación.</li>
</ul>
<p>Hacé la cuenta con tus números en la <a href="/cuotas/">calculadora de cuotas o contado</a>.</p>
""",
    },
    {
        "slug": "cuantos-dias-de-vacaciones-me-corresponden",
        "titulo": "Vacaciones: cuántos días te corresponden y cuánto se cobra",
        "actualizado": "2026-11-23",
        "desc": "Cuántos días de vacaciones te tocan según tu antigüedad, cuándo te las tienen que dar y cómo se calcula el pago de las vacaciones en Argentina.",
        "tool": ("/vacaciones/", "Calcular mis vacaciones"),
        "body": """
<p>La Ley de Contrato de Trabajo fija un mínimo de días de vacaciones pagas para quienes trabajan en relación de dependencia. Tu convenio colectivo puede darte más días, nunca menos.</p>
<h2>Cuántos días te tocan</h2>
<table>
<thead><tr><th>Antigüedad al 31 de diciembre</th><th class="num">Días corridos</th></tr></thead>
<tbody>
<tr><td>Hasta 5 años</td><td class="num">14</td></tr>
<tr><td>Más de 5 y hasta 10 años</td><td class="num">21</td></tr>
<tr><td>Más de 10 y hasta 20 años</td><td class="num">28</td></tr>
<tr><td>Más de 20 años</td><td class="num">35</td></tr>
</tbody></table>
<p>Para tener las vacaciones completas tenés que haber trabajado al menos la mitad de los días hábiles del año. Si empezaste hace poco y no llegás, te corresponde un día de vacaciones cada veinte días trabajados.</p>
<h2>Cuándo te las tienen que dar</h2>
<p>El empleador elige la fecha entre el 1 de octubre y el 30 de abril, y te la tiene que avisar por escrito con al menos 45 días de anticipación. Las vacaciones empiezan un lunes o el día hábil siguiente si es feriado.</p>
<h2>Cuánto se cobra</h2>
<p>Si cobrás un sueldo mensual, cada día de vacaciones se paga como el sueldo dividido 25 (no por 30). Por eso en el recibo aparece un “plus vacacional”.</p>
<p class="card">Pago de vacaciones = Sueldo bruto ÷ 25 × Días de vacaciones</p>
<p>Ejemplo: con un sueldo bruto de $1.000.000 y 14 días, cobrás 1.000.000 ÷ 25 × 14 = $560.000 por las vacaciones, en lugar de los $466.667 que corresponderían a esos días con el sueldo normal. Se tienen que pagar al empezar las vacaciones.</p>
<p>Hacé la cuenta con tus datos en la <a href="/vacaciones/">calculadora de vacaciones</a>.</p>
<p class="disclaimer">Información general basada en la Ley de Contrato de Trabajo. Revisá tu convenio colectivo, que puede mejorar estas condiciones.</p>
""",
    },
]
