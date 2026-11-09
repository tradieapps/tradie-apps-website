/* ==== EDIT HERE: paste your privacy policy web addresses between the quotes ==== */
var CONFIG = {
  qwPrivacy: "",   // QuoteWalk privacy policy URL
  imPrivacy: ""    // Invomile privacy policy URL
};
/* ============================================================================== */

/* Email is assembled only when clicked, so it never shows on the page or to spam bots */
var MAIL = ["dannielappdevelopment", "gmail.com"];

document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll("[data-link]").forEach(function (a) {
    var url = CONFIG[a.getAttribute("data-link")];
    if (url) { a.href = url; a.target = "_blank"; a.rel = "noopener"; }
    else { a.style.display = "none"; }
  });
  document.querySelectorAll("[data-email]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var s = a.getAttribute("data-email");
      window.location.href = "mailto:" + MAIL[0] + "@" + MAIL[1] + (s ? "?subject=" + encodeURIComponent(s) : "");
    });
  });
});

/* Shared helpers for the calculators */
var TA = {
  imperialDefault: /^en-(US|LR|MM)$/i.test(navigator.language || ""),
  num: function (id) { var v = parseFloat(document.getElementById(id).value); return isFinite(v) ? v : 0; },
  fmt: function (n, d) { return (Math.round(n * Math.pow(10, d || 0)) / Math.pow(10, d || 0)).toLocaleString(undefined, { minimumFractionDigits: d || 0, maximumFractionDigits: d || 0 }); },
  money: function (n) { return "$" + n.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 }); },
  units: function (onChange) {
    var box = document.querySelector(".units");
    if (!box) return;
    var set = function (imp) {
      box.querySelectorAll("button").forEach(function (b) { b.classList.toggle("on", (b.dataset.u === "imp") === imp); });
      document.querySelectorAll("[data-m]").forEach(function (el) { el.textContent = imp ? el.dataset.i : el.dataset.m; });
      onChange(imp);
    };
    box.querySelectorAll("button").forEach(function (b) { b.onclick = function () { set(b.dataset.u === "imp"); }; });
    set(TA.imperialDefault);
  }
};
