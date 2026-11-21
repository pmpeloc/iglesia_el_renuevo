# Prompts de imágenes — Unidos a Él

ChatGPT modo Work (GPT 6 Astra), sin imágenes de referencia. Un mensaje por imagen, todas en el mismo chat para que el estilo se mantenga. Salida: JPG 1000×1000 en `img/`.

**Estilo (va al inicio de cada pedido):**
Generá UNA imagen cuadrada (1:1). ESTILO: ilustración vectorial plana y minimalista, formas geométricas simples, sin contornos, sin degradados ni sombras, fondo crema liso. Paleta variada de colores planos y cálidos (terracota, mostaza, azul petróleo, bordó, celeste, naranja, y apenas algo de verde), con negro para pelo y barbas; el verde NO debe ser el color dominante. Personajes de dibujo simple con caras muy expresivas. Encuadre cercano; la escena ocupa todo el lienzo de borde a borde, sin márgenes ni recuadros. Sin texto, sin letras, sin números, sin logos. Sin cruces, aureolas ni velas. Tiene que entenderse de lejos en una pantalla chica: pocos elementos, alto contraste. ESCENA: …

**Personajes fijos (se repite la descripción en cada escena donde aparecen):**
- **Jesús:** barba y pelo castaños, túnica blanca con manto bordó, rostro amable, sin aureola.
- **Pedro:** discípulo del siglo I, robusto, barba negra tupida, túnica azul petróleo.
- **Tomás:** discípulo del siglo I, delgado, barba negra corta, túnica mostaza.
- **Felipe:** discípulo del siglo I, joven, sin barba, pelo negro rizado, túnica terracota.
- **El nene:** de hoy, unos 5 años, pelo negro, pijama celeste.
- **La mamá:** de hoy, pelo negro recogido, remera terracota.
- **El papá:** de hoy, barba negra corta, campera azul petróleo, bolso de viaje mostaza.
- **Los chicos:** de hoy, una nena de 8 con vestido naranja y un nene de 6 con remera celeste.

