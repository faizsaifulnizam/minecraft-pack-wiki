<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-rice-and-cutting/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Grow rice and prepare ingredients

## Baseline
Candidate r2 is unapplied. This is a bounded Farmer's Delight 1.3.4 procedure, not a complete farming catalogue or proof of this pack's effective gameplay.

## Evidence status
Exact shipped recipes and English descriptions support the materials, cutting outputs and shallow-water planting below.[1][2][3][4][5] No world generation, effective tags, crop growth timings, controls or configuration were tested. References to a knife tag or item ability are recipe predicates, not proof that another mod's knife qualifies.

## Prerequisites
- A crafting interface, 1 flint, 3 sticks and 4 items accepted as `minecraft:planks`: 1 stick is for the knife; 2 are for the board.[2][3]
- One Farmer's Delight Rice grain to plant; for a cutting demonstration, one Rice Panicle or one Cabbage. These are distinct items, not interchangeable inputs.[4][5]
- A shallow-water planting spot. Keep at least one grain out of the cooking batch so that your next planting is not consumed; this reserve is a planning recommendation, not a growth-rate claim.

## Steps
1. Craft a Flint Knife with flint directly above a stick (`m / s` in one column). The shipped result is one knife.[3]
2. Craft a Cutting Board with two rows of `stick, plank, plank` (`/## / /##`). The shipped result is one board; place it in your food-preparation area.[2]
3. Start a rice plot by planting a grain in shallow water. The shipped advancement says “Plant grains of Rice in a shallow water puddle”; invalid placement reports “This seed must be planted in shallow water.” Check that placement succeeds before allocating the rest of your grains.[1] This packet does not prescribe unverified water depth, substrate, growth duration or harvest controls.
4. When you have a Rice Panicle, put **that item** on the board and use the board with a qualifying knife/tool in hand. The shipped description says to use the board with a tool to break down an item. For one panicle the cutting recipe specifies **1 Rice and 1 Straw**; collect both before repeating.[1][4]
5. For a second useful preparation task, place one Cabbage on the board and cut with a qualifying knife/tool. Expect **2 Cabbage Leaves**, not two whole cabbages.[5] The recipe accepts `knife_dig` item ability or `c:tools/knife`; it does not name a sword.[4][5]
6. Put planting grains aside, then take cooking stock to [cook a small batch](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-cooking-pot/). Start there with rice; the soup route additionally needs the specific ingredient tags displayed in the recipe. This handoff does not assume a leaf's membership in an unresolved tag.

## Expected result
You have a placed rice crop if the documented planting predicate is satisfied, a board/knife preparation station, and exact panicle or cabbage cutting outputs.[1][2][3][4][5] Growth speed and harvesting yield remain outside this static claim.

## Common failures
- **“Maybe with a different tool…”**: compare the current cutting recipe with your tool. Try the Farmer's Delight knife rather than assuming a similarly named external knife qualifies; effective ability/tag membership is unverified.[1][3][4]
- **“This doesn't seem cuttable…”**: check the item identity. Rice Panicle is the demonstrated cutting input; Rice grain is the cooking/planting handoff. Remove the wrong input using the game's displayed interaction, whose binding is not traced here.[1][4]
- **Planting refused**: relocate the grain to a shallow-water spot, matching the shipped error. Do not infer that a dry ordinary farmland row can substitute.[1]
- **No wild plants nearby**: the shipped descriptions mention beach coasts for wild cabbage and ponds in wet lands such as swamps/jungles for wild rice. Those are documented search hints, not a guarantee for an existing pack world.[1]
- **Conditional tip — separate seed and meal stocks**: if you only have a small supply, reserve a grain before cutting/cooking. Benefit: you retain a next-planting input; trade-off: one less grain in your immediate meal batch. The planting and cooking input identities are shipped; the reserve quantity is an author recommendation.[1][4]

## Sources
[1] `FarmersDelight-1.21.1-1.3.4.jar!assets/farmersdelight/lang/en_us.json` — planting, board usage/errors, wild-crop hints; exact keys `advancements.farmersdelight.plant_rice.description`, `advancements.farmersdelight.use_cutting_board.description`, `block.farmersdelight.rice.invalid_placement`, `block.farmersdelight.cutting_board.invalid_tool`, `block.farmersdelight.cutting_board.invalid_item`, `jei.farmersdelight.info.wild_rice`, `jei.farmersdelight.info.wild_cabbages`.
[2] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cutting_board.json`.
[3] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/flint_knife.json`.
[4] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cutting/rice_panicle.json`.
[5] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cutting/cabbage.json`.
