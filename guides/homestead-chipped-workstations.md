---
layout: default
title: "Choose a Chipped workshop for your homestead"
permalink: /guides/homestead-chipped-workstations/
baseline: dev-0.5-20261015-r2
---
# Choose a Chipped workshop for your homestead

## Baseline
Candidate r2 is unapplied. This is a Chipped 4.0.2 carpenter/mason starter workshop, not a full decorative catalogue.

## Evidence status
Shipped recipes establish workstation crafting and distinct tagged material families.[1][2][3][4] The author's current project description supplies the vanilla-block-to-Chipped-variant direction; it is **not release-pinned to 4.0.2**.[8] Shipped category tags contain both base items and variants, but their presence alone does **not** prove that the interface returns any variant to vanilla or that a held tool performs conversions.[5][6] No conversion code, controls, output ratios, active recipes or effective tag resolution were traced.

## Prerequisites
Choose one workshop instead of crafting every table:
- **Carpenters Table**: 1 iron axe, 1 iron ingot, 1 crafting table, 5 plank-tag inputs.[1]
- **Mason Table**: 3 bricks, 2 iron ingots, 1 crafting table, 3 log-tag inputs.[2]
- One spare oak plank for a carpenter sample or one spare stone for a mason sample, not your entire building stock.[3][4][5][6]

## Steps
1. Pick a task: kitchen woodwork uses the carpenter category; a stone surface uses the mason category. The carpenter recipe lists oak planks, logs, doors, barrels, bookshelves, ladders and torches among its tags. The mason recipe lists stone, cobblestone, andesite, bricks, terracotta and other mineral families.[3][4] These are recipe categories, not a claim that every variant in the catalogue is usable in this pack.
2. Craft the chosen table. Carpenter rows are `iron axe, empty, iron ingot`; `plank, crafting table, plank`; `plank, plank, plank` (`A I / P#P / PPP`). Mason rows are `brick, brick, brick`; `iron ingot, crafting table, iron ingot`; `log, log, log` (`BBB / I#I / LLL`). Each recipe yields one workstation.[1][2]
3. Place it beside your homestead workspace and open its interface using the game interaction shown for you. For the carpenter, supply one oak plank; for the mason, supply one stone. Shipped item tags explicitly list `oak_planks` and `stone` alongside their Chipped families.[5][6] Those unqualified source tokens are preserved here; effective runtime names/tag merging are not established.
4. Following the author's documented vanilla-to-variant workflow, inspect the available variant choices. Select one small sample and inspect the resulting item/count **before** converting building stock.[8] A visible appropriate output is the checkpoint; this packet does not prescribe a keyboard shortcut or guarantee a conversion ratio. If no choice appears, follow the failure checks below.
5. Place the sample where you can compare it with the intended kitchen or rest-area surface. Decide whether the texture works before spending more material. Keep the unconverted stock in your usual [storage organization](storage-choice.md); no special Chipped/storage compatibility is claimed.
6. Treat the **Saw as a separate craft**, not a required held conversion tool: its shipped shapeless recipe is **1 Carpenters Table plus 1 iron ingot → 1 Saw**.[7] This ingredient list budgets the table as a crafting input; do not casually sacrifice your only workshop or assume a returned table. Tool usage and conversion-by-saw are unresolved, so the ordinary table path above does not ask you to craft it.
7. When the cooking area is ready, continue with [the Cooking Pot workflow](homestead-cooking-pot.md). Decorative conversion does not establish heat suitability: retain the cooking page's explicit heat check instead of assuming a Chipped block heats the pot because its base material did.

## Expected result
You have one purpose-chosen workstation and a reviewed decorative sample if the documented interface workflow is available.[1][2][8] This proves neither universal return conversion nor identical functional properties of decorative replacements.

## Common failures
- **Wrong table or family**: compare the category recipe first. Carpenter planks/logs and mason stone families are different; selecting the table only by visual appearance can miss the correct category.[3][4]
- **No variants appear**: confirm item identity and current recipe availability through [recipe search](recipe-search.md), then try the small base sample. Do not assume an external mod's wood/stone is a member of the shipped Chipped category.[3][4][5][6]
- **Want to undo a conversion**: no return-to-vanilla direction is certified here. Inspect the interface with one spare sample; retain base stock until you have independent evidence of the return path. Tag co-membership is not a witnessed conversion algorithm.[5][6]
- **Saw recipe surprises you**: the table is itself an ingredient, not merely nearby equipment. Rebuild from the carpenter pattern if you intentionally used it; table remainder behavior was not traced.[1][7]
- **Conditional tip — sample before a wall-sized batch**: if choosing among unfamiliar textures, convert only one spare base block first. Benefit: compare placement without tying up the main building supply; trade-off: an extra preview step and no guaranteed reversal. The vanilla-to-variant direction is documented, whereas reversal and output ratio remain unproved.[8]

## Sources
[1] `chipped-neoforge-1.21.1-4.0.2.jar!data/minecraft/recipe/workbench/carpenters_table.json`.
[2] `chipped-neoforge-1.21.1-4.0.2.jar!data/minecraft/recipe/workbench/mason_table.json`.
[3] `chipped-neoforge-1.21.1-4.0.2.jar!data/chipped/recipe/carpenters_table.json` — workbench category, not its crafting recipe.
[4] `chipped-neoforge-1.21.1-4.0.2.jar!data/chipped/recipe/mason_table.json` — workbench category.
[5] `chipped-neoforge-1.21.1-4.0.2.jar!data/chipped/tags/item/oak_planks.json`.
[6] `chipped-neoforge-1.21.1-4.0.2.jar!data/chipped/tags/item/stone.json`.
[7] `chipped-neoforge-1.21.1-4.0.2.jar!data/chipped/recipe/saw.json`.
[8] [Author's Chipped project page](https://modrinth.com/mod/chipped) — supplemental current description, not pinned to 4.0.2; vanilla-to-variant direction only.
