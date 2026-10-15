<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/ars-workshop/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Run an Ars Nouveau Source workshop

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Ars Nouveau **5.13.3**, Minecraft 1.21.1 / NeoForge 21.1.250.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Reference and workshop how-to from hash-matched shipped English documentation and recipes. No device, automation interface or save/reopen behavior was exercised. Start with [a saved utility spell](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/ars-first-spell/); this page does not add another mod's power system as a prerequisite.

## Prerequisites

Keep amethyst shards or lapis, Archwood Planks, gold and access to a crop/tree-growing area. A basic Imbuement Chamber uses six Archwood Planks and two gold ingots. A Source Jar uses six Archwood Slabs and two glass-block-tag ingredients. An Agronomic Sourcelink uses two Source Gems, two gold ingots and one wheat. These are individual shipped recipe totals, not a complete workshop bill of materials. [A07]

## Steps

1. **Make the chamber before building a power network.** Its pattern is `xyx / x x / xyx`, where `x` is Archwood Planks and `y` is gold ingots. Put amethyst or lapis into the chamber to obtain Source Gems according to the shipped guide. The chamber passively accumulates Source for recipes; a jar is a speedup route, not a documented prerequisite for the first gem. Exact processing time and input/output count for this conversion were not captured. [A07, A08]
2. **Build a Source Jar beside your crop area.** The recipe has slabs across the top and bottom, with glass at middle left and right. Craft an Agronomic Sourcelink with Source Gems top-center and bottom-center, gold at middle left/right and wheat in the center. [A07]
3. **Use natural growth to supply it.** The documented collection range is 15 blocks for crop and tree growth. Put the jar within five blocks of the Sourcelink for output. The guide expressly says bonemealing crops does **not** grant Source, so do not spend bone meal to diagnose an empty jar. Magical plants provide bonus Source, but ordinary crop/tree growth is already the described trigger. [A09]
4. **Move a filled jar within two blocks of the chamber for faster processing.** For recipes with extra pedestal ingredients, the guide places those pedestals within one block of the chamber and says their items are not consumed. Do not apply that non-consumption rule to the different Enchanting Apparatus. [A08]
5. **Prepare the Enchanting Apparatus as a separate station.** Its recipe uses two Sourcestone, four gold nuggets, two gold ingots and one diamond-tag gem. The Arcane Core uses six Sourcestone, two gold ingots and one Source Gem. Each Arcane Pedestal uses four Sourcestone, four gold nuggets and one Source Gem. Obtaining Sourcestone and selecting a first complete apparatus recipe remain outside this captured material chain. [A10]
6. **Load only a verified apparatus recipe.** The guide requires an Arcane Core next to the Apparatus base, ingredient pedestals within three blocks and the recipe's middle item used on the Apparatus last. Check that recipe's Source cost rather than assuming every craft is passive or free. The exact core geometry and a completed apparatus output still need an authorized runtime check. [A10]

## Expected result

The documented handoff is a Source Gem supply and naturally replenished jar feeding the chamber, followed by a prepared apparatus plan. The player-visible checks are gem conversion and jar accumulation; neither was observed by this authoring task.

## Material and resource distinctions

| Question | Shipped answer |
|---|---|
| Why can I cast but not run a machine? | Casting spends regenerating Mana; workshop functions use Source. [A05, A06] |
| Why does learning more glyphs matter beyond recipe variety? | Learned glyphs give a small permanent Mana-capacity and regeneration increase. No numeric amount is asserted. [A05] |
| How far can a basic relay reach? | Up to 30 blocks. Use the Dominion Wand jar → relay to take Source; relay → destination to send. Sneak-use the wand on the relay to clear links. [A11] |
| Why did a correctly linked relay stop? | A redstone signal disables it. [A11] |

## Common failures

- **No Source from a growing-area setup:** check natural growth within 15 blocks and a receiving jar within five. Bonemealed crop growth is specifically excluded. Effective tick/chunk behavior is untested. [A09]
- **The chamber works slowly:** passive operation is documented. Check the two-block jar distance before rebuilding the station. [A08]
- **Pedestal ingredients vanish unexpectedly:** do not transfer the chamber's catalyst rule to the Apparatus. Check the chosen recipe and stop feeding rare ingredients until its roles are clear. [A08, A10]
- **A relay has no throughput:** check link direction and redstone before assuming a larger Source producer is needed. [A11]
- **A heat-producing alternative damages the work area:** the Volcanic Sourcelink description warns that its heat changes stone to magma and then lava. Keep that option away from a starter garden; stop adding fuel and retreat from exposed hazards. No shutdown/cooling timing is established. [A12]

## Tips with trade-offs

- **Wait for natural growth before spending bone meal.** Prerequisite: an Agronomic Sourcelink and nearby jar. Benefit: tests the actual documented source trigger without wasting bone meal. Trade-off: slower feedback while crops grow. [A09]
- **Keep an uncluttered table inventory boundary.** Prerequisite: a Scribe's Table. Benefit: nearby inventories do not become accidental material suppliers while you learn glyph costs. Trade-off: manual ingredient delivery; the documented Dominion Wand toggle is the later alternative. [A03]
- **Separate the jar bank from your mana diagnosis.** Prerequisite: a saved spell and a chamber. Benefit: waiting for mana and checking Source are separate troubleshooting actions. Trade-off: two resource displays to learn; no cross-conversion is promised. [A05, A06]

## Sources

- [A03, A05–A12] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `ars_nouveau.page1.scribes_table`, `spell_mana`, `source`, `imbuement_chamber`, `enchanting_apparatus`, `volcanic_sourcelink`; `ars_nouveau.page.agronomic_sourcelink`, `ars_nouveau.page.relay`, `ars_nouveau.page2.relay`, `tooltip.source_gem`.
- [A07, A10] Same archive, `data/ars_nouveau/recipe/`: `imbuement_chamber.json`, `source_jar.json`, `agronomic_sourcelink.json`, `enchanting_apparatus.json`, `arcane_core.json`, `arcane_pedestal.json`.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [A03] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_touch.json`: `witness`.
- [A03] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/glyph_light.json`: `witness`.
- [A03] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A05] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A06] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A07] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/imbuement_chamber.json`: `witness`.
- [A07] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/source_jar.json`: `witness`.
- [A07] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/agronomic_sourcelink.json`: `witness`.
- [A08] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A09] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A10] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/enchanting_apparatus.json`: `witness`.
- [A10] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/arcane_core.json`: `witness`.
- [A10] `ars_nouveau-1.21.1-5.13.3.jar!data/ars_nouveau/recipe/arcane_pedestal.json`: `witness`.
- [A10] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A11] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
- [A12] `ars_nouveau-1.21.1-5.13.3.jar!assets/ars_nouveau/lang/en_us.json`: `witness`.
