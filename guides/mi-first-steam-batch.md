---
layout: default
title: "Make a first bronze plate with steam"
permalink: /guides/mi-first-steam-batch/
baseline: dev-0.5-20261015-r2
---

# Make a first bronze plate with steam

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation. Modern Industrialization 2.5.10. This is a static task using shipped recipes and the pinned 2.5.10 release source, not a gameplay-tested result.

## Evidence status
The fire-clay conversion and component quantities below come from the exact archive. Container and output gestures come from release-tag source, commit `2d2b25dc45043375de1126e703b96ace950d8324`. Release-tag correspondence is stronger than an unversioned tutorial but is **not compiled-method parity or effective-runtime proof**. Effective tags, recipe overrides, permissions and NeoForge fluid-container integration are untested. Check each named recipe and checkpoint; stop on disagreement rather than guessing another gesture.

## Prerequisites
Have [first bronze](mi-starter.md), a crafting table, a working ordinary furnace, a pickaxe, fuel and room in inventory for emptied containers. Starting stock below is refined ingots and supplied vanilla components, not a mining/fuel-production bill. Do not use the optional hand-held Hammer: these quantities use the less-efficient **tool slot empty** Forge Hammer recipes.

Choose before crafting:
- **Bucket bootstrap:** only if the current recipe viewer actually offers water bucket → steam bucket. The shipped recipe is disabled when `dehydration` is loaded. Cookingtime is 500 ticks. A historical roster or this recipe object does not prove effective availability.
- **Boiler-first fallback:** does not depend on that conditional recipe. Make all boiler and wrench plates in the Forge Hammer **before** crafting the compressor. It costs more ingots but avoids the circular plan “use the compressor to make its own initial steam supply.” Its fuel requirement is checkpoint-based, not an exact coal-count promise.

### Complete compressor construction bill
One compressor consumes **1 Forge Hammer workstation, 2 copper rods, 2 copper gears, 1 bronze machine casing, 3 fluid pipes** (`rFr / GCG / ppp`). The workstation itself costs **3 heavy weighted pressure plates + 4 iron ingots** (`___ / .i. / iii`). Supplied vanilla plates are not MI bronze/copper plates.

For the no-hand-tool route, prepare these exact intermediate batches:

| Component | Craft / conversion | Stock consumed |
|---|---|---|
| 1 bronze machine casing | 8 bronze plates around 1 bronze gear | 12 bronze plates + 1 bronze ring + 4 bronze bolts after expanding the gear |
| 1 bronze gear | `PbP / bRb / PbP` | 4 bronze plates, 1 bronze ring, 4 bronze bolts |
| 2 copper gears | same gear pattern | 8 copper plates, 2 copper rings, 8 copper bolts |
| 2 copper rotors | `bBb / BRB / bBb` each | 8 copper blades, 2 copper rings, 8 copper bolts |
| 8 copper blades | two `P / P / I` crafts, 4 blades each | 4 copper curved plates, 2 copper rods |
| 16 fluid pipes | `CCC / rPr / CCC` | 6 bronze curved plates, 2 copper rotors, 1 glass pane |
| Compressor rods | direct Forge Hammer conversion | 2 more copper rods |

Forge Hammer conversion rates: **2 ingots → 1 plate or curved plate; 1 ingot → 1 rod or ring; 1 ingot → 2 bolts** for the copper/bronze recipes used here. Thus the compressor plus its unavoidable 16-pipe batch consumes **39 bronze ingots + 40 copper ingots + 1 glass pane + the workstation**; 13 pipes remain. Gear expansion is included, not an extra charge. Tooling, vanilla furnace/fuel and a steam container are separate.

For one test plate, reserve **1 additional bronze ingot**: total **40 bronze ingots + 40 copper ingots**. If making that bronze with the shipped hand-mix recipe, 14 batches use **42 copper dust + 14 tin dust → 42 bronze dust → 42 bronze ingots**, leaving 2 bronze ingots. With the retained 1 ingot → 1 dust recipes, starting metal stock is **82 copper ingots + 14 tin ingots**, plus workstation materials and, for the mandatory pre-consumption fire-clay reserve below, **24 brick items + 8 clay balls**. The hand-mix recipe yields **3**, not 4, bronze dust.

### Full fire-clay bill for one boiler
Do this while the workstation still exists, even if choosing bucket bootstrap and saving the boiler for later:

| Stage | Exact no-tool quantity |
|---|---|
| Hammer ordinary brick items | 24 `minecraft:brick` → 72 `brick_tiny_dust` (3 per brick) |
| Aggregate tiny dust | eight 3×3 crafts → 8 `brick_dust` (9 tiny dust per dust; centre is the exact MI tiny-dust item) |
| Mix fire clay | four `TC / TC` crafts: 8 clay balls + 8 brick dust → 12 `fire_clay_dust` |
| Smelt | 12 dust → 12 `fire_clay_brick` items, cookingtime 200 each |
| Build blocks | three `TT / TT` crafts → 3 `fire_clay_bricks` blocks |

