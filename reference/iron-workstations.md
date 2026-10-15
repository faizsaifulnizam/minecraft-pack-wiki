---
layout: default
title: "Choose an Iron's magic workstation and avoid wasted scrolls"
permalink: /reference/iron-workstations/
baseline: dev-0.5-20261015-r2
---

# Choose an Iron's magic workstation and avoid wasted scrolls

## Baseline

**dev-0.5-20261015-r2 (candidate; unapplied)** — baseline version **1.21.1-3.16.3**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

**Candidate-specific static evidence; not runtime tested.** These revisions target **dev-0.5-20261015-r2**, an unapplied candidate, not the accepted dev-0.5-20261015 baseline. Retained exact text witnesses belong to `irons_spellbooks-1.21.1-3.16.3.jar`, SHA-256 `d01937925160e32bb68910262af861d168e1d792808a29dfb596dc94bdff5c75`. That differs from the old baseline hash; the mismatch establishes different bytes, not their cause, archive origin or changed gameplay. Construction recipes below are now directly supported by those retained objects. Shipped-book statements are labelled as documentation, not demonstrated behavior; unversioned-only details remain provisional. Effective overrides, controls and gameplay have not been tested. [I00]

## Prerequisites

Finish [first-scroll inscription](../guides/iron-first-scroll.md) or already have a book and a safely obtained scroll. Keep your rare scrolls in storage while you identify which workstation the task needs. The stages below are alternatives for different jobs, not a claim that all stations are mandatory in this order.

## Steps

1. **For putting a known spell in a book, use the Inscription Table.** A found scroll is already a spell; the Scroll Forge is not required merely to inscribe it. Check the scroll's rarity against the book rather than trying to combine ingredients at the wrong station. [I03]
2. **For making a new scroll, plan the Scroll Forge.** The retained candidate recipe uses three Polished Deepslate across the top row, Crying Obsidian in the center and Crying Obsidian across the bottom row: four Crying Obsidian total. The documentation describes inputs of ink, paper and a school focus. Do not assume Ars glyphs or Source Gems are valid substitutes. [I04, I05]
3. **Choose ink before committing to a spell.** The guide describes five ink rarities. Unversioned guidance provisionally says ink crafts a spell at the lowest level available in that rarity; exact candidate selection behavior remains unverified. A spell whose minimum rarity is above your ink is unavailable with that ink; a focus alone does not override this. Exact per-spell eligibility is a later reference gap. [I05]
4. **For upgrading or combining magic items, plan an Arcane Anvil.** The retained candidate crafting recipe is three Blocks of Amethyst across the top, one diamond-tag gem in the center, and Polished Deepslate / ordinary Anvil / Polished Deepslate across the bottom. The unversioned guide provisionally lists scroll upgrades, upgrade-orb application and sword imbuement as different anvil tasks; it does not justify a universal two-scroll recipe or level-cap claim. [I06, I07]
5. **Treat sword imbuement as a commitment.** Unversioned official guidance provisionally says a sword holds one imbued spell at a time and that the scroll cannot be retrieved afterward; neither rule is verified for this candidate. Check the intended spell and item before taking an output. Avoid using your only valuable scroll as an interface experiment. [I07]

**Forge checkpoint:** the retained Mid Game entry names ink, paper and a focus; ink determines rarity/level and focus determines school. The retained Ink entry lists Common, Uncommon, Rare, Epic and Legendary inks and warns that a spell whose lowest level is above an ink cannot be crafted with it. The English interface includes “Obtain higher quality ink”. Before gathering more materials, compare the selected school, available spell and displayed ink requirement. No exact per-spell table or focus-item catalogue is established here. [I05, I08]

## Expected result

You can select the correct station, budget the candidate construction materials and explain why a particular ink or book may reject a spell. The candidate identity is recorded, but baseline acceptance, effective recipe selection, successful crafts and casting remain unverified.

**Version-specific upgrade route:** the retained Scrolls entry describes combining a scroll with ink of the corresponding rarity of its **next level** in the Arcane Anvil. Do not substitute a universal two-scroll recipe. Check the target spell, next level and displayed ink requirement before taking output; per-spell caps and effective costs remain unverified. This does not validate the separate sword-imbuement or upgrade-orb rules. [I10]

