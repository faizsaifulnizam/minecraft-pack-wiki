<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/iron-first-scroll/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Put a first scroll into an Iron's spell book

## Baseline

**dev-0.5-20261015-r2 (candidate; unapplied)** — Minecraft 1.21.1, NeoForge 21.1.250; baseline lists Iron's Spells 'n Spellbooks **1.21.1-3.16.3**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

**Candidate-specific static evidence; not runtime tested.** These revisions target **dev-0.5-20261015-r2**, an unapplied candidate, not the accepted dev-0.5-20261015 baseline. Retained exact text witnesses belong to `irons_spellbooks-1.21.1-3.16.3.jar`, SHA-256 `d01937925160e32bb68910262af861d168e1d792808a29dfb596dc94bdff5c75`. That differs from the old baseline hash; the mismatch establishes different bytes, not their cause, archive origin or changed gameplay. Construction recipes below are now directly supported by those retained objects. Shipped-book statements are labelled as documentation, not demonstrated behavior; unversioned-only details remain provisional. Effective overrides, controls and gameplay have not been tested. [I00]

## Prerequisites

Have a safely obtained scroll and a spell book, found or crafted. No particular structure, enemy or drop chance is required by this route. If you do not yet have a scroll, the [workstation reference](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/iron-workstations/) explains the documented crafting alternative; it does not promise that the ingredients are available in your world.

To craft the candidate Ironbound Tome (Iron Spell Book), reserve **three chains, four leather-tag items and two paper**. For an Inscription Table, reserve **one book, three wooden slabs and two wooden fences**. You need an ordinary crafting grid as well. [I01, I02]


**Identify your book before committing a scroll.** The retained translation calls `irons_spellbooks:iron_spell_book` **Ironbound Tome** and the copper book **Flimsy Journal**. The shipped Early Game entry points to the copper recipe as a beginner option; the Ironbound Tome below remains a valid independent construction route, not a required first tier. An optional Iron’s Guidebook recipe combines one ordinary book and one Arcane Essence, but explicitly requires Patchouli to be loaded and produces `patchouli:guide_book` with book component `irons_spellbooks:iss_guide_book`. A documentation book is not the casting book. No guidebook craft or Patchouli loading was tested. [I08, I09]

## Steps

1. **Craft the Ironbound Tome (Iron Spell Book) if you need a book.** Put chains down the left column, leather across the two remaining cells of the top and bottom rows, and paper in the two remaining middle-row cells. The retained candidate recipe produces `irons_spellbooks:iron_spell_book`. Keep this system separate from Ars spellcrafting; this object produces the Iron item, not an Ars book. [I01]
2. **Craft an Inscription Table.** Put a book in the top-right cell, wooden slabs across the middle row and wooden fences in the bottom-left and bottom-right cells. Place the resulting table at your base, not inside an active fight. [I02]
3. **Decide whether to save the scroll.** The documentation distinguishes two uses: consuming a scroll casts it once without mana or cooldown, while inscription puts its spell in a book. If you want repeat use, take it to the table instead of consuming it. The retained Early Game entry says retrieving a scroll uninscribes its spell. This documents an intended recovery route for editable books, not a tested guarantee. Unique books are a documented exception: their existing spells cannot be removed or edited. [I08] [I03]
4. **Open the table and place your book and scroll in its interface.** The guide describes slotting the scroll's spell into the book here. Check whether the book accepts that scroll before taking a result. Rarity can make a scroll too powerful for a particular book; this is a book/scroll constraint, not evidence that another magic mod must be progressed first. [I03]
5. **Inspect the resulting book's spell list.** Confirm that the intended spell is listed. This is the first checkpoint; do not assume a crafted empty book already contains spells. The retained English interface text includes “This scroll is too rare for this spell book.” This supports the rarity warning, but not numeric slot counts or ceilings. [I08] [I03]
6. **Prepare a separate casting check.** Find the mod's current casting/selection controls in the game's Controls screen, read the chosen spell's target and cost information, and use an expendable target in an open practice area. No binding, friendly-fire rule or spell-specific safe range has been verified here. If you cannot establish a safe target, stop at inscription rather than testing on a pet or player.

**Checkpoint and recovery:** note the scroll’s spell/level and the book’s existing spell list before inscription. Inspect the intended result before taking it; if it differs, stop rather than consuming a rare scroll or overwriting a valued slot. Afterward compare the actual spell list with that note. The shipped book documents scroll retrieval for editable books, but this guide does not invent a removal button or promise item recovery after an unexpected result. [I08]

## Expected result

The shipped-book-documented outcome is a book containing the chosen scroll's spell, ready for a later controlled casting check. It is not proof of a working local recipe, active mana settings or compatibility with another mod's power system. Once inscription is understood, use [ink, rarity and workstation checks](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/iron-workstations/) to plan the next spell without wasting a rare scroll.

## Common failures

- **The book rejects a scroll:** compare the scroll's rarity with the book's supported rarity before making another table. The documentation says a better book may be needed. Exact local caps remain unresolved. [I03]
- **You cast the scroll instead of saving it:** the guide explicitly describes consumption as a separate one-use path. Do not consume your only copy when your goal is inscription. No undo is promised. [I03]
- **The crafting grid gives a different result or nothing:** record the recipe ID, displayed inputs and result as a discrepancy; static archive evidence does not establish effective recipe precedence. Do not rename, replace or reinstall the JAR on this guide's authority. [I00]
- **A saved spell does not cast:** binding, mana, cooldown and spell conditions need a runtime check. The no-mana/no-cooldown statement applies to consumed scrolls, not an unlimited spell-book mode. [I03]
- **You encounter hostile magic while gathering:** withdraw to ordinary shelter and retain your normal equipment. This tutorial does not require fighting an identified boss or raiding a specific structure.

## Sources

Candidate archive and internal-entry source citations are listed below; retained evidence is not a public navigation target. I01/I02/I04/I06 now cite actual candidate recipe objects; upstream links below are supplementary comparisons only. I03 is supported for consumption/inscription by shipped book text, but exact UI procedure remains provisional. I05 has shipped support for inputs/rarity/school; the precise lowest-level-in-each-rarity selection remains provisional. I07 sword-imbuement and upgrade-orb details remain unversioned-only and provisional. I08–I10 cite retained candidate documentation, not tested execution.

- [I00] Official repository [version declaration](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/gradle.properties); local identity mismatch retained privately.
- [I01] Pinned upstream [Iron Spell Book recipe](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/src/main/resources/data/irons_spellbooks/recipe/iron_spell_book.json).
- [I02] Pinned upstream [Inscription Table recipe](https://github.com/iron431/irons-spells-n-spellbooks/blob/e4056af90302d37eb1739f5ff05020b020e6e252/src/main/resources/data/irons_spellbooks/recipe/inscription_table.json).
- [I03] Official [Getting Started](https://iron.wiki/#getting-started), unversioned; read as supplementary guidance, not shipped-book verification.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [I01] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/recipe/iron_spell_book.json`.
- [I02] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/recipe/inscription_table.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/lang/en_us.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/early_game.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/scrolls.json`.
- [I03] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/uncraftable_spell_books.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/lang/en_us.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/progression/early_game.json`.
- [I08] `irons_spellbooks-1.21.1-3.16.3.jar!assets/irons_spellbooks/patchouli_books/iss_guide_book/en_us/entries/spell_books/uncraftable_spell_books.json`.
- [I09] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/patchouli_books/iss_guide_book/book.json`.
- [I09] `irons_spellbooks-1.21.1-3.16.3.jar!data/irons_spellbooks/recipe/patchouli_book.json`.
