---
layout: default
title: "Read an enchantment before committing equipment"
permalink: /guides/enchantment-information/
baseline: dev-0.5-20261015-r2
---

# Read an enchantment before committing equipment

## Baseline
EMI Enchanting 0.1.2+1.21+neoforge, Enchantment Descriptions 21.1.11 and EMI 1.1.24. How-to with a compact named-enchantment reference.

## Evidence status
Exact-version translation labels and shipped descriptions; saved EMI lookup bindings. **Not runtime tested.** The Enchantment Info category's presence in a running viewer, generated values, modded-enchantment support and compatibility lists remain unverified. Descriptions are summaries, not damage formulas or promises about pack-specific overrides.

## Prerequisites
An item or enchantment name to inspect; a supported tooltip/recipe-viewer context. Do not equip cursed gear, spend XP or apply an enchantment merely to discover its effect.

## Steps
1. Hover the relevant item or enchanted book and read the enchantment name. Enchantment Descriptions ships the prompt **Hold shift to view enchantment descriptions**. If that prompt is shown, hold Shift while keeping the same target hovered. Shift is a shipped instruction, not proof that this pack's tooltip activation setting is unchanged.
2. Use [EMI search and recipe lookup](recipe-search.md) to find the named item/book; R is the saved recipes action in the applicable context. If an **Enchantment Info** category appears, open it. That is the exact shipped category label; the evidence does not establish a separate Enchantment Info hotkey or guarantee that R reaches it for every target.
3. In that category, read **Enchantment Description**, **Max Level**, **Valid Items** and **Exclusions** before considering an application. Also distinguish **Treasure**, **Curse**, **Villagers Trade** and **Randomly Selectable**. A category label with a yes/no template is not itself an evaluated value for a particular enchantment.
4. Compare a familiar named description below with the tooltip as a low-risk sanity check. If the UI displays **Unknown Enchantment**, a translation key or no description, record the name and stop making effect/compatibility assumptions. Another mod's namespace in Enchantment Descriptions' bundled language file is not evidence that that mod is installed.
5. Leave equipment unchanged until both the effect and the target-item/exclusion information are understood. If no applicable compatibility information appears, ask for exact-item verification rather than treating a missing exclusion as permission to combine enchantments.

## Expected result
You can distinguish effect text from eligible-item and exclusion information, and identify an unresolved entry without spending resources. This authoring has not applied or combined an enchantment.

## Named description reference
The following are concise original summaries of Enchantment Descriptions' shipped text, not numeric or progression guidance.

| Enchantment ID | Shipped-description meaning | Decision it helps |
|---|---|---|
| `minecraft:mending` | XP repairs armor/tool durability | Do not confuse repair with a slower durability-loss rate |
| `minecraft:unbreaking` | Slows durability loss | Different function from Mending; no stacking compatibility proven here |
| `minecraft:fortune` | Some blocks, such as coal/diamond ore, may drop more items | Not a promise of extra drops from every block |
| `minecraft:silk_touch` | Collects fragile blocks such as glass | Identify collection behavior rather than assuming a yield multiplier |
| `minecraft:infinity` | Free normal-arrow shots require at least one arrow | Do not discard the last normal arrow based on the name alone |
| `minecraft:binding_curse` | Prevents removal from an armor slot | Inspect before equipping; no removal/recovery method established here |
| `minecraft:vanishing_curse` | Destroys the cursed item on death while in inventory | Do not assume a storage or death-recovery mod overrides the curse |
| `minecraft:density` | Attack damage increases with fall distance | Not a fixed damage bonus or tested combat recommendation |
| `minecraft:breach` | Attacks are more effective against armored targets | Distinguish armor-related effect from Density's fall condition |
| `minecraft:wind_burst` | Smash attacks launch the user back into the air | Recognize movement consequences before applying; no safe-height guarantee |

## Common failures
- **Shift does not reveal text:** the shipped prompt is not captured effective configuration. Check the target and visible instruction; do not invent another activation key.
- **No Enchantment Info category:** verify the viewer context and item first. Static addon installation does not certify category registration, modded support or transfer.
- **A book describes an effect but cannot apply:** description availability and Valid Items/Exclusions answer different questions. Do not consume another book to test compatibility.
- **A modded enchantment is unknown:** record its literal ID when available. These vanilla descriptions are not substitutes for that enchantment's own mechanics.

## Tip: compare purpose before level
Prerequisite: readable descriptions. Technique: compare Mending with Unbreaking, or Fortune with Silk Touch, by the kind of effect first; then consult Max Level and target eligibility. Benefit: avoids choosing by a high numeral while misunderstanding the function. Trade-off: this is not a best-build recommendation, and no compatibility or numerical yield is implied.

## Sources
EMI Enchanting 0.1.2 `assets/emi_enchanting/lang/en_us.json`; Enchantment Descriptions 21.1.11 `assets/enchdesc/lang/en_us.json`; processed EMI bindings. Retained claims E-ENCHANT-UI and E-ENCHANT-NAMED keep the exact language keys and archive hashes for independent review.
