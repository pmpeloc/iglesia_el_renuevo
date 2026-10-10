# Ref Video Kit: preset de Addictive Drums 2 a partir de un video

Proyecto del 22-09-2026. Objetivo: armar un preset de AD2 que suene lo más parecido posible
a la batería de dos videos de celular (`referencias/`).

## Qué hay en cada carpeta

| Carpeta | Contenido |
|---|---|
| `preset/` | **`Ref Video Kit UP.AD2Preset`**: preset final (AD2 2.5.2, ADpak *United Pop*). También la versión *Modern Heavy*, que solo funciona con AD2 2.8.9. |
| `renders/` | `demo_final_UnitedPop_2.5.2.wav` (demo del preset final), la demo Modern Heavy y los renders de las variantes probadas (`var_up_*`). |
| `referencias/` | Los dos videos originales (`ref.mp4`, `ref2.mp4`) y el audio extraído. |
| `pipeline/` | Scripts para controlar AD2 desde REAPER, medir, comparar y construir el preset, más los inventarios de piezas medidas. |
| `capturas/` | Capturas del kit final en AD2. |

## Instalar el preset

Copiar `preset/Ref Video Kit UP.AD2Preset` a
`C:\Users\pmpel\OneDrive\Documentos\Addictive Drums 2\00100\` (ya está ahí) y cargarlo desde AD2.
**Importante:** no crear dos presets de usuario con el contenido idéntico (ver problemas, punto 4).

## Resultado final

La referencia medida fue `ref2` (28 s; solo batería a partir del segundo 6,2):
caja con fundamental de ~167 Hz, bombo de ~48–51 Hz y un tom de ~130–140 Hz.

| Pieza | KitPiece ID | Ajustes |
|---|---|---|
| Bombo | 130101 | EQ Hi2 +0.7 (más ataque) |
| Caja | 130201 (Ludwig Nickel/Brass 14x6.5) | Pitch −1,6 semitonos (`Pitch_Course` 0.433), EQ medios recortados (0.3 en freq 0.4) |
| Hi-hat | 130301 | — |
| Toms | 130401 / 130501 / 130601 | — |
| Crashes | 130901 / 130903 | — |
| Ride | 131001 | — |

Todas las piezas tienen OH 0.5 y Room 0.35. Los slots que no se usan están vacíos (ID 0).

## El proceso

1. **Analizar la referencia**: se extrajo el audio de los videos. `hits.py` detecta los golpes
   y los clasifica (bombo, caja, tom o platillo). `measure.py` calcula por golpe la fundamental (f0),
   el centroide espectral, la energía por bandas y el tiempo de decaimiento.
2. **Controlar AD2 sin interfaz**: REAPER corre `server.lua`, un servidor que lee comandos desde
   `cmd.txt` (`setchunk`, `dump`, `eval`, `render`). `rcmd.sh` envía un comando y espera la
   respuesta. `dismiss.ps1` cierra automáticamente los diálogos que bloquean REAPER.
3. **Editar el estado del plugin**: `adstate.py` lee y escribe el estado de AD2 dentro del chunk
   de REAPER. Así se cambia cualquier parámetro sin tocar la interfaz.
4. **Inventario de piezas**: `probe_sweep.py` / `probe_ids.py` cargan cada kit piece en un slot,
   renderizan un golpe con todo el procesamiento apagado y lo miden (`inventory_*.txt`).
5. **Ranking**: `rank.py` / `rank_inv.py` calculan una distancia contra la referencia
   (pitch con peso 3, brillo, decaimiento y bandas) y ordenan las piezas candidatas.
6. **Ajuste fino**: `variant.py` renderiza una variante con parámetros dados. `tune_*.py` barren
   el pitch y el EQ de la caja y el bombo, y eligen la variante con menor distancia.
7. **Construir y guardar**: `build_final.py` arma el estado final. El preset se guardó
   **desde la interfaz de AD2** (botón Save) para que AD2 lo registre bien.

### Cómo reutilizar el pipeline

Requisitos: REAPER, AD2 VST3 y `uv` (Python 3.12 con numpy/librosa).

```bash
# 1. En REAPER: Actions > Load ReaScript > pipeline/server.lua (queda escuchando)
# 2. En otra terminal, cerrar diálogos automáticamente:
powershell -File pipeline/dismiss.ps1 -minutes 60
# 3. Probar piezas de caja (slot SNAR, nota 38, categoría 02, paks 13 y 17, hasta 6 por pak):
cd pipeline
uv run --python 3.12 --with numpy,scipy,librosa python probe_sweep.py SNAR 38 02 13,17 6
# 4. Rankear contra los golpes de caja de ref2.wav (tiempos en segundos):
uv run --python 3.12 --with numpy,scipy,librosa python rank_inv.py SNAR 7.40,7.98,10.37,12.72
```

`chunk_252e.txt` es el estado base que usan todos los scripts. Para otro video: reemplazar
`ref2.wav`, sacar los tiempos de golpe con `hits.py` y repetir desde el paso 3.

## Referencia técnica del estado de AD2

- AD2 no expone parámetros VST3 útiles. Todo está en el *state chunk*: pares `clave\0valor\0`
  después de `COTTAD2StateVersion`, más un sufijo JUCE.
- Claves: `Sampler_<SLOT>_*` (KitPieceSelection, Pitch_Enable, Pitch_Course, Level, OH_Level,
  Room_Level, AmpEnv_*) y `FX_<SLOT>/*` (EQ_*, MultiFX*, EnableFX).
  **`Sampler_X_EnvFiltersEnable` es el interruptor maestro**: si vale 0, pitch y envolvente no hacen nada.
- `Pitch_Course`: 0..1 equivale a −12..+12 semitonos (0.5 = sin cambio).
- **KitPieceSelection = PPTTNN**: PP = número de ADpak − 1050; TT = categoría (01 bombo, 02 caja,
  03 hihat, 04–08 toms según el pak, 09 crash, 10 ride); NN = índice. 0 = vacío.
- Paks de la librería 2.5.2 con cajas: 1, 2, 4 (Black Oyster), 5 (Blue Oyster), 6–10, 12,
  13 (United Pop), 14–16, 17 (Vintage Dead). Los paks 11 y 18 en adelante no suenan.
- Mapa MIDI: bombo 36, caja 38, hihat cerrado 49, tom1 71, tom2 69, tom3 67, ride 60,
  crash1 77, crash2 79.
- Los presets de usuario (`.AD2Preset`) son tablas Lua en texto plano:
  `AD2Sampler.X` ↔ `Sampler_X_*` y `AD2Channels.X` ↔ `FX_X/*`.

## Problemas encontrados y soluciones

1. **Dos versiones de AD2 mezcladas.** La instalación oficial 2.8.9 solo tiene 3 ADpaks con licencia.
   La librería de `C:\Addictive Drums 2` (22 paks) es la 2.5.2 y es incompatible con el binario 2.8.9.
   Se volvió al setup standalone 2.5.2. Los backups de `config.txt` están como `*.bak_libraryplacer`.
   Por eso el preset se rehízo con piezas *United Pop* (13xxxx). La versión Modern Heavy (18xxxx)
   quedó guardada aparte.
2. **El standalone se cerraba al iniciar con ASIO4ALL** (fallaba al enumerar dispositivos; había un
   parlante Bluetooth conectado). Solución: usar "Windows Audio". Backups en
   `AppData\Roaming\Addictive Drums 2\Settings` (`.bak_asio4all` / `.bak_windowsaudio`).
3. **REAPER cargaba el VST3 2.8.9.** Para usar el 2.5.2: en `REAPER.ini`, poner `vstpath64` en
   `C:\Program Files\Common Files\VST3\XLN Audio` y borrar las líneas de AD2 de
   `reaper-vstplugins64.ini` (backups `.bak_20260922`; después se restauró el original).
4. **Los presets borrados volvían y aparecían copias "conflicted".** Había dos causas:
   - AD2 deduplica los presets idénticos: escribe `Meta.Duplicate = "<otro>.AD2Preset ..."` y al
     cargar abre el *otro* archivo, regenerándolo si no existe. Se quitó esa línea y se actualizó
     el hash en `AD2preset.AD2PresetList`.
   - **XLN Cloud Sync** vuelve a bajar los presets de la nube y los trata como la versión válida.
     Solución: se renombró el ejecutable a `XLN Cloud Sync.exe.disabled_20260922` en
     `C:\ProgramData\XLN Audio\XLN Cloud Sync\App\XLN Cloud Sync\prg\` (script `disable_cloudsync.ps1`).
     Para reactivarlo, devolverle el nombre original, pero la nube todavía tiene los presets malos.
5. **Editar un `.AD2Preset` a mano genera conflictos.** Conviene guardar siempre desde la interfaz de AD2.

Los archivos apartados durante la limpieza están en `Downloads\AD2 presets apartados\`.
