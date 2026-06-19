# El Renuevo · Sistema de Diseño (Predica General)

A design system for the preaching slides of **Iglesia El Renuevo (MCyM)** — the
*Reunión General* meetings (Thursdays & Sundays). The look is modern, high-contrast,
and bold: a warm **cream** canvas, **deep-ink** black, and a single **lime-green**
accent, set in heavy condensed display type with a signature green-marker highlight.

> Everything here is in **Spanish** — copy, scripture, labels. Keep it that way.

## Sources provided
- Brand logos (uploaded PNGs), now in `assets/`:
  - `logo-full-on-black.png` — full lockup, white/green mark + wordmark on black (orig. `LOGO-EL RENUEVO-PERFIL-2.png`)
  - `logo-full-on-light.png` — full lockup on light (orig. `LOGO-EL RENUEVO-PERFIL-3.png`)
  - `mark-green-circle.png` — "R" mark, white on green circle (orig. `R-1`)
  - `mark-black-circle.png` — "R" mark, green on black circle (orig. `R-3`)
  - `mark-green.png` — bare green "R" mark, transparent (orig. `R-4`) → **the corner mark**
- Palette & type direction supplied by the brand owner (see below). No codebase or
  Figma was provided — the system is built from the logos + the written brief.

---

## CONTENT FUNDAMENTALS — how copy is written

- **Language:** Spanish, always. Reina-Valera style scripture quotations.
- **Voice:** warm, direct, pastoral. Speaks to the congregation as **"tú"** (informal
  singular) and the collective **"nosotros"** — never the formal "usted." Imperatives
  are common in applications: *"Vuelve", "Acuérdate", "Decídelo, agéndalo y preséntate."*
- **Tone:** convicting but hopeful; invites action, not guilt. Short, punchy lines over
  long paragraphs. A slide makes **one** point.
- **Casing:** Titles in Anton are **UPPERCASE**. Kickers/eyebrows are uppercase, wide-tracked.
  Body and quotes are sentence case. Scripture references are uppercase in pills (*APOCALIPSIS 2:4*).
- **Highlight discipline:** the green marker emphasizes a **short phrase** (1–4 words) —
  the heart of the statement — never a whole sentence.
- **Scripture:** quoted in Playfair Display *italic*; the reference sits in a green pill or
  green uppercase label beneath it. Quote marks are curly “ ”.
- **No emoji.** No exclamation-spam. Numerals for points ("01", "02"). Meeting signatures
  read *"Iglesia El Renuevo · MCyM · Reunión General."*
- **Examples:**
  - Portada title: *VOLVER AL **PRIMER AMOR*** (green marker on "primer amor")
  - Application: *Esta semana, **vuelve a lo primero**: 15 minutos a solas con Él, cada día.*
  - Closing frame: *"Acuérdate, pues, de dónde has caído, y arrepiéntete…"*

---

## VISUAL FOUNDATIONS

**Colors.** Three only. `--cream #F7F1E8` is the default canvas; `--ink #1A1A1A` is text
and the portada/closing/application surfaces; `--green #5DBE2C` is THE accent — used as the
highlight marker, point numbers, kickers, pills and the corner mark. Green has press
(`#4A9E22`) and hover (`#6FD635`) steps. Green is never used for long runs of body text.
High contrast is the whole point: cream↔ink, with green as the spark.

**Type.** Four roles:
- **Anton** — huge UPPERCASE display (portada hero, point titles). Tracking ~0.01em, line-height 0.9.
- **Montserrat 800** — highlighted statements; the host text for the green marker.
- **Montserrat 400** — body copy, lists, captions; line-height 1.45 for legibility at distance.
- **Playfair Display *italic*** — scripture and framing lines only.
Kickers are Montserrat 700, uppercase, letter-spacing 0.22em. Type scale is tuned for the
1920×1080 canvas (display up to 200px; body 32px; nothing below 24px).

