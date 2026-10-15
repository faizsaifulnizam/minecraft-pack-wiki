<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/backup-recovery-safety/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Prepare a stopped-copy backup recovery checklist

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
**Development documentation snapshot:** Minecraft 1.21.1 / NeoForge 21.1.250; SimpleBackups 1.21-4.0.21. The [selected release metadata](https://api.modrinth.com/v2/version/6JQL4qSR) links the [source commit](https://github.com/ChaoticTrials/SimpleBackups/commit/b3cc8b033f042471592031c6d69297e55e36ba67) used below. This is release-linked upstream evidence, not a fresh binary audit, effective configuration check or successful restore.

## Prerequisites

The world owner must identify the world, backup custodian and recovery objective privately. This task prepares a checklist only. Do not create, inspect, extract, restore or delete a backup; do not open worlds or modify settings while following it. The later stopped-copy work requires separate owner authorization and verified backup inputs.

## Understand what must be verified

- **Mode:** `FULL_BACKUPS`, `MODIFIED_SINCE_LAST` and `MODIFIED_SINCE_FULL` are distinct modes. The default declaration is full backups; that is not the effective setting. A partial archive is not a complete world. [Mode declarations](https://github.com/ChaoticTrials/SimpleBackups/blob/b3cc8b033f042471592031c6d69297e55e36ba67/src/main/java/de/melanx/simplebackups/config/CommonConfig.java#L46-L53).
- **Location and retention:** output path, per-world subdirectories, count and storage-size limits are configurable. Old files can be deleted by retention logic. Do not assume the default folder or an old timestamp proves a usable recovery point still exists. [Configuration](https://github.com/ChaoticTrials/SimpleBackups/blob/b3cc8b033f042471592031c6d69297e55e36ba67/src/main/java/de/melanx/simplebackups/config/CommonConfig.java#L54-L75), [retention implementation](https://github.com/ChaoticTrials/SimpleBackups/blob/b3cc8b033f042471592031c6d69297e55e36ba67/src/main/java/de/melanx/simplebackups/BackupThread.java#L117-L153).
- **Scope:** the implementation walks the selected world tree, skips `session.lock` and `biomancy.spatial.db`, and applies configured exclusions. It does not establish that launcher settings, the whole pack or every external mod database is backed up. [Backup traversal](https://github.com/ChaoticTrials/SimpleBackups/blob/b3cc8b033f042471592031c6d69297e55e36ba67/src/main/java/de/melanx/simplebackups/BackupThread.java#L219-L280).
- **Completion:** a ZIP filename or a started notification alone is insufficient. The source's finished notification occurs after backup creation and retention-size processing; completion still does not prove restore integrity. [Run lifecycle](https://github.com/ChaoticTrials/SimpleBackups/blob/b3cc8b033f042471592031c6d69297e55e36ba67/src/main/java/de/melanx/simplebackups/BackupThread.java#L156-L171).

## Steps

The following are **owner gates for a later authorized recovery**, not actions performed by this documentation task or a verified SimpleBackups restore command.

1. **Authorization gate:** record who owns the world, which recovery point they approve and where the separate disposable destination will be. Require explicit approval for access to private backup/world contents. Do not request public uploads.
2. **Stopped-state gate:** require the owner to save and stop the host/server normally and confirm it remains stopped before copy/restore work. If it cannot be confirmed, defer recovery. Do not overwrite an active world.
3. **Rollback gate:** require a separate preserved copy of the current stopped world and the original backup set before attempting recovery. Record identities privately. Preserve originals unchanged; a rolling backup folder subject to retention is not the only copy to rely on.
4. **Backup verification gate:** require the custodian to verify integrity, intended world, timestamp, actual backup mode and exclusions. For partial backups, require the necessary full base and dependent partial set plus a supported reconstruction procedure. That exact reconstruction procedure is **not established here**; do not extract only the newest partial ZIP and call it restored. A missing dependency blocks the attempt.
5. **Disposable-copy gate:** require the approved procedure to target a new, separate stopped-copy location only. Verify archive root layout and the compatible pack revision before later use. Do not merge into or replace the live world. Exact extraction/reconstruction commands are deliberately not supplied without the verified inputs and owner-approved procedure.
6. **Acceptance gate:** before any production switch, require separately authorized copy-only load, inventory/container checks, relevant dimensions, normal save/stop and save/reopen checks. Record the owner's acceptance and rollback destination. Neither authoring this checklist nor seeing a finished notification passes those checks.

## Expected result

The owner can say which gates are satisfied, who verifies each remaining gate and why recovery is blocked if any prerequisite is missing. The deliverable is a recovery decision checklist, **not a restored world**.

## Common failures

If integrity, backup mode, dependencies or target identity cannot be verified, keep both original world and backup set unchanged. Stop at the failed gate rather than trying alternate archive orders against the live world. Escalate to the custodian privately; do not “fix” a missing backup by deleting old files or changing retention.

## Tip and trade-off

Prefer a verified complete recovery set preserved outside the rolling retention destination before any later experiment. The cost is additional storage; the benefit is avoiding dependence on files the documented retention logic may remove. This is a safety recommendation, not a claim that any copy currently exists.

For a shared world, identify the [actual host owner](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/connection-preflight/) first and keep [base permissions](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/shared-base-preflight/) separate from backup custody.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
