# Awning math

The awning depth that shades a window against the high summer sun, the winter sun that same awning still admits, and the square meters of material to buy. Works in sun slopes - stick height over shadow length, measured yourself. Exact arithmetic in the browser, every borrowed number labeled.

Live site: https://ilanis-agent.github.io/awningmath/

## The three tools

- **Depth plan** - `depthPlan(windowHCm, gapCm, slope)`: the projection needed for full summer shade.
- **Reach plan** - `reachPlan(depthCm, gapCm, windowHCm, slope)`: shadow run, shade and sun on the window at a low slope.
- **Fabric plan** - `fabricPlan(depthCm, widthCm, wastePct)`: square meters of material including waste.

## Labeled norms (illustrative references, not rules)

- Summer slope 1.9 (high sun), winter slope 0.55 (low sun) - measure your own: vertical stick height divided by shadow length. Waste 10% for hems and seams. Your wall, window and shadow-stick decide the real numbers.

## Files

- `index.html` / `app.html` - landing and calculators (static, no dependencies)
- `engine.js` - pure arithmetic + renderers, runs in browser and node
- `oracle.py` - python mirror of the engine; regenerates `expected.json`
- `test.js` - compares engine output to the oracle: `node test.js` (17 cases, 66 checks)

Regenerate the oracle expectations: `python3 oracle.py`
