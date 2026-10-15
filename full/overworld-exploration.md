---
layout: default
title: "FULL SPOILERS"
permalink: /full/overworld-exploration/
baseline: dev-0.5-20261015-r2
---
<!-- wiki.py managed full human schema=1 -->
**FULL SPOILERS**

WARNING: FULL SPOILERS. Direct links, reload and history may reveal everything here; this distinct full-human route is exempt from ordinary-entry consent/reset guarantees.

[Return to safe entry](/minecraft-pack-wiki/reference/overworld-exploration/)

# Overworld exploration reference

FULL SPOILERS — structure names, quest-map destinations and trade implementation details follow.

## Baseline
Private candidate-r2; unapplied, not canonically adopted. Dungeons and Taverns v4.4.4 retained candidate text, not observed world generation. This is an overworld reconnaissance / tavern-map slice, not a guide to every dungeon, key, boss, Nether or End structure. [Preparation](/minecraft-pack-wiki/guides/exploration-preparation/) remains the safe starting point.

## Evidence status
Structure and structure-set JSON prove declarations, not the contents of your world. Functions prove written commands, not that the commands ran or their selectors matched. Advancement parents describe tree structure unless criteria independently enforce a dependency. The selected command chain is stronger evidence than a translation hint, but datapack loading, overrides, effective biome tags, generation and live NPC offers are still unknown. No copied map, world coordinate or seed was used.

## Prerequisites
A replaceable scouting kit, spare recovery equipment and a route you can retrace without these documents supplying a location. For an already-encountered tavern cartographer, read its **currently displayed** offers before spending anything. Do not assume an NPC has the implementation tag, that an offer is available, or that a map implies an easy destination.

## Steps
1. Choose an achievable reconnaissance objective: inspect a naturally encountered tavern from outside, or identify an entrance without committing to a dungeon. Do not equate “Safe Haven” advancement wording with a cleared building or immunity to local hazards.
2. Understand the selected generation declarations before making a search plan:

| Selected declaration | What it actually says | What it does not prove |
| --- | --- | --- |
| `tavern_oak` structure | Jigsaw; start pool `nova_structures:tavern_start_oak`; biome tag `#nova_structures:collections/oak_structure_biomes`; `surface_structures`; heightmap `WORLD_SURFACE_WG`; size 6 and max distance 80 | An oak tavern near you, safe inhabitants, a chest layout, or eligibility in an effective merged biome set. [S1] |
| `taverns` structure set | Eleven named variants, each weight 1; random spread spacing 40, separation 15, salt 783; exclusion zone against `minecraft:villages` with `chunk_count:10` | These placement parameters are not “one tavern every 40 chunks,” exact travel distance, a grid you can copy, or equal observed biome frequency. [S2] |
| `undead_crypt` structure | Jigsaw, biome tag `#nova_structures:collections/stronghold_related_ruins_biomes`; `underground_structures`; start pool `nova_structures:undead_crypt_spawner`; start height absolute 0, dimension padding bottom 3 / top 238; size 4, max distance 100 | A guaranteed accessible entrance at a fixed depth or a safe excavation route. [S3] |
| `undead_crypt` structure set | One named structure with random spread spacing 100, separation 20, salt 96586859 | A guaranteed crypt within a radius or that already-generated chunks contain it. [S4] |

3. If you already reach a tavern, compare the two visible advancement definitions. `find_tavern` uses location criteria for any of the eleven variants. Its description suggests trading once to unlock a map, but the location award itself has **no reward function**. `adventure/tavern_quest` has `find_tavern` as parent; its actual criterion is a villager trade with NBT tag `dnt_quest_trader`, with no explicit `find_tavern` predicate or reward function. A parent edge is not the map-generation handler. [S5–S6]
4. The separate implementation advancement `minecraft:give_quest_trader_trade` checks a trade with the same tagged villager and declares reward function `nova_structures:choose_dnt_quest_trader`; its parent is `nova_structures:root`. This is the actual written dispatch chain to inspect when a map offer is missing, not the visible quest node alone. The parent ID is present in the retained candidate index; complete ancestor/predicate closure and effective datapack loading remain unverified. Do not carry an older archive's missing-parent diagnosis into this candidate. [S7]
5. **Only when such an offer is actually shown and you choose to buy it**, budget against the written implementation, not a guessed universal shop price. `choose_dnt_quest_trader` selects the nearest villager tagged `dnt_quest_trader` and not `trader`, invokes `add_trade`, then revokes `minecraft:give_quest_trader_trade` for `@a`. `add_trade` prepends an offer, generates `nova_structures:tavern_quest` loot into the NPC's main hand and copies that stack to the sell slot, then calls `add_trade2`, which prepends another such offer and tags the NPC `trader`. Both written offers cost **14 emeralds plus 1 compass**, with `maxUses:1`. These are conditional command effects, not a guarantee of two working offers, repeated refreshes, a particular villager match, or per-player restocking. Do not execute commands or manipulate tags yourself. [S8–S10]
6. Read the resulting map item's name before choosing a destination. The handler references the **root** `loot_table/tavern_quest.json`, which rolls once among thirteen table references. Each selected referenced map table declares one map and an exploration-map destination, `zoom:4`, `skip_existing_chunks:false`, plus component naming and the shared loot modifier reference. This is a possible destination menu, **not an ordered quest chain, guaranteed generated target, unique treasure, safe route or a copied map**. [S11, M1–M13]

