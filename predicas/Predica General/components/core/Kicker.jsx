import React from "react";

/**
 * Kicker — small uppercase, wide-tracked label. Sits above titles to mark
 * the point number, series, or meeting ("PUNTO 01", "REUNIÓN GENERAL").
 */
export function Kicker({
  children,
  color = "var(--green-deep)",
  style = {},
  ...rest
}) {
  return (
    <div
      style={{
        fontFamily: "var(--font-body)",
        fontWeight: 700,
        textTransform: "uppercase",
        letterSpacing: "var(--tracking-kicker)",
        fontSize: "var(--fs-kicker)",
        lineHeight: 1,
        color,
        ...style,
      }}
      {...rest}
    >
      {children}
    </div>
  );
}
