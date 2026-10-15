---
layout: default
title: "Craft an oak drawer"
permalink: /guides/craft-first-oak-drawer/
baseline: dev-0.5-20261015-r2
---

# Craft an oak drawer

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
> Development documentation snapshot **dev-0.5-20261015-r2**. Storage Drawers **13.11.4**. Static recipe task; effective recipes and gameplay are not tested.

## Prerequisites
Prepare one `storagedrawers:oak_full_drawers_1` from its shipped recipe, if that recipe is available in your current recipe view. This page covers crafting, not drawer placement, deposit, withdrawal or persistence. Use [the route comparison](storage-choice.md) if you have not chosen between workshop storage and [a carried backpack](first-backpack-access.md).

You need a 3-by-3 crafting grid, six `minecraft:oak_planks` and one ingredient that your current recipe view accepts for `c:chests/wooden`. Tag membership and resource overrides are not established by the declaration. Do not substitute another wood just because its texture is similar.

## Steps
1. Use [recipe search](recipe-search.md) for `storagedrawers:oak_full_drawers_1`. Compare the displayed output and ingredients with the declaration below before committing materials. A missing entry or different output is a boundary to resolve, not permission to change pack settings.
2. For the matching declared recipe, fill the top and bottom rows with oak planks. Put the accepted wooden-chest-tag ingredient in the centre of the middle row; leave its other two slots empty. The exact shaped rows are `["///", " X ", "///"]`, where `/` means oak plank and `X` means the chest ingredient.
3. Check that the output is one `storagedrawers:oak_full_drawers_1`, then take that single output. The shipped declaration specifies a yield of one, not multiple drawers.

## Expected result
The recipe-supported target is one oak full drawer item with one compartment. This is not evidence of its capacity, controls or successful storage. Keep bulk stock in its existing container until a separately supported deposit-and-withdrawal task is available; [storage boundaries](../reference/storage-boundaries.md) explains what remains unproved.

## Common failures
If no matching output appears, leave the output untouched and compare the exact item ID and current accepted ingredients. A recipe-viewer omission alone does not prove a recipe cannot load. If the result conflicts, do not repeatedly consume ingredients to diagnose it. Keep the ingredients rather than editing configs or installing another mod.

## Tips and trade-offs
Use a small first craft rather than converting all your chests: it limits the materials committed while access and capacity remain unresolved. This does not promise that crafting can be undone. Do not add a Void Upgrade to solve capacity: the shipped description says “Destroys excess items.” That warning establishes deletion intent, not the precise runtime overflow algorithm.

## Sources
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!data/storagedrawers/recipe/oak_full_drawers_1.json` — complete shaped recipe declaration.
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!assets/storagedrawers/lang/en_us.json` — `item.storagedrawers.void_upgrade.desc`; label evidence only.
