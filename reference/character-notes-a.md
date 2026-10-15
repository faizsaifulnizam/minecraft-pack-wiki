---
layout: default
title: "Character notes A"
permalink: /reference/character-notes-a/
baseline: dev-0.5-20261015-r2
---

# Character notes A

> **FULL SPOILERS** — this page reveals skill behavior, evolution wording and reset consequences. [Return to the safe character-helper route](../guides/character-tools.md).

## Baseline
This is an bounded statically reviewed revision for candidate **dev-0.5-20261015-r2**, not an applied replacement for dev-0.5-20261015. New core text corresponds only to Tensura archive SHA-256 `2309a22ceb7e423e2f3212ea87686ccc510fe0003595500037e0b6c64baef213`. The original baseline/pins remain unchanged. Static descriptions and feedback are not runtime or award-handler proof.

foxablazeaqzl_wiki 1.0.2.3, tensura_trepu 1.0.0.2 and Tensura-Leveling 1.0.14. Reference with conditional how-to techniques.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.
New candidate-core text independently establishes skill/mode names, learning feedback, evolution requirement vocabulary, awakening refusal messages and reset warnings. Imported addon numerical descriptions still have no pinned core correspondence; their ranges, probabilities and learning bonuses below remain **addon-shipped documentation**, not verified candidate implementation. No acquisition route for Great Sage or Sage is established. Do not consume rare resources or reset solely from these notes.

## Read entry and race selection without forcing reincarnation
1. If **Reincarnation** is already open, read its candidate-core information box: Difficulty, Aura Range, Magicule Range and Intrinsic Skills. Compare those fields before choosing. These are displayed ranges, not a promised starting roll or power conversion.
2. **Random** explicitly selects from a configurable list. Do not treat all displayed or tagged races as its pool. The live list was not read; a fixed best-race recommendation is unsupported.
3. **Select Race** is the submit label. Do not submit as a harmless preview. First-join access, repeat selection, confirmation and persistence are not encoded by these translation strings.
4. If you cannot reach the screen, stop at [the safe control check](../guides/character-tools.md). No deliberate-death or reset route is authorized by this evidence.

The separate `tensura:reincarnation` magic description says it sacrifices a portion of the caster’s power to reincarnate. It does not state the fraction, target eligibility or that casting it is the normal first-life route. The reincarnated advancement listens for `tensura:reincarnated`; its icon is a Race Reset Scroll, not a recipe or requirement to use one. The retained resource has no emitter implementation. **Do not infer entry from its icon or title.** (REV-03; core `tensura.reincarnation.*`, `tensura.skill.reincarnation.description`; reincarnated.json.)

## Distinguish learning progress from an acquired ability
1. In an available **Ability Selection** view, record **Learn Points**, **Mastery** and **[Mod: …]** for the intended ability. Origin matters when reading addon entries.
2. If feedback says **now available to learn**, that is availability, not acquisition. **You have become closer to acquiring …** likewise indicates progress. Do not claim ownership yet.
3. If feedback says **currently unable to be learnt**, stop the attempted route. If it says **requires mastery over … to be learnt**, record the named prerequisite and inspect that ability’s Mastery; do not substitute an unrelated advancement parent.
4. Treat **has been acquired through learning** and the owned ability list as the acquisition checkpoint; treat **You have mastered the usage of …** and the Mastery display as a separate checkpoint. Actual point thresholds and the action that adds points remain untraced.
5. For an already-owned active skill, select the intended mode using **Next Ability Mode / Previous Ability Mode** and your assigned **Ability 1/2/3 Activation** control. These names do not prove slot placement, mode entitlement or the default keys. Do not test a combat mode against an unknown target.

The candidate core independently names Great Sage / Analysis / Analytical Appraisal / Refining and describes Sage as increasing learning/mastery speed. It does **not** corroborate the addon’s +2/+9, 20/30-block, EP ratio or success-rate figures. Keep those conditional techniques separate from exact implementation proof.

