CNK Drift Gauge + Reserves Meter - EU adaptation 1.0.8

Original mod, artwork and gameplay-display logic: tomtotom
Original page: https://gamebanana.com/mods/729041
EU compatibility adaptation and testing: Majed-allababedi
GitHub: https://github.com/Majed-allababedi/CTR-CNK-Drift-Gauge-EU

Supports CUSA14876 update 01.21 on a compatible EU-aware OCTR launcher.
Enable this package in Mods and SELECT THE SPEEDOMETER HUD IN-GAME.
Fully restart the game after enabling the package. Disable overlapping CNK,
boost-gauge or reserves packages; back up saves first.

The original mod supplies a curved drift-timing gauge beside the kart and a live
boost-reserves display below the stock speedometer. The original display uses
three color passes: green 0-20 seconds, yellow 20-40, orange 40-60. Above 60 seconds
the display remains orange; this is not a cap on actual reserves. The original
mod does not change boost timing, speed or gameplay mechanics.

EU adaptation: 29 resource indices resolved by asset name, 5 HUD payloads retain
EU language dependencies, and 7 executable writes are verified with original-byte
hashes. Hook and helper calls are rebuilt for the tested EU executable.
Version 1.0.8 adds explicit original-author/EU-adapter credit; executable write
addresses/values and asset payloads are unchanged from the gameplay-tested 1.0.7.
Majed-allababedi confirmed the EU 1.21 package works in-game. This is not proof of
compatibility with every executable variant, ultrawide mode or multiplayer.

Requires EU support in the loader, not just the base launcher executable.
Launcher: https://github.com/Majed-allababedi/OCTR-NitroFueled-PC
No original game executable, save, keys or full game archives are included.

Copyright and original license remain with the respective authors. Original
GameBanana page lists CC BY-NC-ND 4.0; the repository owner confirms permission
from tomtotom to distribute this modified EU version. This permission is not a
blanket sublicense for further modified redistribution; ask the original author.
