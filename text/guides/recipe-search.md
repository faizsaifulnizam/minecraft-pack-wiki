Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/
Baseline: dev-0.5-20261015

# Find recipes and item uses

> Development snapshot: **dev-0.5-20261015**. Minecraft **1.21.1**, NeoForge **21.1.250**. The pack is still changing.

## Baseline
EMI 1.1.24 and JEI 19.32.0.359 in `dev-0.5-20261015`.

## Evidence status
**Saved configuration.** These bindings/layout values were read from global files. Recipe categories, contextual key handling and transfers have not been exercised as part of this documentation check.

## Prerequisites
An open inventory/recipe-viewer context with EMI enabled. If the sidebar is hidden, check its saved visibility binding rather than reinstalling mods.

## Steps
1. In an inventory screen, look for the item sidebar on the right. Press Ctrl+F to focus EMI search in its supported context.
2. Type an item name. The saved search includes tooltips by default; do not assume tags or mod names are included without a prefix or setting change.
3. Hover an item and try R for recipes, or U for uses. EMI also saves left/right-click recipe/use actions in the appropriate item context.
4. Press A on an item in the applicable context to add it to favourites. The saved favourites panel is on the left.
5. Use Backspace to go back in EMI's supported context.

## Expected result
A matching item list and a recipe/uses view for a supported category. This is the intended UI flow from saved bindings, not a promise that every custom recipe is registered or transferable.

## Common failures
- No sidebar: Ctrl+O is the saved EMI visibility toggle; JEI has an overlapping binding, so test the actual screen response.
- U opens a waypoint-related screen: the same key has contextual uses. Check Controls and the screen you are using.
- An ingredient does not transfer: first check the category, inventory, container and missing ingredients. Do not treat transfer failure as proof the craft is impossible.

## Sources
Saved global `config/emi.css` binding/layout descriptions and selected `config/jei/jei-client.ini` settings. The handbook omits raw personal configuration. [Troubleshooting](https://faizsaifulnizam.github.io/minecraft-pack-wiki/troubleshooting/) covers overlaps.