Learning data has real restrictions but is not an award algorithm: `copiable_magic.json` includes aspectual and summoning magic and removes the medium/greater elemental summoning entries. `found_in_tome.json` includes the magic tag and removes the tome-copy-excluded tag. `unlearnt_cast_excluded.json` explicitly includes Reincarnation among exclusions. These declarations do not prove effective tag resolution, tome loot, use requirements or copying success in this pack. (REV-04/05; core language keys above and the four retained tag files.)

## Read evolution eligibility by requirement type
If **Select Evolution** is offered, inspect **Requirements** before **Evolve**. The candidate core supplies distinct templates: **Reach Existence Points of …**, **Be named**, **Acquire …**, **Master …**, **Obtain a Spirit**, **Have a physical body**, **Carrying … of …**, **Consume … of …**, **Battle …**, **Defeat …**, **Kill … bosses**, **Awaken […/…]**, and **Get cured with Weakness and Enchanted Golden Apple**. None maps a specific template/value to every race.

**Carrying is not Consume.** Do not infer spending, refunds or completed eligibility from inventory presence. Record the exact current target, quantity and requirement text; use **Track / TRACKED** only as named vocabulary, since its interaction was not exercised. **Evolution Available**, percentage progress and **No Evolutions** are distinct display states, not proof of a completed transition.

The retained text supports requirement interpretation but contains no complete per-race evaluator, AND/OR rule, effect/consumption ordering or failed-transition rollback. The addon’s Wastelander and Angel strings below remain separate display documentation, not a repaired candidate-core gate. (REV-06; core `tensura.evolution_menu.*`, `tensura.main_menu.evolution_progress.*`.)

## Read awakening refusal and state messages
The core provides **Become Demon Lord** and **Become Chosen Hero** labels; their presence does not prove availability for this character.

| Candidate-core message | What it establishes | Safe next check |
|---|---|---|
| Not a Demon Lord Seed / not enough soul points | Those are distinct refusal messages | Record displayed state and Souls; no numeric threshold supplied here |
| Already a True Demon Lord / You are a True Hero | Distinct state/conflict vocabulary | Do not retry assuming more souls solve every refusal |
| Not a Hero Egg / correct situation requirement not met | Different eligibility failures exist | Record exact message; no boss, timing or situation is inferred |
| Lost Seed due to Naming / lost Egg due to Naming or evolution | Shipped warnings name progress-loss paths | Do not name/evolve as a recovery experiment |
| Awakened into a True Demon Lord / True Hero | Success feedback vocabulary | Inspect actual resulting state, not merely the button |

`demonLordAwaken.description` says a gamerule controls the Soul Points needed for True Demon Lord. It supplies no live value or complete gate. The text also names subordinate evolution thanks to a master’s Harvest Festival; this is a description, not proof every subordinate qualifies. No boss-kill prescription, seed/egg acquisition route or exact awakening handler follows from these strings. (REV-07; `tensura.evolve.demon_lord.*`, `tensura.evolve.hero.*`, `gamerule.demonLordAwaken.description`.)

## Avoid using resets as recovery
Before any reset, stop if feedback says **not allowed to reset at this state** or **not safe to reset here**. The text does not define a safe location, permitted state or a bypass; do not move elsewhere and assume authorization.

The candidate core now independently documents:
- Race Reset: Statistic, Naming status, Awakening status, Spirits, Resistances, Race and its Intrinsic Skills.
- Character Reset: everything from the user. The addon separately mentions achievements; that narrower assertion is still addon description, not an independently traced core effect.
- Skill Reset: every skill of every type except race Intrinsic Skills. Its warning says the scroll will not cover Unique Skill MP cost and may leave you with **no Unique Skills**.
- Incomplete Reset Counter requirements can lose the displayed number of reset points when `resetIncompletePenalty` is enabled. No live rule value was inspected.

Counter-check messages name Awakening Status, Final Race Evolution and defeated-boss checks; they do not encode which boss or evaluator. Skill-lock messages and configurable bonuses do not establish a guaranteed preservation procedure. No five-second cooldown is a rollback window. Safe recovery here means **stop further destructive actions and record the exact feedback**, not restoration of lost state. (REV-08; `tooltip.tensura.reset_scroll.*`, counter-check strings and reset gamerule descriptions.)