**Three dust are not three blocks.** This bill starts with 24 ordinary brick items and 8 additional clay balls; obtaining/smelting those ordinary bricks and fuel is outside the supplied-stock bill. Before consuming the hammer, count all **72 tiny dust / 8 full dust / 12 fire-clay dust** at the appropriate stage, then all **3 finished blocks**. Do not substitute ordinary brick blocks.

### Boiler-first additions
One boiler is `#T# / #F# / BBB`: **4 bronze plates + 1 bronze tank + 1 supplied furnace + 3 fire-clay blocks**. The tank is `### / #G# / ###`: **8 bronze plates + 1 tagged glass block**. A wrench is `b.b / bbb / .b.`: **6 bronze plates**. Make those **18 additional bronze plates from 36 bronze ingots before the workstation is consumed**. This is one tank consumed by construction, not a spare transfer tank.

Including the compressor and one test ingot, the boiler-first route needs **76 bronze ingots + 40 copper ingots**, the workstation materials, **24 brick items + 8 clay balls**, **1 glass pane + 1 glass block**, **1 furnace consumed in the boiler**, an additional working smelting furnace, **1 water bucket**, and fuel. Hand-mixing 26 batches gives 78 bronze ingots from 78 copper dust and 26 tin dust, leaving 2 bronze ingots: total starting metals **118 copper ingots + 26 tin ingots** plus the workstation's vanilla components. Fuel is not included in this exact construction total; warm-up depends on operation and supply. Do not confuse a construction bill with a proven finite-fuel runtime run.

## Steps
1. Craft and place the Forge Hammer. Open it. Leave its optional hand-tool slot empty. Put the relevant ingots/bricks in the input, select the desired visible recipe, and take the output; inserting input alone does not craft it. Confirm each output name and quantity. The release source selects a recipe button and consumes inputs when its result is taken.
2. Make the full fire-clay chain above **before consuming the workstation**. Also finish the casing, copper gears, rods, blade/rotor batches and all 16 fluid pipes. For boiler-first, make the 18 extra plates, tank and wrench now. Keep the test ingot separate. If anything is short, do not assemble the compressor yet.
3. Empty the workstation's input/tool slots and recover it with the appropriate pickaxe; keep it as the `F` ingredient. Craft the compressor with `rFr / GCG / ppp`. Count 13 spare pipes. The Forge Hammer is consumed; it is not a reusable crafting remainder.
4. **Bucket branch, only with the effective recipe present:** smelt one water bucket into one steam bucket in the ordinary furnace. Retrieve the result. Do not use/right-click that bucket into the world to try to power a machine. Open the placed compressor with an empty hand. Leave lock mode OFF. Pick up the single steam bucket onto the cursor and **ordinary left-click the compressor's steam fluid slot**, then put the returned container in inventory. This is a GUI fluid-slot operation, not a world tank-click or an item-input placement. The source calls `tryEmptyContainerAndStow` on the carried item and updates the actual fluid slot only on success. **Checkpoint:** steam visible in that slot, at least 200 mB available, and the container/result accounted for. A nominal bucket is 1000 mB, but verify the displayed transfer; this packet did not run the NeoForge container implementation. If it fails, put the unchanged bucket away, close the GUI and stop this branch; do not scatter trial world clicks.
5. **Conditional transfer test — output-only eligibility unresolved:** MIInventory/TransferHelper establish neighbour selection and transfer order, but the required MIStorage extraction predicate is not retained. Do not treat the following control settings as proof of which fluids can leave storage. Proceed only as an isolated checkpoint test; stop additional fuel input if delivery disagrees. **Boiler-first branch / fallback:** use the prepared three fire-clay blocks, tank, furnace and four plates to craft the boiler. Place it with its east side initially clear. With the wrench in hand, **sneak + right-click the centre of the boiler's east face** to select east as its output. In its GUI, hover the fluid-auto-extract control and enable it; the source control toggles `extractFluids`, which defaults false for a new machine. Verify its ON tooltip rather than assuming adjacency alone enables delivery. Place the compressor immediately east of the boiler, touching that face. Open the boiler; with lock mode OFF, carry a water bucket and ordinary left-click its water input fluid slot. Account for the returned empty bucket and check visible water. Add valid fuel to its item input and wait for heat/steam production. **Checkpoint:** boiler water exists, fuel is being used/temperature changes, then compressor steam increases. Keep water supplied manually. The source boiler is output-side/auto-extract gated: do not read the book's “automatically sends” as unconditional all-side output.
6. Only after observing the steam checkpoint (the boiler branch remains subject to step 5’s unresolved output-only eligibility), put **exactly 1 bronze ingot** in the compressor item input, leaving output space empty and no overclock catalysts installed. The shipped `materials/bronze/compressor/main` recipe is **1 ingot → 1 bronze plate, 2 EU/t, duration 100**, nominal energy **200 EU = 200 mB steam**. Wait for completion, take the plate and check no extra ingots were queued. Do not use the distinct `compressor/plate` recipe, which consumes an existing plate to make a curved plate.
7. Stop with the plate and container inventory accounted for. For a sustained water supply, use the separately qualified [pump feed procedure](mi-pipe-workcell.md). Do not attach a large mixed-fluid network to this first test.

