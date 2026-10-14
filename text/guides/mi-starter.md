Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/mi-starter/
Baseline: dev-0.5-20261015

# Make your first MI bronze

> Development snapshot: **dev-0.5-20261015**. Minecraft **1.21.1**, NeoForge **21.1.250**. The pack is still changing.

## Baseline
Modern Industrialization **2.5.10** in `dev-0.5-20261015`.

## Evidence status
**Shipped documentation.** The installed Forge Hammer and bronze pages support this sequence. Effective recipes, tag substitutions and machine operation have not been tested in-game for this handbook.

## Prerequisites
Ingredients for the Forge Hammer and access to copper/tin materials. Use [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/) for exact recipes. This page deliberately does not invent a copper-to-tin ratio or a complete first-boiler build.

## Steps
1. Find the Forge Hammer recipe in the current viewer and gather its ingredients. The installed guide puts it before bronze processing.
2. Make the Forge Hammer, then use it to process copper/tin ingots into dusts, or nuggets into tiny dusts, following the current recipe display.
3. Combine the matching copper and tin dusts into bronze dust. Keep dust and tiny-dust recipes separate; the guide states that nine tiny dusts make one dust.
4. Smelt bronze dust to get bronze ingots.
5. Before moving to steam automation, read the next shipped guide pages and verify the boiler, pipes, fuel/water and machine recipes. That full operational setup is not yet mapped here.

## Expected result
Bronze ingots for the next MI stage, if the current recipes and processing UI match the shipped guide. The guide also describes Forge Hammer ore processing and a hand-held Steam Mining Drill, but those are separate from a validated steam-machine network.

## Common failures
- Similar dusts from different mods may not substitute unless the actual recipe tags/unification allow it. Check the viewer rather than assuming.
- Dust and tiny dust are different quantities. Do not use the same ingredient count blindly.
- The hand-held Steam Mining Drill needs both water and solid fuel according to the installed guide. That does not establish how a boiler or steam pipe is operated.
- No MI-to-AE2 power bridge is verified by this starter page.

## Sources
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/forge_hammer.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/steam_age/making_bronze.md`

[Pack map](https://faizsaifulnizam.github.io/minecraft-pack-wiki/pack-map/) lists the next systems without imposing a shared progression gate.
