<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-comforts-rest/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Rest with Comforts without replacing home respawn

## Baseline
Candidate r2 is unapplied. This page uses Comforts **9.0.5+1.21.1** recipes, shipped descriptions and placement errors. It does not change your personal spawn or instruct you to use a vanilla bed to reset it.

## Evidence status
The exact-release metadata says: “Adds sleeping bags and hammocks for, respectively, portability and turning day to night, without setting new spawns.”[1] This is shipped documentation, not a runtime respawn test. The current author README describes sleeping bags as bed-like and hammocks as inverse beds; it is supplemental, not a 9.0.5 pin.[6] Use this distinction: **sleeping bag = portable bed-like night rest; hammock = documented day-to-night rest; neither sets a new personal spawn**.[1][6] Sleeping-time rules are configurable: the exact release exposes `sleepingBagUse` and `hammockUse` descriptions and multiple hammock time-denial messages.[2] No active config or default enum value was read, so “only daytime in every pack” and guaranteed night skipping are not certified facts here.

## Prerequisites
- For one white Sleeping Bag: **3 white wool**, arranged vertically.[3]
- For one white Hammock Cloth: **1 white wool, 2 wooden-rod-tag inputs, 2 string-tag inputs**.[4]
- For the pair of Rope and Nail used to hang it: **4 string-tag inputs and 1 iron-ingot-tag input → 2 Rope and Nail**.[5]
- A sheltered rest spot and two suitable facing supports for the hammock. Geometry below comes from the author's unversioned wiki, not local placement code.[7] No personal coordinates, world data or existing spawn are inspected.

## Steps
1. Decide the purpose before spending materials. Take a sleeping bag for portable bed-like rest; choose a hammock only when deliberately moving the documented **day toward night**, which may expose you to nighttime hazards.[1][6] Neither item is a method to set or relocate home respawn.
2. Craft a white sleeping bag with rows `empty, white wool, empty` repeated three times (` #  /  #  /  # `). The shipped output is one bag and its recipe has the `comforts:sleeping_bag_enabled` condition.[3] This selected-release recipe is vertical; do not replace it with an unversioned “straight line” interpretation.
3. At a suitable rest time/location, follow the bag tooltip if it is shown: **Automatically attempts to sleep; to place, use while crouching**.[2] This is the shipped auto-use tooltip, not proof that auto-use is currently enabled. If an ordinary interaction does not match that behavior, use the current game's displayed item interaction rather than changing configs. Check whether rest begins or a denial message appears.
4. For a hammock, craft its cloth with rows `empty, wooden rod, empty`; `string, white wool, string`; `empty, wooden rod, empty` (` X  / S#S /  X `).[4] **Only two string inputs are in the shipped 9.0.5 recipe.** Use the selected 9.0.5 recipe for quantities rather than unversioned recipe advice.[4]
5. Craft the hanging pair with rows `string, string, empty`; `string, iron ingot, empty`; `empty, empty, string` (`AA  / AX  /   A`). This yields the needed two Rope and Nail, subject to `comforts:hammock_enabled`.[5]
6. Following supplemental author instructions, use two supports described as “exactly four spaces apart”, place the Rope and Nail facing each other, then use the cloth on either attachment.[7] Do not infer a precise coordinate span from that wording: inspect placement feedback before building a permanent structure. The selected release specifically reports a missing pair, missing other-end rope or insufficient space.[2]
7. Interact to rest at the supported time. The release includes both “You can only sleep during the day” and an alternate “during the day, at night, or during thunderstorms” message.[2] Which branch applies depends on unresolved effective settings; obey the actual feedback. Expect the documented hammock outcome to be **day to night**, not night to morning.[1] Exact wake tick/time is not established.
8. Return to [your cooking batch](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/homestead-cooking-pot/) after resting, without touching a vanilla bed or a spawn command. Do not die as a test of respawn preservation; this packet's evidence is documentary and no in-game verification was performed.

## Expected result
You have a recipe-backed portable bag or suspended hammock; successful use rests according to effective rules while the selected-release description says it does not set a new spawn.[1][2][3][4][5] Sleep, time advancement, spawn preservation, phantom behavior and respawn destination are distinct questions. This page does not assert an executed answer for any of them.

## Common failures
- **Recipe unavailable**: the shipped recipes have explicit enablement conditions; use [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/) to check availability. Do not edit settings to force a result.[3][4][5]
- **No rope / missing other-end rope / insufficient space**: install the facing pair and clear the proposed hammock span, following the displayed error. Exact supported blocks/spacing logic remain untraced.[2][7]
- **Too far away or occupied**: approach the item or wait until it is free. Those are exact shipped failure messages; do not treat them as a respawn-setting prompt.[2]
- **“You don't feel sleepy yet”**: another rest attempt is blocked by the sleepiness mechanic; wait rather than inventing a fixed cooldown. **“This is decorative, you cannot sleep here”** means decoration is not a functioning rest place.[2]
- **Bag breaks**: the selected release documents a configurable break chance and reports breakage; no numeric default or immunity is established. Bring a spare only if the material cost suits you.[2]
- **Conditional tip — choose the time direction intentionally**: if you want to keep working through daylight, avoid the hammock's documented day-to-night transition. Benefit: avoid deliberately entering night; trade-off: forego that rest option. For travel, a bag's no-new-spawn documentation makes it preferable to resetting home with a bed, but effective behavior is untested.[1][6]

## Sources
[1] `comforts-neoforge-9.0.5+1.21.1.jar!META-INF/neoforge.mods.toml` — exact version and no-new-spawn/day-to-night description.
[2] `comforts-neoforge-9.0.5+1.21.1.jar!assets/comforts/lang/en_us.json` — `item.comforts.sleeping_bag.auto_use.tooltip.0`, `.1`; `block.comforts.hammock.no_sleep`, `.no_sleep.2`, `.no_rope`, `.missing_rope`, `.no_space`; `capability.comforts.not_sleepy`; `gui.comforts.config.hammockUse.description`, `sleepingBagUse.description`, `sleepingBagBreakChance.description`; occupied/too-far/decorative/break messages.
[3] `comforts-neoforge-9.0.5+1.21.1.jar!data/comforts/recipe/sleeping_bag_white.json`.
[4] `comforts-neoforge-9.0.5+1.21.1.jar!data/comforts/recipe/hammock_white.json`.
[5] `comforts-neoforge-9.0.5+1.21.1.jar!data/comforts/recipe/rope_and_nail.json`.
[6] [Author's Comforts README](https://github.com/illusivesoulworks/comforts) — unversioned supplemental portability/bed distinction; not a selected-release recipe source.
[7] [Author's Hammocks wiki](https://github.com/illusivesoulworks/comforts/wiki/Hammocks) — unversioned supplemental construction geometry; not a selected-release recipe or verified leisure-configuration source.