**Backgrounds.** Flat solid fills — cream or ink. **No gradients, no photographic textures,
no patterns.** Imagery lives in dedicated containers (the subpunto right column), framed as a
hard-edged block, never bled behind text. Where no photo exists, a black placeholder block
labelled *IMAGEN* with a faint watermark mark is used.

**Layout.** Fixed 1920×1080 canvas, safe margins 120px (x) / 96px (y). The bare green corner
mark (`mark-green.png`) sits **top-right at ~80–96px** on every slide — discreet, watermark-like.
Slide archetypes: **Portada** (ink, centered-left hero), **Título de punto** (cream, giant
green number + Anton title), **Subpunto** (cream, two columns: text left / image right),
**Aplicación** (cream, centered black box), **Cierre** (ink, centered mark + italic frame).

**Shape & depth.** The brand is hard-edged. Radii are minimal: 0 on most surfaces, 6px on
small chips, **14px only on the black application box** — which is the *single* lifted surface
and carries the one drop shadow in the system (`--shadow-card`, soft ink at 22%). Everything
else is flat with no shadow. Rules/underlines are heavy (4px ink). Pills use full radius for
scripture chips only.

**Highlight marker.** `background: var(--green)`, ink text, padding `0.04em 0.12em`,
`box-decoration-break: clone` so it wraps cleanly across lines. ~3px corner softening.

**Motion.** Restrained. Slide changes are simple cuts or a quick fade; no bounce, no
parallax, no infinite loops. Entrances (if any) fade/translate in once. Respect
`prefers-reduced-motion`.

**Interaction (for any UI built with this system).** Hover = lighten to `--green-bright`;
press = darken to `--green-deep`. No scale-on-hover on slide content. Buttons/controls are
green pills with ink text.

**Imagery vibe.** When real photos are added they should read warm and human (congregation,
hands, nature/renewal motifs that echo the leaf-and-R mark), cropped hard into their block.

---

## ICONOGRAPHY

The brand is **typographic, not iconographic.** There is no icon set in the source material
and none is invented here.
- **No emoji**, ever.
- List bullets are small **green squares** (4px radius) — a brand device, not icon glyphs.
- Separators use a thin middot **·** between meeting labels.
- The only "iconography" is the **"R" mark** itself (leaf + R), supplied in three forms in
  `assets/` (bare / green circle / black circle). Do not redraw it.
- If a future surface genuinely needs UI icons (e.g. a control panel), use **Lucide**
  (CDN, 2px stroke) to match the clean, modern weight — and flag it as an addition, since it
  is **not** part of the original brand. No icon font is bundled.

---

## INDEX — what's in this system

**Root**
- `styles.css` — the entry point consumers link (imports the token + font closure).
- `readme.md` — this guide. `SKILL.md` — portable Agent-Skill wrapper.

**`tokens/`** — `fonts.css` (Anton, Montserrat, Playfair via Google Fonts), `colors.css`,
`typography.css`, `spacing.css` (spacing, radius, shadow).

**`assets/`** — logos & "R" marks (see Sources above).

**`components/core/`** — reusable React primitives (namespace `window.PredicaGeneral_ebc788`):
- `Highlight` — green marker for key phrases.
- `Kicker` — uppercase wide-tracked eyebrow label.
- `ScriptureBadge` — verse-reference pill (solid / outline).
- `BlackCard` — the "caja de aplicación" black box.
- `LogoMark` — the "R" mark (bare corner / green / black).

**`slides/`** — sample slides + an interactive deck:
- `portada.html`, `punto.html`, `subpunto.html`, `aplicacion.html`, `cierre.html`
- `index.html` — navigable 5-slide deck (← → keys), also a Starting Point.

**`guidelines/`** — foundation specimen cards (Colors, Type, Spacing, Brand) for the
Design System tab.

---

### Notes & caveats
- **Fonts** are loaded from **Google Fonts** (Anton, Montserrat, Playfair Display) — exact
  matches to the brief, no substitution. If the church has licensed/branded font files,
  drop them in `tokens/` and swap the `@import` for local `@font-face` rules.
- No photographic assets were provided, so image areas use labelled placeholders.
