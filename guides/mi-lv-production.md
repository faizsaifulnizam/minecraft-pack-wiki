---
layout: default
title: "Plan an MI low-voltage production route"
permalink: /guides/mi-lv-production/
baseline: dev-0.5-20261015-r2
---

# Plan an MI low-voltage production route

## Baseline
Private candidate **dev-0.5-20261015-r2**, unapplied; canonical baseline unchanged. Modern Industrialization 2.5.10 and AlmostUnified 1.21.1-1.4.2. This is a bounded static curriculum, not pack-wide or runtime acceptance.

## Evidence status
Selected exact-archive recipes and shipped prose, supplemented only where explicitly identified by pinned primary source. Recipes below describe shipped defaults, not resolved runtime recipes. Effective tags, resource precedence, generated recipes and active server configuration remain unverified. Reviewed against retained static evidence; not runtime-tested.

## Prerequisites
The [steel workshop](mi-steel-workshop.md), mixer, Steam Blast Furnace, Wiremill access and the current recipes for cables, turbine and electric machines. This is **MI electricity**, not an AE2 network. Analog Circuits and machine component recipes are prerequisites, not silently supplied by this page.

## Steps
These are advanced conditional planning/reference notes, not a completed executable production tutorial. The whole-wiki/tutorial goal remains unchanged and incomplete.

1. **STOP before insulation production:** retain the selected oil/rubber/wire/cable recipe IDs, quantities and complete component bills first. Prepare cable insulation using the guide's chain: mix Coke Dust with water for Raw Synthetic Oil; process that in a Steam Blast Furnace for Synthetic Oil; mix the oil with paper for rubber sheets. Paper can come from wood through wood pulp. Quantities and intermediate recipe selection are not retained, so follow each current recipe and keep fluids separated.
2. Make wires using the Wiremill, then combine wires with rubber sheets into cables. Copper, silver and tin cables are LV according to the guide; select an LV route for the first single-block electrical machines.
3. **STOP before turbine assembly/wiring:** require its complete component bill, steam-input and electricity-output controls and cable connection proof first. Craft the LV Steam Turbine and route steam to it. The turbine converts **one mB steam to one EU**, up to **32 mB/t**. Its electricity output goes only toward its output side: direct-connected machines or cables on that side. Do not use an arbitrary adjacent cable as proof of an energy connection.
4. **STOP before an electric-machine test:** name one exact machine and recipe ID, its complete circuit/component/insulation bill, input/output quantities, energy and controls first. No such test task is supplied here. Only after this gate passes, plan to attach that LV machine and test that recipe. Electric machines use electricity instead of steam and progressively overclock up to 32 EU/t. A turbine's maximum is not guaranteed from a bronze boiler: supply, not the turbine label, bounds the small line.
5. **STOP before Assembler construction/automation:** retain exact Assembler and chosen recurring-component recipe chains, quantities and slot/control proof first. Build one Assembler after satisfying its actual component recipe. Dedicate it to one displayed recurring component, lock the slots and feed it with the validated item-pipe method from [the workcell](mi-pipe-workcell.md). The guide permits up to three recipes per Assembler using slot locking; start with one to make faults attributable. Suggested later components are Machine Hulls, Analog Circuits, Motors, Pistons, Robot Arms and Conveyor Belts—not a proof that their entire dependency graph is automated.
6. Where Analog Circuits are available, a Configurable Chest offers **27 configurable slots** and auto-eject. Use an ordinary output inventory or that chest as the stock endpoint. No MI-to-AE2 power conversion, import wiring, autocrafting pattern or machine integration is proved here. See the existing [AE2 starter](ae2-starter.md) for its separately evidenced starting point.
7. Expand only after the single-machine check. The guide limits LV network intake to **256 EU/t**, not every individual machine's draw or an absolute transient output ceiling. Single-block electric machines connect only to LV cables; larger distribution uses separate networks or transformers with tier-appropriate inputs/outputs.

## Expected result
An advanced conditional planning/reference route with energy-limit context; no named electric-machine recipe task or executable Assembler production line is delivered. Circuit recipes, rubber quantities and complete automation remain open, not filled by generic technology-mod assumptions.

## Common failures
- Turbine has steam but machine lacks power: inspect the turbine output side and LV connection before adding generators.
- Speed does not reach the headline: distinguish boiler supply, turbine conversion ceiling, machine overclock and network intake. They are different limits.
- Tip: lubricant from creosote plus redstone can manually improve electric-machine overclock efficiency; the guide gives 25 mB per efficiency tick. This is optional and not a substitute for sufficient energy.
- Redstone Control Modules are documented as configured in hand then inserted into a machine/controller. Their mode meanings are not traced here; do not activate an unknown setting as a diagnostic.
- A Portable Storage Unit initially has zero capacity until batteries are inserted. Removing batteries can lose excess energy. It is inventory-carried MI energy storage, not an established AE2 power bridge.

## Sources
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/electric_age/making_cables.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/electric_age/electricity.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/electric_age/basic_machines.md`
- `Modern-Industrialization-2.5.10.jar!assets/modern_industrialization/mi_guidebook/electric_age/portable_storage_unit.md`
