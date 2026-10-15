---
layout: default
title: "Check connection responsibilities before sharing a world"
permalink: /guides/connection-preflight/
baseline: dev-0.5-20261015-r2
---

# Check connection responsibilities before sharing a world

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
**Development documentation snapshot:** Minecraft 1.21.1 / NeoForge 21.1.250; e4mc 6.1.0. Version-matching upstream source supports a bounded preflight, not a successful connection, authenticated access policy or service-availability guarantee. The upstream build declares 6.1.0 but uses a 1.20.2 compile target; this is source-version correspondence, not proof of installed-binary equivalence on this pack. [Build declaration](https://github.com/vgskye/e4mc-minecraft-architectury/blob/765e93282765d0d23c1f2820e56b7c96e0f1bf71/gradle.properties#L3-L8).

## Prerequisites

Name a host owner and invited players privately. Agree on the same pack revision and a session window. This is an offline planning task: do not open a world, choose Open to LAN, reveal an address or join a server to complete it.

## Steps

1. Write down who runs the world and who merely connects. Upstream's usage instruction is “Open to LAN as normal.” Treat that as the **exposure boundary**, not a harmless way to inspect options. Do not invoke it during this preflight. [Usage](https://github.com/vgskye/e4mc-minecraft-architectury/blob/765e93282765d0d23c1f2820e56b7c96e0f1bf71/README.md#L17-L19).
2. Assign the host responsibility for the running world, saves and recovery approval. The source starts a relay session from the server TCP-listener hook when `hostEnabled` is true and stops its session from the server stop hook. A saved setting or installed mod does not establish that a relay is live. This is not unattended server rental, a promise of uptime or evidence that the external relay is available. [Listener lifecycle](https://github.com/vgskye/e4mc-minecraft-architectury/blob/765e93282765d0d23c1f2820e56b7c96e0f1bf71/common/src/main/java/link/e4mc/mixin/ServerConnectionListenerMixin.java#L37-L56).
3. Assign guests responsibility for matching the agreed gameplay pack. Do not infer from the host-side relay hook either that every guest needs e4mc or that every gameplay mod is optional on guests. Exact guest-side requirements and full-pack join/rejoin remain unverified here. Record that question before distributing a pack; do not install or remove anything based on this page.
4. Ask the owner for an explicit access-control decision before any later exposure. The selected source alters vanilla whitelist-command permission checks to allow the single-player owner, otherwise retaining the original predicate. That establishes a command-authorization hook, **not that a whitelist is enabled, populated or enforced for this session**. Do not issue whitelist or ban commands as an inspection shortcut. [Owner permission hook](https://github.com/vgskye/e4mc-minecraft-architectury/blob/765e93282765d0d23c1f2820e56b7c96e0f1bf71/common/src/main/java/link/e4mc/mixin/WhitelistCommandMixin.java#L15-L26).
5. Agree on private address handling, how the host will announce session closure, and who approves a later reconnect test. Keep addresses, account identities and connection output out of public support requests. Verify [shared-base policy](shared-base-preflight.md) independently: transport access does not grant container or land permissions.

## Expected result

Your session note identifies host, guests, pack revision, access-control approver, private communication channel and closure/reconnect owner. Unresolved guest requirements and live access-control checks remain explicit. No connection has been opened or tested by this task.

## Common failures

If a later authorized session cannot connect, confirm that the owner intended the session to be live and that everyone used the agreed pack revision. Do not publish the address, disable security, forward ports or change team claims as speculative fixes. Escalate the specific failure privately. No stable-address/rejoin guarantee is established; an old address is not evidence of a current session.

## Tip and trade-off

Separate “can connect” from “can use the base” in your session checklist. This avoids widening [FTB permissions](shared-base-preflight.md) to solve a transport failure, at the cost of checking two distinct boundaries. Before any future recovery, use the [stopped-copy checklist](backup-recovery-safety.md); a guest's client installation is not an identified backup of the host's world.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
