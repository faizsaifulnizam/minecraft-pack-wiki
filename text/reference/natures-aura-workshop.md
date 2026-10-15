<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/reference/natures-aura-workshop/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Supply a Natural Altar without exhausting its surroundings

## Baseline

Candidate **dev-0.5-20261015-r2 (unapplied)**. The versioned description below is imported from previous-baseline retained witnesses for dev-0.5-20261015; it is not a fresh candidate archive revalidation. Effective recipes, settings and gameplay remain unverified.

**dev-0.5-20261015** — Nature's Aura **41.10**.

## Evidence status

Bounded retained-evidence static review only; candidate dev-0.5-20261015-r2 remains unapplied. This is not runtime validation, integration approval, baseline adoption or publication.

Reference and intermediate how-to from hash-matched shipped book entries and recipes. Not runtime tested. Follow [the first garden and Environmental Eye route](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/natures-aura-first-garden/) first. Structure IDs and recipe fields are verified; exact code-defined multiblock geometry, per-device operating range and effective server settings remain unresolved.

## Prerequisites

Keep an Environmental Eye in your hotbar and retain Gold Leaf. You need the Ritual of the Forest setup and its book structure page for the following crafts. Avoid adding passive consumers near your main garden before you can measure the surroundings. Aura is environmental; a full internal device buffer does not establish a healthy surrounding area. [N04, N05]

## Steps

1. **Bottle the right Aura for the first token.** The Aura Bottling entry directs you to craft a **Bottle and Cork**, then interact with the air while holding it. Use the Overworld for the first Token of Joy: the recipe specifically requires `naturesaura:aura_bottle` carrying `aura_type = naturesaura:overworld`. A generic glass bottle or the same item with Nether Aura is not that ingredient. Craft it shapelessly from one glass bottle and one plank-tag item. This is the book's `naturesaura:bottle_two_the_rebottling` recipe; the plain bottle by itself is not sufficient. [N06]
2. **Make Tokens of Joy.** At the Forest ritual, use a central oak sapling plus six stand ingredients: the Overworld Aura bottle, one Gold Leaf, one small-flower-tag item, one apple, one torch and one iron ingot. The shipped recipe produces two `naturesaura:token_joy`. Grow the central sapling to start, as in the beginner route. [N07]
3. **Make a Natural Altar.** Use a central oak sapling, three stone, one Gold Leaf, one gold ingot and one Token of Joy in the Forest ritual. The result is `naturesaura:nature_altar`. This crafts the block; it does not complete its surrounding multiblock. [N08]
4. **Build the altar's separate structure from the book.** Open The Natural Altar entry and match structure `naturesaura:altar`. It uses Golden Stone Bricks among its construction materials; one Stone Bricks plus one Brilliant Fiber crafts one Golden Stone Bricks item, shapeless. An exact total and spatial placement cannot be given until the code-defined structure is independently reviewed. Do not assume the Forest ritual's powder pattern is also the altar's structure. [N08]
5. **Infuse one ordinary iron ingot.** Once the completed altar has collected sufficient Aura, place the ingot onto it and wait. The exact recipe is iron ingot → one Infused Iron, Aura cost **15000**, serialized time **80**. The field's time unit was not independently traced, so this is not a promise of an 80-second wait. The book describes internal collection from the surroundings and a depletion limit, not an unlimited resource. [N09]
6. **Plan replenishment rather than adding consumers indefinitely.** The Herbivorous Absorber consumes nearby small flowers to create Aura and functions only in the Overworld according to its entry. Repeating the same flower reduces its effectiveness; the guide recommends roughly six different kinds for maximum efficiency. Supply variety rather than a single flower type. [N10]

## Expected result

A measured first infusion, followed by a replenishment plan whose input costs you understand. This is not a fully closed automated system. The absorber's recipe uses four plank-tag ingredients, three Infused Iron, one peony and one Token of Joy. A peony is a construction ingredient here; the operating text calls for **small flowers**, not an assumption that every decorative flower works as fuel. [N10]

## Common failures

