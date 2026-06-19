import React from "react";

/**
 * ScriptureBadge — reference chip for a Bible verse ("2 Corintios 5:17").
 * solid = green pill on ink text; outline = green outline, transparent fill.
 */
export function ScriptureBadge({
  children,
  variant = "solid",
  style = {},
  ...rest
}) {
  const solid = variant === "solid";
  return (
    <span
      style={{
        display: "inline-block",
        fontFamily: "var(--font-body)",
        fontWeight: 700,
        textTransform: "uppercase",
        letterSpacing: "0.16em",
        fontSize: "var(--fs-small)",
        lineHeight: 1,
        padding: "0.5em 1em",
        borderRadius: "var(--radius-pill)",
        background: solid ? "var(--green)" : "transparent",
        color: solid ? "var(--ink)" : "var(--green)",
        border: solid ? "var(--border-1) solid var(--green)" : "var(--border-1) solid var(--green)",
        ...style,
      }}
      {...rest}
    >
      {children}
    </span>
  );
}
