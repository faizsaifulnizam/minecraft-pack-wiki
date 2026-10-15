---
layout: default
title: "Choose a storage direction"
permalink: /systems/storage/
baseline: dev-0.5-20261015-r2
---

# Choose a storage direction

## Baseline
Development snapshot **dev-0.5-20261015-r2**, Minecraft 1.21.1 / NeoForge 21.1.250. AE2 19.2.18, Storage Drawers 13.11.4 and Sophisticated Backpacks 3.26.9 are installed.

## Evidence status
Shipped guide, translations and selected recipes were read. No storage interaction, transfer or persistence test was run. This hub helps you choose a route; it does not certify a working combined network.

## Prerequisites
Decide whether your immediate problem is carrying loot, organizing workshop materials or searching a base inventory. Use [recipe search](../guides/recipe-search.md) to check the chosen item's current recipe. Those saved bindings are not a guarantee of custom-category coverage.

## Steps
1. If you need a portable option, examine the Backpack candidate in [choose your first storage route](../guides/storage-choice.md). Its shipped recipe uses leather, string and a wooden-chest tag, with an item-enabled condition.
2. If you want workshop compartments, examine the oak 1x1 drawer recipe in the same guide. Do not infer effective capacity from the item's name.
3. If your goal is a searchable ME inventory, follow [AE2 preparation](../guides/ae2-starter.md), which separates materials, processors and the small network. Compatible power is still a blocker, not an assumed MI prerequisite.
4. Before joining systems, read [storage boundaries](../reference/storage-boundaries.md). Treat each as a separate route until its interface has evidence.

## Expected result
A chosen first route and a short list of unresolved prerequisites. You have not yet proved a successful craft or safe migration of existing stock.

## Common failures
- Planning a searchable inventory does not provide power. Stop at the AE2 power boundary rather than crafting a controller as a universal fix.
- A backpack's filter and void upgrades are different tools: the shipped text describes pipe filtering versus item deletion. Keep voiding out of your initial route. See the [deletion boundary](../reference/storage-boundaries.md#deletion-is-not-capacity).
- Do not make this route a mandatory gate for magic or exploration; no such pack-wide ordering is established.

## Sources
- `appliedenergistics2-19.2.18.jar!assets/ae2/ae2guide/getting-started.md`
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!data/storagedrawers/recipe/oak_full_drawers_1.json`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/backpack.json`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!assets/sophisticatedbackpacks/lang/en_us.json`
