Deep-ink box with cream text — the application-slide container that lifts a directive off the cream background.

```jsx
<BlackCard>
  <Kicker color="var(--green)">Aplicación</Kicker>
  <p style={{ fontFamily: "var(--font-body)", fontWeight: 800, fontSize: "var(--fs-h3)", marginTop: 16 }}>
    Esta semana, <Highlight>perdona a alguien</Highlight> de verdad.
  </p>
</BlackCard>
```

- The only lifted surface in the system — it carries `--shadow-card`. Everything else is flat.
- Cream text inside; use `Highlight` and a green `Kicker` for accents.
- One box per slide, centered with generous slide margins around it.
