---
layout: default
title: "Diagnose an Occultism ritual and manage its books"
permalink: /reference/occultism-workbench/
baseline: dev-0.5-20261015-r2
---

# Diagnose an Occultism ritual and manage its books

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Occultism **1.224.5**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Reference/how-to from hash-matched Dictionary of Spirits entries, translations, recipes and conditions. Not runtime tested. Start with [the conversion work area](../guides/occultism-first-workbench.md). Detailed first-summon identity, layout and discovery mechanics live on [Occultism procedures — FULL SPOILERS](occultism-procedures.md), not in this safe reference.

## Prerequisites

Identify the exact ritual you intend to run in the Dictionary. You need its matching pentacle, activation item and ingredients, not merely a generic chalk circle. Keep ordinary protection and an unobstructed way out. The book cautions that summoning can cause harm; this page does not certify all rituals as friendly. [O07]

## Steps

1. **Check the center and ingredient roles.** The golden bowl activates the ritual; ordinary sacrificial bowls hold ingredient items. Keep the ingredient bowls within eight blocks horizontally of the pentacle center. Their exact decorative positions do not matter according to the bowl entry. The first-ritual walkthrough separately describes its four bowls as within eight blocks of the central bowl; use a same-level nearby layout rather than assuming vertical freedom. [O08]
2. **Match the drawing, not its decorative glyph shapes.** The chalk instructions say color and position matter, while repeated clicks cycle a decorative sign. Stop redrawing a correctly positioned mark merely because its symbol differs from an illustration. A higher ritual may need different chalk; basic chalk is not a universal substitute. [O09]
3. **Check the activation book type and binding.** The shipped guide says the correct tier of Book of Binding must be bound using the Dictionary. The individual spirit name is decorative for recipe eligibility, but the book type is not. Crafting with the Dictionary does not consume that Dictionary. [O10]
4. **Read the waiting state before adding more items.** Grey particles with no ingredient consumption mean the ritual may be waiting for a specified item use or sacrifice. Check that exact ritual's instructions; do not provide an arbitrary animal or valuable item. The golden bowl's documented redstone states are 0 inactive, 1 waiting for sacrifice, 2 waiting for item use and 8 running. These are output strengths, not seconds or progress percentages. [O11]
5. **If you are automating, distinguish activation from output collection.** A hopper or pipe can insert the activation item into the golden bowl to start the ritual. The guide warns that automation of rituals producing tamed animals/familiars instead creates untamed ones. A down-facing sacrificial bowl above the golden bowl can hold crafted item outputs instead of leaving them on the ground, up to three blocks higher; do not treat that as guaranteed entity capture. [O12]

## Expected result

A fault can be separated into wrong drawing, missing ingredients, wrong/unbound activation item, an intentional waiting state or an automation-specific outcome. The checks do not establish that an unknown ritual is safe to start, cancel or leave unattended. If harm or unexpected entities appear, retreat rather than feeding further ingredients; no universal despawn/cancellation command is supplied.

## Book reference

| Book | Job | Important limit |
|---|---|---|
| Dictionary of Spirits | Guide and binding aid | Its naming behavior can affect automated item matching. [O10, O13] |
| Book of Binding | Ritual activation after correct binding | A matching name does not replace the required spirit tier/type. [O10] |
| Book of Calling | Instructions, capture and release for supported worker spirits | Not every summoned spirit has a corresponding calling book. [O14] |

The calling-book text documents right-click air for configuration; sneak-right-click a block to apply the selected action; sneak-right-click a matching spirit to capture it; and right-click a book carrying a captured spirit to release it. If a supported spirit's book is lost, a replacement recipe exists and sneak-right-click assigns it. These are shipped interaction descriptions, not verified saved keyboard bindings or a promise that every entity is capturable. [O14]

## Common failures

- **An automated bound-book craft never finishes:** random spirit-name components can make the result differ from a pattern's expected item. The guide proposes naming a Dictionary in an anvil, configuring patterns with that Dictionary if needed, and using that same Dictionary in subsequent crafts so the produced names agree. This is documented advice, not a tested AE2 integration. [O13]
- **Ingredients are present but ignored:** check ordinary versus golden bowl roles and the eight-block horizontal limit before changing the ritual. [O08]
- **The drawing looks different:** position and chalk color matter, not the decorative symbol. [O09]
- **Grey particles persist:** consult the explicit sacrifice/item-use conditions; adding more ordinary ingredients does not answer a different waiting requirement. [O11]
- **A calling book does not capture something:** it needs the same supported spirit type. Do not infer boss/player capture or use a main-world entity as a probe. [O14]

## Tips with trade-offs

- **Use repeatable book names for planned automation.** Prerequisite: an anvil, Dictionary and a pattern-based crafting system. Benefit: removes one documented source of component mismatch. Trade-off: existing random-name patterns may need reconfiguration; no integration was tested here. [O13]
- **Use redstone state as a question, not a success certificate.** Prerequisite: a way to read the bowl's signal. Benefit: distinguishes waiting from running without supplying random items. Trade-off: it does not identify the missing sacrifice/item; the exact recipe still must be read. [O11]
- **Keep crafted item outputs off the floor.** Prerequisite: an appropriate sacrificial bowl mounted facing down above the center. Benefit: the documented output catcher reduces loose item handling. Trade-off: it applies to crafted items, not a general creature-containment system. [O12]

## Sources

- [O07–O14] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `book.occultism.dictionary_of_spirits.getting_started.` prefixes `intro`, `ritual_prep_bowl`, `ritual_prep_chalk`, `books_of_binding`, `grey_particles`, `first_ritual`, `books_of_binding_automation`, `books_of_calling`.
- Same archive, corresponding `data/occultism/modonomicon/books/dictionary_of_spirits/entries/getting_started/*.json`; per-page conditions are retained privately. Navigation-parent edges are not claimed as hard gameplay gates.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [O07] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O08] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O09] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O10] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O11] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O12] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O13] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
- [O14] `occultism-1.21.1-neoforge-1.224.5.jar!assets/occultism/lang/en_us.json`: `witness`.
