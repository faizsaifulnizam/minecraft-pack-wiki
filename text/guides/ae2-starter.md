Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/ae2-starter/
Baseline: dev-0.5-20261015

# Prepare your first AE2 storage system

> Development snapshot: **dev-0.5-20261015**. Minecraft **1.21.1**, NeoForge **21.1.250**. The pack is still changing.

## Baseline
Applied Energistics 2 **19.2.18** in `dev-0.5-20261015`.

## Evidence status
**Shipped documentation/data.** The installed guide supports this route. This is a preparation/build outline, not a gameplay-tested end-to-end network tutorial. A working power source and this pack's cross-mod power compatibility are not established here.

## Prerequisites
Access to meteorite materials, a way to make the listed AE2 components, and a power supply compatible with the energy acceptor. Check each current recipe in [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/). Do not assume MI cables are compatible merely because MI is installed.

## Steps
1. Find an AE2 meteorite. The shipped guide suggests a Meteorite Compass if needed; check its actual recipe before crafting.
2. Collect certus material and the Mysterious Cube's four inscriber presses. **Do not break flawless budding certus with a pickaxe, even Silk Touch**: the guide says it degrades and cannot be restored to flawless.
3. Use the Charger to obtain charged certus as needed. The guide makes Fluix from charged certus, redstone and nether quartz in water.
4. Use the Inscriber and presses to prepare processors. Consult the current recipe view for each processor rather than mixing up printed circuits and completed processors.
5. Prepare one ME Drive, one Terminal or Crafting Terminal, one Energy Acceptor, a few ordinary glass/covered/smart cables and storage cells. The shipped small-network list does not require a controller.
6. Place the drive and energy acceptor together; the guide distinguishes cube and flat acceptor forms. Connect the terminal through cable, insert the cells, and supply compatible energy. Stop here if the power interface is unresolved rather than adding random power mods.

## Expected result
The shipped guide's target is a small searchable ME inventory, without autocrafting. Whether it works with the chosen power source and current pack configuration still needs a real build check.

## Common failures
- Breaking flawless budding certus loses its flawless form according to the installed guide. Preserve the source in place.
- A storage cell outside a drive/chest is not the network storage setup described here.
- A dark terminal can have several causes; this handbook has not validated your energy, channels or connections. Do not infer a missing controller as the default cause.
- A later network expansion needs a separate channels/devices check; this guide does not certify a large network or optimiser correctness.

## Sources
- `appliedenergistics2-19.2.18.jar!assets/ae2/ae2guide/getting-started.md`
- `appliedenergistics2-19.2.18.jar!data/ae2/recipe/charger/guide.json`
- `appliedenergistics2-19.2.18.jar!data/ae2/recipe/inscriber/calculation_processor_print.json`
- `appliedenergistics2-19.2.18.jar!data/ae2/recipe/inscriber/calculation_processor.json`

[Pack map](https://faizsaifulnizam.github.io/minecraft-pack-wiki/pack-map/) separates this storage route from unverified cross-mod automation.
