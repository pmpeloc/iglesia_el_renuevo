import React from "react";

/**
 * LogoMark — the El Renuevo "R" mark. `bare` is the corner mark that lives
 * top-right on every slide; `green` / `black` are the circular badges.
 * Point `basePath` at wherever the assets folder sits relative to the page.
 */
export function LogoMark({
  variant = "bare",
  size = 96,
  basePath = "assets",
  alt = "Iglesia El Renuevo",
  style = {},
  ...rest
}) {
  const file =
    {
      bare: "mark-green.png",
      green: "mark-green-circle.png",
      black: "mark-black-circle.png",
    }[variant] || "mark-green.png";
  return (
    <img
      src={`${basePath}/${file}`}
      alt={alt}
      style={{ height: size, width: "auto", display: "block", ...style }}
      {...rest}
    />
  );
}
