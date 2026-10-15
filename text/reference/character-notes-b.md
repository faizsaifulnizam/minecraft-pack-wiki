<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/full/character-notes-b/
Baseline: dev-0.5-20261015-r2
Spoiler: full
WARNING: FULL SPOILERS. This text may reveal progression and outcomes.

# Character notes B

> **FULL SPOILERS** — subordinate commands and addon skill interactions follow. [Return to the safe character-helper route](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/character-tools/).

## Baseline
This is an bounded statically reviewed revision for candidate **dev-0.5-20261015-r2**, not an applied replacement for dev-0.5-20261015. New core text corresponds only to Tensura archive SHA-256 `2309a22ceb7e423e2f3212ea87686ccc510fe0003595500037e0b6c64baef213`. The original baseline/pins remain unchanged. Static descriptions and feedback are not runtime or award-handler proof.

foxablazeaqzl_wiki 1.0.2.3 and Tensura: Better Subordinates 1.2.4. Conditional how-to for an existing subordinate, not a recruitment or naming tutorial.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.
New exact candidate-core translations independently establish Thought Communication and its Movement Behaviour/Targeting Behaviour mode names, naming refusal messages, and reached-subordinate command feedback. The bundled wiki’s numeric ranges/cycle descriptions still lack pinned core correspondence. Acquisition, naming cost, eligibility and server ownership checks were not traced; no command was tested.

