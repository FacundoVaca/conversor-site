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
        "titulo": "Aguinaldo: cuándo se cobra y cómo se calcula",
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
]
