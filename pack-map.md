---
layout: default
title: "Pack map"
permalink: /pack-map/
baseline: dev-0.5-20261015-r2
---

# Pack map

> Development snapshot: **dev-0.5-20261015-r2**. Minecraft **1.21.1**, NeoForge **21.1.250**. The pack is still changing.

## Choose a direction
| System | Installed examples | Start here / current limit |
|---|---|---|
| Machines and processing | Modern Industrialization | Forge Hammer to bronze is documented; full steam automation is not yet mapped. |
| Searchable storage | Applied Energistics 2 | Meteorite materials and the small network are documented; MI power compatibility is Unknown. |
| Portable and bulk storage | Sophisticated Backpacks, Storage Drawers | Installed; upgrade rules and capacities still need mapping. |
| Spellcraft and rituals | Ars Nouveau, Iron's Spells 'n Spellbooks, Occultism, Nature's Aura | [Ars](guides/ars-first-spell.md), [Iron's](guides/iron-first-scroll.md), [Occultism](guides/occultism-first-workbench.md) and [Nature's Aura](guides/natures-aura-first-garden.md) have independent bounded starters; advanced curricula and effective gameplay remain incomplete. |
| Character progression | Tensura, SoloCraft: Reawakening, Tensura-Leveling | Installed; awakening, reincarnation and evolution entry paths are Unknown here. |
| Bosses and dimensions | Twilight Forest, Bosses of Mass Destruction, Tensura boss addons | Installed; encounters, entry/exit and death recovery are not tutorial-ready. |
| Exploration | Dungeons and Taverns, YUNG's Better Dungeons, Tectonic | Shipped resources indexed; this does not prove encounter placement. |
| Loot and equipment | Lootr, Artifacts, Relics, Reliquified Twilight Forest | Installed; acquisition and levelling need further checks. |
| Farming and building | Farmer's Delight, Chipped, Supplementaries | [Cooking pot](guides/homestead-cooking-pot.md), [rice/cutting](guides/homestead-rice-and-cutting.md), [Chipped](guides/homestead-chipped-workstations.md) and [Supplementaries](guides/homestead-supplementaries-devices.md) have bounded guides; broader farming/building loops remain incomplete. |
| Everyday tools | EMI/JEI, Jade, IPN, Xaero, FTB Chunks/Teams | Selected saved settings mapped; key contexts and multiplayer policies need testing. |

For an independent rest project, read [Comforts rest](guides/homestead-comforts-rest.md): rest is not a new respawn guarantee. These links do not certify completed curricula or gameplay.

## Connections we can and cannot claim
- Reliquified Twilight Forest ships recipes referencing Twilight Forest items. That is concrete cross-mod recipe data, not a successful craft or a tested progression shortcut.
- AE2 and MI are both installed. Their power/automation interface has not been established by this mapping, so do not assume their cables or energy units connect directly.
- Tensura-Leveling and SoloCraft have separate declared IDs. Similar names do not prove shared levels, skills or awakening.
- An advancement's parent can position it in the UI. It does not automatically impose a gameplay gate. Some criteria do contain explicit checks; those need to be read individually.

## Coverage
All **120 active top-level JARs** are indexed: nine have representative gameplay data read, 93 have resource-path classification only, and 18 are metadata-only/unmapped. The **121 declared top-level mod IDs** are a different count. Two JARs are disabled. Nested libraries are not additional active top-level mods.

The active archives contain 9,950 recipe JSON entries, 4,498 advancement JSON entries and 2,626 loot-table JSON entries. These are shipped files, not final runtime IDs or working recipes. Conditions, tags, overrides, generated data and server settings can change what is available.

## Customization boundary
The saved enabled resource-pack list includes an icon pack and local client-resource repair packs. Static inspection found assets rather than server data in those selected ZIPs. This does not prove a live reload or a repaired gameplay feature. Global Moonlight datapack and coremods directories were empty when inspected. Generated resource providers, final override precedence and world/server configuration remain unresolved.

## Questions still open
- How is SoloCraft awakening awarded, and what does Tensura reincarnation/evolution require?
- Which documented magic starter steps resolve under effective recipes/settings, and which advanced paths still need evidence?
- How do dimension entry, exit and death recovery work in this exact build?
- Which key overlaps are harmless contexts versus real conflicts?
- Which claims, team permissions and force-loading settings are enforced in multiplayer?

[First guides](getting-started.md) cover only the evidence-backed starting points. [Sources](sources.md) explains the status labels.