The inspected auto-extract callee queries only the adjacent selected-output neighbour, on its opposite face, and delegates simulated drain/fill followed by execution. However, output-only eligibility still depends on the storage extraction chain: retained MIFluidStorage delegates to extract, while its MIStorage implementation is not retained. **Downstream gate:** output-only filtering is not fully established by this packet; the closed-feed path remains a conditional test, not a complete static transfer trace. Stop at any failed steam/water checkpoint; adjacency alone is not acceptance.

## Expected result
A source-supported **conditional static first-plate procedure**, with complete MI construction quantities and two explicitly distinct bootstrap branches. The required in-game checkpoint is one collected bronze plate and visible steam consumption, **not observed here**. The boiler-first fallback remains conditional on step 5’s unresolved output-only eligibility and removes only the dehydration recipe dependency, but does not prove effective tags, valid fuel availability or actual production. If either branch disagrees with the current recipe viewer or GUI, this task remains blocked at that checkpoint.

## Common failures
- Only tiny brick dust: intended. Nine tiny dust make one full dust; do not feed tiny dust directly to the fire-clay craft.
- No brick dust after consuming the hammer: build another workstation from 3 pressure plates + 4 iron ingots, or return to a separately evidenced machine route; no refund/remainder is promised. Prevent this by finishing all preparation first.
- No steam-bucket smelting recipe: use boiler-first **only if its plates/tool were prepared**, otherwise build a replacement workstation. This is an honest higher-cost fallback, not an invented recipe.
- Fluid click only locks a slot: exit lock mode, restore the carried container to inventory, recheck the identified fluid input. No successful transfer means no permission to continue the test.
- Boiler hot but compressor empty: step 5’s output-only eligibility remains unresolved; these checks cannot establish the missing storage policy. Stop additional fuel input if delivery remains unproved. check water, actual steam output, east output marking and the fluid-auto-extract ON tooltip. The compressor accepts steam input from any side according to the shipped guide; rotating its front is not the repair.
- Avoid breaking running machines to “reset” them. Stored-fluid recovery on break is not proved here. The book warns that breaking a machine with a wrench does not drop it; use a pickaxe for empty-machine relocation.
- Trade-off: bucket bootstrap saves pre-steam boiler plate work but depends on a conditional smelting recipe/container integration. Boiler-first costs 36 extra bronze ingots for the boiler plates plus output-setting wrench, but has no dependence on steam-bucket smelting.

## Sources
Exact archive recipe witnesses:
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/forge_hammer.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/forge_hammer/brick_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/brick/craft/dust_from_tiny_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/fire_clay_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/fire_clay/smelting/dust_to_ingot_smelting.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/fire_clay_bricks.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/steam_age/bronze/compressor_asbl.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/steam_age/bronze/machine_casing_asbl.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/craft/gear.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/craft/gear.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/craft/rotor.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/craft/blade.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/steam_age/fluid_pipe_asbl.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_plate.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_curved_plate.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_rod.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_ring.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_bolt.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/forge_hammer/ingot_to_plate.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/forge_hammer/ingot_to_curved_plate.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/forge_hammer/ingot_to_ring.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/forge_hammer/ingot_to_bolt.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/copper/forge_hammer/ingot_to_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/tin/forge_hammer/ingot_to_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze_dust.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/smelting/dust_to_ingot_smelting.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/steam_age/bronze/boiler_asbl.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/craft/tank.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/tools/wrench.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/vanilla_recipes/steam_bucket.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze/compressor/main.json`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/steam_machines.md`

Pinned primary source: [Forge Hammer recipe selection and consumption](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/blocks/forgehammer/ForgeHammerScreenHandler.java#L253-L344); [GUI carried-container click](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/inventory/ConfigurableScreenHandler.java#L109-L144); [fluid transfer and result](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/inventory/ConfigurableFluidStack.java#L280-L324); [boiler water and output tick](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/machines/blockentities/BoilerMachineBlockEntity.java#L73-L143); [output direction](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/machines/components/OrientationComponent.java#L95-L110); [auto-extract click](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/client/java/aztech/modern_industrialization/client/machines/guicomponents/AutoExtractClient.java#L60-L111); [server toggle](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/network/machines/SetAutoExtractPacket.java#L45-L63); [steam conversion](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/machines/helper/SteamHelper.java#L33-L53).


Pinned transfer supplement: [selected neighbour callee](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/inventory/MIInventory.java#L104-L110); [delegated simulated and executed transfer](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/util/TransferHelper.java#L152-L178); [overlay dispatch to orientation](https://github.com/AztechMC/Modern-Industrialization/blob/2d2b25dc45043375de1126e703b96ace950d8324/src/main/java/aztech/modern_industrialization/machines/MachineBlockEntity.java#L171-L181).
