import React from "react";

/**
 * Small uppercase wide-tracked eyebrow label above a title — point number,
 * series name, or meeting tag.
 */
export interface KickerProps {
  children: React.ReactNode;
  /** Label color. Default var(--green-deep). Use var(--green) on ink. */
  color?: string;
  style?: React.CSSProperties;
}

export function Kicker(props: KickerProps): JSX.Element;
