---
layout: default
title: "Storage Drawers reference"
permalink: /reference/mods/storagedrawers/
baseline: dev-0.5-20261015-r2
---

# Storage Drawers reference

## Applicability and evidence
Candidate documentation snapshot **dev-0.5-20261015-r2**, Minecraft **1.21.1**, NeoForge **21.1.250**. Candidate unapplied; not canonical adoption or release validation. Retained static documentation only; **not-runtime-tested**. No family completeness claim.

Exact identity: `storagedrawers`, version **13.11.4**, archive `StorageDrawers-neoforge-1.21.1-13.11.4.jar`. Identity is recorded in the [shared archive reference](../../mods.md); it is not a fresh instance observation.

## Choose a destination
- Beginner: [Storage Drawers starting route](../../guides/craft-first-oak-drawer.md). Read its prerequisites and action-local limits first.
- Advanced planning: [storage boundaries](../storage-boundaries.md); advanced tasks below are missing, not completed tutorials.
- Comparison: [storage choice](../../guides/storage-choice.md); these are independent alternatives, not a prerequisite chain.
- Family context: [storage systems](../../systems/storage.md).

## What the retained reference supports
`storagedrawers:oak_full_drawers_1` has a shaped recipe declaring six `minecraft:oak_planks` and one `c:chests/wooden` ingredient, yielding one drawer. The linked beginner task gives exact arrangement and a current-recipe comparison stop.[1]

This proves a recipe declaration, not current tag membership, effective recipe or a usable storage lifecycle. Keep bulk stock where it is until placement, deposit and withdrawal are supported.[1]

The Void Upgrade description says “Destroys excess items.” Deletion intent is not extra capacity or proof of the runtime overflow algorithm. Avoid it while learning; no undo is established.[2]

## Missing tasks
- Beginner: exact 13.11.4 placement/deposit/withdrawal callers and helpers, then a recoverable nonvaluable-item lifecycle.
- Advanced: capacities, locking, upgrades, controller range, filtering and safe automation.
- Integration: a named Drawers-to-ME interface with direction, priority, loops and overflow remains unknown.
- Runtime: actual craft, item recovery and save/reopen persistence remain unconfirmed.

Stop if the displayed recipe differs. Keep ingredients rather than editing settings. If deletion is suspected, stop feeding the container; do not break stocked storage as a recovery experiment.[1][2]

## Sources
- [1] `StorageDrawers-neoforge-1.21.1-13.11.4.jar!data/storagedrawers/recipe/oak_full_drawers_1.json` — Complete recipe declaration as retained in the beginner guide.
- [2] `StorageDrawers-neoforge-1.21.1-13.11.4.jar!assets/storagedrawers/lang/en_us.json` — item.storagedrawers.void_upgrade.desc; label evidence only.

Claim summaries inherit the limits in [the retained task guide](../../guides/craft-first-oak-drawer.md) and [storage boundaries](../storage-boundaries.md); no new source acquisition or runtime check is implied.