## Advancement criteria are not ability-award recipes
The retained objects establish exact serialized event subscriptions:

| Resource | Criterion | Declared reward |
|---|---|---|
| reincarnated | `tensura:reincarnated` | No rewards field |
| higher_form | `tensura:awaken_race` | 30 experience |
| fast_learner | one group containing battlewill/magic/skill learnt | No rewards field |
| master_skill | one group containing battlewill/magic/skill mastered | No rewards field |
| master_unique_skill | `tensura:unique_skill_mastered` | 20 experience |

The single inner group in fast_learner/master_skill is the serialized alternative criterion group, not three mandatory achievements. Custom trigger IDs still need their emitter/conditions traced. `higher_form`’s parent `s_rank` does not prove S rank is an awakening gate. Experience fields are actual declarations, not proof rewards executed or extra skills granted. (REV-09; exact retained advancement JSON.)

## Prerequisites
For the techniques below, you must already own the relevant skill, know your actual skill control, and have the applicable mode available. This chapter supplies no skill-award command or reincarnation recipe.

## Steps
### Inspect with Great Sage before trying to copy
1. Select **Analytical Appraisal** and aim at the intended entity. The bundled entry says the base distance is **20 blocks**, or **30 with Mastery**.
2. If you see only Name, HP, SHP and Armor, do not assume the reference is broken. It describes that restricted display when the target exceeds **five times your EP**, or **ten times with Mastery**. Those thresholds remain documentation-only, not a measured effective rule.
3. If you already have **Analysis**, use it only with a target in line of sight and within its documented **20-block** reach. The entry excludes Unique Skills and Resistances, spirit-related magic, and Ultimate Skill users; it is not a method to obtain every ability.
4. A failed copy is not proof of a broken skill: the entry describes **25% success**, **50% with Mastery**, a **10-second** cooldown on success and **5 seconds** after failure. Wait for the actual UI to allow another action; do not spam a control based only on a stopwatch.
5. Check your owned skill/magic list for a new entry before calling the attempt successful. Displaying a reference description is not the acquisition checkpoint.

### Compare a learning toggle with ownership
The bundled **Sage** entry says its passive toggle increases points gained by two, for three total. **Great Sage / Parallel Processing** says plus nine, ten total, for skill/magic/Battlewill/Arts learning and mastery. These are descriptions of already-owned toggles, not evidence of how to award either skill or a promise that both bonuses stack. A conditional tip: read whether your owned learning passive is toggled before diagnosing slow mastery. Prerequisite: ownership and accessible toggle; benefit: catches a disabled documented passive; trade-off: no verified combined multiplier or resource cost is supplied here.

## Evolution reference, not complete gates
The evolution UI's selected translation says **Consume Heaven Cleansing Elixir**, **Win the Dream Realm challenge after sleeping at night**, and **Use Break and Rebuild Manual** for Wastelander-to-Human wording. Another label says **Possess an Okami** for Angel-to-Tengu. These four strings do not establish whether the first three are alternatives or cumulative requirements, how to acquire the named items, or how the base mod authorizes a transition. Do not turn them into an AND checklist.

The built-in item reference separately says **ten Daemon Essence** are used for Enlightened Ogre/Kijin-to-Wicked Oni evolution, and **ten Royal Blood** for High Orc-to-Orc Lord evolution. It also describes feeding Royal Blood to a Royal Orc. These are addon-shipped descriptions with unresolved core-version correspondence. No exact consumption handler, naming cost, resource refund or failed-evolution recovery was read.

## Reset and reincarnation risks
The bundled **Race Reset Scroll** entry says it resets Stats, Name, Awakening Status, Spirits, Resistances, Race and race Intrinsic Skills, with a five-second cooldown. The **Character Reset Scroll** entry describes resetting everything, including obtained achievements, and calls it like reincarnating from scratch. Its crafting text is incomplete, so no recipe is supplied here.

