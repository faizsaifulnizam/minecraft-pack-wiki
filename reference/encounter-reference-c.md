---
layout: default
title: Encounter reference C
permalink: /reference/encounter-reference-c/
baseline: dev-0.5-20261015-r2
---

# Encounter reference C

## Baseline

FULL SPOILERS. Bosses of Mass Destruction 1.3.3, Minecraft 1.21.1; documentation baseline. Return to [encounter readiness](../guides/encounter-readiness.md) for the spoiler-safe preparation task.

## Evidence status

The local archive supplies exact declaration evidence for the Night Lich tower, defeat criterion and loot table. Public primary commit `1a7bd955d201d1b4d066157b8335cd967677e209` declares version 1.3.3 and Minecraft 1.21. Five selected JSON objects match the archive semantically, not byte-for-byte. This strengthens selected data correspondence; it does not prove that compiled item/entity handlers match that commit. The controls below describe that pinned source, not verified installed behavior. This page delivers a conditional readiness/result-comparison task, not a complete combat or exact summon tutorial. [S1–S7]

## Prerequisites

- Complete [encounter readiness](../guides/encounter-readiness.md).
- For result comparison, an encounter independently undertaken by the party and actual observed inventory/advancement information. Nothing here requires initiating combat to inspect the documentation.
- For any later activation task: separately confirmed Soul Star supply, exact installed controls, site geometry, permission, server difficulty and a viable return. These are not established here. Do not craft an improvised altar from the source offsets or spend a star to test the handler.

## Steps

1. **Separate site eligibility from a found encounter.** The tower declaration is a jigsaw structure using `#bosses_of_mass_destruction:has_structure/lich_tower`; its tag includes `#bosses_of_mass_destruction:collections/cold`. That nested tag's effective members are not resolved here. The structure set writes spacing 100 and separation 50 with random-spread placement. These values are not a guaranteed nearby tower or a walking-distance instruction. An empty monster spawn override is not an encounter summon handler. [S2–S4]
2. **Understand the unverified control before committing resources.** In the pinned 1.3.3 source, the registered `soul_star` item uses `SoulStarItem`. Its use-on-block branch selects an unlit chiseled stone altar, marks it lit and shrinks the held stack by one. Relative candidates are rotations of `(12,0,0)` and `(6,0,6)` from the clicked altar. Exactly three lit candidates schedule altar destruction and a `spawnLich` call after 20 ticks. This is a code predicate, not proof that four arbitrary blocks form a working installed summon. Client success effects do not prove the server call completed. **Do not invoke this as an exact installed recipe until handler correspondence and actual site geometry are established.** [S7]
3. **Budget navigation separately from activation.** In that same unverified handler, use away from an altar attempts `findNearestMapStructure` through a structure tag. Only when a target is found does the server create a flying item entity and shrink a noncreative stack. The selected evidence does not close that target tag or the flying entity's return/break lifecycle. Do not assume a free locator, guaranteed target or refunded star. [S7]
4. **After an independently completed fight, compare the advancement separately from drops.** The shipped challenge criterion is `minecraft:player_killed_entity` with entity type `bosses_of_mass_destruction:lich`. It has no reward object. This is not proof that every participant gets credit or that the displayed parent is a combat access gate. Check each player's actual notification/progress rather than inferring team-wide completion. [S5]
5. **Compare collected items with the declared table, not a promised payout.** The entity table writes one roll for 2 Ancient Anima, one roll for 3–6 bones, one roll for 5–7 diamonds and five book rolls with `enchant_with_levels` level 30 and `treasure:true`. These are table values, not a guarantee of five usable books or any installed drop. Effective table loading, entity death dispatch, overrides, pickup, loss and permissions remain distinct. Do not treat this table as advancement rewards or personal Lootr loot. [S6]
6. **Finish the comparison with a bounded conclusion.** Record separately: site encountered, activation observed, entity encountered, player credit observed, items seen, items collected, and party returned. An unobserved step stays unknown. Return and organize what was actually collected; leave refund/respawn/recovery claims unasserted.

## Expected result

A readiness/result record distinguishes a possible structure, an upstream-described control, a player-kill criterion and a separate reward declaration. The complete static task is interpretation and comparison; exact entry→summon→combat→reward→return execution remains unproved.

## Common failures

- **No site:** eligibility and random placement do not guarantee one in explored terrain. Do not exhaust supplies on an unverified locator target.
- **Star spent, no visible boss:** the source mutates altar state and consumes before scheduling spawn. Repeated spending is not a proven repair. Preserve supplies, withdraw, and ask the host to establish actual handler/settings behavior.
- **Leaving did not reset it:** the pinned entity delegates despawn handling to `MobUtils.preventDespawnExceptPeaceful`; that helper's implementation and effective difficulty are not verified here. Retreat is not a demonstrated reset/refund. [S8]
- **No credit or no loot:** advancement credit and entity loot are independent. A table declaration is not dispatch proof; a missed notification is not proof of an empty table. Do not promise reruns will fix either.
- **Death on approach or collection:** no exact death persistence, grave protection, despawn timer or safe rescue route is established. Decide whether another recoverable kit is worth risking; do not guarantee retrieval.

**Tip/trade-off:** keep locator and activation budgets separate. The upstream handler has different consumption branches; reserving supplies can prevent an exploratory trip from spending the intended activation budget, but the exact required total and supply route are still unknown. This is planning advice, not an instruction to test either branch.

## Sources

- [S1] `BOMD-NeoForge-1.21-1.3.3.jar!META-INF/neoforge.mods.toml`.
- [S2] `BOMD-NeoForge-1.21-1.3.3.jar!data/bosses_of_mass_destruction/worldgen/structure/lich_tower.json`.
- [S3] `BOMD-NeoForge-1.21-1.3.3.jar!data/bosses_of_mass_destruction/worldgen/structure_set/lich_tower.json`.
- [S4] `BOMD-NeoForge-1.21-1.3.3.jar!data/bosses_of_mass_destruction/tags/worldgen/biome/has_structure/lich_tower.json`.
- [S5] `BOMD-NeoForge-1.21-1.3.3.jar!data/bosses_of_mass_destruction/advancement/adventure/night_lich_defeat.json`.
- [S6] `BOMD-NeoForge-1.21-1.3.3.jar!data/bosses_of_mass_destruction/loot_table/entities/lich.json`.
- [S7] Pinned primary [version declaration](https://github.com/CERBON-MODS/Bosses-of-Mass-Destruction-FORGE/blob/1a7bd955d201d1b4d066157b8335cd967677e209/gradle.properties), [item registration](https://github.com/CERBON-MODS/Bosses-of-Mass-Destruction-FORGE/blob/1a7bd955d201d1b4d066157b8335cd967677e209/Common/src/main/java/com/cerbon/bosses_of_mass_destruction/item/BMDItems.java), and [item handler](https://github.com/CERBON-MODS/Bosses-of-Mass-Destruction-FORGE/blob/1a7bd955d201d1b4d066157b8335cd967677e209/Common/src/main/java/com/cerbon/bosses_of_mass_destruction/item/custom/SoulStarItem.java). Version/data correspondence only; compiled-handler equivalence unproved.
- [S8] Pinned primary [entity implementation](https://github.com/CERBON-MODS/Bosses-of-Mass-Destruction-FORGE/blob/1a7bd955d201d1b4d066157b8335cd967677e209/Common/src/main/java/com/cerbon/bosses_of_mass_destruction/entity/custom/lich/LichEntity.java), same correspondence limit.
