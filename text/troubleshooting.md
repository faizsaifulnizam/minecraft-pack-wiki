Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/troubleshooting/
Baseline: dev-0.5-20261015

# Troubleshooting

> Development snapshot: **dev-0.5-20261015**. Minecraft **1.21.1**, NeoForge **21.1.250**. The pack is still changing.

## Recipe search is missing or in the wrong place
The saved EMI search sidebar is right and Center Search Bar is off. Ctrl+O toggles EMI visibility in its context. JEI also has overlapping bindings, so verify what actually responds before changing mods. A missing category or transfer is not proof that the recipe itself is broken.

JEI's optional synthetic tag-recipe browsing is saved off. Normal JEI integrations and EMI recipe import have not been exhaustively tested by this mapping. Do not describe all JEI features as disabled.

## Map and inventory controls overlap
M is saved for both Xaero's map and FTB Chunks' map. C, Z and right bracket also have contextual overlaps among installed features. Check the relevant Controls entries and the screen you are in. The overlap alone does not establish a broken binding.

## Shadows are missing
Iris is saved enabled with MakeUp Ultra Fast 9.5g selected, but the shader override explicitly saves shadow casting off. That explains the saved intent, not a live rendering result. Older notes about keeping shadows do not override the current saved value. No setting has been silently corrected by this handbook.

## An optimiser appears disabled
AE2 Crafting Optimizer has its compiled graph and authoritative planner saved off, while other optimisation domains and execution features remain on. That is not an all-off state. Saved switches do not prove compatibility, active runtime use or a speed gain.

## Claims or force-loading differ from this handbook
FTB global files contain templates and defaults. Existing worlds, teams, permissions or server configuration may override them. This edition does not establish effective quotas, protection rules or operator access. Do not rely on a claim as tested protection of valuables until the server policy is checked.

## Terrain or distant rendering behaves strangely
Distant Horizons is installed. Saved generation mode is FEATURES with SURFACE_THEN_CHUNKS, eight threads and runtime ratio 1.0. Those are observations, not a recommended fix or a hard CPU cap. Rendering distant terrain does not keep distant machines simulated.

Do not transplant a separate trial's configuration or patch into this baseline. A static inspection or menu startup is not proof that generation, boss encounters, reloads or save/reopen work correctly.

## Reporting a problem
Give the pack revision, relevant mod/system, action, expected result and what happened. Redact account data, addresses and world locations before sharing any diagnostic material. This wiki does not collect logs or private saves.

[Sources and evidence](https://faizsaifulnizam.github.io/minecraft-pack-wiki/sources/) explain what is verified and what remains Unknown.
