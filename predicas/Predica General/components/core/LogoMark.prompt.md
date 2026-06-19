The brand "R" mark. The `bare` variant is the discreet corner mark required top-right on every slide.

```jsx
<LogoMark variant="bare" size={84} basePath="../assets"
  style={{ position: "absolute", top: 48, right: 56 }} />
```

- `bare` → top-right corner of slides (transparent, green). `green` / `black` → circular badges for portada/closing.
- Set `basePath` to the relative path from the current page to `assets/`.
- Keep the corner mark small and out of the way — it is a watermark, not a focal point.
