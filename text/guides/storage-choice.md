<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/storage-choice/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Choose your first storage route

## Baseline
Development snapshot **dev-0.5-20261015-r2**: Storage Drawers 13.11.4, Sophisticated Backpacks 3.26.9 and AE2 19.2.18.

## Evidence status
Static decision how-to, not a tested crafting or migration tutorial. The recipes below are shipped declarations; enabled conditions, resolved tags, overrides and recipe-viewer coverage still need confirmation.

## Prerequisites
A clear goal and access to [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/). Do not move valuable stock or install deletion upgrades as part of choosing a route. The [storage hub](https://faizsaifulnizam.github.io/minecraft-pack-wiki/systems/storage/) keeps the alternatives separate.

## Steps
1. Write down one immediate outcome: carry items, use workshop compartments, or search an ME inventory. Choose only the matching route below; these are alternatives, not a progression sequence.
2. For carrying items, look up `sophisticatedbackpacks:backpack`. Its shipped pattern is `SLS / SCS / LLL`: S is the string tag, L the leather tag, C the wooden-chest tag. The declared output is one Backpack. The recipe uses the custom `sophisticatedbackpacks:basic_backpack` type and an item-enabled condition; if the viewer has no entry, stop rather than assume the pattern is currently craftable.
3. For workshop compartments, look up `storagedrawers:oak_full_drawers_1`. The shipped pattern has three oak planks across the top and bottom rows and a wooden-chest-tag ingredient in the middle slot. It declares one drawer. Keep capacities, locks and item removal as unresolved interaction checks, not guessed instructions.
4. For searchable storage, use [AE2 preparation](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/ae2-starter/). Its material and processor route is documented, but working power must be established before you treat it as usable storage. MI installation alone does not close that prerequisite.
5. Record the chosen item, the recipe you actually see and the first unresolved boundary. Use [storage boundaries](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/storage-boundaries/) before any later transfer or upgrade work.

## Expected result
You can name the route and its next prerequisite without buying into an unverified cross-system dependency. This how-to completes a choice, not a working in-game build.

## Common failures
- Missing backpack recipe: its enabled condition and custom serializer need checking. Do not remove mods or rewrite configs to force the declaration to load.
- Conflicting output: stop before taking the result. Polymorph is installed, but this pilot has not established its exact controls or supported containers. Record the displayed output ID and context; do not repeatedly consume ingredients.
- No recipe transfer: check the current item/container/category and ingredients as described in [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/#common-failures); failed transfer does not prove a recipe impossible.

## Tips with trade-offs
- Before preparing an AE2 expansion, preserve flawless budding certus in place. The shipped guide says a pickaxe degrades it even with Silk Touch, with no repair to flawless. Benefit: keep the non-degrading source; trade-off: travel to it until a separately evidenced relocation route is available. This is resource preservation, not an instruction to attempt advanced transport.
- When selecting backpack automation, start by investigating the Filter Upgrade rather than a Void Upgrade. The translation describes filtering piped input/output, while voiding deletes selected items. Benefit: frame a non-deletion design; prerequisite: verify the actual filter UI and pipe compatibility separately. Trade-off: rejected items still need an overflow plan, which is not yet verified here.

## Sources
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/backpack.json`
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!data/storagedrawers/recipe/oak_full_drawers_1.json`
- `appliedenergistics2-19.2.18.jar!assets/ae2/ae2guide/getting-started.md`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!assets/sophisticatedbackpacks/lang/en_us.json`
