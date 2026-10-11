(function (root) {
  "use strict";
  function r0(x) { return Math.round(x); }
  function r1(x) { return Math.round(x * 10) / 10; }
  function r2(x) { return Math.round(x * 100) / 100; }

  function depthPlan(windowHCm, gapCm, slope) {
    if (!(windowHCm > 0) || !(gapCm >= 0) || !(slope > 0)) return { error: "window and slope must be positive, gap zero or more" };
    var depthCm = r0((gapCm + windowHCm) / slope);
    return { depthCm: depthCm };
  }

  function reachPlan(depthCm, gapCm, windowHCm, slope) {
    if (!(depthCm > 0) || !(gapCm >= 0) || !(windowHCm > 0) || !(slope > 0)) return { error: "awning, window and slope must be positive, gap zero or more" };
    var shadowCm = r1(depthCm * slope);
    var shadedCm = r0(Math.min(windowHCm, Math.max(0, shadowCm - gapCm)));
    var litCm = r0(windowHCm - shadedCm);
    return { shadowCm: shadowCm, shadedCm: shadedCm, litCm: litCm };
  }

  function fabricPlan(depthCm, widthCm, wastePct) {
    if (!(depthCm > 0) || !(widthCm > 0) || !(wastePct >= 0)) return { error: "depth, width and waste must be positive or zero" };
    var areaM2 = r2(depthCm * widthCm / 10000 * (1 + wastePct / 100));
    return { areaM2: areaM2 };
  }

  function renderDepth(r, windowH, gap, slope) {
    return "To shade a " + r0(windowH) + " cm window under a " + r0(gap) + " cm gap against a labeled sun slope of " + slope + ", the awning needs to project about " + r.depthCm + " cm.";
  }

  function renderReach(r, depth, slope) {
    return "With a " + r0(depth) + " cm awning and a labeled sun slope of " + slope + ", the shadow runs " + r.shadowCm + " cm down the wall - " + r.shadedCm + " cm of window in shade, " + r.litCm + " cm in sun.";
  }

  function renderFabric(r, depth, width, waste) {
    return "A " + r0(depth) + " x " + r0(width) + " cm awning at a labeled " + waste + "% waste is about " + r.areaM2 + " m² of material.";
  }

  var api = { depthPlan: depthPlan, reachPlan: reachPlan, fabricPlan: fabricPlan, renderDepth: renderDepth, renderReach: renderReach, renderFabric: renderFabric };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.AwningMath = api;
})(this);
