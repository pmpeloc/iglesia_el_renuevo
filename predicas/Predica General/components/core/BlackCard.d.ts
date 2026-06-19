import React from "react";

/**
 * The "caja de aplicación" — deep-ink box with cream text that frames a
 * directive or takeaway on application slides over the cream background.
 */
export interface BlackCardProps {
  children: React.ReactNode;
  style?: React.CSSProperties;
}

export function BlackCard(props: BlackCardProps): JSX.Element;
