---
layout: default
title: "Storage boundaries and unresolved interfaces"
permalink: /reference/storage-boundaries/
baseline: dev-0.5-20261015-r2
---

# Storage boundaries and unresolved interfaces

## Baseline
**dev-0.5-20261015-r2**, Minecraft 1.21.1 / NeoForge 21.1.250. Exact archive versions appear in the sources below.

## Evidence status
Static reference. A translated feature description establishes shipped intent, not active configuration, tested compatibility or item persistence.

## Prerequisites
Use [storage choice](../guides/storage-choice.md) to select an independent route before planning integration.

## Steps
For a proposed connection, identify the producing system, receiving system, item/fluid/energy type, direction, filter and overflow behavior. Leave any unproven field unknown. Do not move your main inventory to answer an unknown.

## Expected result
A boundary checklist that distinguishes a known declaration from an untested handoff.

| Boundary | Evidence available | Not established |
|---|---|---|
| Drawer starter | `storagedrawers:oak_full_drawers_1` recipe declares oak planks and wooden-chest tag | Capacity, click controls, locking persistence and controller range |
| Backpack starter | `sophisticatedbackpacks:backpack` custom recipe and enabled condition; [first backpack access](../guides/first-backpack-access.md) supplies provisional same-version upstream held-item use evidence | Exact installed open control and build-2195 correspondence remain unknown; effective recipe, slots, Curios behavior, deposit/withdrawal, carrying lifecycle and contents through upgrades/persistence are not established |
| ME starter | Shipped guide describes drive, cells, terminal, cables and energy acceptor; small route does not require controller | Chosen power source, effective channels and working network |
| MI -> AE2 | Both identities are installed | Energy units/interface conversion, sided item/fluid transfers and automation safety |
| Drawers/backpack -> ME | Candidate connection only | Interface choice, priorities, looping, filtering and overflow behavior |

The access guide separates held-item Use Item from placement; it is not proof of the installed compiled behavior or an established open key. Stop if the interface differs and keep the empty Backpack; do not infer safe storage from an empty menu. J2's processing/interface handoff remains unresolved.

## Deletion is not capacity
Storage Drawers' shipped Void Upgrade description says it destroys excess items. Sophisticated Backpacks' Void Upgrade description says it deletes items selected by a filter; its recipe also carries an item-enabled condition. Neither is ordinary extra capacity. Avoid both while learning storage. If deletion is suspected, stop feeding the affected container and record the upgrade/filter context before further interaction; this reference cannot promise an undo or restore deleted items.

## Common failures
- A dark ME terminal is not evidence that you need a controller. Return to [AE2's unresolved power and connection checks](../guides/ae2-starter.md#common-failures).
- Equal ingredient tags do not establish identical effective outputs or interchangeable machine interfaces.
- No test here establishes save/reopen persistence. Keep a later authorized check limited to expendable items and an isolated world; do not test by breaking a stocked container.

## Sources
- `appliedenergistics2-19.2.18.jar!assets/ae2/ae2guide/getting-started.md`
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!data/storagedrawers/recipe/oak_full_drawers_1.json`
- `StorageDrawers-neoforge-1.21.1-13.11.4.jar!assets/storagedrawers/lang/en_us.json`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/backpack.json`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/void_upgrade.json`
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!assets/sophisticatedbackpacks/lang/en_us.json`
