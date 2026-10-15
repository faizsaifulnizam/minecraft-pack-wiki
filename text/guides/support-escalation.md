<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/support-escalation/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Prepare a privacy-safe support request

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
> Development documentation snapshot: **dev-0.5-20261015-r2**. Minecraft **1.21.1**, NeoForge **21.1.250**. Static records are not effective settings or runtime acceptance.

Prepare a text-only request before deciding whether any diagnostic collection is necessary. You need the revision label and an account of what you already observed. Do not reproduce a crash, start hosting, launch a world or run a profiler for this checklist.

## Prerequisites
Use only the revision label and already-known observations described above. This task does not require opening the game or private files.

## Steps
1. Name the documentation revision, Minecraft/loader versions and affected system. If your installation may differ, say so instead of asserting an exact match. Use [graphics roles](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/graphics-and-books/) to separate renderer, shader, distant terrain and frame-generation questions.
2. Describe the action, expected result, actual result and whether it happens every time. State “not measured” for performance when appropriate. Separate camera movement, walking, hand animation and distant-terrain symptoms rather than grouping them as “lag.” Do not invent a reproduction you have not tried.
3. Add only already-known context: single-player versus multiplayer, host versus joining client, affected screen, and whether the symptom followed an approved change. Do not include the address, seed, coordinates, world name or another player's identity.
4. Review the request before sending. Remove account names/UUIDs, tokens, IP/domain addresses, local user paths, chat, maps/waypoints and world locations. A screenshot can expose these in overlays, chat and window titles: use text instead unless a reviewed crop is genuinely needed.
5. Ask the pack maintainer which **specific minimal excerpt** is needed and why, who will receive it, and whether it leaves your machine. Start privately with the maintainer; do not paste into a public issue or upload service by default. This page does not send anything.

## Copy this template
```text
Documentation revision / actual installation match: known or unknown
System and symptom:
Action already performed:
Expected / actual:
Frequency and last approved change:
Single-player or multiplayer / host or client (no address):
Already-known shader / DH / generation state, otherwise unknown:
Evidence level: owner observation / saved record / not measured
Requested next decision:
Redaction reviewed: yes or no
```

## Gate additional evidence
A complete log, crash report, profiler recording, F3+L archive, screenshot or world backup is not automatically safe to share. Review contents and upload/export behavior before authorizing collection. Treat F3+L bundles as private world-derived data, not just timing CSVs. This is a conservative sharing rule, not a claim that every bundle contains every sensitive field.

Spark is present as a diagnostic utility (`spark-1.10.124-neoforge.jar!META-INF/neoforge.mods.toml`); that establishes neither a safe command nor an upload policy. Do not run commands, attach recording tools or generate a viewer link from this guide. Exact selected-build collection controls, output contents and service behavior need separate review and explicit permission.

**Checkpoint:** you have a redacted draft that separates facts from unknowns and asks one answerable question. No collection or upload is required to complete it.

**Recovery:** if a draft contains sensitive data, do not send it; remove the data and review again. If already shared, contact the recipient/platform to request removal and tell the owner what category was exposed without reposting the secret. Redaction is not retroactive access control.

**Tip:** report “loaded,” “saved enabled,” “visually accepted” and “measured improvement” separately. None implies the next. See [existing troubleshooting](https://faizsaifulnizam.github.io/minecraft-pack-wiki/troubleshooting/) for bounded saved-state explanations, and [comfort choice](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/comfort-settings-choice/) before proposing graphics changes.

## Expected result
A labelled choice record or redacted support draft as described above, not a settings change, diagnosis or runtime result.

## Common failures
Missing observations remain unknown. Stop before collection, changes or sending; retain the permission and privacy gates above.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
