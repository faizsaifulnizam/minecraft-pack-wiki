---
layout: default
title: "FULL SPOILERS"
permalink: /full/equipment-workshop/
baseline: dev-0.5-20261015-r2
---
<!-- wiki.py managed full human schema=1 -->
**FULL SPOILERS**

WARNING: FULL SPOILERS. Direct links, reload and history may reveal everything here; this distinct full-human route is exempt from ordinary-entry consent/reset guarantees.

[Return to safe entry](/minecraft-pack-wiki/guides/equipment-workshop/)

# Equipment workshop reference

## Baseline

Development documentation snapshot **dev-0.5-20261015-r2**; not release validation. Static documentation only; effective datapacks, settings and gameplay have not been verified.

## Evidence status

FULL SPOILERS. Exact selected recipes and item tags support these bounded procedures. Ingredient acquisition, loot dispatch and numerical effects remain separate. Neither a recipe nor a boss-themed item name proves a drop route.

## Prerequisites

For the cooking upgrade: one already-owned `artifacts:everlasting_beef`, a furnace and fuel able to complete one operation, or an available smoker/campfire. For the separate shaped recipe: one bone and one already-owned `reliquified_twilight_forest:twilight_gem`, plus a 2×2 crafting grid. No trip to Twilight is required or justified merely by these declarations.

## Steps

### Cook one upgrade

1. Check the displayed recipe before starting. Place Everlasting Beef in the furnace ingredient slot and fuel below it. The selected smelting recipe declares Eternal Steak as the result, 200 cooking ticks and 0.35 experience.
2. Wait for the output and take Eternal Steak. Check the input was transformed; cooking is not the same operation as eating.
3. Alternatives use the same ingredient/result: smoker 100 cooking ticks, campfire 600. These are declared work times, not measured wall time under server lag.
4. The shared food tooltip says not consumed when eaten. Config descriptions expose enabled/cooldown controls, so do not promise unlimited immediate eating or a particular cooldown in this pack.

### Craft the separate declared tool

1. In a 2×2 grid, put the Twilight Gem in the top-right cell and the bone in the bottom-left; leave the other two cells empty.
2. Check the output is one `twilightforest:twilight_scepter` before collecting it. The addon owns the recipe; the result belongs to Twilight Forest. That proves this recipe reference, not a broader progression or combat integration.
3. If the output differs or is absent, stop before spending ingredients. Do not replace it with a guessed recipe.

## Expected result

One exact cooking transformation or one shaped craft completes within its stated ingredient boundary. For equipping already-owned Running Shoes, the Artifacts feet tag is explicitly referenced by Curios' feet tag; do not infer eligibility from “Shoes.” For an already-owned Lich Crown, Reliquified explicitly includes it in the Curios head tag. Use [equipment slot reference](/minecraft-pack-wiki/guides/equipment-slots/); tags do not prove duplicate/stack acceptance or summed effects.

## Common failures

- Missing input: neither selected recipe establishes its acquisition. No farming or boss drop claim is made.
- Furnace output absent: compare the displayed recipe and fuel state; effective overrides are unverified. Do not destroy the input or assume a runtime bug.
- Crown gems: shipped prose describes right-click insertion and empty-cursor right-click removal, but exact gem validity/capacity and caller correspondence are not established here. Do not use this as an executable inlay guide.
- Cross-mod builds: no Artifacts/Relics synergy or implicit Twilight acquisition bridge is proven. Return to [relic research](/minecraft-pack-wiki/guides/relic-research/) for its separate UI task.

Tip: prefer the smoker when already available because its declared cook work is lower; constructing one and its recursive material bill are outside this bounded transformation. Check the displayed recipe before starting; do not process additional inputs until the first result matches.

## Sources

- `artifacts-neoforge-13.2.5.jar!data/artifacts/recipe/eternal_steak_furnace.json`
- `artifacts-neoforge-13.2.5.jar!data/artifacts/recipe/eternal_steak_smoker.json`
- `artifacts-neoforge-13.2.5.jar!data/artifacts/recipe/eternal_steak_campfire.json`
- `artifacts-neoforge-13.2.5.jar!assets/artifacts/lang/en_us.json`
- `artifacts-neoforge-13.2.5.jar!data/curios/tags/item/feet.json`
- `artifacts-neoforge-13.2.5.jar!data/artifacts/tags/item/slot/feet.json`
- `reliquified_twilight_forest-1.21.1-0.5.3.jar!data/reliquified_twilight_forest/recipe/twilight_scepter.json`
- `reliquified_twilight_forest-1.21.1-0.5.3.jar!data/curios/tags/item/head.json`
- `reliquified_twilight_forest-1.21.1-0.5.3.jar!assets/reliquified_twilight_forest/lang/en_us.json`
