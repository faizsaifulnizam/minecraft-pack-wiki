<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/inventory-safety/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Organize items without treating locks as a backup

## Baseline
Inventory Profiles Next 2.2.5, Mouse Tweaks 2.26.1, Crafting Tweaks 21.1.11 and TrashSlot 21.1.11. How-to: prepare a bounded inventory operation and avoid destructive shortcuts.

## Evidence status
Exact shipped option descriptions plus processed saved IPN settings; **not runtime tested**. Feature descriptions establish what options intend to control, not which options are enabled here. Mouse Tweaks gestures and wheel direction remain unverified for the saved pack configuration. No default hotkey is prescribed.

## Prerequisites
A safe place to stop and an ordinary storage container with spare space. Put irreplaceable equipment and unusually named or enchanted items aside manually before experimenting. Use a few disposable items for the first check; do not start with a machine input/output slot or crafting result.

## Steps
1. Identify the intended operation: sort the player's inventory, sort the opened container, move matching items, refill stacks or clear a crafting grid. [Resolve the action and context](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/control-contexts/) before pressing a hotkey. IPN's saved overlay, inventory editor and inventory settings buttons are hidden; their absence is not evidence that sorting is disabled.
2. For sorting or moving, inspect IPN's **Enable Locked Slots** and lock controls in its own settings. The shipped description says locks exclude slots from sort, move all, clean cursor and crafting/refill supply storage. It also explicitly excludes auto-refill monitoring slots from that protection. No saved lock shortcut or active lock state is captured here: stop if you cannot identify the control and its visual state.
3. Check the separate protections relevant to your task. **Disable Shift+Click and Ctrl+Q and Q** describes inventory-screen protections; **Disable (Q) Drop For Non-Stackable Locked Slots In Game** describes a separate world-context protection. **Disable All User Input on Locked Slots** does not stop automated actions, profiles or auto refill. A lock is not a universal deletion barrier, a grave or a backup.
4. Before a move, inspect **Move All Under the Cursor**. Its description distinguishes source-under-cursor behavior from player-to-container behavior. For a focused item-type operation, inspect **Only focused Item type**: the description says it moves all of the selected type even if that type is not already on the other side. For topping up existing stacks only, inspect **Just refill stacks** instead. Confirm the destination has room and inspect the first disposable result before repeating.
5. Before enabling or relying on auto refill, inspect **Use Items From Locked Slots** and **Refill With Any Food**. The latter can choose an enchanted golden apple before ordinary food, according to the shipped description. **Allow refill with harmful foods** is a further condition. Keep valuable food outside the experiment; do not assume a lock or custom name preserves it.
6. For a crafting grid, use the visibly labelled **Clear Grid** action only after making inventory space. Do **not** substitute **Force Clear Grid**: its exact tooltip says it drops items if necessary. Rotation, balance and spread change grid arrangement; after any such action recheck [the actual output](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/conflicting-outputs/) before taking it. Hotkeys, clear-grid overflow behavior and current Crafting Tweaks mode are not captured; use the labelled supported UI or stop.
7. For TrashSlot, first establish the **Lock/Unlock TrashSlot** control and visible lock state using disposable items only. The captured evidence contains no saved key or active deletion options. Hiding the slot is not a universal safety method: **Allow Deletion While TrashSlot is Invisible** exists. Do not use **Delete All Items of Type** for a first check, and do not promise an undo.

## Expected result
A small, inspected operation with valuable items excluded and the chosen source/destination understood. If a control, mode or protection is unknown, leave the items where they are and use deliberate individual clicks instead of guessing a bulk gesture.

## Common failures
- **Locked slots moved or supplied items:** inspect auto-refill exceptions and automated/profile actions before treating this as a broken lock. Do not reproduce with valuable gear.
- **Row/column sort does not fit around locks:** IPN's description requires the remaining unlocked shape to be rectangular. Ordinary sorting is a different operation; do not unlock precious slots just to obtain a rectangular pattern.
- **Closing the screen did not immediately stop sorting:** with interval-between-clicks enabled, IPN has a separate Stop Sorting If Screen Closes option. Its saved value is unknown. Screen close is not a guaranteed cancel.
- **Wheel movement is surprising:** IPN has item scrolling and Mouse Tweaks is also installed. No saved Mouse Tweaks direction or enabled-gesture evidence was captured. Stop scrolling, empty the cursor and return to individual clicks. Installed co-presence does not establish a reproduced conflict or justify a universal wheel direction.
- **TrashSlot is disabled on a server:** its shipped message says the server must have TrashSlot installed. Do not install or change a server as part of this guide.
- **An item is already gone:** stop further deletion, inspect the visible slot without adding another item, and seek the owner's recovery procedure. This evidence does not establish a recoverable buffer, lifetime, persistence or undo control. Creative delete keys are explicitly described as permanent regardless of Instant Deletion.

## Tips with trade-offs
**Top up rather than evacuate a container.** Prerequisite: identify IPN's Just refill stacks modifier and the move direction. Technique: constrain the operation to existing destination stacks. Benefit: avoids introducing new item types to a deliberately arranged inventory. Trade-off: it will not create a new destination stack; no binding or successful pack transfer is verified.

**Keep valuable food out of refill candidates.** Prerequisite: inspect auto-refill choices. Technique: store special food separately before using an uncertain refill setup. Benefit: avoids the shipped any-food preference choosing rare food. Trade-off: that food is not immediately available on the hotbar. This is a precaution, not an assertion that any-food is enabled.

## Sources
IPN 2.2.5 `assets/inventoryprofilesnext/lang/en_us.json` option descriptions; processed IPN global settings. Crafting Tweaks 21.1.11 `assets/craftingtweaks/lang/en_us.json`; TrashSlot 21.1.11 `assets/trashslot/lang/en_us.json`. Mouse Tweaks 2.26.1 metadata establishes installed presence only. Claims E-IPN-LOCK, E-IPN-MOVE, E-IPN-REFILL, E-GRID and E-TRASH.
