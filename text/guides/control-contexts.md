<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/control-contexts/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Find the control for the screen you are using

## Baseline
Minecraft 1.21.1, NeoForge 21.1.250; Controlling 19.0.5, EMI 1.1.24 and JEI 19.32.0.359. How-to: identify a control before changing it.

## Evidence status
Saved bindings and exact-version UI labels; **not runtime tested**. The same physical key can serve different screens. A duplicate binding is a lead, not proof of a conflict. This guide does not prescribe a replacement key.

## Prerequisites
Know the screen where the unwanted action occurs and the action you intended. Start with no item on the cursor. Do not investigate by pressing deletion, drop or bulk-transfer controls while carrying valuable items.

## Steps
1. Write down the context: looking at the world, ordinary inventory, a recipe page or a particular container. Include what is hovered and whether a search field has focus. These distinctions matter more than a key name alone.
2. Open the game's controls list. Controlling supplies **Show All**, **Show Conflicts**, **Show Unbound** and **Available Keys**. Use Show All to find the intended action, then Show Conflicts to inspect possible overlaps. Show Unbound means an action needs a binding; it does not mean the feature is absent.
3. For [recipe search](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/recipe-search/), compare the saved actions below. Start with Ctrl+F and a plain item-name query, not a crafting click. The expected checkpoint is a focused search field and matching items.
4. If U opens another screen, compare the saved JEI/EMI uses action with the waypoint action in the table. Return to the inventory/recipe context; do not conclude that the recipe viewer is broken merely because a world-context action won.
5. If a binding must change, record its original value first and change only the intended action. Available Keys is a candidate list, not a guarantee against every mod-specific mouse or contextual handler. Check the same original screen and hovered target with disposable items before trusting the change. Restore the original binding if the intended action still fails. Do not use a global reset to fix one overlap.

## Expected result
You can name the intended action, its saved binding if captured, and the context in which you need it. Runtime success remains an owner check, not a result of this documentation work.

## Common failures
- **No separate JEI panel:** the captured JEI setting is `enabled=false`, whereas EMI saves `enabled=true`. Treat EMI as the first visible route; neither value proves live loading or complete imported-category coverage.
- **Ctrl+O appears to do nothing:** both viewers save the same visibility key. Check which viewer is visible before changing both.
- **A mouse action moves items instead of browsing:** left/right clicks also have inventory meanings. Use R/U over the intended viewer item first, keeping the cursor empty.
- **An action is missing from this table:** the processed settings did not capture every mod's keys. Find the exact action label in Controls or that mod's configuration; do not apply a remembered default. For inventory operations use [item safety](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/inventory-safety/); for world overlays use [Jade identification](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/jade-identification/).

## Saved binding reference
| Action | Captured binding | Context/limit |
|---|---|---|
| Open inventory | E | Saved game control |
| EMI focus search / JEI focus search | Ctrl+F / Ctrl+F | Supported viewer context; field focus must be visible |
| EMI recipes / uses | R or left click / U or right click | Viewer item context, not a general inventory gesture |
| EMI favourites / back | A / Backspace | Applicable viewer context |
| EMI visibility / JEI overlay | Ctrl+O / Ctrl+O | Potential overlap, not reproduced conflict |
| EMI craft one / craft all | Left click / Shift+left click | Crafting action context; avoid bulk action until output is checked |
| JEI recipe back / close | Backspace / Escape | JEI recipe GUI, if accessible |
| JEI previous / next recipe page | Page Up / Page Down | JEI recipe GUI |
| JEI previous / next category | Shift+Page Up / Shift+Page Down | JEI recipe GUI |
| Xaero waypoint screen | U | Saved overlap with item uses; separate system, not a recipe function |

`key.keyboard.unknown` denotes an unbound captured entry, not a physical key called Unknown. Uncaptured IPN, Jade, TrashSlot and Crafting Tweaks bindings are **unknown**, not unbound.

## Sources
Processed saved-controls evidence and global EMI/JEI settings for this baseline; Controlling 19.0.5 `assets/controlling/lang/en_us.json` (Show Conflicts, Show Unbound, Available Keys). Private retained witnesses and claim IDs E-CONTROL, E-VIEWER, E-IPN-SAVED are provided to reviewers. No original settings were reopened.
