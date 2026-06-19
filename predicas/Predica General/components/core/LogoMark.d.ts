import React from "react";

/**
 * The El Renuevo "R" mark. The bare variant is the discreet top-right corner
 * mark used on every slide.
 */
export interface LogoMarkProps {
  /** "bare" (corner mark), "green" (green circle), "black" (black circle). */
  variant?: "bare" | "green" | "black";
  /** Rendered height in px. Default 96. */
  size?: number;
  /** Path to the assets folder relative to the host page. Default "assets". */
  basePath?: string;
  alt?: string;
  style?: React.CSSProperties;
}

export function LogoMark(props: LogoMarkProps): JSX.Element;
