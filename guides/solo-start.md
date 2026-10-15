---
layout: default
title: "Inspect your SoloCraft character and quests"
permalink: /guides/solo-start/
baseline: dev-0.5-20261015-r2
---

# Inspect your SoloCraft character and quests

## Baseline
This is an bounded statically reviewed revision for candidate **dev-0.5-20261015-r2**, not an applied replacement for dev-0.5-20261015. New core text corresponds only to Tensura archive SHA-256 `2309a22ceb7e423e2f3212ea87686ccc510fe0003595500037e0b6c64baef213`. The original baseline/pins remain unchanged. Static descriptions and feedback are not runtime or award-handler proof.

SoloCraft: Reawakening 1.3.3 in dev-0.5-20261015. This is an independent SoloCraft entry route. A cross-system awakening requirement has not been established; no absence-of-gates claim is made.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.
Documented-static UI vocabulary, not runtime-tested screen navigation. The exact language file contains old panel labels and a reworked panel's labels together; presence does not prove that every control is visible in your active panel. Initial hunter-awakening eligibility, rank selection and first-join behavior have not been traced. In particular, the Hunter Rank Evaluator label is not proof of how to obtain or use it.

## Prerequisites
An existing character, a safe location, and access to Controls. If you have not received access to SoloCraft's panel, this guide can identify the control but cannot supply the missing award route.

## Steps
1. In Controls, find the category **Solo Leveling Keybinds** and the action **Open Panel**. Use your actual assigned key; this manuscript deliberately does not assert a physical default or overwrite a binding.
2. Use Open Panel in the game context. If no panel appears, stop at the control/access check in Common failures; do not enter a gate to force access.
3. If a panel is available, identify the displayed character values before changing anything. The selected language file names Level, Health, Mana, Fatigue, Strength, Vitality, Intelligence, Agility, Sense, Defense and Skill Points. Not all values necessarily appear in the reworked panel. Record only what you actually see.
4. If **Quests** is present, open it and inspect **Goals** and the current progress. The reworked panel's quest tooltip is Quests; older resources call the view Active Quests or Daily Quests. Use the actual label, not a screenshot from another release.
5. Complete only the goals your live quest displays. This source capture does not establish running distances, required kills, timer length or reward eligibility. Reopen the quest view and use its progress as your checkpoint; **QUEST REMAINS INCOMPLETE** is an explicit shipped status label, not a command to claim a reward anyway.
6. If **Collectible Rewards** is present, inspect the reward view after the quest reports completion. Do not assume an old reward-label quantity is your actual payout. The server can control quest rules, and no reward handler was disassembled in this lane.

## Expected result
You have identified the panel control and, where access exists, read your current state and quest goal. Successful opening and payout remain gameplay checks; this guide does not certify them from translations.

## Common failures
- Open Panel does nothing: check the named action's current binding and whether the game rather than another screen has focus. A key name exists, but the panel's entitlement condition is still unknown. Do not use a reset or administrator award as ordinary recovery.
- No daily quest: the shipped description for soloDailyQuest says the rule enables/disables system daily quests. Its live value was not read. Ask the host whether quests are enabled rather than changing a rule yourself.
- Conflicting penalty text: a language entry calls one quest optional while soloPunishment describes penalties for incomplete daily quests. Translation wording alone cannot decide active behavior. Treat the live timer and host's rules as unresolved until checked; no penalty-safe guarantee is given here.
- A job quest does not appear at a level from another guide: the selected rule description allows Job Change Quest Level 20–100, default 40. That is documentation of a configurable value, not the effective server threshold or a complete job-change unlock procedure.

## Sources
SLR1.3.3.jar, assets/sololeveling/lang/en_us.json: key.sololeveling.open_panel, key.categories.sololeveling, panel_early label keys, panel_rework_2 quest/reward keys, daily_quests status keys, soloDailyQuest, soloPunishment and soloLevelingJobChangeLevel descriptions. The awakening resource data/sololeveling/advancement/awakened.json uses minecraft:impossible, so the award handler must be traced separately. Claims CHAR-003 through CHAR-007.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [CHAR-003] `SLR1.3.3.jar!data/sololeveling/advancement/awakened.json`: `criteria.awakened.trigger`.
- [CHAR-004] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `key.sololeveling.open_panel; key.categories.sololeveling; gui.sololeveling.panel_early.label_*`.
- [CHAR-005] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `gui.sololeveling.panel_rework_2.tooltip_daily_quest; gui.sololeveling.daily_quests.label_goals; gui.sololeveling.daily_quests.label_quest_remains_incomplete; gui.sololeveling.panel_rework_2.tooltip_collectible_rewards`.
- [CHAR-006] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `gamerule.soloDailyQuest.description; gamerule.soloPunishment.description; gui.sololeveling.daily_quests.label_penalties_will_be_given`.
- [CHAR-007] `SLR1.3.3.jar!assets/sololeveling/lang/en_us.json`: `gamerule.soloLevelingJobChangeLevel.description`.
