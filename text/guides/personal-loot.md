<!-- wiki.py managed raw export schema=1 -->
Source: https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/personal-loot/
Baseline: dev-0.5-20261015-r2
Spoiler: safe

# Personal loot and the shared container

## Baseline

Development documentation snapshot **dev-0.5-20261015-r2**; not release validation. Static documentation only; effective datapacks, settings and gameplay have not been verified.

## Evidence status

This exact Lootr release describes unique loot for each player opening a loot container. Its shipped warnings explicitly say breaking the block or destroying the entity prevents other players obtaining loot. Personal contents therefore do not make the physical container disposable. Conversion eligibility, refresh configuration and claim permissions are not established by that description.

## Prerequisites

A container positively identified as Lootr, room for the items you intend to take, and host permission to interact. Ordinary base storage is not assumed personal. Do not probe by breaking a container.

## Steps

1. Agree that each player opens the intact Lootr container themselves. Do not nominate a first opener to distribute everyone's supposed contents.
2. Open normally and take the items you want into your inventory. Leave the physical container in place for other players.
3. A second player opens it independently. Their own contents are the intended checkpoint; different rolls need not be identical. This is a proposed group check, not a reported test.
4. Close it and return supplies to agreed shared storage yourself. Personal loot does not mean items subsequently placed in ordinary storage remain private.
5. Before moving on, read any displayed refresh or decay message. These messages describe timed states; their presence in translations does not mean either feature is enabled for every chest.

## Expected result

Players can distinguish their loot from the shared access point and preserve access for the group. Continue with [equipment slot reference](https://faizsaifulnizam.github.io/minecraft-pack-wiki/guides/equipment-slots/).

## Common failures

- Cannot break: respect the refusal. Shipped messages mention sneak-breaking overrides in some contexts; they are destructive warnings, not a recovery instruction.
- Empty after returning: do not promise a refill or run refresh/clear commands. Timers and conversion can be configured; ask the host with the container's displayed identity, without publishing coordinates.
- Container decayed or destroyed: no player restoration procedure is documented in the retained evidence. Stop interacting and request host assessment; commands may change everybody's state.
- Claim denies access: Lootr ships an FTB Chunks whitelist tag reference, but that does not prove effective permission policy. Team/claim permissions require a separate host check.

Tip: open as a group before leaving rather than removing the chest. This preserves access but still cannot guarantee later availability if decay is enabled.

## Sources

- `lootr-neoforge-1.21.1-1.11.38.127.jar!META-INF/neoforge.mods.toml`
- `lootr-neoforge-1.21.1-1.11.38.127.jar!assets/lootr/lang/en_us.json`
- `lootr-neoforge-1.21.1-1.11.38.127.jar!data/ftbchunks/tags/block/interact_whitelist.json`