Neither entry proves a reversible retry. Do not use either scroll as a fix for an unavailable menu. The five-second cooldown is not a recovery window, and a reset description does not establish the normal first-life reincarnation route.

## Integration skill classification
The exact bridge tags append **tensuraleveling:system** to the **unique_skills** and **no_plundering** tags, with replace=false. Its English description calls System a passive mark of recognition for someone bound to the System. These are real declarations, not evidence of the binding/recognition award condition. Do not infer that killing, plundering, reaching a particular level, or awakening in one system grants it.

## Expected result
You can read the bundled restrictions and avoid treating a UI label, reset cooldown or tag as a completed unlock route. The conditional skill technique provides observable checkpoints, but requires independent gameplay validation.

## Common failures
- Appraisal shows limited information: compare the documentation's EP restriction before diagnosing a UI failure; actual transformed behavior remains untested.
- Analysis does not grant the desired skill: check the documented exclusions and eligibility, and do not confuse a random-copy chance with a guaranteed targeted award.
- An evolution option remains unavailable after gathering an item: only selected display text was captured. Do not invent an absent extra gate or assume that resource consumption succeeded.
- A reset lost progress: no restore procedure was established. Stop before further resets and report the action; this documentation cannot promise recovery.

## Sources
foxablazeaqzl_wiki-1.0.2.3.jar: assets/foxablazeaqzl_wiki/wiki/skill_descriptions.json, entries great_sage and sage; item_descriptions.json, entries daemon_essence, royal_blood, race_reset_scroll and character_reset_scroll. tensura_trepu-1.0.0.2.jar: assets/tensura_trepu/lang/en_us.json, four requirement strings. tensuraleveling-1.0.14.jar: data/tensura/tags/manascore_skill/skills/unique_skills.json, no_plundering.json and assets/tensuraleveling/lang/en_us.json. Claims CHAR-016 through CHAR-020.


Candidate-core additions: assets/tensura/lang/en_us.json and the exact selected advancement/tag objects cited in the revision sections. Archive/internal-entry citations below identify the documented source without exposing retained-evidence storage. No trigger emitter or runtime path was read.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [CHAR-016] `foxablazeaqzl_wiki-1.0.2.3.jar!assets/foxablazeaqzl_wiki/wiki/skill_descriptions.json`: `entries[id=great_sage].description.en_us`.
- [CHAR-017] `foxablazeaqzl_wiki-1.0.2.3.jar!assets/foxablazeaqzl_wiki/wiki/skill_descriptions.json`: `entries[id=sage].description.en_us; entries[id=great_sage].description.en_us`.
- [CHAR-018] `tensura_trepu-1.0.0.2.jar!assets/tensura_trepu/lang/en_us.json`: `gui.tensura_trepu.evolution_requirements.wastelander_to_human.*; gui.tensura_trepu.evolution_requirements.angel_to_tengu`.
- [CHAR-019] `foxablazeaqzl_wiki-1.0.2.3.jar!assets/foxablazeaqzl_wiki/wiki/item_descriptions.json`: `entries[id=daemon_essence,royal_blood,race_reset_scroll,character_reset_scroll].description.en_us`.
- [CHAR-020] `tensuraleveling-1.0.14.jar!data/tensura/tags/manascore_skill/skills/unique_skills.json`: `$`.
- [CHAR-020] `tensuraleveling-1.0.14.jar!data/tensura/tags/manascore_skill/skills/no_plundering.json`: `$`.
- [CHAR-020] `tensuraleveling-1.0.14.jar!assets/tensuraleveling/lang/en_us.json`: `tensuraleveling.skill.system.description`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!assets/tensura/lang/en_us.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/reincarnated.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/higher_form.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/fast_learner.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/master_skill.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/master_unique_skill.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/tags/manascore_skill/skills/copiable_magic.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/tags/manascore_skill/skills/found_in_tome.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/tags/manascore_skill/skills/tome_copy_excluded.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/tags/manascore_skill/skills/unlearnt_cast_excluded.json`.