## Inspect selection and naming failure before spending
1. If a naming interface is already open, read its displayed target context without submitting a name or activating **Naming**. Until invocation is traced, do not invoke Naming as an inspection or recovery test. The core names **Name**, **Subdue the target**, **Endow the target** and **Evolve the target** as different labels, not a mandatory sequence.
2. If feedback says **already named**, **cannot be named**, **faithful with its current owner**, **not sane enough**, **does not want to submit**, **cannot name your master** or **Not enough EP**, preserve that exact reason. Do not replace an ownership refusal with an EP-farming recommendation.
3. A naming success message identifies the bestowed name/namer. It does not establish the cost, a refund, future obedience or universal tameability. Naming can also affect awakening states; consult [Character notes A — FULL SPOILERS](https://faizsaifulnizam.github.io/minecraft-pack-wiki/full/character-notes-a/) before committing.
4. If Thought Communication feedback says **look at a subordinate or a pet**, check the intended target rather than repeatedly issuing group actions. **Can not find any subordinate reachable from your place** identifies a reachability failure, not a numeric radius proof.
5. Follow / Stay / Wander feedback is different from Neutral / Passive / Aggressive / Protect. The core also names Rampage and Meat Shield. Do not interpret an addon’s selected subordinate or **successfully used** skill message as proof a movement mode or combat policy changed.

The core corroborates base mode names, not the imported wiki’s 30-block reach, 50-block wander boundary, crouch scope or mode cycle order. Better Subordinates adds Status Menu / Select Subordinate / Use Skill labels; neither retained language file defines the combined mode order, ownership predicate or cost/refund. Inspect one already-owned target, avoid group activation, and stop on explicit failure. This reduces the scope of a test but is not a proven undo. (REV-10; `tensura.naming.*`, `tensura.telepathy.*`, base mode keys; unchanged Better Subordinates translation witness.)

## Keep taming evidence separate from recruitment instructions
`monster_tamer.json` requires `minecraft:tame_animal` with entity type matching `#tensura:monster`; this is an actual criterion predicate, not a list of bait or a naming prerequisite. `name_a_mob.json` listens for custom `tensura:name`; its monster_tamer parent is not proof naming requires that advancement.

`ruler_of_monster.json` has five separate requirement groups: tame-event predicates for direwolf, goblin, lizardman, orc and slime. All five groups are represented, unlike the single alternative learning group in notes A. It declares loot table `tensura:advancement_reward/ruler_of_monster`, but this revision does not resolve its contents or claim a particular item payout. No player taming method or ability award follows from those criteria. (REV-11; three exact retained advancement objects.)

## Prerequisites
An already-owned subordinate and already-owned **Thought Communication**, an available skill mode, a safe area and your actual assigned activation control. If you have none of these, do not interpret the following as a start-from-zero recruitment route.

## Steps
### Command one subordinate before issuing a group order
1. Select **Movement Behaviour**, stand within the entry's documented **30-block** reach and aim at the owned subordinate, not a non-ally.
2. Activate without crouching. The bundled entry says this cycles **stay / follow / wander** on the selected subordinate. Check its observable behavior after one activation before using the control again.
3. If it wanders, the entry describes movement within **50 blocks of the position where Wander was set**. Do not assume that it will follow you indefinitely while in that mode. Cycle back toward the intended movement mode and verify what the subordinate actually does.
4. Do not crouch for this first single-target check. The bundled description says shifted activation changes all subordinates in a **30×30×30** range; its use of the word radius is geometrically ambiguous, so this is not a measured spherical targeting guarantee.
5. Avoid aiming at a non-ally as a harmless movement test: the same documented mode orders nearby subordinates to attack that target. A command-side effect is not safely reversible merely because you can switch movement afterward.

### Understand targeting separately from movement
The bundled **Targeting Behavior** mode requires Mastery and cycles neutral / passive / aggressive / protect. The entry describes neutral as defensive, passive as targeting nothing even when hit, aggressive as targeting non-allies, and protect as targeting threats to the owner or ally. Read this as a separate combat policy, not a stay/follow toggle. A conditional tip: for a single-subordinate check, avoid shifted group activation; prerequisite is the mastered mode and one known-owned subordinate, benefit is a smaller unintended-command scope, trade-off is that each subordinate must be checked individually.

### Read the Better Subordinates extension
1. If your humanoid subordinate menu shows **Open Skills**, inspect its skill view. The addon also names Thought Communication modes **Status Menu**, **Select Subordinate** and **Use Skill**; screen location and mode order were not disassembled.
2. Before requesting a skill, verify that the selected subordinate is the intended one. The addon has an explicit **%s selected** message, not proof that any nearby creature can be commanded.
3. Inspect **Magicule Cost** if shown, then use the exact success/failure feedback to tell a request from a successful action. The addon translates separate messages for **failed to use** and **successfully used**. No cost formula or spend/refund condition is established here.
4. If **Skill Granting** is offered, do not assume every owned skill is transferable. Metadata says the addon expands obtainable subordinate skills, while the selected translations name acquisition sources **learning** and **Food Chain**. Eligibility and grant prerequisites remain unknown.

## Expected result
You distinguish single-target movement, group commands, targeting policy, and an addon skill request. A displayed cost or request button is not evidence that the subordinate acquired or executed a skill.

## Common failures
- Targeting mode is unavailable: the bundled reference specifies Mastery; the selected code's eligibility and mastery-award route remain unverified.
- A different creature acts: stop repeated activation and verify the target and crouch state before another command. No guaranteed mass-order undo was established.
- A requested skill fails: preserve the selected subordinate, skill name and explicit failure feedback. Do not interpret failure as a grant or repeatedly spend resources.
- The base movement description differs from the addon screen: Better Subordinates modifies the interaction surface. Do not silently merge both mode sets into a single sequence without an exact handler trace.

## Sources
foxablazeaqzl_wiki-1.0.2.3.jar, assets/foxablazeaqzl_wiki/wiki/skill_descriptions.json, thought_communication. tensura_better_subs-neoforge-1.2.4.jar, META-INF/neoforge.mods.toml and assets/tensura_better_subs/lang/en_us.json, all selected menu/cost/acquisition/result keys. Claims CHAR-021 and CHAR-022.


Candidate-core additions: assets/tensura/lang/en_us.json and the exact selected advancement/tag objects cited in the revision sections. Archive/internal-entry citations below identify the documented source without exposing retained-evidence storage. No trigger emitter or runtime path was read.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [CHAR-021] `foxablazeaqzl_wiki-1.0.2.3.jar!assets/foxablazeaqzl_wiki/wiki/skill_descriptions.json`: `entries[id=thought_communication].description.en_us`.
- [CHAR-022] `tensura_better_subs-neoforge-1.2.4.jar!META-INF/neoforge.mods.toml`: `mods[0].description`.
- [CHAR-022] `tensura_better_subs-neoforge-1.2.4.jar!assets/tensura_better_subs/lang/en_us.json`: `$`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!assets/tensura/lang/en_us.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/monster_tamer.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/name_a_mob.json`.
- [Candidate core documentation] `tensura-neoforge-2.0.1.3.jar!data/tensura/advancement/ruler_of_monster.json`.
