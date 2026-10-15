---
layout: default
title: "FULL SPOILERS"
permalink: /full/occultism-procedures/
baseline: dev-0.5-20261015-r2
---
<!-- wiki.py managed full human schema=1 -->
**FULL SPOILERS**

WARNING: FULL SPOILERS. Direct links, reload and history may reveal everything here; this distinct full-human route is exempt from ordinary-entry consent/reset guarantees.

[Return to safe entry](/minecraft-pack-wiki/reference/occultism-procedures/)

# Occultism procedures

**FULL SPOILERS — this entire page reveals discovery mechanics, the first summon's identity and its working ritual.** Return to [the safe work-area tutorial](/minecraft-pack-wiki/guides/occultism-first-workbench/) if you prefer to discover these through the book. Direct links expose this static page; it is not a consent or access-control boundary.

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Occultism **1.224.5**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Full-spoiler how-to, based on hash-matched shipped recipes, the first-ritual multiblock and translated Dictionary entries. Not gameplay tested. The book's old introductory link calls the ritual `summon_crusher_t1`, but the actual displayed recipe and retained resource are `occultism:ritual/summon_foliot_crusher`. Use the latter resource identity; do not silently treat the stale link as a working recipe ID. [O15]

## Prerequisites

Complete [the safe conversion setup](/minecraft-pack-wiki/guides/occultism-first-workbench/). Set aside a Golden Sacrificial Bowl, at least four ordinary bowls, White Chalk and four candles. The first summon consumes one iron-tag ingot, one gold-tag ingot, one copper-tag ingot and one silver-tag ingot, plus its bound Foliot Book of Binding activation item. An accepted silver-ingot source is not established here; namespace co-presence is not an ore availability guarantee. [O15]

Keep the work area separate from valuable storage. Demon's Dream fruit may produce effects with a chance; the stronger essence has negative as well as positive side effects. Do discovery/harvesting from a secure area, not while crossing lava, fighting or depending on a timed effect for your escape. Exact duration, chance and a cure are unverified. [O16]

## Steps

1. **Get harvestable Otherworld wood for chalk.** Convert an oak sapling in Spirit Fire to `occultism:otherworld_sapling_natural`, then grow the tree. The guide distinguishes seeing the Otherworld from harvesting its materials: Demon's Dream grants the harvesting interaction, while other Third Eye sources do not necessarily do so. Consume grown Demon's Dream fruit only from a secure position and confirm the relevant effect before trying to harvest. The fruit's effect is probabilistic. The guide describes essence as guaranteed and longer-lasting, and a purified version without negative effects, but their complete recipes were not retained; this is not an instruction to craft an unspecified mixture. [O16, O17]
2. **Finish the chalk chain.** Convert an accepted Otherworld log in Spirit Fire for one Otherworld Ashes per item. Smelt Otherstone once into Polished Otherstone and again into Burnt Otherstone. The shipped `c:dusts/otherworld_wood` tag contains the ashes and `c:dusts/otherstone` contains the burnt material. Three of each, in adjacent vertical columns, craft Impure White Chalk; convert that chalk in Spirit Fire. No ore crusher is needed to obtain these two tag members by this route. Growth/harvest interaction and actual recipe resolution remain runtime checks. [O06, O17]
3. **Craft and bind the Foliot book.** Arrange `ink / blue dye / feather` across the top, `blue dye / Taboo Book / blue dye` across the middle, and one blue dye at bottom-center. The ink must be Purified Ink and the feather Awakened Feather from the safe tutorial. Craft this Foliot Book of Binding with the Dictionary to obtain its bound form; the guide says the Dictionary is retained. Confirm `occultism:book_of_binding_bound_foliot`, not the unbound item, before activation. [O05, O10]
4. **Build Aviar's Circle.** Put the golden bowl at `G` in the top-down layout below. Put four candles at `C` and draw the 24 marks at `W` using the basic chalk. Dots are positions not occupied by the shown ritual elements. The lower resource layer is a ground/display layer; its gray concrete is declared as a display predicate, not a requirement to build a concrete floor. The serialized mark predicate uses `#occultism:foundation_glyphs_any`; the basic book walkthrough recommends White Chalk. Do not assume every higher-tier ritual uses the same tags or color rule. [O18]

```text
.........
...WWW...
..W.W.W..
.W.CWC.W.
.WWWGWWW.
.W.CWC.W.
..W.W.W..
...WWW...
.........
```

