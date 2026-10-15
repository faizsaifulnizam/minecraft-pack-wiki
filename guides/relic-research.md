---
layout: default
title: "Research an already-owned relic"
permalink: /guides/relic-research/
baseline: dev-0.5-20261015-r2
---

# Research an already-owned relic

## Baseline

Development documentation snapshot **dev-0.5-20261015-r2**; not release validation. Static documentation only; effective datapacks, settings and gameplay have not been verified.

## Evidence status

The exact release's UI text supplies the research gesture, constellation task and wrong-container recovery. This is a research task, not a proven acquisition route or an executable numerical leveling build. Costs are dynamic UI substitutions, not fixed numbers recoverable from the translations.

## Prerequisites

An already-owned Relics item in the player's main inventory. Locate Controls → Research relic under the cursor. Have room to keep the item in inventory. Use [equipment slot reference](equipment-slots.md) separately.

## Steps

1. Hover the relic in the main inventory and hold the currently bound research control shown by the tooltip. Do not assume a default keyboard letter.
2. In the research interface, choose an ability available at the item's current level. A low-level message means it is not ready; do not spend resources attempting to bypass it.
3. For an unresearched available ability, connect hidden stars so the constellation matches its background image. The shipped tip says correct alignment automatically researches the ability.
4. Check that the unresearched prompt is gone. Read the ability and Experience Sources tabs before using it. An experience source can itself require an associated ability to be unlocked and researched.
5. For later planning, distinguish relic experience from vanilla player experience and leveling points. The UI says relic level-ups increase the upgrade-point pool; ability upgrades also list player-XP costs. Read the current cost before any purchase. This guide does not direct spending or prescribe an untraced upgrade click.

## Expected result

An available ability is researched through the documented puzzle. This does not establish its equip requirement, combat effect or save persistence. Optional [FULL SPOILERS — equipment workshop](equipment-workshop.md) gives a separate exact cooking upgrade.

## Common failures

- Wrong-container message: move the relic to the player's main inventory and retry; this is the release's explicit recovery.
- Hint offers a price: hints consume displayed player experience. Solve manually to avoid that expense; Shift offers automatic research, not a free shortcut.
- Quality mistaken for ability level: UI text calls quality a visual summary of random characteristics. A higher quality display is not itself more levels.
- Reroll/reset: do not use them as free undo. Both display player-XP costs, and rerolling can replace perfect values; Shift can automate costly repeated operations.

Tip: inspect Experience Sources before training. It identifies relevant use instead of wasting unrelated XP; exact quantities remain item- and state-dependent.

## Sources

- `relics-1.21.1-0.10.7.8.jar!assets/relics/lang/en_us.json`
