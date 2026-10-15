---
layout: default
title: "Craft and open a first backpack"
permalink: /guides/first-backpack-access/
baseline: dev-0.5-20261015-r2
---

# Craft and open a first backpack

## Baseline
Development documentation snapshot **dev-0.5-20261015-r2**; not release validation.

## Evidence status
> Development documentation snapshot **dev-0.5-20261015-r2**. Sophisticated Backpacks **3.26.9.2195**. Recipe declaration plus provisional same-version upstream control evidence; no effective-recipe or gameplay acceptance.

## Prerequisites
Prepare one basic Backpack and, conditionally, open its held-item menu without equipping it or moving stock. Choose [an oak drawer](craft-first-oak-drawer.md) instead for a workshop crafting route; these are independent alternatives, not prerequisites for each other. [Storage choice](storage-choice.md) retains the wider comparison.

You need a 3-by-3 crafting grid, four ingredients accepted by `c:strings`, four accepted by `c:leathers`, and one accepted by `c:chests/wooden`. The shipped Backpack recipe uses a custom `sophisticatedbackpacks:basic_backpack` type and a `sophisticatedcore:item_enabled` condition for `sophisticatedbackpacks:backpack`. Its presence in a JAR does not prove it is enabled or displayed correctly in this pack.

## Steps
1. In [recipe search](recipe-search.md), compare the current recipe for `sophisticatedbackpacks:backpack` with the shipped rows `SLS`, `SCS`, `LLL`: S is the string tag, L the leather tag, C the wooden-chest tag. Confirm the output is one basic Backpack before committing ingredients. If the current recipe cannot be confirmed, retain your ingredients and resolve that uncertainty first.
2. For the matching declaration, arrange those three rows and take one `sophisticatedbackpacks:backpack`. Do not add upgrades or put valuables inside it during this first access check.
3. **Provisional control, not exact-build proof:** upstream source declaring `mod_version=3.26.9` opens the Backpack menu from the held item's `use` method. With the new Backpack selected in your main hand, aim into empty air and use the item (your configured Use Item control). Do not sneak-use it on a block: the same source has a separate placement route. This source has not been tied to build 2195 or the installed compiled behavior; if your interface differs, stop instead of trying guessed bindings.

## Expected result
For the provisional control in step 3, the expected result is a Backpack container menu, not equipping or placing the item. Read only its title and visible layout; leave slots and upgrade controls untouched. Menu opening is not proof of deposit/withdrawal, capacity, safe item eligibility or save/reopen persistence. A first useful carrying-and-return task remains unverified until those boundaries are established.

## Common failures
If the provisional use action does not open the expected menu, do not compensate with a Curios slot, drop action, repeated placement or forced pickup. Keep the empty Backpack and record which item and action differed. Missing recipe display can reflect conditions, custom serializer or viewer support; do not rewrite settings to force a recipe. Do not infer item loss merely from a menu failing to open.

## Tips and trade-offs
A held-item access check avoids making worn-slot eligibility a prerequisite, but does not establish worn upgrades or shortcut keys. Avoid deletion upgrades while learning: the shipped Void Upgrade tooltip says it voids items selected in its filter. The Filter Upgrade tooltip instead describes filtering items piped in/out. Those labels distinguish purposes, not proved controls, pipe compatibility or non-deleting capacity expansion. Keep [transfer and deletion boundaries](../reference/storage-boundaries.md) open.

## Sources
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!data/sophisticatedbackpacks/recipe/backpack.json` — full declared recipe and enabled condition.
- `sophisticatedbackpacks-1.21.1-3.26.9.2195.jar!assets/sophisticatedbackpacks/lang/en_us.json` — selected Filter/Void Upgrade labels, not UI proof.
- [BackpackItem.java, lines 239–253 and 327–338](https://github.com/P3pp3rF1y/SophisticatedBackpacks/blob/565bd1bfac58f5e57c56b0be9a681dc042ba07ec/src/main/java/net/p3pp3rf1y/sophisticatedbackpacks/backpack/BackpackItem.java#L239-L338) — placement separation and held-item menu caller; provisional same-version source.
- [gradle.properties, line 18](https://github.com/P3pp3rF1y/SophisticatedBackpacks/blob/565bd1bfac58f5e57c56b0be9a681dc042ba07ec/gradle.properties#L18) — source version declaration, not installed-binary correspondence.
