---
layout: default
title: "Plan shared-base access without changing permissions"
permalink: /guides/shared-base-preflight/
baseline: dev-0.5-20261015-r2
---

# Plan shared-base access without changing permissions

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
**Development documentation snapshot:** Minecraft 1.21.1 / NeoForge 21.1.250; FTB Teams 2101.1.10 and FTB Chunks 2101.1.22. Exact-version upstream declarations and command registration support this preflight; effective permissions, compiled correspondence and multiplayer behavior are not runtime verified.

## Prerequisites

You need the base owner's agreement on who may build, open ordinary containers, use machines and invite others. This task produces an access request, not a claim or a permission change. No world, map or team screen needs to be opened to complete it.

## Steps

1. Make an access-request table with four columns: person/role, intended action, target type and owner decision. Separate placing/breaking blocks from interacting with a block. FTB Chunks declares separate `block_edit_mode` and `block_interact_mode` properties; do not collapse these into one promise of “base access.” [Property declarations](https://github.com/FTBTeam/FTB-Chunks/blob/a90e58e431879f5213629373ea9cde7001ebef45/common/src/main/java/dev/ftb/mods/ftbchunks/api/FTBChunksProperties.java#L36-L44).
2. Add separate rows for real players and automation using fake players. The source declares `allow_fake_players`, `allow_named_fake_players` and `allow_fake_players_by_id`. These are policy inputs, not evidence that a particular machine is authorized. Leave their owner decisions unresolved rather than enabling them. [Fake-player properties](https://github.com/FTBTeam/FTB-Chunks/blob/a90e58e431879f5213629373ea9cde7001ebef45/common/src/main/java/dev/ftb/mods/ftbchunks/api/FTBChunksProperties.java#L15-L20).
3. Record which owner will confirm membership. For a later owner-authorized session, `/ftbteams info` is a documented information command: its handler sends team-info lines and invokes the `TeamEvent.INFO` extension event. Its subscribers are untraced, so it is **not proven side-effect-free**; no harmful behavior is demonstrated. This is a source reference, **not permission to execute any command, join or start a world now**. Any later invocation requires separate owner authorization before action, with the untraced INFO event explicitly considered. Treat its output as private; do not publish identities. Do not substitute `/ftbteams info server_id`. [Registration](https://github.com/FTBTeam/FTB-Teams/blob/20bc18fd15c5c71f19be530e86fd0db038e2acd4/common/src/main/java/dev/ftb/mods/ftbteams/data/FTBTeamsCommands.java#L158-L165), [information handler](https://github.com/FTBTeam/FTB-Teams/blob/20bc18fd15c5c71f19be530e86fd0db038e2acd4/common/src/main/java/dev/ftb/mods/ftbteams/data/FTBTeamsCommands.java#L347-L351).
4. Keep ordinary shared containers separate from [personal-loot expectations](personal-loot.md). Permission to interact is not proof that everyone sees the same loot, that a transfer succeeds, or that items persist. FTB's block-interaction policy can return `CHECK`, which explicitly means further checks are needed. It is not an allow/deny matrix for every modded container. [Interaction policy](https://github.com/FTBTeam/FTB-Chunks/blob/a90e58e431879f5213629373ea9cde7001ebef45/common/src/main/java/dev/ftb/mods/ftbchunks/api/Protection.java#L44-L56), [CHECK meaning](https://github.com/FTBTeam/FTB-Chunks/blob/a90e58e431879f5213629373ea9cde7001ebef45/common/src/main/java/dev/ftb/mods/ftbchunks/api/ProtectionPolicy.java#L3-L15).
5. Mark all proposed changes and tests as requiring the owner. A future disposable-container test should distinguish opening, depositing, withdrawing and persistence after reconnect; it must not use valuables or personal-loot containers as a proxy for ordinary storage. This is a safety test design, not a completed test or a claim about current access.

## Expected result

Every requested action has an owner decision or an explicit unknown. You have not changed membership, claims, chunk loading or settings. A completed table is planning progress; shared-base operation remains unverified.

## Common failures

If permission is denied later, stop the attempted operation and ask the owner to compare the exact action and target with the agreed table. Do not unclaim land, disband a team, invite everyone or broaden fake-player policy to make one container work. Preserve current membership while diagnosing. Unknown effective rules cannot be repaired from these source declarations alone.

## Tip and trade-off

Keep build access narrower than container access when the owner wants that distinction. The separate source properties make it a meaningful policy question, but their actual values and downstream checks still require owner verification. This reduces accidental permission expansion at the cost of a longer preflight.

## Next steps

Check [connection responsibilities](connection-preflight.md), [backup recovery gates](backup-recovery-safety.md) and [navigation control attribution](navigation-controls.md) before a separately authorized shared session. Team membership, transport connectivity, claims and personal loot are different questions; success in one does not close the others.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
