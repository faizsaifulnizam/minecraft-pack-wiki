---
layout: default
title: Exploration reference A
permalink: /reference/exploration-reference-a/
baseline: dev-0.5-20261015-r2
---
# Exploration reference A

FULL SPOILERS — progression identities, branches and checkpoints follow.

## Baseline
Private candidate-r2; unapplied and not canonically adopted. Twilight Forest 4.8.3345 retained candidate text, not a completed gameplay test. [Travel and return](../guides/dimension-travel.md) and [Preparation](../guides/exploration-preparation.md) come first.

## Evidence status
This is the **declared advancement-condition reference**, not a boss-fight walkthrough. Every row separates a display-tree parent from actual criteria. Requirements are AND between outer groups and OR within each group. A `parent` alone is not a runtime lock. Explicit advancement predicates in tick criteria are real declared conditions, but custom `hurt_boss`, pedestal and phantom trigger **handlers/call sites were not inspected**. Their names do not prove participant range, damage contribution, last-hit sharing, trophy-placement acceptance or server-wide awards.

Language descriptions explain intended protection relationships but are not enforcement handlers. In particular, they describe scepters, fur clothing and fiery tears more narrowly/differently than some JSON alternatives. Use the actual conditions below to diagnose an advancement; do not turn its alternatives into a guarantee of protection removal. No effective progression game rule, tag merge, resource order or per-player state was read. [A1–A16, L]

## Prerequisites
A confirmed retreat/return route, combat readiness chosen by the player, and a safe place to inspect advancement text. No armour tier, boss-spawn procedure, coordinate or bypass is established. Keep rewards until the relevant inventory/consumption checkpoint has been observed; use [Exploration reference B](exploration-reference-b.md) to distinguish loot declarations from awards.

## Steps
1. Start with the entrance checkpoint. `root` allows being in `twilightforest:twilight_forest` **OR** the custom `make_tf_portal` trigger. It does not prove that you entered after construction, exited, or found a safe landing. [A1]
2. Follow the common opening stages, checking your own advancement before leaving safety:

| Stage | Display parent | Actual declared requirements | Checkpoint / stop |
| --- | --- | --- | --- |
| Naga (`progress_naga`) | `root` | Any one: player kills Naga, inventory contains Naga trophy, inventory contains Naga scale, or custom hurt-boss criterion for Naga | No explicit root predicate is required in these criteria. Do not invent a compulsory last hit. [A2] |
| Lich (`progress_lich`) | `progress_naga` | Tick predicate requires `progress_naga`; AND any one: Lich kill, Lich trophy, lifedrain/twilight/zombie/fortification scepter inventory criterion, or custom hurt-boss criterion for Lich | Confirm this stage on each player's own advancement view before choosing a branch. [A3] |

3. Choose a branch after the Lich stage; the JSON does **not** impose an order among these branches. Translation prose describes intended environmental/device changes, not observed safety:

| Branch / stage | Display parent | Actual declared requirements | Intended relationship / caution |
| --- | --- | --- | --- |
| Wetland `progress_labyrinth` | `progress_lich` | Tick predicate for `progress_lich` AND consume `twilightforest:meef_stroganoff` | Merely carrying the food or a Minoshroom trophy is not this condition. Language says acclimatize to Fire Swamp heat. [A4, L] |
| `progress_hydra` | `progress_labyrinth` | Tick predicate for `progress_labyrinth` AND any one: Hydra kill, Hydra trophy inventory, custom hurt-boss for Hydra | Do not assume heat effects or structure protection are removed until actually observed. [A5] |
| Dark-forest `progress_trophy_pedestal` | `progress_lich` | Tick predicate for `progress_lich` AND custom `placed_on_trophy_pedestal` | Language says place a trophy on the Dark Forest ruins pedestal; accepted trophies and exact barrier-handler behaviour are unresolved. No invented interaction count or boss summon. [A6, L] |
| `progress_knights` | `progress_trophy_pedestal` | Tick predicate for `progress_trophy_pedestal` AND (`kill_all_phantoms` custom trigger OR Knight Phantom trophy inventory) | Language associates settling phantoms with the tower's devices responding. Trigger implementation remains unknown. [A7, L] |
| `ghast_trap` | `progress_knights` | Custom `activate_ghast_trap` only | This is a displayed side checkpoint, not an explicit prerequisite predicate in the next row. No untraced trap activation tutorial is supplied. [A8] |
| `progress_ur_ghast` | `ghast_trap` | Tick predicate for `progress_knights` AND any one: Ur-Ghast kill, Ur-Ghast trophy inventory, custom hurt-boss for Ur-Ghast | Parent is **not** the required tick predicate. Fiery tears are in the description but are **not an inventory alternative in this advancement**. [A9, L] |
| Snow `progress_yeti` | `progress_lich` | Tick predicate for `progress_lich` AND any one: Alpha Yeti kill, Alpha Yeti trophy inventory, Alpha Yeti fur inventory, custom hurt-boss for Alpha Yeti | Language mentions fur-lined garments; the advancement itself does not require equipping armour. Actual cold protection handler remains unresolved. [A10, L] |
| `progress_glacier` | `progress_yeti` | Tick predicate for `progress_yeti` AND any one: Snow Queen kill, Snow Queen trophy inventory, custom hurt-boss for Snow Queen | Language describes defeating her atop the Aurora Palace. This does not prove a particular combat tactic, spawn or reward pickup. [A11, L] |

