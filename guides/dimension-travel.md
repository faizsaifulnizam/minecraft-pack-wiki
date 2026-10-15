---
layout: default
title: Dimension travel and return
permalink: /guides/dimension-travel/
baseline: dev-0.5-20261015-r2
---
# Dimension travel and return

## Baseline
Private candidate-r2, dev-0.5-20261015-r2; unapplied, not canonical adoption. Candidate Twilight Forest 4.8.3345 text is distinct from current runtime behaviour. Start with [Exploration preparation](exploration-preparation.md).

## Evidence status
**The exact candidate construction, activation caller and return lifecycle are not fully proved.** The retained candidate tip says “Throw a diamond into a pool of water surrounded by flowers.” Its tags declare water as portal fluid, `#c:gems/diamond` as activator, and separate edge and decoration sets. A tag is not a complete geometric recipe or proof of effective merged tags. [S1–S5]

An immutable upstream primary-source trace on the **1.21.1** branch, commit `008085c660f1f9fc9aad6376ea0dc8080b3c0629`, declares Minecraft 1.21.1 / mod version 4.8. It is dated to the release day of the 4.8.3345 listing, but the build-3345-to-commit correspondence and modified candidate's provenance are **unknown**. The listing reports a JAPPA reload fix, not portal mechanics. Do not treat the trace as exact-binary verification. The similarly named 1.21.x branch targets another Minecraft/mod version and is not used here. [P1–P4]

## Prerequisites
- An already approved crossing with a group plan for return; otherwise use this page to identify what still needs confirmation, not as permission to experiment with your only gear.
- Reserve activation material if the owner confirms its effective role; the candidate tag alone does not establish that all diamond-like items work.
- A clear nonflammable working area is prudent: the candidate translations describe destructive activation lightning as a configurable possibility. No effective value was read. [S1]

## Steps
1. Read the shipped hint as a **hint**, not a complete build specification: diamond, water pool, flowers. The edge tag additionally names farmland, dirt path and `#minecraft:dirt`; the decoration tag includes flowers via a tag reference and many other entries. These are declared inputs, not permission to substitute anything without confirming effective tags. [S1–S5]
2. If you need exact construction dimensions, stop at this evidence boundary. The upstream trace has a minimum of four pool spaces, horizontal validation, a sturdy floor, tagged edges and tagged decoration above those edges; successful creation shrinks the catalyst by one and invokes configurable lightning. **This is an unmatched upstream example, not a verified 2×2 construction recipe for candidate 4.8.3345.** Its activator-detection caller was not traced. Do not throw repeated valuables or enlarge a pool to solve an unresponsive candidate crossing. [P2]
3. For an already-established, owner-confirmed crossing, enter with only the planned scouting kit and clear the arrival edge before the next person comes through. Entry timing is not fixed by this evidence. In the unmatched upstream trace, normal active portal contact registers the entity for transition and delay is read from game rules, with an advancement-lock check for survival players. That does not establish this candidate's effective rules. [P2]
4. Make return the first objective after arrival. The upstream direction switch sends entities outside Twilight Forest to it, and sends entities inside it to the **configured origin dimension**, not necessarily a universal Overworld or the exact starting block. Destination creation can reuse or make a portal, reroute, or fall back; a safety-search name does not guarantee a harmless arrival. These remain upstream-only mechanics here. Do not infer a fixed coordinate ratio or a guaranteed same-portal round trip. [P2–P3]
5. Identify the existing return crossing and keep its border intact. In the unmatched upstream source, a generated portal may carry `is_one_way`, affected by a `locked` input or `shouldReturnPortalBeUsable`; candidate translation text says a return portal may require an activation item. **No universally usable exit or exact reactivation procedure is proved for this candidate.** If the group cannot confirm return, do not leave the arrival area to start combat. [S1, P3]
6. If crossing is blocked, move clear and ask the owner to confirm its established method. Candidate messages distinguish “It doesn't seem safe here...” from an unresponsive/unworthy pool; candidate translation keys describe portal disablement, permission, advancement locks and other-dimension creation. They establish available concepts, not their effective values. Do not change configuration or use commands as an assumed fix. [S1]

## Expected result
You can distinguish a shipped material hint, declared tags, an upstream implementation example and an actually confirmed group crossing. A successful outward trip does not complete the return check. An exact self-service portal recipe and universally reliable exit are deliberately **not delivered** where source correspondence is insufficient.

Useful tip: once the owner has established the crossing, make one light-kit round trip before taking rare equipment. Benefit: tests the route you will depend on. Trade-off: an extra journey; it still does not guarantee later safety, respawn location or item recovery.

## Common failures
- **The tip looks exact enough.** It omits geometry, effective tags, activation permissions, origin dimension and return locking. Do not fill those gaps from remembered wiki recipes.
- **An arrival portal guarantees escape.** Its presence, usability and linking must be distinguished. The source trace contains return-lock and fallback paths.
- **The root advancement proves entry.** The candidate root allows either being in the dimension or the custom make-portal trigger; it is not round-trip proof. [S6]
- **The source version is 4.8, so this is build 3345.** Family version and release-day alignment do not prove exact commit correspondence, original provenance or candidate bytecode equivalence.

## Sources
- [S1] `twilightforest-1.21.1-4.8.3345-universal.jar!assets/twilightforest/lang/en_us.json` — `twilightforest.tips.twilight_portal`, `config.twilightforest.*portal*`, destructive-lightning and portal warning keys.
- [S2] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/tags/item/portal/activator.json`.
- [S3] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/tags/block/portal/fluid.json`.
- [S4] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/tags/block/portal/edge.json`.
- [S5] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/tags/block/portal/decoration.json`.
- [S6] `twilightforest-1.21.1-4.8.3345-universal.jar!data/twilightforest/advancement/root.json`.
- [P1] [Primary version declaration](https://github.com/TeamTwilight/twilightforest/blob/008085c660f1f9fc9aad6376ea0dc8080b3c0629/gradle.properties#L5-L19).
- [P2] [Upstream portal validation/contact/direction](https://github.com/TeamTwilight/twilightforest/blob/008085c660f1f9fc9aad6376ea0dc8080b3c0629/src/main/java/twilightforest/block/TFPortalBlock.java#L55-L295), selected methods only; correspondence unestablished.
- [P3] [Upstream transition and generated return state](https://github.com/TeamTwilight/twilightforest/blob/008085c660f1f9fc9aad6376ea0dc8080b3c0629/src/main/java/twilightforest/world/TFTeleporter.java#L42-L530), selected methods only; correspondence unestablished.
- [P4] [Exact 4.8.3345 release listing](https://www.curseforge.com/minecraft/mc-mods/the-twilight-forest/files/7797302) — release identity only; no original-file provenance established.
