import React from "react";

/**
 * Pill chip for a scripture reference. Solid green or green outline.
 */
export interface ScriptureBadgeProps {
  children: React.ReactNode;
  /** "solid" (green fill) or "outline" (transparent). Default "solid". */
  variant?: "solid" | "outline";
  style?: React.CSSProperties;
}

export function ScriptureBadge(props: ScriptureBadgeProps): JSX.Element;
