import React from "react";

/**
 * BlackCard — the "caja de aplicación": a deep-ink box with cream text used
 * on application slides to set a directive apart from the cream background.
 */
export function BlackCard({
  children,
  style = {},
  ...rest
}) {
  return (
    <div
      style={{
        background: "var(--ink)",
        color: "var(--text-on-ink)",
        borderRadius: "var(--radius-md)",
        padding: "var(--space-6)",
        boxShadow: "var(--shadow-card)",
        fontFamily: "var(--font-body)",
        ...style,
      }}
      {...rest}
    >
      {children}
    </div>
  );
}
