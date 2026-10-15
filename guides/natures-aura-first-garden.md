---
layout: default
title: "Start a Nature's Aura garden and measure its Aura"
permalink: /guides/natures-aura-first-garden/
baseline: dev-0.5-20261015-r2
---

# Start a Nature's Aura garden and measure its Aura

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Minecraft 1.21.1, NeoForge 21.1.250; Nature's Aura **41.10**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Tutorial from hash-matched recipes and shipped Book of Natural Aura entries. Not gameplay tested. Patchouli renders that book; it is not an independent magic system. The book's ritual structure is identified, but its exact code-defined geometry has not been independently transcribed here. Use its in-game structure page rather than a guessed ring diagram. [N00]

## Prerequisites

Bring two paper, one leather and any accepted sapling for the book. For one batch of Brilliant Fiber, collect four leaf blocks, four gold nuggets and one Short Grass item. Keep access to a grown tree and an oak sapling with enough space to grow. For an Environmental Eye ritual, reserve one spider eye, one gold ingot and two Gold Leaf; those are ingredient items in addition to the central oak sapling and the setup materials. [N01, N02, N04]

Work away from your main garden while learning Aura consumption. The shipped guide warns that draining an area and dimension changes affect behavior. If conditions worsen, stop adding consumers and leave the affected area; no instant restoration or universal safe radius is established. [N05]

## Steps

1. **Craft the Book of Natural Aura.** Combine two paper, leather and a sapling, shapeless. The output is a Patchouli guide book carrying `patchouli:book = naturesaura:book`; a generic empty book is not the same item. Its orange icons point toward next research steps, while red icons mark newly unlocked chapters. [N00, N01]
2. **Craft four Brilliant Fiber.** Arrange leaves at the four corners, gold nuggets at the four edge centers and Short Grass in the center. Do not substitute wheat seeds or an ordinary Grass Block. The result is `naturesaura:gold_fiber`, count four. [N02]
3. **Apply Brilliant Fiber to a tree's crown and wait.** The Brilliant Trees entry describes this as the way to produce a tree that sheds Gold Leaf when harvested. Watch for the transformed foliage before harvesting. Conversion timing, tree-size limits and the exact interaction gesture are not established by the retained text; follow the book's presentation and do not assume an immediate result. [N02]
4. **Divide your Gold Leaf between setup and products.** One leaf crafts into two Gold Powder. One leaf above one log crafts one Wooden Stand. Do not turn every leaf into powder: the Eye recipe itself consumes two leaf. [N03, N04]
5. **Prepare the Ritual of the Forest.** Open that book entry and reproduce its Gold Powder configuration around the central sapling position. Put the recipe ingredients on Wooden Stands around the setup. The text says not every shown stand is required, but it does not specify a stand radius; do not infer one from another magic mod. This manuscript cannot replace the missing geometry with a prose approximation. [N03]
6. **Make an Environmental Eye.** Use an **oak** sapling in the center and provide one spider eye, one gold ingot and two Gold Leaf on stands. Grow the central sapling, naturally or using fertilizer, to start the ritual. The ritual consumes the growing tree while transforming the ingredients. Check for `naturesaura:eye` as the recipe result. [N03, N04]
7. **Move the Eye into your hotbar.** It does not need to be actively selected according to the shipped text. Check the top-left Aura bar: half full represents the expected default level, not an empty environment. The Eye can also show stored Aura for Aura-bearing blocks. [N04]

## Expected result

You have the book, a Gold Leaf supply and a way to observe Aura before committing to consuming devices. The Eye is the handoff to [the Natural Altar and sustainable Aura reference](../reference/natures-aura-workshop.md). Do not use a full-looking bar as proof of unlimited capacity; the basic Eye cannot quantify beyond the ends of its displayed scale. [N04]

## Common failures

- **A chapter is missing:** the shipped book ties chapter visibility to advancements and highlights next steps. Its `tree_ritual` entry declares `naturesaura:gold_leaf`; the Eye entry declares `naturesaura:wood_stand`. These are book conditions, not proof of a universal code-enforced crafting lock. [N00]
- **A sapling grows but no ritual result appears:** compare the powder arrangement, stand ingredients and exact sapling species with the chosen recipe. Different rituals require different saplings. Exact geometry remains an explicit documentation gap. [N03]
- **You cannot make the setup after crafting powder:** retain leaf for stands and recipe ingredients as well. [N03, N04]
- **Aura seems absent at half a bar:** that is the documented normal level. Consult the [measurement and depletion checks](../reference/natures-aura-workshop.md), not Ars Source Jars; no cross-system power conversion is established. [N04, N05]

## Sources

- [N00–N05] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/`: `intro/intro.json`, `intro/aura.json`, `practices/gold_trees.json`, `practices/tree_ritual.json`, `items/eye.json`.
- [N00–N04] Same archive, `data/naturesaura/patchouli_books/book/book.json`; `data/naturesaura/recipe/book.json`, `gold_fiber.json`, `gold_powder.json`, `wood_stand.json`, `tree_ritual/eye.json`.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [N00] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/intro/intro.json`: `witness`.
- [N00] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/practices/tree_ritual.json`: `witness`.
- [N00] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/items/eye.json`: `witness`.
- [N00] `NaturesAura-41.10.jar!data/naturesaura/patchouli_books/book/book.json`: `witness`.
- [N01] `NaturesAura-41.10.jar!data/naturesaura/recipe/book.json`: `witness`.
- [N02] `NaturesAura-41.10.jar!data/naturesaura/recipe/gold_fiber.json`: `witness`.
- [N02] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/practices/gold_trees.json`: `witness`.
- [N03] `NaturesAura-41.10.jar!data/naturesaura/recipe/gold_powder.json`: `witness`.
- [N03] `NaturesAura-41.10.jar!data/naturesaura/recipe/wood_stand.json`: `witness`.
- [N03] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/practices/tree_ritual.json`: `witness`.
- [N04] `NaturesAura-41.10.jar!data/naturesaura/recipe/tree_ritual/eye.json`: `witness`.
- [N04] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/items/eye.json`: `witness`.
- [N05] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/intro/aura.json`: `witness`.
