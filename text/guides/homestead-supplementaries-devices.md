<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-supplementaries-devices/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Add a faucet and bellows to the workshop

## Baseline
Candidate r2 is unapplied. This Supplementaries 3.6.7 slice selects **two useful devices**: a faucet item-output task and adjacent-furnace bellows. It is not a catalogue or an automation compatibility promise.

## Evidence status
Exact-release recipes establish materials and explicit feature-flag conditions.[1][2] Local English text names the blocks and their sound subtitles but does not describe transfer or acceleration algorithms.[3] Functional procedures therefore use the author's Redstone Blocks wiki, edited October 11, 2026, **not release-pinned to 3.6.7**.[4] Treat these as documented mechanics to check on a small setup, not a tested result for this candidate. No settings, world, logs or game classes were inspected.

## Prerequisites
- Faucet: **1 wooden-rod-tag input plus 4 iron-ingot-tag inputs → 1 Faucet**.[1]
- Bellows: **6 wooden-slab-tag inputs plus 2 leather → 1 Bellows**.[2]
- A spare inventory with one expendable item, a clear collection area beneath the faucet nozzle, and an already usable furnace for the bellows check. These are author-recommended low-risk test fixtures, not certified cross-mod integration.
- A controllable redstone source for bellows; its recipe and controls are not authored here. Leave the faucet unpowered for its initial handle test so that documented redstone inversion does not obscure the state.[4]

## Steps
### Output a small item sample with a faucet
1. Craft the faucet with rows `empty, wooden rod, empty`; `iron, iron, iron`; `empty, empty, iron` (` 1  / 222 /   2`). The shipped output is one faucet and its NeoForge condition requires the `faucet` flag.[1]
2. Set it above the spare inventory as described by the author's **item** mechanic, with its nozzle output location clear. Do not confuse that with the separate **fluid** arrangement, whose source sits behind the faucet. The wiki says items come from the inventory below and spill directly below the nozzle.[4]
3. Put one expendable item in the source, then interact with the handle to activate. The author documents a one-second output interval; the checkpoint is the source losing the sample and the item appearing under the nozzle.[4] This interval is supplemental documentation, not a selected-release measurement. Collect the sample; leave valuable storage disconnected until this direction is confirmed.
4. With the faucet still unpowered, interact with the handle again to request stop. Put the collected expendable item back into the source; an empty source cannot prove shutdown. Keep the setup loaded and observe that the replenished sample remains in the source and no item appears under the nozzle for at least three documented one-second output intervals (at least three seconds). This is an author-recommended checkpoint based on the unversioned wiki, not a release-pinned timing guarantee or a test performed here. If the sample leaves, or timing/loading is uncertain, the off state is not established: keep valuable storage disconnected and recover the expendable sample. If you later add redstone, note that power **inverts** active/non-active status rather than being documented here as a simple always-on switch.[4]

### Apply bellows to an adjacent furnace
5. Craft bellows with rows `slab, slab, slab`; `leather, empty, leather`; `slab, slab, slab` (`000 / 1 1 / 000`). The shipped output is one bellows and its NeoForge condition requires the `bellows` flag.[2]
6. Place the bellows directly adjacent to the furnace with the air-facing front toward the intended target. The author documents facing any direction, blowing air when powered, and speeding furnace-like blocks right next to it.[4] No effect on the Farmer's Delight Cooking Pot is claimed; return to [the pot heat check](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-cooking-pot/) for cooking rather than borrowing a furnace claim.
7. Use a small normal smelting batch and a controllable redstone supply. Compare the furnace progress while powered and unpowered with otherwise equivalent inputs/fuel. Expect documented acceleration if that furnace is supported; no multiplier or fuel saving is promised.[4] This is a player checkpoint, not a test this authoring session ran.
8. Remove power after checking. Keep entities away from the front: the same wiki documents pushing entities up to five blocks away and sustaining fire in front within two blocks.[4] Do not point it at exposed fire or an occupied walkway for the homestead task.

## Expected result
The first task yields an observed item-output direction and a bounded manual-stop checkpoint only if the replenished sample remains through the observation window and the documented faucet mechanic applies. This does not prove permanent shutdown; if the checkpoint fails or cannot be completed, the off state is not established. The second yields a recipe-backed bellows and a small supported-furnace comparison.[1][2][4] Neither establishes universal inventory/fluid compatibility or integration with decorative replacement blocks. Use [storage choices](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/storage-choice/) for organization and [Chipped sample work](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-chipped-workstations/) for appearance, not as evidence of device compatibility.

## Common failures
- **Recipe absent**: both recipes have feature-flag conditions. Check [current recipe availability](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/); do not edit configuration or assume a shipped file necessarily loads.[1][2]
- **Faucet on/off seems reversed**: disconnect power for the initial handle check. The documented power behavior is inversion, so power and handle state need to be considered together.[4]
- **Item fails to appear**: recheck the inventory-below/item-output-under-nozzle arrangement and your single sample. A fluid source behind is a different documented task; no universal inventory support is promised.[4]
- **Bellows sounds but furnace does not accelerate**: recheck direct adjacency and air-facing orientation, then compare with a basic furnace before blaming fuel or spending more materials. “Furnace-like” is documentation, not a list of all compatible mod machines.[4]
- **Conditional tip — isolate power during commissioning**: if a shared redstone line is hard to reason about, use a separate controllable supply for the first bellows test and no faucet power. Benefit: distinguish placement/compatibility from faucet inversion; trade-off: temporary extra setup. The inversion and powered blowing are documented; this isolation is an author recommendation.[4]
- **Optional fluid extension, not delivered as a full task**: the wiki describes fluid sources behind, destination containers below, and 250 mB increments.[4] Accepted fluids, exact destination capacity, voiding behavior and pack-specific integrations need more evidence. Do not route valuable fluids based on this item-only starter.

## Sources
[1] `supplementaries-neoforge-1.21.1-3.6.7.jar!data/supplementaries/recipe/faucet.json`.
[2] `supplementaries-neoforge-1.21.1-3.6.7.jar!data/supplementaries/recipe/bellows.json`.
[3] `supplementaries-neoforge-1.21.1-3.6.7.jar!assets/supplementaries/lang/en_us.json` — `block.supplementaries.faucet`, `block.supplementaries.bellows`, `subtitles.supplementaries.faucet.turn`, `subtitles.supplementaries.bellows.blow`.
[4] [Author's Redstone Blocks wiki](https://github.com/MehVahdJukaar/Supplementaries/wiki/Redstone-Blocks) — supplemental wiki edited October 11, 2026, not pinned to 3.6.7; Faucet and Bellows sections.
