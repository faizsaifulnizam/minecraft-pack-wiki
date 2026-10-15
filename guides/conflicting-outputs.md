---
layout: default
title: "Check and choose a conflicting crafting output"
permalink: /guides/conflicting-outputs/
baseline: dev-0.5-20261015-r2
---

# Check and choose a conflicting crafting output

## Baseline
Polymorph 1.1.0+1.21.1, EMI 1.1.24 and JEI 19.32.0.359. How-to: avoid consuming ingredients for the wrong result.

## Evidence status
Installed Polymorph identity is freshly hash-matched. The UI procedure below is **supplemental upstream documentation**, pinned to the project's 1.21.x branch, not proven to match the exact installed release. No pack-specific conflicting recipe pair, selection packet success or recipe transfer has been runtime verified. Continue only when the described selector and result actually appear.

## Prerequisites
A crafting screen with a visible result; enough ordinary ingredients for a small test and inventory space for the result. Start from [recipe search](recipe-search.md) to identify the item you actually want. Do not use EMI's saved Shift+left-click craft-all action until a single output is confirmed. There is no named guaranteed conflict example in this evidence.

## Steps
1. Find the wanted recipe and note its result name, count and item identity where the UI exposes it. Place the ingredients in the relevant crafting grid. Merely locating the desired item in EMI does not establish that the current result slot produces it.
2. Inspect the actual result slot before taking anything. If it matches your goal, no selector intervention is needed. If it differs, leave the ingredients unconsumed.
3. When those ingredients match multiple recipes and a Polymorph button appears above the output slot, press that button. Upstream describes a list of possible results. If the button is missing or its location differs, stop this procedure rather than clicking an unlabelled nearby control.
4. Select the wanted listed result. The checkpoint is the crafting output changing to that item. If the desired item is absent from the list, do not take another item as a workaround; investigate the recipe, workstation and ingredients instead.
5. Take one ordinary result and inspect it. Recheck name and count before repeating or using a bulk craft. Upstream describes remembering the choice while the ingredients do not change, but this pack has not exercised that behavior. Recheck after changing ingredients, reopening a screen or transferring a recipe.
6. To back out before a craft, do not take the result. Remove the ingredients individually into available inventory slots. Avoid Force Clear Grid because its [drop warning](inventory-safety.md) makes it unsuitable as a universal rollback.

## Expected result
The visible output and the one inspected craft agree with the wanted item, or you stop without consuming the ingredients. These are reader checkpoints; no craft was executed during authoring.

## Common failures
- **No selector:** it may not be a multiple-recipe situation in the effective pack, or the screen/integration may not expose a selector. Static installation does not decide which cause applies. A removed or overridden recipe cannot be restored merely by choosing another output.
- **The wanted result is not listed:** compare the exact recipe and workstation instead of repeatedly choosing the wrong result. Do not assume recipes with similar ingredient names use interchangeable tags.
- **Viewer transfer chose a different output:** inspect the result after transfer and use the selector only if available. Installed EMI/JEI integration classes do not prove successful transfer on this stack.
- **Selection does not change the output:** stop before crafting. Preserve a description of screen, inputs, visible choices and expected item for the owner. Polymorph ships a Networking Failure message, but this work has not observed such a failure.
- **A furnace also appears ambiguous:** upstream documents a selector above furnace output and block-persisted selection. That is a separate, untested route; this guide does not establish fuel timing, existing-output handling or save/reopen behavior. Do not start a valuable smelt to test it.

## Tip: preview, select, then scale
Prerequisite: a visible supported selector and disposable ingredients. Technique: confirm the selected output with one small craft before bulk action. Benefit: limits the ingredients committed to a wrong output. Trade-off: one extra inspection and no protection against subsequent changed inputs. Sources: upstream crafting selector description and saved EMI craft-one/craft-all bindings.

## Sources
[Polymorph upstream crafting and smelting documentation](https://github.com/illusivesoulworks/polymorph/blob/a2dc1e5a91e5694943d84e32caa729cd477098e3/README.md), pinned 1.21.x branch; exact installed metadata and `assets/polymorph/lang/en_us.json`; processed EMI bindings. Claim E-POLY explicitly retains the release-correspondence limitation. No commands were run to enumerate conflicts and no logs were read.
