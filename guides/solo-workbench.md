---
layout: default
title: "Craft documented SoloCraft equipment"
permalink: /guides/solo-workbench/
baseline: dev-0.5-20261015-r2
---

# Craft documented SoloCraft equipment

## Baseline
This is an bounded statically reviewed revision for candidate **dev-0.5-20261015-r2**, not an applied replacement for dev-0.5-20261015. New core text corresponds only to Tensura archive SHA-256 `2309a22ceb7e423e2f3212ea87686ccc510fe0003595500037e0b6c64baef213`. The original baseline/pins remain unchanged. Static descriptions and feedback are not runtime or award-handler proof.

SoloCraft: Reawakening 1.3.3 in dev-0.5-20261015. How-to: turn already-owned materials into two exact shipped recipe results.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.
Documented-static shaped recipes, not runtime-tested crafting or effective pack recipe resolution. Crystal acquisition, rank entitlement, item use and any later progression award are outside these recipe objects. Neither recipe declares a hunter-rank condition; that does not prove the complete game lacks additional restrictions.

## Prerequisites
A crafting grid large enough for the shown pattern and the exact named ingredients. Check whether your current recipe viewer shows the selected result; return to [the independent SoloCraft route](solo-start.md) for panel/access questions. A missing viewer entry is not alone proof the recipe is disabled.

## Steps
### Make the E Rank Sword
1. Obtain two **sololeveling:mana_crystal_e** and one **minecraft:stick** from your existing inventory. The source of the crystals is not documented here.
2. Place the two crystals above the stick in one vertical column: crystal, crystal, stick. The shipped pattern is a / a / b.
3. Inspect the result before taking it. The recipe declares **one sololeveling:e_tier_sword**, whose English name is **E Rank Sword**.
4. Take the result only if it matches. Using it successfully, its damage and any class restriction require separate evidence; the recipe does not award a rank.

### Make the Magic Reader
1. Gather four **minecraft:redstone**, four **minecraft:iron_ingot** and one **sololeveling:mana_crystal_d**.
2. Put redstone in the four corners, iron in the four edge-center slots, and the D crystal in the center. The pattern is aba / bcb / aba, with a=redstone, b=iron and c=the crystal.
3. Inspect the result: **one sololeveling:magic_reader**, named **Magic Reader** in the selected English translation.
4. Take the result if it matches. Do not equate this item with the separately named **Hunter Rank Evaluator** block. Crafting this item is not an evidenced awakening procedure.

## Expected result
One declared result per craft. The material totals and layouts come from the exact recipe objects. Successful crafting and use have not been observed in this documentation work.

## Common failures
- Empty output: first compare the ingredient IDs, pattern and grid size. If these match, stop and report the recipe ID plus what the viewer shows. Pack overrides and runtime recipe registration were not resolved by this lane.
- A different tier crystal looks similar: use the exact namespace and suffix, not only the icon or a generic crystal name.
- The crafted reader does not awaken you: no such effect is established. Do not repeatedly spend materials on the assumption that an item label promises a progression award.

## Sources
SLR1.3.3.jar: data/sololeveling/recipe/basic_sword_e.json and data/sololeveling/recipe/magic_reader_recipe.json; assets/sololeveling/lang/en_us.json item.sololeveling.e_tier_sword, item.sololeveling.magic_reader and block.sololeveling.hunter_rank_evaluator. Claims CHAR-008 and CHAR-009.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [CHAR-008] `SLR1.3.3.jar!data/sololeveling/recipe/basic_sword_e.json`: `$`.
- [CHAR-008] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `item.sololeveling.e_tier_sword`.
- [CHAR-009] `SLR1.3.3.jar!data/sololeveling/recipe/magic_reader_recipe.json`: `$`.
- [CHAR-009] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `item.sololeveling.magic_reader; block.sololeveling.hunter_rank_evaluator`.