| Archivo | Diap. | Frase en pantalla | Escena |
|---|---|---|---|
| `01_portada` | 1 | (portada) | Jesús caminando con un brazo sobre el hombro de un hombre de hoy (remera celeste); los dos sonríen. |
| `02_domingo` | 2 | El domingo, cerca | Una familia de hoy (papá, mamá, dos chicos) cantando contenta en un salón de iglesia con sillas. |
| `03_lunes` | 2 | El lunes, solos | Un hombre de hoy solo en la mesa de la cocina, con facturas y una calculadora, la cabeza apoyada en la mano. |
| `04_se_va` | 3 | Jesús se va | Jesús sentado a una mesa baja hablando con la mano levantada; tres discípulos lo escuchan con cara triste. |
| `05_pedro` | 3 | Pedro le va a fallar | Pedro con la mano en el pecho, seguro de sí, frente a Jesús que lo mira con tristeza; al fondo, un gallo sobre un muro. |
| `06_miedo_perderlo` | 3 | Miedo de perderlo | Tres discípulos angustiados; uno le agarra el manto a Jesús, que está de espaldas empezando a irse. |
| `07_mama` | 5 | "¡Mamá!" | Pieza a oscuras, de noche; el nene sentado en la cama, asustado, gritando con la boca abierta; ventana con luna. |
| `08_alguien_venga` | 5 | Que alguien venga | La mamá entrando por la puerta de la pieza a oscuras con la linterna del celular; el nene en la cama estira los brazos hacia ella. |
| `09_mano` | 5 | Ya no tiene miedo | La mamá sentada en la cama agarrándole la mano al nene, que está acostado y tranquilo; la pieza sigue a oscuras, la lámpara apagada. |
| `10_revuelto` | 6 | Revuelto por dentro | Un hombre de hoy con la mano en el pecho y cara de angustia; dentro del pecho se ve un remolino de agua agitada. |
| `11_turbada` | 6 | "Turbada mi alma" | Jesús solo, de rodillas, de noche, con la mano en el pecho y el rostro angustiado. |
| `12_creed` | 6 | "Creed también en mí" | Jesús con la mano sobre su propio pecho, mirando con ternura a dos discípulos que levantan la vista hacia Él. |
| `13_salida` | 7 | Buscamos la salida | Una mujer de hoy, de noche, con el celular en la oreja, una calculadora en la otra mano y papeles sobre la mesa. |
| `14_final` | 7 | Jesús, para el final | Un hombre de hoy agotado, rodeado de papeles arrugados, que recién ahora junta las manos para orar; un reloj de pared marca muy tarde (sin números). |
| `15_vuelve_papa` | 10 | Vuelve papá | El papá llegando a la puerta de casa con el bolso al hombro; los chicos corren hacia él con los brazos abiertos. |
| `16_que_me_trajiste` | 10 | "¿Qué me trajiste?" | Los chicos arrodillados en el piso revisando el bolso abierto, entusiasmados; del papá solo se ven las piernas detrás. |
| `17_brazos_abiertos` | 10 | Él volvió por ellos | El papá de pie con los brazos abiertos y sonrisa triste; los chicos, de espaldas a él, siguen con el bolso. |
| `18_lugar` | 11 | Hay un lugar | Una casa grande y cálida con muchas ventanas iluminadas y la puerta abierta, bajo un cielo de atardecer. |
| `19_tomare` | 11 | "Os tomaré a mí mismo" | Jesús abrazando a un discípulo y acercándolo a su lado; el discípulo sonríe con alivio. |
| `20_camino` | 11 | "Yo soy el camino" | Tomás con un mapa desplegado y cara de confundido; Jesús, frente a él, se señala a sí mismo con la mano en el pecho. |
| `21_lo_que_da` | 12 | Lo que da, más que a Él | Una persona de hoy abrazando feliz una caja de regalo, de espaldas a Jesús, que la espera detrás con los brazos abiertos. |
| `22_lista` | 12 | Una lista de pedidos | Una persona de hoy de rodillas orando, leyendo una lista de papel larguísima que llega hasta el piso y se enrosca (el papel sin letras, solo rayitas). |
| `23_enfriamos` | 12 | Nos enfriamos | Una persona de hoy de brazos cruzados y ceño fruncido, dándose vuelta y alejándose; a sus pies, una caja de regalo vacía. |
| `24_ordenamos` | 15 | Ordenamos todo | Una familia de hoy ordenando el comedor apurada: uno barre, otra pone vasos lindos sobre un mantel. |
| `25_puerta` | 15 | La puerta cerrada | Una mujer de hoy sonriendo hacia adelante mientras con la mano atrás cierra una puerta de la que asoma ropa y desorden. |
| `26_vive_en_casa` | 15 | El que vive en casa | Cocina a la mañana: una familia de hoy en pijama desayunando en una mesa con tazas y migas, despeinados y contentos. |
| `27_morada` | 16 | Donde uno se queda a vivir | Un hombre de hoy dentro de una casa sencilla colgando su abrigo en el perchero junto a la puerta, con una valija abierta y vacía al lado. |
| `28_dos_casas` | 16 | Su casa y la nuestra | Arriba, una casa grande y luminosa; abajo, una casita de barrio; un camino las une y Jesús baja caminando hacia la casita. |
| `29_palabra` | 16 | "Mi palabra guardará" | Una mujer de hoy abrazando contra el pecho un libro grande abierto (sin letras), con los ojos cerrados y sonrisa serena. |
| `30_visita_jesus` | 17 | Como a una visita | Jesús sentado derecho en el sillón de un living de hoy, con una taza en la mano; la familia, muy formal, sentada enfrente. |
| `31_felipe` | 17 | "¿Tanto tiempo, Felipe?" | Felipe mirando hacia arriba, buscando algo en el cielo con la mano sobre los ojos; a su lado, Jesús le toca el hombro. |

La diapositiva 19 (Conclusión) reutiliza `09_mano`, `17_brazos_abiertos` y `26_vive_en_casa`.
