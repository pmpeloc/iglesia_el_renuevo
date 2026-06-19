/* @ds-bundle: {"format":3,"namespace":"PredicaGeneral_ebc788","components":[{"name":"BlackCard","sourcePath":"components/core/BlackCard.jsx"},{"name":"Highlight","sourcePath":"components/core/Highlight.jsx"},{"name":"Kicker","sourcePath":"components/core/Kicker.jsx"},{"name":"LogoMark","sourcePath":"components/core/LogoMark.jsx"},{"name":"ScriptureBadge","sourcePath":"components/core/ScriptureBadge.jsx"}],"sourceHashes":{"components/core/BlackCard.jsx":"6ff65e3c3242","components/core/Highlight.jsx":"f25298b17706","components/core/Kicker.jsx":"95db3eb483b6","components/core/LogoMark.jsx":"3565671b26e3","components/core/ScriptureBadge.jsx":"9df8ffa89240"},"inlinedExternals":[],"unexposedExports":[]} */

(() => {

const __ds_ns = (window.PredicaGeneral_ebc788 = window.PredicaGeneral_ebc788 || {});

const __ds_scope = {};

(__ds_ns.__errors = __ds_ns.__errors || []);

// components/core/BlackCard.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * BlackCard — the "caja de aplicación": a deep-ink box with cream text used
 * on application slides to set a directive apart from the cream background.
 */
function BlackCard({
  children,
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      background: "var(--ink)",
      color: "var(--text-on-ink)",
      borderRadius: "var(--radius-md)",
      padding: "var(--space-6)",
      boxShadow: "var(--shadow-card)",
      fontFamily: "var(--font-body)",
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { BlackCard });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/BlackCard.jsx", error: String((e && e.message) || e) }); }

// components/core/Highlight.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Highlight — the signature El Renuevo marker. Montserrat ExtraBold text
 * sitting on a lime-green block. Wraps inline inside a larger statement.
 */
function Highlight({
  children,
  color = "var(--green)",
  textColor = "var(--ink)",
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
      background: color,
      color: textColor,
      fontFamily: "var(--font-body)",
      fontWeight: 800,
      padding: "var(--highlight-pad-y) var(--highlight-pad-x)",
      borderRadius: "3px",
      boxDecorationBreak: "clone",
      WebkitBoxDecorationBreak: "clone",
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Highlight });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Highlight.jsx", error: String((e && e.message) || e) }); }

// components/core/Kicker.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * Kicker — small uppercase, wide-tracked label. Sits above titles to mark
 * the point number, series, or meeting ("PUNTO 01", "REUNIÓN GENERAL").
 */
function Kicker({
  children,
  color = "var(--green-deep)",
  style = {},
  ...rest
}) {
  return /*#__PURE__*/React.createElement("div", _extends({
    style: {
      fontFamily: "var(--font-body)",
      fontWeight: 700,
      textTransform: "uppercase",
      letterSpacing: "var(--tracking-kicker)",
      fontSize: "var(--fs-kicker)",
      lineHeight: 1,
      color,
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { Kicker });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/Kicker.jsx", error: String((e && e.message) || e) }); }

// components/core/LogoMark.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * LogoMark — the El Renuevo "R" mark. `bare` is the corner mark that lives
 * top-right on every slide; `green` / `black` are the circular badges.
 * Point `basePath` at wherever the assets folder sits relative to the page.
 */
function LogoMark({
  variant = "bare",
  size = 96,
  basePath = "assets",
  alt = "Iglesia El Renuevo",
  style = {},
  ...rest
}) {
  const file = {
    bare: "mark-green.png",
    green: "mark-green-circle.png",
    black: "mark-black-circle.png"
  }[variant] || "mark-green.png";
  return /*#__PURE__*/React.createElement("img", _extends({
    src: `${basePath}/${file}`,
    alt: alt,
    style: {
      height: size,
      width: "auto",
      display: "block",
      ...style
    }
  }, rest));
}
Object.assign(__ds_scope, { LogoMark });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/LogoMark.jsx", error: String((e && e.message) || e) }); }

// components/core/ScriptureBadge.jsx
try { (() => {
function _extends() { return _extends = Object.assign ? Object.assign.bind() : function (n) { for (var e = 1; e < arguments.length; e++) { var t = arguments[e]; for (var r in t) ({}).hasOwnProperty.call(t, r) && (n[r] = t[r]); } return n; }, _extends.apply(null, arguments); }
/**
 * ScriptureBadge — reference chip for a Bible verse ("2 Corintios 5:17").
 * solid = green pill on ink text; outline = green outline, transparent fill.
 */
function ScriptureBadge({
  children,
  variant = "solid",
  style = {},
  ...rest
}) {
  const solid = variant === "solid";
  return /*#__PURE__*/React.createElement("span", _extends({
    style: {
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
      ...style
    }
  }, rest), children);
}
Object.assign(__ds_scope, { ScriptureBadge });
})(); } catch (e) { __ds_ns.__errors.push({ path: "components/core/ScriptureBadge.jsx", error: String((e && e.message) || e) }); }

__ds_ns.BlackCard = __ds_scope.BlackCard;

__ds_ns.Highlight = __ds_scope.Highlight;

__ds_ns.Kicker = __ds_scope.Kicker;

__ds_ns.LogoMark = __ds_scope.LogoMark;

__ds_ns.ScriptureBadge = __ds_scope.ScriptureBadge;

})();
