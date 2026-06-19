import React from "react";

/**
 * Highlight — the signature El Renuevo marker. Montserrat ExtraBold text
 * sitting on a lime-green block. Wraps inline inside a larger statement.
 */
export function Highlight({
  children,
  color = "var(--green)",
  textColor = "var(--ink)",
  style = {},
  ...rest
}) {
  return (
    <span
      style={{
        background: color,
        color: textColor,
        fontFamily: "var(--font-body)",
        fontWeight: 800,
        padding: "var(--highlight-pad-y) var(--highlight-pad-x)",
        borderRadius: "3px",
        boxDecorationBreak: "clone",
        WebkitBoxDecorationBreak: "clone",
        ...style,
      }}
      {...rest}
    >
      {children}
    </span>
  );
}