- **The altar block exists but will not operate:** check its separate multiblock, stored Aura and input recipe. The declared altar chapter advancement is `naturesaura:aura_bottle_overworld`; that explains book presentation, not proof of a universal block-use gate. [N08, N09]
- **The Eye reads half full:** that is the expected default environmental level. The Eye has a display ceiling and floor and cannot quantify farther beyond them. [N04]
- **A generator emits red sparks:** the book describes this as the production ceiling. Some generators stop; others keep behaving without producing more Aura. Do not blindly add more input material. An Aura Detector is the documented control lead; wiring and settings are not researched here. [N11]
- **A generator seems ineffective after relocation:** new generation first repairs a depleted nearby area, and Aura can migrate. Check the Environmental Eye over time rather than expecting a local instant spike. [N05]
- **The absorber runs poorly on the same flower:** diversify the sequence; the shipped entry explicitly describes repetition loss. In the Nether it has no effect at all. [N10]
- **Passive consumption is becoming hazardous:** stop adding consumers and retreat from the affected area. The later Aura Imbalance Ward is documented to stop an adjacent consumer when local Aura is too low, at no operating cost; its own recipe/access chain is not completed here. [N12]

## Tips with trade-offs

- **Measure before building a larger consumer array.** Prerequisite: an Environmental Eye. Benefit: gives a baseline for distinguishing normal Aura from depletion. Trade-off: the basic Eye cannot measure beyond its range. [N04, N05]
- **Rotate the absorber's flowers.** Prerequisite: the Herbivorous Absorber in the Overworld and several small flower types. Benefit: avoids the documented repetition penalty. Trade-off: a diverse supply is harder to replenish than one monoculture; no exact six-flower threshold or operating radius is asserted. [N10]
- **Treat bottling automation as an item-collection job too.** Prerequisite: Bottle and Corks plus a dispenser. Benefit: the book describes automatic Aura bottling. Trade-off: filled bottles are expelled, not pulled back into the dispenser; add a collection route such as a hopper rather than leaving valuable outputs loose. No throughput or cross-mod item transfer was tested. [N06]

## Sources

- [N04–N12] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/`: `items/eye.json`, `intro/aura.json`, `practices/aura_bottle.json`, `practices/tree_ritual.json`, `using/altar.json`, `creating/flower_generator.json`, `creating/on_generating.json`, `using/lower_limiter.json`.
- [N07–N10] Same archive, `data/naturesaura/recipe/`: `tree_ritual/token_joy.json`, `tree_ritual/nature_altar.json`, `gold_brick.json`, `altar/infused_iron.json`, `flower_generator.json`.

### Archive and internal-entry citations

These locators identify the documented archive contents, not downloadable retained evidence or a guarantee of effective gameplay.

- [N04] `NaturesAura-41.10.jar!data/naturesaura/recipe/tree_ritual/eye.json`: `witness`.
- [N04] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/items/eye.json`: `witness`.
- [N05] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/intro/aura.json`: `witness`.
- [N06] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/practices/aura_bottle.json`: `witness`.
- [N06] `NaturesAura-41.10.jar!data/naturesaura/recipe/bottle_two_the_rebottling.json`: `witness`.
- [N06] `NaturesAura-41.10.jar!data/naturesaura/recipe/tree_ritual/token_joy.json`: `witness`.
- [N07] `NaturesAura-41.10.jar!data/naturesaura/recipe/tree_ritual/token_joy.json`: `witness`.
- [N07] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/practices/tree_ritual.json`: `witness`.
- [N08] `NaturesAura-41.10.jar!data/naturesaura/recipe/tree_ritual/nature_altar.json`: `witness`.
- [N08] `NaturesAura-41.10.jar!data/naturesaura/recipe/gold_brick.json`: `witness`.
- [N08] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/using/altar.json`: `witness`.
- [N09] `NaturesAura-41.10.jar!data/naturesaura/recipe/altar/infused_iron.json`: `witness`.
- [N09] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/using/altar.json`: `witness`.
- [N10] `NaturesAura-41.10.jar!data/naturesaura/recipe/flower_generator.json`: `witness`.
- [N10] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/creating/flower_generator.json`: `witness`.
- [N11] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/creating/on_generating.json`: `witness`.
- [N12] `NaturesAura-41.10.jar!assets/naturesaura/patchouli_books/book/en_us/entries/using/lower_limiter.json`: `witness`.
