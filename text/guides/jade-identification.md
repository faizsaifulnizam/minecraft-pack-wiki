<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/jade-identification/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Identify a target without breaking it

## Baseline
Jade 15.10.6+neoforge. How-to: use a world-target overlay as the starting point for item/recipe research.

## Evidence status
Exact shipped configuration descriptions and control labels; **not runtime tested**. The processed settings do not contain Jade's saved bindings, display mode or enabled information providers. No key such as a remembered default is prescribed.

## Prerequisites
A target you can safely look at and no need to mine or interact with it. An overlay is informational; it does not grant access to a container or establish that a block can be safely harvested.

## Steps
1. Look at the unfamiliar target without breaking it. If Jade's overlay is already visible, read the displayed name before acting. If not, find **Show Overlay** and **Open Config** in the controls/configuration UI via [control-context inspection](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/control-contexts/). Stop if you cannot identify their bindings.
2. Check **Display Mode** before treating Show Overlay as a toggle. The shipped descriptions distinguish **Toggle** (press Show Overlay), **Hold** (keep Show Overlay held) and **Lite** (hold Show Details for further information). The active mode is unknown here; follow the mode you actually observe rather than repeatedly tapping a key.
3. If the ordinary overlay gives too little detail, identify **Show Details** or **Show Details (Alternative)** and use the mode's instruction. Jade describes separate detailed/ordinary amounts for item storage and optional detail-only energy/fluid information. Their existence does not guarantee that every modded machine exposes those values.
4. Take the displayed name to [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/) to investigate ingredients and uses. Jade also ships **Show Recipes** and **Show Uses** action labels, but neither saved keys nor successful viewer integration are captured; use the established inventory-viewer route if those actions are unknown.
5. Before any actual harvest, distinguish name identification from tool/harvest information. A readable block name alone does not certify an appropriate tool, drop, ownership permission or safe machine removal. Leave the target intact if those conditions are unresolved.

## Expected result
A target name and, where supplied, additional information that can guide the next lookup without changing the block. This is the intended source-backed route, not an observed HUD result.

## Common failures
- **Overlay vanishes in a GUI, debug screen or player list:** Jade ships Hide from GUIs, Hide from Debug Screen and Hide from Player List options. Inspect the relevant option, not every rendering setting; saved values are unknown.
- **Only some information appears:** Lite mode and detail-only providers are possible documented causes. A missing field is not proof that a tank is empty or that a block has no stored energy.
- **Fluid target is hard to select:** Jade ships Toggle Fluid and a fallback option that shows fluid only when no other target exists. Their saved state is unknown; do not break a block to force a fluid target.
- **The HUD and boss bar overlap:** Jade includes boss-bar overlap choices including Hide Tooltip and Hide Boss Bar. This documents an option, not a recommendation to hide important combat warnings or a verified saved layout.
- **Name lookup finds the wrong item:** blocks and their item forms need not share every behavior. Recheck the target name and exact identifier when exposed; do not infer a recipe from a similar name.

## Tip: identify before interacting
Prerequisite: a working overlay on the target. Technique: read the name, then perform an inventory-viewer lookup before mining or opening an unfamiliar machine. Benefit: gathers an initial lead without changing the target. Trade-off: the overlay may be incomplete and is not a permission, break-safety or compatibility check.

## Sources
Jade 15.10.6 `assets/jade/lang/en_us.json`: key labels, display-mode descriptions, GUI/debug/player-list hiding, detail-only storage fields and fluid fallback. Claim E-JADE retains selected witnesses and exact archive identity. No HUD placement or live feature state was read or changed.
