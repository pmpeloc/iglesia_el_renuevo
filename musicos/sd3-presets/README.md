# Presets de Superior Drummer 3

## Dónde van los presets de usuario
`Documentos\Toontrack\Superior3\PresetsEZX\<librería>\S3Presets\<nombre>` (sin extensión).
SD3 muestra solo los de la librería elegida en el menú de librerías: *User Presets*, después *Rescan User Presets*.

## Worship Fa Music (EZ2 Modern), 23-09-2026
El original (`Downloads\Worship Fa Music`) necesita la librería **Core de SD3**, que no está instalada
(en esta PC solo están EZdrummer 2 Modern/Vintage, SD3 Electronic y SD3 Percussion).
Ya quedó copiado en la carpeta `SL-SUPERIOR_DRUMMER_3\S3Presets`, así que aparecerá cuando se instale la Core.

`port_preset.py` genera la versión para EZdrummer 2 Modern:
- **Base:** el preset "Modern Kit" (piezas, pads y micrófonos válidos para esa librería).
- **Se copia del original:** los canales del mixer (EQ/compresión, volúmenes, sends), todos los buses
  (Kicks, Drum, Tons, PLATE) y el ride afinado 2 semitonos abajo (pitch 0.8928).
- **Mapeo de canales:** Kick In → Kick, Kick Out → KickExt, Tom2 → Toms, OH Beyer → Oh, Room R88 → Amb.
- **No se traslada:** el bombo electrónico KD312 que iba en el lugar del Tom1, el Tom3 vacío,
  el micrófono Kick Sub, los OH Sanken y los micrófonos de sala adicionales (esos no existen en EZ2 Modern).

```bash
uv run --no-project python port_preset.py "<original>" "<preset base de la librería destino>" "<salida>" "<nombre>"
```
