import React from "react";

declare module "react";

/**
 * The signature El Renuevo marker — Montserrat ExtraBold text on a lime-green
 * block, used to emphasize key words inside a statement.
 */
export interface HighlightProps {
  children: React.ReactNode;
  /** Marker background. Default var(--green). */
  color?: string;
  /** Text color on the marker. Default var(--ink). */
  textColor?: string;
  style?: React.CSSProperties;
}

export function Highlight(props: HighlightProps): JSX.Element;