5. **Load the four ingots into ordinary bowls.** Put those bowls nearby, within eight blocks horizontally of the center. Do not put the ordinary ingredients in the golden activation bowl. Position and chalk color matter, not the decorative glyph signs. The Dictionary's blue pentacle link on a ritual page opens its in-world preview; use that to compare the layout rather than guessing from perspective. [O08, O09, O15, O18]
6. **Activate with the bound Foliot book.** Right-click the central golden bowl with it, as the shipped walkthrough directs. Wait for ingredient consumption and the Foliot crusher to appear. The recipe's duration is serialized as 60; its unit was not independently traced and is not asserted as seconds. Keep a retreat route clear and do not assume every future summon is equally safe. [O15]
7. **Try a single appropriate ore input.** The walkthrough says to drop suitable ores near the crusher and wait for dust. Check that a corresponding crushing recipe is actually available before providing a valuable stack. For example, the retained raw-iron-block recipe only loads when both its raw-iron-block and iron-dust tags are nonempty. Its declared output count is not a universal multiplier for every ore or worker tier. [O19]

## Expected result

The documented result is a Foliot with the tier-1 crushing job, not merely the recipe viewer's spawn-egg/dummy icon. The actual ritual declares `summon_spirit_with_job` and `crush_tier1`; do not read its display result as a promise that an egg is placed into your inventory. [O15]

## Common failures

- **You can see special materials but cannot harvest them:** seeing through Third Eye and Demon's Dream harvesting are distinct in the shipped text. Do not infer harvesting from visibility alone. [O16]
- **The bound book looks right but activation fails:** check its tier/type, not the decorative spirit name. [O10]
- **No ingredients disappear:** inspect [the safe waiting-state diagnostics](/minecraft-pack-wiki/reference/occultism-workbench/), then verify the correct pattern and bowl range. Do not sacrifice a random mob. [O11]
- **The crusher ignores an input:** inspect its exact recipe and nonempty-tag conditions. One conditional recipe does not prove that every cross-mod ore has a valid output. [O19]
- **You are about to automate:** read the safe reference's activation/output distinction first. Automation can change taming outcomes for other rituals; a working crusher does not certify a familiar automation line. [O12]

## Tips with trade-offs

- **Use the Spirit Fire sapling conversion rather than searching blindly.** Prerequisite: an oak sapling and conversion fire. Benefit: gives a serialized starting item for the wood chain. Trade-off: growth and the documented harvest effect still matter; it is not instant unrestricted wood collection. [O16, O17]
- **Compare the preview before spending the activation book.** Prerequisite: the Dictionary's ritual/pentacle page. Benefit: checks spatial layout with the shipped structure rather than decorative sign appearance. Trade-off: using the book reveals the ritual itself; this page is already full-spoiler. [O18]

## Sources

- [O05–O19] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`, `book.occultism.dictionary_of_spirits.getting_started.` prefixes `demons_dream`, `spirit_fire`, `ritual_prep_chalk`, `books_of_binding`, `first_ritual`, `grey_particles`.
- Same archive, `data/occultism/modonomicon/books/dictionary_of_spirits/entries/getting_started/first_ritual.json`; `data/occultism/modonomicon/multiblocks/summon_foliot.json`.
- Same archive, `data/occultism/recipe/ritual/summon_foliot_crusher.json`, `crafting/book_of_binding_foliot.json`, `spirit_fire/otherworld_sapling_natural.json`, `spirit_fire/otherworld_ashes.json`, `smelting/polished_otherstone.json`, `smelting/burnt_otherstone.json`, `crushing/iron_dust_from_raw_block.json`; dust and log tags retained privately.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [O05] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/purified_ink.json`: `witness`.
- [O05] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/awakened_feather.json`: `witness`.
- [O05] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/taboo_book.json`: `witness`.
- [O05] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/crafting/book_of_binding_foliot.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/crafting/chalk_white_impure.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/chalk_white.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/smelting/polished_otherstone.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/smelting/burnt_otherstone.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/otherworld_ashes.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/c/tags/item/dusts/otherstone.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/c/tags/item/dusts/otherworld_wood.json`: `witness`.
- [O06] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/tags/item/dusts/chalk_base.json`: `witness`.
- [O08] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O09] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O10] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O11] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O12] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O15] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/ritual/summon_foliot_crusher.json`: `witness`.
- [O15] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/modonomicon/books/dictionary_of_spirits/entries/getting_started/first_ritual.json`: `witness`.
- [O15] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O16] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O17] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/otherworld_sapling_natural.json`: `witness`.
- [O17] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/spirit_fire/otherworld_ashes.json`: `witness`.
- [O17] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/tags/item/otherworld_logs.json`: `witness`.
- [O18] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/modonomicon/multiblocks/summon_foliot.json`: `witness`.
- [O18] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/modonomicon/books/dictionary_of_spirits/entries/getting_started/first_ritual.json`: `witness`.
- [O18] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O19] `occultism-1.21.1-neoforge-1.224.5.jar!data/occultism/recipe/crushing/iron_dust_from_raw_block.json`: `witness`.
- [O19] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
