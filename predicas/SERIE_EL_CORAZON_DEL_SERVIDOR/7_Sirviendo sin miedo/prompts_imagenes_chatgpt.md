# Prompts de imágenes — Sirviendo sin miedo

ChatGPT modo Work (GPT 6 Astra), sin imágenes de referencia. Un mensaje por imagen, todas en el mismo chat para que el estilo se mantenga. Salida: JPG 1000×1000 en `img/`.

**Estilo (va al inicio de cada pedido):**
Generá UNA imagen cuadrada (1:1). ESTILO: ilustración vectorial plana y minimalista, formas geométricas simples, sin contornos, sin degradados ni sombras, fondo crema liso. Paleta variada de colores planos y cálidos (terracota, mostaza, azul petróleo, bordó, celeste, naranja, y apenas algo de verde), con negro para pelo y barbas; el verde NO debe ser el color dominante. Personajes de dibujo simple con caras muy expresivas. Encuadre cercano; la escena ocupa todo el lienzo de borde a borde, sin márgenes ni recuadros. Sin texto, sin letras, sin números, sin logos. Sin cruces, aureolas ni velas. Tiene que entenderse de lejos en una pantalla chica: pocos elementos, alto contraste. ESCENA: …

**Personajes fijos (se repite la descripción en cada escena donde aparecen):**
- **El siervo:** hombre joven del siglo I en Medio Oriente, barba negra corta, pelo negro rizado, vincha mostaza, túnica terracota.
- **Su señor:** hombre mayor de barba gris, turbante bordó, túnica azul petróleo con manto mostaza, aspecto de hombre rico.
- **Jesús:** barba y pelo castaños, túnica blanca con manto bordó, rostro amable, sin aureola.
- **El adolescente:** de hoy, remera celeste, pelo castaño, ropa moderna.

| Archivo | Diap. | Frase en pantalla | Escena |
|---|---|---|---|
| `01_portada` | 1 | (portada) | El siervo abrazando una bolsa de monedas con miedo; detrás, la sombra enorme de un hombre con turbante. |
| `02_mirada` | 2 | La mirada | Salón de iglesia de hoy; el adolescente sentado; dos adultos orando de rodillas lo miran de reojo. |
| `03_reto` | 2 | El reto | Un adulto de ceño fruncido le señala una escoba al adolescente. |
| `04_burla` | 2 | La burla | El adolescente recién levantado, con una manta; dos adultos con un libro bajo el brazo se ríen de él. |
| `05_dos_servidores` | 3 | Para ganar… o para que no nos castiguen | Dos personas acomodando sillas: una sonríe hacia unas manos que aplauden; la otra mira con miedo por encima del hombro. |
| `06_jesus_ensena` | 3 | Una parábola para los que sirven | Jesús sentado en una piedra enseñando a cuatro discípulos. |
| `07_entrego` | 5 | Les entregó sus bienes | El señor pone una bolsa grande de monedas en las manos del siervo. |
| `08_capacidad` | 5 | Conforme a su capacidad | Tres siervos con bolsas de distinto tamaño, los tres tranquilos. |
| `09_gozo` | 5 | Entra en el gozo de tu señor | El señor con los brazos abiertos en la puerta de una fiesta, invitando a pasar a un siervo. |
| `10_duro` | 6 | Hombre duro | El siervo preocupado; en una nube de pensamiento imagina a su señor enorme, de ceño fruncido. |
| `11_cavando` | 6 | Tuve miedo y escondí | El siervo cavando un pozo para esconder la bolsa, mirando por encima del hombro. |
| `12_lo_tuyo` | 6 | Aquí tienes lo que es tuyo | El siervo, con el brazo estirado y desde lejos, le devuelve al señor la bolsa sucia de tierra. |
| `13_propia_boca` | 7 | Por tu propia boca | El señor, tranquilo, señala la boca del siervo, que se la tapa con la mano. |
| `14_banco` | 7 | Al menos, el banco | Mesa de cambista con monedas y balanza; un banquero esperando; nadie se acerca. |
| `15_no_excusa` | 7 | El miedo explica, pero no excusa | El siervo de rodillas con la bolsa sucia en el suelo; el señor de pie lo mira serio. |
| `16_ventana` | 10 | ¿Qué Señor se ve a través nuestro? | Ventana con el vidrio sucio; por un círculo limpio se ve un día de sol. Sin personas. |
| `17_criado_ajeno` | 11 | El criado es ajeno | Un siervo frente a su señor; un tercero se mete desde el costado señalándolo. |
| `18_silla` | 11 | La silla del Señor | Un hombre con una lista, sentándose en un trono que le queda enorme. |
| `19_cambio_senor` | 11 | Le cambiamos de señor | El siervo barriendo con los ojos puestos en un hombre que lo vigila; al fondo, pequeño, su señor. |
| `20_dureza` | 12 | Con dureza | Un pastor con la vara levantada y tres ovejas asustadas. |
| `21_egipto` | 12 | Como en Egipto | Un capataz egipcio con látigo y dos esclavos cargando ladrillos. |
| `22_oveja` | 12 | La débil, la enferma, la quebrada | Una oveja sola con la pata vendada; al fondo, el rebaño. |
| `23_miramos_cristo` | 16 | Miramos a Cristo | Una persona de espaldas a un dedo acusador, mirando con alivio a Jesús. |
| `24_manso` | 16 | Manso y humilde | Jesús con los brazos abiertos recibiendo a tres trabajadores cansados y cargados. |
| `25_yugo` | 16 | Mi yugo es fácil | Jesús y un hombre caminando bajo un mismo yugo liviano. |
| `26_otra_vez` | 17 | Otra vez en temor | Un hombre libre, con cadenas rotas a los pies, mirando hacia una celda abierta. |
| `27_casa_suya` | 17 | La casa es suya | Dos jóvenes en la misma casa: uno barre con miedo; el otro riega una planta, tranquilo. |
| `28_todo_tuyo` | 17 | Todas mis cosas son tuyas | Un padre anciano abraza a su hijo mayor enojado y le muestra la casa y el campo. |
| `29_castigo` | 18 | El temor lleva en sí castigo | Una persona encogida, con los ojos apretados, esperando un reto; no hay nadie. |
| `30_amo_primero` | 18 | Él nos amó primero | Un padre abraza fuerte a su hijo; una sombra oscura queda afuera, alejándose. |
| `31_dos_temores` | 18 | Un temor que acerca, un miedo que esconde | Frente a una luz cálida: una persona se acerca agradecida; otra se esconde detrás de un árbol. |
| `32_escondido` | 21 | Tuve miedo y me escondí | Un hombre escondido entre arbustos; solo se le ve la cara asustada. |
| `33_donde_estas` | 21 | ¿Dónde estás tú? | Un rayo de luz entra entre los árboles hasta el arbusto donde asoma el hombre. Sin figura de Dios. |
| `34_desenterrar` | 21 | A tiempo de desenterrar | Dos manos sacando del pozo la bolsa de monedas cubierta de tierra. |
