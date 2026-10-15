<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/unification-workbench/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Check transformed recipes before scaling a batch

## Baseline
Private candidate **dev-0.5-20261015-r2**, unapplied; canonical baseline unchanged. Modern Industrialization 2.5.10 and AlmostUnified 1.21.1-1.4.2. This is a bounded static curriculum, not pack-wide or runtime acceptance.

## Evidence status
Selected exact-archive recipes and shipped prose, supplemented only where explicitly identified by pinned primary source. Recipes below describe shipped defaults, not resolved runtime recipes. Effective tags, resource precedence, generated recipes and active server configuration remain unverified. Reviewed against retained static evidence; not runtime-tested.

## Prerequisites
A specific recipe and ingredient/output identity, preferably the [first bronze batch](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/mi-first-steam-batch/), plus its current viewer display. AlmostUnified metadata identifies this installed release as 1.21.1-1.4.2. No saved preference order or effective configuration was inspected for this packet.

## Steps
1. Write down the exact recipe ID, machine/type, ingredient IDs or tags, and displayed result ID/count. For the retained shipped bronze recipe, the inputs are three `c:dusts/copper` tags and one `c:dusts/tin` tag; its result is three `modern_industrialization:bronze_dust`. This is the pre-transformation object, not the final pack outcome.
2. Compare the current display with that shipped object before creating a large supply line. The installed English strings include “Modified by Almost Unified!”, “Unified” and “Had Duplicates”. If the viewer exposes those markers, preserve their state alongside the ID/count. The strings alone do not prove every viewer or recipe category actually displays them.
3. Interpret differences narrowly. At exact-version upstream commit `8c2c6b0ec41a3eb6c31e39061b1c189b31cf45a4` (tag `v1.21.1-1.4.2`), GenericRecipeUnifier calls both input and output unification helpers for common keys. This is recipe-data processing, not evidence that similarly named items already in your inventory convert automatically.
4. The pinned RecipeTransformer copies recipe JSON, applies settings only when `shouldIncludeRecipe` permits, and replaces changed recipes in the map. Its duplicate handling removes non-master recipes when the type is not ignored; recipe-ID ignore checks also apply. Therefore a missing duplicate or changed result can be intended processing, but this source does not identify this pack's master or preferred material.
5. Test the current intended recipe with one batch and observe the actual output identity before changing item-pipe filters. Only whitelist the observed target after confirming it is the intended product; do not globally blacklist every other mod's bronze because one recipe changed.
6. For a discrepancy, retain the original recipe ID, current result, relevant markers and one-batch observation for review. The installed warning says not to report recipe issues to the original author. Investigate transformation/configuration first; neither that warning nor metadata establishes that AlmostUnified caused this particular fault.

## Expected result
A recipe-specific diagnosis separating shipped data, possible unification/duplicate processing, displayed results and observed production. There is no asserted preferred namespace, inventory conversion rule, universal tag equivalence or exact effective MI recipe rewrite.

## Common failures
- Same name, rejected input: spelling is not a tag-membership proof. Check the actual recipe and exact item identity.
- Shipped output differs from display: do not overwrite the source claim or assume the viewer is wrong; effective data can differ after transforms and overrides.
- No marker visible: optional viewer dependencies in metadata do not prove category coverage or loaded integration.
- Tip: retain a small sample of the actual output before setting long-lived pipe filters. This costs a test batch but avoids encoding an unverified namespace preference.
- Unresolved routes: preferred-mod order, configured exclusions, effective tags, duplicate master selection, runtime rewrite results and existing-inventory behavior. None is reconstructed from generic mod descriptions.

## Sources
- `almostunified-neoforge-1.21.1-1.4.2.jar!META-INF/neoforge.mods.toml`
- `almostunified-neoforge-1.21.1-1.4.2.jar!assets/almostunified/lang/en_us.json`
- `Modern-Industrialization-2.5.10.jar!data/modern_industrialization/recipe/materials/bronze_dust.json`
- `https://raw.githubusercontent.com/AlmostReliable/almostunified/8c2c6b0ec41a3eb6c31e39061b1c189b31cf45a4/Common/src/main/java/com/almostreliable/unified/api/unification/bundled/GenericRecipeUnifier.java`
- `https://raw.githubusercontent.com/AlmostReliable/almostunified/8c2c6b0ec41a3eb6c31e39061b1c189b31cf45a4/Common/src/main/java/com/almostreliable/unified/unification/recipe/RecipeTransformer.java`
