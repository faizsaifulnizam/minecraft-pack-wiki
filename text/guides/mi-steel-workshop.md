<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/mi-steel-workshop/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Plan the coke-to-steel continuation

## Baseline
Private candidate **dev-0.5-20261015-r2**, unapplied; canonical baseline unchanged. Modern Industrialization 2.5.10 and AlmostUnified 1.21.1-1.4.2. This is a bounded static curriculum, not pack-wide or runtime acceptance.

## Evidence status
Selected exact-archive recipes and shipped prose, supplemented only where explicitly identified by pinned primary source. Recipes below describe shipped defaults, not resolved runtime recipes. Effective tags, resource precedence, generated recipes and active server configuration remain unverified. Reviewed against retained static evidence; not runtime-tested.

## Prerequisites
A functioning [steam workcell](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/mi-pipe-workcell/), coal, iron, macerator, mixer access and resources for two multiblocks. Use the in-game structure preview for exact block placement; the retained prose does not encode every coordinate or orientation.

## Steps
These are advanced conditional planning/reference notes, not a completed executable production tutorial. The whole-wiki/tutorial goal remains unchanged and incomplete.

1. **STOP before construction:** retain exact controller/hatch/component bills and coordinate/orientation-complete structure proof first. The following are shipped reference counts, not a costed construction tutorial. Build a Coke Oven controller, **21 Bricks** and three mandatory bronze hatches: item input, item output, fluid input. The guide counts 24 replaceable structure blocks, three occupied by these hatches. An optional fluid output hatch collects creosote; do not treat adding it as permission to increase the shape size.
2. Place the structure using its preview. Hold a wrench to see missing blocks/errors, or a hatch to see allowed positions. Proceed when the controller reports **Shape Valid**, not merely when its outer silhouette looks right.
3. Send steam to the fluid input hatch and coal to the item input hatch. Retrieve coke from item output. Controllers generally are not the material I/O interface; the guide directs all inputs and outputs through hatches. Creosote is a chanced output and is voided without room, so fit fluid output/storage before the run if collecting it matters.
4. **STOP before preparing a steel batch:** exact coke-to-dust, uncooked-steel mixture, selected machine recipe and output quantities must be proved first. Macerate coke into Coke Dust; combine that with iron into Uncooked Steel Dust. The guide says the mixer improves the ratio, but this packet does not retain the exact mixture recipe. Read its current quantities before batching; do not infer them from ordinary bronze ratios.
5. Craft a Steam Blast Furnace controller, **29 Fire Clay Bricks** and the same three mandatory hatch types. Its structure follows the Coke Oven with fire clay replacing brick and an extra hollow layer on top. Use the preview and missing-block diagnostics for actual placement.
6. **STOP before feeding the furnace:** require the exact named steel recipe ID, input/output quantities, steam amount, duration and validated hatch/control procedure. A viewer request is remaining evidence work, not a supplied recipe. Feed the valid furnace through its input hatches with steam and the uncooked steel recipe, and check its output for steel before scheduling more coke. Exact steam amount, duration and steel output count are unresolved, so first process only the viewer's single batch.
7. After obtaining steel, optionally craft a Steel Upgrade: the guide supports applying it in a crafting table or sneaking/right-clicking a placed bronze machine with the upgrade. Upgraded machines support up to 4 EU/t and speed recipes up only within that ceiling. Recheck supply before upgrading the workcell.
8. Continue to [MI electricity](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/mi-lv-production/), or keep a steel Packer for simple repeated crafts such as double ingots and pipes. Its available recipes must be checked in the current viewer; this is not universal crafting automation.

## Expected result
An advanced planning/reference continuation with shipped structure counts and blocked batch checkpoints, not evidence of constructed multiblocks or a delivered first steel batch. It is not a coordinate-complete multiblock schematic or a fully costed steel production line.

## Common failures
- Shape invalid: check mandatory hatches and preview positions. Sending steam into the controller is not the documented input route.
- Coke works, steel does not: verify uncooked steel preparation, fire-clay structure and extra hollow layer independently before changing fuel infrastructure.
- Lost creosote: the source describes voiding the chanced output without room. Do not promise recovery of previously voided fluid.
- Tip: one steel hatch upgrades a multiblock to steel tier according to the guide; higher speed also raises supply demand. A steel boiler's maximum doubles to 16 EU/t, not unlimited steam.
- Keep an Automatic Trash Can away from this first line: the guide says piped items/fluids are destroyed. It is not a safe diagnostic sink.

## Sources
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/coke_oven.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/steel.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/steel_machines.md`
