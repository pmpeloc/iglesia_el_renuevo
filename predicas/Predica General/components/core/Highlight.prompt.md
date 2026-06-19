Inline lime-green marker for emphasizing the key words of a statement — the brand's most recognizable type treatment.

```jsx
<h1 style={{ fontFamily: "var(--font-body)", fontWeight: 800, fontSize: "var(--fs-h1)", color: "var(--ink)" }}>
  No es religión, es <Highlight>una relación</Highlight>
</h1>
```

- Always wraps a SHORT phrase (1–4 words), never a whole sentence.
- Use on cream backgrounds. On ink, pass `textColor="var(--ink)"` (default) — the green block keeps contrast.
- Pair with Montserrat ExtraBold host text so weights match.