| Map table suffix | Declared destination | Citation |
| --- | --- | --- |
| `jungle_ruin` | `nova_structures:jungle_ruins` | [M1] |
| `undead_crypt` | `nova_structures:undead_crypt` | [M2] |
| `stray_fort` | `nova_structures:stray_fort` | [M3] |
| `creeping_crypt` | `nova_structures:creeping_crypt` | [M4] |
| `desert_ruin` | `nova_structures:desert_ruins` | [M5] |
| `ancient_city` | `minecraft:ancient_city` | [M6] |
| `illager_hideout` | `nova_structures:illager_hideout` | [M7] |
| `badlands_miner_outpost` | `nova_structures:badlands_miner_outpost` | [M8] |
| `witch_villa` | `nova_structures:witch_villa` | [M9] |
| `illager_manor` | `nova_structures:illager_manor` | [M10] |
| `trident_trial_monument` | `nova_structures:trident_trial_monument` | [M11] |
| `lone_citadel` | `nova_structures:lone_citadel` | [M12] |
| `toxic_lair` | `nova_structures:toxic_lair` | [M13] |

7. Do not confuse that chain with `loot_table/chests/tavern_quest.json`: the latter embeds map entries directly, while `add_trade` and `add_trade2` name `nova_structures:tavern_quest`, not `nova_structures:chests/tavern_quest`. No caller for the chest-named variant is established here. The shared `item_modifier/loot_modifier.json` is an empty array in this candidate; it does not prove absence of external overrides or every other loot modification. [S12–S13]
8. Survey a destination's exterior first; postpone underground descent, sealed doors and unidentified triggers until you have supplies and a retreat. No key acquisition chain, boss trigger, room-clear reward, chest placement or complete loot catalogue is proved by this slice. Bank a map or other valuables before extending the trip when practical. If you die, re-equip and use the known route; no map replacement, grave safety, item permanence or automatic return is promised.

## Expected result
A bounded overworld search plan, a distinction between a visible advancement and the written map-offer handler, and a complete reference to the thirteen destinations of the **selected** tavern trade table. Not full Dungeons and Taverns coverage, not terrain-family completion and not runtime acceptance.

Useful tip: inspect the current offer and resulting map name before planning an expedition. Benefit: avoids assuming the reward points to a chosen dungeon or that a similar chest-table filename is the active trade route. Trade-off: you may choose not to buy an unpredictable destination, and no target or successful lookup is guaranteed.

## Common failures
- **No tavern appeared after walking a placement interval.** Spacing and separation are generator inputs, not a spawn promise; effective biome eligibility, resource order, existing terrain and runtime generation are unknown.
- **The quest toast should create a map offer.** Its display node has no rewards; the separate implementation advancement and command chain must actually load and run.
- **The shop will refresh forever.** The implementation both tags a selected NPC and revokes an implementation advancement for all players; that is not a verified unlimited-restock contract.
- **A model called a key proves the key opens this door.** Models, structure declarations and advancement parents do not prove lock handlers. No key or boss activation procedure is invented here.

## Sources
Citations identify exact candidate archive entries:
- [S1] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/worldgen/structure/tavern_oak.json`.
- [S2] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/worldgen/structure_set/taverns.json`.
- [S3] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/worldgen/structure/undead_crypt.json`.
- [S4] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/worldgen/structure_set/undead_crypt.json`.
- [S5] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/advancement/adventure/find_tavern.json`.
- [S6] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/advancement/adventure/tavern_quest.json`.
- [S7] `dungeons-and-taverns-v4.4.4.jar!data/minecraft/advancement/give_quest_trader_trade.json` — root presence is index-only context, not complete root-content review.
- [S8] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/function/choose_dnt_quest_trader.mcfunction`.
- [S9] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/function/add_trade.mcfunction`.
- [S10] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/function/add_trade2.mcfunction`.
- [S11] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/tavern_quest.json`.
- [S12] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/chests/tavern_quest.json`.
- [S13] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/item_modifier/loot_modifier.json`.
- [M1] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/jungle_ruin.json`.
- [M2] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/undead_crypt.json`.
- [M3] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/stray_fort.json`.
- [M4] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/creeping_crypt.json`.
- [M5] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/desert_ruin.json`.
- [M6] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/ancient_city.json`.
- [M7] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/illager_hideout.json`.
- [M8] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/badlands_miner_outpost.json`.
- [M9] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/witch_villa.json`.
- [M10] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/illager_manor.json`.
- [M11] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/trident_trial_monument.json`.
- [M12] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/lone_citadel.json`.
- [M13] `dungeons-and-taverns-v4.4.4.jar!data/nova_structures/loot_table/maps/toxic_lair.json`.
