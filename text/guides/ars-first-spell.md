<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/ars-first-spell/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Make your first Ars Nouveau utility spell

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Minecraft 1.21.1, NeoForge 21.1.250; Ars Nouveau **5.13.3**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Tutorial based on hash-matched shipped recipes and English documentation. Not gameplay tested. Ingredient tags and recipes describe shipped intent, not resolved pack overrides. Ars spells are assembled from glyphs; this is not the scroll-inscription route used by [Iron's Spellbooks](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/iron-first-scroll/).

## Prerequisites

Set aside a book, an iron shovel, iron pickaxe, iron axe and iron sword for the Novice Spell Book. These are crafting ingredients, so do not use your only working tools. For a Scribe's Table, collect three Archwood Slabs, two gold nuggets and two Archwood Logs. Keep experience available. The two optional glyph recipes below each declare **`exp: 27`**; the experience-unit implementation was not independently traced. Check the displayed cost rather than reading that as 27 levels. [A01]

Work in a clear area away from containers, animals and valuable blocks. Use a utility spell before experimenting with destructive effects. This is safety advice, not a tested protection mechanism.

## Steps

1. **Craft the Novice Spell Book.** Combine the ordinary book and the four iron tools in a shapeless recipe. You should receive `ars_nouveau:novice_spell_book`. A separate documentation item, `ars_nouveau:worn_notebook`, is displayed as **Tattered Tome** in this version; make it from a book and a lapis-tag gem if you want the shipped documentation. The alternate novice-book recipe consumes that tome instead of an ordinary book, so keep a separate copy if you want both. [A01]
2. **Build a Scribe's Table.** In the crafting grid put three Archwood Slabs across the top, gold nuggets at middle left and right, and Archwood Logs at bottom left and right. Place the table somewhere you can reach. Use your spell book on it to open the glyph codex. [A02]
3. **Check for Touch and Conjure Magelight.** If either is missing from your learned glyphs, select it in the table's codex and choose **Select**. Supply the displayed ingredients by throwing them onto the table: Touch takes one button accepted by the `minecraft:buttons` tag; Conjure Magelight takes one lantern and one torch. Supply the recipe's experience cost as well. The table can also pull from nearby inventories, so keep unrelated materials away while learning. [A03]
4. **Learn each produced glyph.** Consume the crafted glyph item. Crafting it alone does not add it to your spellcrafting list. If the glyph is already learned, do not craft another just for this tutorial. [A03]
5. **Open spellcrafting with the spell book selected.** Use your configured spellcrafting control. The shipped text prints **[C]**, but this is not a verified saved keybinding. Choose a free bookmark, add **Touch**, then **Conjure Magelight**, give the spell a name, and choose **Create**. Clicking an unwanted glyph in the assembled spell removes it. A spell must start with exactly one Form; Touch is the targeting Form here. [A04]
6. **Try the spell against an expendable solid block.** Use the book's cast action while aiming at that block. The Light description says a block-targeted cast creates a permanent light source. Your mana should fall when the spell casts and regenerate over time. The cast binding and the appearance of the result still need a runtime check; no key is assumed here. [A05]

## Expected result

You have a Novice Spell Book, learned utility glyphs and a saved two-glyph spell. The documented checkpoint is a light at the target and mana expenditure, not a combat victory. Continue with [Source production and the Ars workshop](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/ars-workshop/) only after you can save and select this spell.

## Common failures

- **The glyph was crafted but is absent from the list:** consume the glyph item, then reopen spellcrafting. [A03]
- **The spell cannot be constructed:** put one Form first; remove extra Forms and unsupported augments. The Novice book casts tier-I glyphs only. Do not spend materials on higher-tier glyphs for this book. [A04]
- **The table seems to take items unexpectedly:** its shipped documentation says it pulls nearby inventories. The Dominion Wand can disable that behavior, but crafting the wand is outside this starter route. Move unrelated stock away meanwhile. [A03]
- **Casting stops after repeated attempts:** wait for mana regeneration before changing your Source setup. Mana is the casting resource; Source powers workshop processes. Their co-presence does not make them interchangeable. [A05, A06]
- **The controls do not match the text:** inspect the game's current Controls screen rather than changing keys based on this manuscript. No current binding was verified.

## Sources

- [A01–A03] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/`: `novice_spell_book.json`, `novice_spellbook_alt.json`, `worn_notebook.json`, `scribes_table.json`, `glyph_touch.json`, `glyph_light.json`.
- [A02–A06] Same archive, `assets/ars_nouveau/lang/en_us.json`: `item.ars_nouveau.worn_notebook`, `ars_nouveau.page1.scribes_table`, `learning_glyphs`, `introduction_to_glyphs`, `introduction_to_spellcrafting`, `spell_mana`, `source`; `ars_nouveau.glyph_desc.glyph_touch`, `glyph_light`.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/novice_spell_book.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/novice_spellbook_alt.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/worn_notebook.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/scribes_table.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_touch.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_light.json`: `witness`.
- [A01] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A02] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/scribes_table.json`: `witness`.
- [A02] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A03] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_touch.json`: `witness`.
- [A03] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_light.json`: `witness`.
- [A03] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A04] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A05] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A06] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
