---
layout: default
title: "Accessory slot reference and conditional UI check"
permalink: /guides/equipment-slots/
baseline: dev-0.5-20261015-r2
---

# Accessory slot reference and conditional UI check

## Baseline

Development documentation snapshot **dev-0.5-20261015-r2**; not release validation. Static documentation only; effective datapacks, settings and gameplay have not been verified.

## Evidence status

Curios' shipped README describes tag-based item eligibility, merged slot identifiers and the equipment GUI. This supports a bounded reference and conditional attempted UI check, not a proven equip/removal procedure, stacking bonuses, duplicate-item acceptance or a fixed slot count. Exact placement/removal controls and item predicates remain unresolved. The README says applicable Curses work on equipped items; it does not establish a specific curse rule or guaranteed removal. Artifacts and Relics both supply feet-slot definitions; their individual declared sizes must not be added together as an effective capacity claim.

## Prerequisites

An already-obtained, nonvaluable accessory with no known applicable binding or removal restriction, one empty main-inventory cell, and a positively identified matching functional slot. Unknown removal restrictions or unidentified slots are a stop condition, not permission to experiment with valuables. Acquisition is separate. Read its Slot tooltip; do not choose a slot from the item's name.

## Steps

1. In Controls, find Curios → Open/Close Curios Inventory. Use its current binding; the shipped README says the default is G, not that this pack still uses G.
2. Read the matching slot label and item tooltip. “Toggle Visibility” and “Toggle Cosmetics” are shipped control labels only, not verified behavior or a way to identify functional versus cosmetic cells. Do not infer semantics from labels or slot appearance; do not place valuables in unidentified slots. If the functional slot or operation is unclear, stop here.
3. Only if the prerequisite and identified UI permit it, attempt placement of one nonvaluable accessory using the UI's identified operation. Exact clicks/drag controls are unresolved here; no gesture is prescribed. If placement is denied, stop; do not force placement or drop the item.
4. If placement succeeds, inspect the occupied slot. This observation does not prove ability execution or save persistence.
5. If an identified removal operation is available, attempt return to the reserved main-inventory cell. If removal is denied or its control is unclear, stop and ask the host; do not force removal or drop the item. Do not assume this check is reversible.

## Expected result

The conditional check may show placement and, if permitted, removal; either may remain unresolved or be denied. No successful check has been observed here, and removal is not guaranteed. No claim that merely holding it activates its equipped effects. Continue with [Relic research](relic-research.md) or [personal loot handling](personal-loot.md). Optional [FULL SPOILERS — equipment workshop](equipment-workshop.md) contains named items and recipes.

## Common failures

- No slot: Curios does not provide a universal default set; integrations supply slots. Do not edit settings to create one for this guide.
- Wrong slot, unidentified cell or inactive tooltip: stop and inspect eligibility without further placement. If removal is denied, ask the host; do not force or drop. Cosmetic visibility is not an effect test.
- Inventory full: clear a safe cell first; do not drop the accessory as a workaround.
- Death, disconnect or missing item after reload: recovery and persistence are not established here. Do not assume soulbinding, gravestone support or keep-inventory. Ask the host before risking valuable equipment.

Tip: read slot labels and removal restrictions at a safe base before an expedition. A conditional check with a nonvaluable item may expose a conflict, but is not guaranteed reversible and does not establish loadout synergy.

## Sources

- `curios-neoforge-9.5.1+1.21.1.jar!README.md`
- `curios-neoforge-9.5.1+1.21.1.jar!assets/curios/lang/en_us.json`
- `artifacts-neoforge-13.2.5.jar!data/artifacts/curios/slots/feet.json`
- `relics-1.21.1-0.10.7.8.jar!data/relics/curios/slots/feet.json`
