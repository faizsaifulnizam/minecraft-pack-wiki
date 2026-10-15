<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/comfort-settings-choice/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Prepare a comfort and graphics choice

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
> Development documentation snapshot: **dev-0.5-20261015-r2**. Minecraft **1.21.1**, NeoForge **21.1.250**. Static records are not effective settings or runtime acceptance.

Choose what to discuss or change later without replacing the saved look. This is a paper/settings-choice task, not a tuning recipe. You need the pack revision and your own description of discomfort; no game session, config edit or diagnostic upload is required.

## Prerequisites
Use only the revision label and already-known observations described above. This task does not require opening the game or private files.

## Steps
1. Describe one symptom in plain language: camera jolts, movement softness, glare, text size, or black rendering. Note whether it is owner-observed or only a question. Stop playing if you feel unwell; a diagnostic is not worth worsening symptoms.
2. Use the saved observations below as a comparison, not instructions to copy. Write “unknown” for your effective value unless you already know it. Do not open personal configuration files to fill this worksheet.
3. Write the desired outcome and the features to preserve: **Distant Horizons, shaders plus meaningful frame generation, and motion comfort**. A suggestion to disable generation globally or while moving is a diagnostic trade-off, not completion of that objective. No such switch is requested here.
4. Pick one question for the pack owner: for example, “Can text be made easier to read without changing the shader preset?” Record the present state, proposed scope, approval needed and how the original choice would be restored. Do not apply a new preset or activate an optional addon.
5. Check the record: it names one symptom, distinguishes saved from observed state, preserves the objectives, and requests no automatic rewrite. If it cannot, narrow the question using the [support checklist](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/support-escalation/).

## Compare with saved observations
The [snapshot evidence definitions](https://faizsaifulnizam.github.io/minecraft-pack-wiki/sources/) distinguish selected saved keys from runtime behavior. These are historical saved observations, not universal accessibility defaults:

| Area | Recorded value | What not to infer |
|---|---|---|
| Camera | `bobView=false`, `autoJump=false`, `damageTiltStrength=0.0`, `fovEffectScale=0.0`, `screenEffectScale=0.0` | Not a promise that every mod camera effect is suppressed. |
| Other effects | `darknessEffectScale=1.0` | Screen-effect reduction does not establish darkness reduction. |
| Readability/audio | `guiScale=2`, `gamma=1.0`, `soundCategory_master=0.25` | Not a prescribed size, brightness or safe listening level for every person. |
| Steady Sight | `strength=OFF`, `smoothStepCamera=true`, `optimizeVanillaSettings=false`, `optimizeOtherMods=false` | OFF is the saved strength key, not proof that the entire mod is inactive. Keep the vignette off; do not enable automatic optimizers to inspect them. |
| Iris | `enableShaders=true`, `shaderPack=MakeUp-UltraFast-9.5g.zip` | Selected is not proof that the shader rendered in a session. |
| MakeUp override | `AA_TYPE=0`, `BLOOM=false`, `SHADOW_CASTING=false` | Do not silently restore shadows from older preferences or guess numeric enum meanings. |

The installed identities are Steady Sight 0.3.0, Iris 1.8.12 and FrameGen 1.3; identity does not prove their combined rendering or generation state. Exact identity citations: `steady_sight-0.3.0+neoforge-1.21.1.jar!META-INF/neoforge.mods.toml`; `iris-neoforge-1.8.12+mc1.21.1.jar!META-INF/neoforge.mods.toml`; `framegen-1.3-neoforge-1.21.1.jar!META-INF/neoforge.mods.toml`. Metadata supports identity only, not the saved-key table.

## Common failures
If advice conflicts with these observations, keep both labelled: historical saved state and proposed choice. Ask the owner to resolve the conflict; do not overwrite either. If the exact menu label or reset behavior is unknown, stop before changing it. Black rendering is a support symptom, not proof of a particular mod's fault.

**Tip:** a written one-variable proposal is easier to approve and undo than “optimize everything.” Its benefit here is clarity, not a claimed FPS gain. This task ends with a usable choice record; it does not establish relief, performance or live uptake. Continue with [graphics and documentation roles](https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/graphics-and-books/).

## Historical saved-file/key citations
These game-directory-relative pointers identify only the historical selected observations above, not live files, effective values or instructions to open configuration. No whole configuration or private provenance is published.

- `minecraft/options.txt#bobView` — `bobView=false` (historical saved; runtime unverified).
- `minecraft/options.txt#autoJump` — `autoJump=false` (historical saved; runtime unverified).
- `minecraft/options.txt#damageTiltStrength` — `damageTiltStrength=0.0` (historical saved; runtime unverified).
- `minecraft/options.txt#fovEffectScale` — `fovEffectScale=0.0` (historical saved; runtime unverified).
- `minecraft/options.txt#screenEffectScale` — `screenEffectScale=0.0` (historical saved; runtime unverified).
- `minecraft/options.txt#darknessEffectScale` — `darknessEffectScale=1.0` (historical saved; runtime unverified).
- `minecraft/options.txt#guiScale` — `guiScale=2` (historical saved; runtime unverified).
- `minecraft/options.txt#gamma` — `gamma=1.0` (historical saved; runtime unverified).
- `minecraft/options.txt#soundCategory_master` — `soundCategory_master=0.25` (historical saved; runtime unverified).
- `minecraft/config/iris.properties#enableShaders` — `enableShaders=true` (historical saved; runtime unverified).
- `minecraft/config/iris.properties#shaderPack` — `shaderPack=MakeUp-UltraFast-9.5g.zip` (historical saved; runtime unverified).
- `minecraft/shaderpacks/MakeUp-UltraFast-9.5g.zip.txt#AA_TYPE` — `AA_TYPE=0` (historical saved; runtime unverified).
- `minecraft/shaderpacks/MakeUp-UltraFast-9.5g.zip.txt#BLOOM` — `BLOOM=false` (historical saved; runtime unverified).
- `minecraft/shaderpacks/MakeUp-UltraFast-9.5g.zip.txt#SHADOW_CASTING` — `SHADOW_CASTING=false` (historical saved; runtime unverified).
- `minecraft/config/steady_sight-client.toml#strength` — `strength=OFF` (historical saved; runtime unverified).
- `minecraft/config/steady_sight-client.toml#smoothStepCamera` — `smoothStepCamera=true` (historical saved; runtime unverified).
- `minecraft/config/steady_sight-client.toml#optimizeVanillaSettings` — `optimizeVanillaSettings=false` (historical saved; runtime unverified).
- `minecraft/config/steady_sight-client.toml#optimizeOtherMods` — `optimizeOtherMods=false` (historical saved; runtime unverified).

## Expected result
A labelled choice record or redacted support draft as described above, not a settings change, diagnosis or runtime result.

## Sources
The inline exact-source citations and explicitly historical observations above support only their stated boundaries; safety recommendations are not observed gameplay.