4. Rejoin only after the three branch endpoints. `progress_merge` has parent `progress_lich`, but its actual three tick criteria require **all** of `progress_hydra`, `progress_ur_ghast`, and `progress_glacier`. Translation prose describes clearing acid rain for the Highlands; the protection implementation and effective server rule were not traced. If the terrain is still hazardous, retreat rather than assuming the toast wins. [A12, L]
5. Treat the upper-area checkpoints carefully:

| Stage | Display parent | Actual declared requirements | Boundary |
| --- | --- | --- | --- |
| `beanstalk` | `progress_merge` | Inventory has magic beans AND `item_used_on_block` with magic beans on uberous soil | No explicit merge predicate here; this records declared use, not a guaranteed stalk height, safe ascent or source of beans. [A13] |
| `giants` | `beanstalk` | Player kills giant miner AND the criterion named `pickaxe` actually checks **magic beans inventory** | Description/icon mention giant pickaxe, but the item predicate does not. Preserve this discrepancy; do not silently “fix” it or require a pickaxe to award this advancement. [A14] |
| `progress_troll` | `giants` | Lamp of Cinders inventory AND a tick predicate for `progress_merge` | No explicit `giants` predicate. Language says the lamp can burn thorn barriers; exact use, cost and enforcement are untraced. [A15, L] |
| `progression_end` | `progress_troll` | Tick predicate for `progress_troll` AND location in biome `twilightforest:final_plateau` | The shipped text states content beyond this point / Final Castle is unfinished. Do not invent a final boss, castle-clear award or completion trigger. [A16, L] |

6. At each checkpoint, return to safety, inspect your own advancement, and decide whether to deposit rewards. If conditions appear satisfied but advancement or access does not change, stop escalation: custom trigger dispatch, per-player state, runtime rules and resource overrides remain unknown. Death recovery uses the known route with spare gear; it is not a progression-reset workaround.

## Expected result
A connected condition-level route through the declared core progression endpoints, including three parallel branches and the explicit unfinished endpoint. This is **not full-family completion**: combat mechanics, actual biome/structure protection handlers, treasure placement, all side advancements and runtime acceptance are not covered.

Useful tip: separate the tree's connecting line from the condition text when troubleshooting. Benefit: avoids farming the wrong action (for example trap activation as an assumed Ur-Ghast award prerequisite). Trade-off: the tree alone is simpler to read, and this condition reference cannot prove enforcement outside the advancement JSON.

## Common failures
- **A teammate's kill should unlock everyone.** No participation radius, sharing or custom-trigger implementation was proved. Check each player's state without promising an award.
- **Inventory always equals a reward from this encounter.** Inventory predicates can match an item without proving where it came from; loot/dispatch is a separate question.
- **Progression end means a final castle boss was beaten.** This JSON checks a location plus previous advancement, and the shipped text explicitly says unfinished.
- **A tooltip overrides a JSON predicate.** Preserve both and label the difference; do not substitute fur equipment, fiery tears or giant pickaxe for the actual criteria.

## Sources
All A citations use `twilightforest-1.21.1-4.8.3345-universal.jar!` with these exact entries:
- [A1] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/root.json`.
- [A2] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_naga.json`.
- [A3] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_lich.json`.
- [A4] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_labyrinth.json`.
- [A5] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_hydra.json`.
- [A6] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_trophy_pedestal.json`.
- [A7] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_knights.json`.
- [A8] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/ghast_trap.json`.
- [A9] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_ur_ghast.json`.
- [A10] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_yeti.json`.
- [A11] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_glacier.json`.
- [A12] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_merge.json`.
- [A13] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/beanstalk.json`.
- [A14] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/giants.json`.
- [A15] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progress_troll.json`.
- [A16] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/progression_end.json`.
- [L] `twilightforest-1.21.1-4.8.3345-universal.jar!assets/twilightforest/lang/en_us.json` — progression descriptions and unfinished-endpoint message only; complete explorer-book coverage is not included.
