---
icon: lucide/git-compare
---

# Compare datasets

Pairs that people often confuse. Fields come from each dataset page.

## MTBS and WFIGS perimeters

| | [MTBS](../datasets/perimeters/mtbs.md) | [WFIGS](../datasets/perimeters/wfigs-perimeters.md) |
| --- | --- | --- |
| Source | Landsat imagery, mapped by USGS and USDA Forest Service | Agency-reported perimeters from US interagency sources |
| Period | 1984 to present | Current year and historical archive |
| Update | Annual | Continuous |
| Size cutoff | 1,000 acres in the West, 500 acres in the East | See the provider page |
| Adds | Burn severity mosaics | Near real time incident perimeters |

Use MTBS for severity and a consistent satellite record. Use WFIGS for current incidents and agency-reported perimeters. MTBS also includes prescribed fire perimeters.

## FIRMS and GOES-R fire detection

| | [NASA FIRMS](../datasets/active-fire/firms.md) | [GOES-R FDC](../datasets/active-fire/goes-fdc.md) |
| --- | --- | --- |
| Orbit | Polar-orbiting MODIS and VIIRS | Geostationary |
| Coverage | Global | Americas |
| Resolution | 375 m to 1 km | 2 km |
| Revisit | Several passes per day | 5 to 15 minutes |
| Period | 2000 to present (MODIS), 2012 to present (VIIRS) | 2017 to present |

Use FIRMS for finer pixels and global coverage. Use GOES-R when timing within the hour matters.

## Burned area products

| | [MCD64A1](../datasets/perimeters/mcd64a1.md) | [GlobFire](../datasets/perimeters/globfire.md) | [Fire_cci](../datasets/perimeters/fire-cci51.md) | [SE FireMap](../datasets/prescribed-fire/se-firemap.md) |
| --- | --- | --- | --- | --- |
| Coverage | Global | Global | Global | Southeastern US |
| Period | 2000 to present | 2001 to 2020 | 2001 to 2020 | 1994 to 2025 |
| Resolution | 500 m | Event polygons from 500 m MODIS | 250 m | 30 m |
| Unit | Monthly pixels with burn date | Fire events with daily progression | Pixels with burn date and confidence | Annual pixels with burn date |

GlobFire builds events from MCD64A1. Fine regional products detect smaller burns but cover less area.

## Fire event datasets

| | [Global Fire Atlas](../datasets/fire-behavior/global-fire-atlas.md) | [FIRED](../datasets/fire-behavior/fired.md) |
| --- | --- | --- |
| Source | MODIS MCD64A1 | MODIS MCD64A1 |
| Coverage | Global | United States, with regional releases elsewhere |
| Period | 2003 to 2016 | 2001 to 2019 (US) |
| Outputs | Size, duration, daily expansion, speed, direction | Event polygons with daily spread estimates |

Both group burned pixels into events. Their grouping rules differ, so event counts and sizes will not match.