## Workstation reference

| Goal | Station | Important boundary |
|---|---|---|
| Save a scroll's spell in a book | Inscription Table | Scroll rarity may exceed book capability. [I03] |
| Craft a scroll from materials | Scroll Forge | Ink constrains rarity/level; focus constrains school. [I05] |
| Upgrade scrolls or apply upgrade orbs | Arcane Anvil | Individual recipes and caps must be checked; no free upgrade is promised. [I07] |
| Put a spell on a sword | Arcane Anvil | Provisional unversioned guidance: one spell at a time; scroll not retrievable. Candidate behavior unverified. [I07] |

## Common failures

- **The Forge has no desired spell:** check its minimum rarity against your ink, then the school focus. The guide does not say every spell can be crafted with common ink. [I05]
- **A scroll will not enter a book:** return to book rarity/capability checks, not Forge ingredients. Exact capacities remain unknown here. [I03]
- **You expected a returned scroll after imbuement:** unversioned documentation provisionally warns otherwise; candidate behavior remains unverified. Stop before taking the result if reversibility matters. No recovery is established. [I07]
- **Material names match but the local recipe differs:** record the recipe ID and displayed inputs/output and use the in-game recipe as a player-side check; do not infer the cause from a hash difference. This manuscript does not authorize changing the installation. [I00]
- **You found a video with another recipe:** this reference did not view or vet any video. Prefer the retained candidate recipe objects for version-labelled construction facts, without treating a recipe-object match as whole-archive or gameplay equivalence.

## Tips with trade-offs

- **Separate a trial scroll from a keeper.** Prerequisite: at least one scroll whose loss you can accept. Benefit: learning consumption versus inscription need not destroy your only desired spell. Trade-off: you may delay testing until another scroll is available. The consumption/inscription distinction and retrieval with uninscription are documented in the retained Early Game entry; unique-book spells are not editable. Actual UI recovery remains untested. [I08] [I03]
- **Check ink rarity before searching for a rare focus.** Prerequisite: a specific target spell and Forge access. Benefit: avoids gathering a school ingredient for a spell your ink cannot make. Trade-off: requires inspecting the intended spell's minimum rarity, which this reference does not catalogue. [I05]
- **Keep sword imbuement last.** Prerequisite: a deliberately chosen sword/scroll pairing. Benefit: avoids an irreversible scroll commitment while still learning the workstation. Trade-off: postpones the imbued weapon; unversioned guidance provisionally says the scroll cannot be retrieved afterward; candidate behavior remains unverified. [I07]

## Sources

Candidate archive and internal-entry source citations are listed below; retained evidence is not a public navigation target. I01/I02/I04/I06 now cite actual candidate recipe objects; upstream links below are supplementary comparisons only. I03 is supported for consumption/inscription by shipped book text, but exact UI procedure remains provisional. I05 has shipped support for inputs/rarity/school; the precise lowest-level-in-each-rarity selection remains provisional. I07 sword-imbuement and upgrade-orb details remain unversioned-only and provisional. I08–I10 cite retained candidate documentation, not tested execution.

- [I00] [Pinned version declaration](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/gradle.properties); identity comparison retained privately.
- [I04] [Pinned Scroll Forge recipe](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/src/main/resources/data/irons_spellbooks/recipe/scroll_forge.json).
- [I06] [Pinned Arcane Anvil recipe](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/src/main/resources/data/irons_spellbooks/recipe/arcane_anvil.json).
- [I03, I05, I07] Official [Getting Started, Ink, Scroll Forge and Arcane Anvil documentation](https://iron.wiki/), unversioned.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/lang/en_us.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/early_game.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/scrolls.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/uncraftable_spell_books.json`.
- [I04] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/recipe/scroll_forge.json`.
- [I05] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/lang/en_us.json`.
- [I05] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/ink.json`.
- [I05] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/mid_game.json`.
- [I06] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/recipe/arcane_anvil.json`.
- [I07] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/scrolls.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/lang/en_us.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/early_game.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/uncraftable_spell_books.json`.
- [I10] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/scrolls.json`.
