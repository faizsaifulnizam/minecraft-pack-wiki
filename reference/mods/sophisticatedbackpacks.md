---
layout: default
title: "Sophisticated Backpacks reference"
permalink: /reference/mods/sophisticatedbackpacks/
baseline: dev-0.5-20261015-r2
---

# Sophisticated Backpacks reference

## Applicability and evidence
Candidate documentation snapshot **dev-0.5-20261015-r2**, Minecraft **1.21.1**, NeoForge **21.1.250**. Candidate unapplied; not canonical adoption or release validation. Retained static documentation only; **not-runtime-tested**. No family completeness claim.

Exact identity: `sophisticatedbackpacks`, version **3.26.9.2195**, archive `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar`. Identity is recorded in the [shared archive reference](../../mods.md); it is not a fresh instance observation.

## Choose a destination
- Beginner: [Sophisticated Backpacks starting route](../../guides/first-backpack-access.md). Read its prerequisites and action-local limits first.
- Advanced planning: [storage boundaries](../storage-boundaries.md); advanced tasks below are missing, not completed tutorials.
- Comparison: [storage choice](../../guides/storage-choice.md); these are independent alternatives, not a prerequisite chain.
- Family context: [storage systems](../../systems/storage.md).

## What the retained reference supports
`sophisticatedbackpacks:backpack` declares rows `SLS`, `SCS`, `LLL`: S is `c:strings`, L is `c:leathers`, C is `c:chests/wooden`. Its custom `sophisticatedbackpacks:basic_backpack` recipe carries a `sophisticatedcore:item_enabled` condition. Presence is not proof that the effective recipe is enabled.[1]

The linked beginner route's held-item menu action is provisional: upstream source declares `mod_version=3.26.9` but is not tied to installed build 2195 or compiled behavior. Menu opening does not prove slot eligibility, insert/remove safety or useful carrying-and-return storage. Do not infer Curios controls or use a worn slot to compensate.[2][3]

Filter/Void Upgrade labels distinguish piped-item filtering from filtered deletion intent, not proved controls, compatibility or capacity. Avoid deletion upgrades and leave menu slots untouched during the provisional first-access check.[4]

## Missing tasks
- Beginner: build2195 source/binary correspondence; container/helper/slot predicates; safe deposit, retrieval and return.
- Advanced: capacities, upgrade transitions/content retention, filters, shortcuts and safe worn-slot removal.
- Integration: backpack-to-ME direction, priorities, filtering and overflow remain unknown.
- Runtime: effective recipe, successful opening, recovery, death and save/reopen persistence remain unconfirmed.

Stop if the provisional interface differs. Keep the empty Backpack; do not try forced pickup, dropping, repeated placement or valuables to diagnose access.[2]

## Sources
- [1] `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/backpack.json` — Recipe and enabled condition; retained declaration.
- [2] `https://github.com/P3pp3rF1y/SophisticatedBackpacks/blob/565bd1bfac58f5e57c56b0be9a681dc042ba07ec/src/main/java/net/p3pp3rf1y/sophisticatedbackpacks/backpack/BackpackItem.java#L239-L338` — Retained source; placement separation and held-item caller, provisional same-version only.
- [3] `https://github.com/P3pp3rF1y/SophisticatedBackpacks/blob/565bd1bfac58f5e57c56b0be9a681dc042ba07ec/gradle.properties#L18` — Retained version declaration, not build2195 correspondence.
- [4] `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!assets/sophisticatedbackpacks/lang/en_us.json` — Selected Filter/Void labels only.

Claim summaries inherit the limits in [the retained task guide](../../guides/first-backpack-access.md) and [storage boundaries](../storage-boundaries.md); no new source acquisition or runtime check is implied.
