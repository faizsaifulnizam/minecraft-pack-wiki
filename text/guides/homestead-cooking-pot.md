<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-cooking-pot/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Cook and serve a small meal batch

## Baseline
Candidate r2 is unapplied. Materials and recipe payloads are from Farmer's Delight 1.3.4. This page delivers a first cooked-rice batch and a conditional vegetable-soup extension, not the entire meal catalogue.

## Evidence status
Shipped recipes establish pot crafting, ingredient predicates and outputs; shipped UI text establishes “Needs heat from below”, “Heated” and “Served on: %s”.[1][2][3][4] Interface slot workflow supplements these with the author's latest/default-config wiki, **not release-pinned to 1.3.4**.[7] Neither local recipe shown explicitly names a serving container: use the actual result-slot/container display instead of pretending the JSON proves a bowl. Effective recipe loading, tags, container defaults and heat-state logic were not executed.

## Prerequisites
- One wooden shovel, two bricks, five inputs accepted as `c:ingots/iron`, and one accepted `c:buckets/water` item.[2]
- One `c:crops/rice` input for the first recipe. [Prepare rice from a panicle](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-rice-and-cutting/), but check that the current recipe accepts it.[3]
- A suitable heat location: the shipped heat-source tag includes magma block, lava cauldron and the Farmer's Delight stove; its nested tray tag lists lava, campfires and fire.[5][6] This is membership evidence, not a promise that every state of those blocks heats a pot. Prefer an already-established safe cooking area; do not handle exposed lava for this tutorial.
- Serving containers indicated by the result slot. Bowls are a common example in supplemental author documentation, not a local explicit container field for these two recipes.[7]

## Steps
1. Craft the pot with rows `brick, wooden shovel, brick`; `iron, water bucket, iron`; `iron, iron, iron` (`bSb / iWi / iii`). Check that the displayed output is **1 Cooking Pot** before taking it.[2] The recipe does not establish the returned bucket behavior; check the crafting interface rather than budgeting a guaranteed remainder.
2. Place the pot above a suitable heat source and open it using your current game interaction. Check the heat indicator: the shipped labels distinguish **Heated** from **Needs heat from below**.[1] Supplemental documentation also describes bubbling above a suitable heat source.[7]
3. Put **one** accepted rice input in an ingredient slot; leave unrelated ingredients out for this first batch. The shipped cooked-rice recipe has one ingredient, result **1 Cooked Rice**, `cookingtime: 100` and experience `0.35`.[3] These are recipe values, not measured wall-clock timing or guaranteed experience receipt.
4. Wait for the meal/result indication, then read **Served on**. Following supplemental documented workflow, put the indicated container in its corresponding slot or interact with the pot while holding that container to take a serving.[1][7] Check that the serving enters your inventory and that the stored-meal indication changes. If the live GUI differs, do not move a whole ingredient stock into it.
5. If you want a vegetable-soup extension, check the current recipe for **one carrot-tag input, one potato-tag input, one beetroot-tag input and one leafy-green-tag input**: `c:crops/carrot`, `c:crops/potato`, `c:crops/beetroot`, `c:foods/leafy_green`. Its shipped output is **1 Vegetable Soup** and experience value `1.0`; this JSON specifies neither cooking duration nor container.[4] The local leafy-green tag points to `#c:foods/cabbage`; its effective nested membership is not established here.[8] Use [the accepted recipe-search guide](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/) to identify currently accepted items instead of assuming every leaf works.
6. If you will carry that meal away from home, prepare [a Comforts sleeping bag](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-comforts-rest/) for documented portable rest without setting a new spawn; the meal is travel stock, not a sleep prerequisite or interaction requirement.
7. Once a single serving works, repeat the same verified ingredient combination in a small batch. Keep planting stock separate and return to [rice preparation](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-rice-and-cutting/) when grain supply is low. Store ingredients through [the accepted storage-choice guide](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/storage-choice/) if useful; this link is organization guidance, not proof of pot automation compatibility.

## Expected result
The exact shipped first recipe produces Cooked Rice; the soup extension produces Vegetable Soup when its four predicates are met.[3][4] Serving is a documented workflow plus a live-interface checkpoint, not a claimed runtime test.[1][7]

## Common failures
- **Unheated**: check heat below the pot and the indicator, rather than blaming the rice. A listed tag member alone does not establish active state or any required placement gap.[1][5][6]
- **Ingredients sit without progress**: remove unrelated inputs; compare with the displayed current recipe and accepted tags. Do not substitute a Rice Panicle for a `c:crops/rice` input merely because both names contain “rice”.[3]
- **Meal exists but no takeable serving**: check the indicated serving container and corresponding slot/held item. Do not add the container as a seventh ingredient; documentation distinguishes six ingredient slots from the container slot.[1][7]
- **Soup tag ambiguity**: this packet deliberately does not certify cabbage-leaf eligibility. Follow the current recipe's accepted-input list; tag resolution is a remaining gap.[4][8]
- **Conditional tip — prove one recipe before scaling**: if tags or controls are unfamiliar, use one ingredient set and one serving container first. Benefit: distinguish heat, recipe and serving failures without committing your reserve. Trade-off: smaller immediate batch. This is an author technique based on the three separate documented checkpoints, not a throughput guarantee.[1][3][7]

## Sources
[1] `FarmersDelight-1.21.1-1.3.4.jar!assets/farmersdelight/lang/en_us.json` — keys `container.farmersdelight.cooking_pot.not_heated`, `.heated`, `.served_on` and `tooltip.farmersdelight.cooking_pot.many_servings`.
[2] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cooking_pot.json`.
[3] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cooking/cooked_rice.json`.
[4] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/recipe/cooking/vegetable_soup.json`.
[5] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/tags/block/heat_sources.json`.
[6] `FarmersDelight-1.21.1-1.3.4.jar!data/farmersdelight/tags/block/tray_heat_sources.json`.
[7] [Author's Getting Started wiki](https://github.com/vectorwing/FarmersDelight/wiki/Getting-Started) — supplemental latest/default configuration documentation, not pinned to 1.3.4; ingredient/container workflow.
[8] `FarmersDelight-1.21.1-1.3.4.jar!data/c/tags/item/foods/leafy_green.json`.
