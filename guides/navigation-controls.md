---
layout: default
title: "Identify navigation controls without opening a map"
permalink: /guides/navigation-controls/
baseline: dev-0.5-20261015-r2
---

# Identify navigation controls without opening a map

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
**Development documentation snapshot:** Minecraft 1.21.1 / NeoForge 21.1.250; Xaero's Minimap 26.6.0, Xaero's World Map 1.47.0 and FTB Chunks 2101.1.22. This reference uses previously processed saved bindings, not live controls or private map data. The saved-controls observation predates this documentation snapshot and has not been refreshed. It does not prove exact-version navigation behavior or current effective bindings.

## Prerequisites

You want to distinguish map providers or report an overlapping control without revealing terrain, waypoints or server identity. This task needs only the reference below and your intended action; do not launch a game or open a map to complete it. For a later authorized controls review, use [control contexts](control-contexts.md), not trial keypresses over valuables.

## Read the saved-control reference

These are historical **saved values**, not factory defaults or instructions to press them. The literal action identifiers let you distinguish similarly named providers.

| Provider and action identifier | Previously saved value | Boundary |
|---|---|---|
| Xaero World Map `gui.xaero_open_map` | M | Same saved key as FTB map; do not invoke to diagnose overlap |
| FTB Chunks `ftbchunks.map` | M | A second provider, not evidence of synchronized maps |
| Xaero minimap settings `gui.xaero_minimap_settings` | Y | Saved settings control; no permission to change it |
| Xaero World Map settings `gui.xaero_open_settings` | Right bracket | Also saved for Sophisticated transfer-to-inventory; context matters |
| Xaero waypoint screen `gui.xaero_waypoints_key` | U | Also a recipe-viewer uses key; opening waypoints exposes private state |
| Xaero new waypoint `gui.xaero_new_waypoint` | B | Creation control; not an inspection shortcut |
| Xaero instant waypoint `gui.xaero_instant_waypoint` | Keypad add | Creation control; do not test as a harmless toggle |
| Xaero enlarge map `gui.xaero_enlarge_map` | Z | Also saved for Twilight zoom; not a proved conflict |
| Xaero World Map zoom `gui.xaero_map_zoom_in` / `gui.xaero_map_zoom_out` | Unbound / unbound | `key.keyboard.unknown` is the recorded value, not a key called Unknown |
| FTB minimap zoom `ftbchunks.minimap.zoomIn` / `ftbchunks.minimap.zoomOut` | Equals / minus | Do not transfer these keys to Xaero by analogy |

## Steps

1. Write the desired action and provider: for example, “identify the Xaero World Map control,” not just “map broken.” Use the table to separate the two map providers without opening either.
2. Classify the intended action as display, settings or state creation. Keep waypoint creation separate from viewing. Do not press B or Keypad add merely to discover what happens.
3. Record the screen context in which the problem happened, without coordinates, terrain screenshots or waypoint names. A saved duplicate key is a possible overlap, not proof that both handlers run in that context.
4. If a later controls-only inspection is authorized, compare the current action entry with this historical reference. Controlling 19.0.5 supplies Show All, Show Conflicts, Show Unbound and Available Keys. Its exact labels are documented in `Controlling-neoforge-1.21.1-19.0.5.jar!assets/controlling/lang/en_us.json` (`options.showAll`, `options.showConflicts`, `options.showNone`, `options.availableKeys`). Inspect only; this task prescribes no reset or remap. Missing/unbound entries do not establish missing map data.
5. Produce a short support note: provider, action identifier, intended context, historical binding and whether a current value is known. Leave current values unknown if they have not been inspected. Do not attach map folders, personal settings exports or server-profile files.

## Expected result

You can name the map provider and action without opening a private map, creating a waypoint or changing settings. This does not establish navigation, dimension switching, waypoint sharing, teleport permission, map persistence or restoration behavior. Those mechanics need additional exact-version evidence and separately authorized acceptance.

## Common failures

If M selects an unexpected provider later, do not delete map caches or reset both mods. Preserve personal map state and report the provider/context mismatch first. If U opens an unexpected screen, return to the original context rather than creating a waypoint to test the key. See [inventory safety](inventory-safety.md) before any future item-context investigation.

## Tip and trade-off

Use action identifiers in a support note instead of a screenshot of your world. This makes two M bindings distinguishable without exposing explored terrain; the trade-off is that a control-only report cannot diagnose the map's contents. A map display also does not prove [claim permissions](shared-base-preflight.md).

## Evidence limits

The binding table is a historical saved observation, not an archive-derived default table. Only the Controlling labels above have the cited exact-version archive-entry witness. Actual Xaero navigation controls, gestures and map/waypoint lifecycle remain unsupported by the available exact-version evidence; no navigation tutorial is claimed.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
