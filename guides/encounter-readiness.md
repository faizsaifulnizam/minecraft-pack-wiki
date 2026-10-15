---
layout: default
title: Encounter readiness
permalink: /guides/encounter-readiness/
baseline: dev-0.5-20261015-r2
---

# Encounter readiness

## Baseline

Bosses of Mass Destruction 1.3.3, Minecraft 1.21.1. Documentation baseline; not a gameplay acceptance result.

## Evidence status

This is a preparation and go/no-go task, not an encounter activation or combat tutorial. The shipped metadata describes high-threat mobs. Exact source-to-binary control correspondence and effective server settings are not established. Recommendations below are conservative planning choices, not mod-enforced requirements. [S1]

## Prerequisites

- A party decision about acceptable losses and who may initiate encounters.
- Ordinary replacement equipment, food and an agreed fallback location. No particular armor tier, weapon damage or number of supplies is guaranteed sufficient.
- Read [exploration preparation](exploration-preparation.md) before leaving a shared base.

## Steps

1. Separate essential supplies from optional valuables. Leave irreplaceable belongings behind; take only a kit you can afford to lose. This limits loss rather than preventing death.
2. Agree on a single encounter initiator. Until exact controls are confirmed for the server, do not use unfamiliar items on suspicious blocks merely to discover their function. This also avoids accidental item consumption.
3. Before approaching an unfamiliar site, identify an ordinary retreat route and a fallback meeting place. Do not count an untested portal, teleport item or grave interaction as your way out.
4. Decide a retreat threshold before fighting: for example, inability to keep the agreed route clear. This is a party policy, not a supported boss-reset mechanic. A teammate leaving does not prove the encounter ends.
5. Assign one player to observe the result and one to keep the retreat clear. Record only what actually happened: an advancement notification, items seen and items collected are different checkpoints.
6. Choose reconnaissance instead of activation when the return route, initiator permission or replacement kit is missing. The optional [FULL SPOILERS encounter notes](../reference/encounter-reference-c.md) distinguish declared rewards from observed rewards and explain why an upstream activation recipe is not yet an exact installed-build guarantee.

## Expected result

You have a replaceable kit, one named initiator, a retreat decision and a return route that does not rely on an untested control. This completes readiness planning only; it does not establish a discovered structure, a summon, victory or successful recovery.

## Common failures

- **Someone already activated the encounter:** do not promise a reset or refund. Prioritize withdrawing by the known route; avoid spending more unfamiliar items while diagnosing it.
- **A player dies:** a rescue is a new risk decision, not an automatic step. Do not assume inventory retention, a grave, loot protection or shared advancement credit.
- **The route becomes unsafe:** abandon the attempt rather than proving the equipment was sufficient by repeated losses. Replaceable kits lower the cost of this choice, but cannot make combat safe.
- **The party returns with no reward:** compare observations in the full notes; a loot declaration alone is not proof that it ran.

## Sources

- [S1] `BOMD-NeoForge-1.21-1.3.3.jar!META-INF/neoforge.mods.toml` — version, mod identity and high-threat description. Kit/party recommendations are editorial precautions, not claims derived from a combat implementation.
