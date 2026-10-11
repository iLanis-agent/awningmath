import json, math

def r0(x): return math.floor(x + 0.5)
def r1(x): return math.floor(x * 10 + 0.5) / 10
def r2(x): return math.floor(x * 100 + 0.5) / 100
def jsnum(x):
    return int(x) if isinstance(x, float) and x == int(x) else x

def depth_plan(windowH, gap, slope):
    if not (windowH > 0) or not (gap >= 0) or not (slope > 0):
        return {"error": "window and slope must be positive, gap zero or more"}
    return {"depthCm": r0((gap + windowH) / slope)}

def reach_plan(depth, gap, windowH, slope):
    if not (depth > 0) or not (gap >= 0) or not (windowH > 0) or not (slope > 0):
        return {"error": "awning, window and slope must be positive, gap zero or more"}
    shadowCm = r1(depth * slope)
    shadedCm = r0(min(windowH, max(0, shadowCm - gap)))
    litCm = r0(windowH - shadedCm)
    return {"shadowCm": jsnum(shadowCm), "shadedCm": shadedCm, "litCm": litCm}

def fabric_plan(depth, width, waste):
    if not (depth > 0) or not (width > 0) or not (waste >= 0):
        return {"error": "depth, width and waste must be positive or zero"}
    return {"areaM2": jsnum(r2(depth * width / 10000 * (1 + waste / 100)))}

def render_depth(r, windowH, gap, slope):
    return ("To shade a " + str(r0(windowH)) + " cm window under a " + str(r0(gap))
            + " cm gap against a labeled sun slope of " + str(slope)
            + ", the awning needs to project about " + str(r["depthCm"]) + " cm.")

def render_reach(r, depth, slope):
    return ("With a " + str(r0(depth)) + " cm awning and a labeled sun slope of " + str(slope)
            + ", the shadow runs " + str(r["shadowCm"]) + " cm down the wall - "
            + str(r["shadedCm"]) + " cm of window in shade, " + str(r["litCm"]) + " cm in sun.")

def render_fabric(r, depth, width, waste):
    return ("A " + str(r0(depth)) + " x " + str(r0(width)) + " cm awning at a labeled "
            + str(waste) + "% waste is about " + str(r["areaM2"]) + " m² of material.")

cases = []
for windowH, gap, slope in [(120, 20, 1.9), (150, 10, 2.2), (100, 0, 1.5), (180, 30, 2.7),
                             (0, 20, 1.9), (120, 20, 0)]:
    r = depth_plan(windowH, gap, slope)
    cases.append({"fn": "depthPlan", "args": [windowH, gap, slope], "result": r,
                  "render": None if "error" in r else render_depth(r, windowH, gap, slope)})
for depth, gap, windowH, slope in [(74, 20, 120, 0.55), (74, 20, 120, 3), (60, 10, 100, 0.4),
                                    (90, 0, 150, 0.7), (0, 20, 120, 0.55), (74, 20, 0, 0.55)]:
    r = reach_plan(depth, gap, windowH, slope)
    cases.append({"fn": "reachPlan", "args": [depth, gap, windowH, slope], "result": r,
                  "render": None if "error" in r else render_reach(r, depth, slope)})
for depth, width, waste in [(74, 250, 10), (60, 200, 15), (100, 300, 5), (0, 250, 10), (74, 250, 0)]:
    r = fabric_plan(depth, width, waste)
    cases.append({"fn": "fabricPlan", "args": [depth, width, waste], "result": r,
                  "render": None if "error" in r else render_fabric(r, depth, width, waste)})

with open("expected.json", "w") as f:
    f.write(json.dumps(cases, separators=(",", ":")) + "\n")
print("wrote", len(cases), "cases")
