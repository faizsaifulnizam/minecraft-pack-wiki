---
layout: default
title: "FULL SPOILERS"
permalink: /full/character-notes-c/
baseline: dev-0.5-20261015-r2
---
<!-- wiki.py managed full human schema=1 -->
**FULL SPOILERS**

WARNING: FULL SPOILERS. Direct links, reload and history may reveal everything here; this distinct full-human route is exempt from ordinary-entry consent/reset guarantees.

[Return to safe entry](/minecraft-pack-wiki/reference/character-notes-c/)

# Character notes C

> **FULL SPOILERS** — encounter identities, abilities and structure IDs follow. [Return to the safe character-helper route](/minecraft-pack-wiki/guides/character-tools/).

## Baseline
This is an bounded statically reviewed revision for candidate **dev-0.5-20261015-r2**, not an applied replacement for dev-0.5-20261015. New core text corresponds only to Tensura archive SHA-256 `2309a22ceb7e423e2f3212ea87686ccc510fe0003595500037e0b6c64baef213`. The original baseline/pins remain unchanged. Static descriptions and feedback are not runtime or award-handler proof.

Tensura Boss Structure 1.0.3.3 and TenSura: Not Enough Bosses 2.0.0.3. Reference for planning exploration, not a boss-clear or reward tutorial.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.
Documented-static resource declarations. Structure generation, actual encounters, kill credit, loot resolution and progression awards were not tested. Spawn templates and boss AI were not executed or fully traced. New candidate-core advancement resources identify some event criteria, but not their emitters; no encounter-to-awakening award route has been established.

## Separate the addons' jobs
Boss Structure metadata says it adds custom boss structures. NEB metadata says it adds bosses. Structure IDs and NEB entities are not interchangeable award conditions; their co-presence does not prove that a particular structure spawns a particular boss or grants an evolution reward.

## Placement lookup
The selected structure-set objects use minecraft:random_spread. These are spacing/separation parameters in the serialized placement definition, not a guaranteed distance from you, a waypoint, or proof that a structure exists in already generated terrain.

| Structure ID | Spacing | Separation |
|---|---|---|
| `tensura_boss_structure:beast_kingdom_of_eurazania` | 200 | 50 |
| `tensura_boss_structure:hinata_church` | 200 | 50 |
| `tensura_boss_structure:night_rose` | 200 | 50 |
| `tensura_boss_structure:orc_disaster_temple` | 200 | 50 |
| `tensura_boss_structure:rimuru_ogre_fight` | 200 | 50 |
| `tensura_boss_structure:shizhu_school` | 200 | 50 |

For **tensura_boss_structure:hinata_church**, the structure object declares minecraft:jigsaw, start pool tensura_boss_structure:hinata_church/start_pool, size 1, maximum distance from center 80, WORLD_SURFACE_WG height projection and biome tag #forge:has_structure/hinata_church. The set's salt is 87654321. This identifies a resource accurately; it is not a natural-spawn guarantee or a player instruction to use administrator locate/teleport commands.

## Read a threat profile without inventing a strategy
The exact NEB Carrion entity-existence object declares **minimum Aura 500,000**, **maximum Aura 525,000**, **minimum Magicules 100,000**, **maximum Magicules 125,000** and **Spiritual Health 3,000**. Its abilities include Royal Beast, Magic Sense, physical-attack resistance, magic resistance, multiple elemental resistances, Elephant Stampede, Roaring Lion Punch and Aura Slash. These are declared resource values; no HP conversion, actual initialized values or resist multiplier was measured. Do not turn them into a recommended character level or promise that an unlisted damage type bypasses the encounter.

## Steps for a returning explorer
1. Use the table to identify the exact resource name relevant to an encounter report, not to infer an awakening gate.
2. Before entering an unfamiliar structure, keep an ordinary route back outside and avoid testing an unverified transport, skill, or reset as your only exit. This is general safety advice, not a claim that a named structure traps you.
3. If you encounter a named boss, separate what you observe from what the resource declares. Record the identity and available retreat route before attempting a fight; this chapter supplies no safe-clear strategy or validated power threshold.
4. After any fight, inspect actual inventory and progression messages rather than treating an advancement's display relationship or a boss identity as guaranteed loot, kill credit or an evolution award.

## Expected result
You can identify the selected structures and one concrete threat declaration without fabricating spawn, combat, loot or progression outcomes. First entry, survival and successful retreat remain runtime checks.

## Common failures
- Nothing appears where a spacing value suggests: the table is not a coordinate map. Biome eligibility, generation, template completion and existing terrain are unresolved here.
- Defeating a boss gives no expected awakening: this lane has not established such an award. Do not assume a missing parent advancement is the cause.
- Your character dies or a subordinate receives credit: death recovery and integration kill-credit semantics were not traced. Do not claim a fixed recovery or reward rerun from this resource table.

## Sources
Tensura Boss Structure 1.0.3.3: META-INF/neoforge.mods.toml; six selected data/tensura_boss_structure/worldgen/structure_set objects and worldgen/structure/hinata_church.json. NEB 2.0.0.3: META-INF/neoforge.mods.toml and data/tensura_neb/entity_existence/carrion.json. Claims CHAR-023, CHAR-024 and CHAR-025.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [CHAR-023] `tensura_boss_structure-1.0.3.3.jar!META-INF/neoforge.mods.toml`: `mods[0].description`.
- [CHAR-023] `tensura_neb-neoforge-2.0.0.3.jar!META-INF/neoforge.mods.toml`: `mods[0].description`.
- [CHAR-024] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure_set/beast_kingdom_of_eurazania.json`: `placement; structures`.
- [CHAR-024 / REV-12 (corrected)] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure/hinata_church.json`.
- [CHAR-024] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure_set/night_rose.json`: `placement; structures`.
- [CHAR-024] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure_set/orc_disaster_temple.json`: `placement; structures`.
- [CHAR-024] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure_set/rimuru_ogre_fight.json`: `placement; structures`.
- [CHAR-024] `tensura_boss_structure-1.0.3.3.jar!data/tensura_boss_structure/worldgen/structure_set/shizhu_school.json`: `placement; structures`.
- [CHAR-025] `tensura_neb-neoforge-2.0.0.3.jar!data/tensura_neb/entity_existence/carrion.json`: `$`.
