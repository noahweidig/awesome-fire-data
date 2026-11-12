---
icon: lucide/history
---

# Changelog

## Unreleased

- Audit pass: updated GlobFire (to 2021), FIRED (V2, to 2024 with Alaska), GFED (5.1 and 4s), Global Fire Atlas, Fire_cci S3 SYN, GABAM, FINN, Landsat Burned Area, LANDFIRE, GOES-R FDC, Wildfire Risk to Communities and FEMA NRI. MODIS and VNP64A1 caveats now give shutdown dates and S-NPP status.
- Moved GlobFire to Fire behavior & spread, SE FireMap to Perimeters & burned area and FEMA NRI to Risk, WUI & management. Renamed Social vulnerability & communities to Exposure & vulnerability. URLs for the moved pages changed.
- Added topic, sensor and time step tags. Added Alaska, Western US and Multi-country regions, Vector, Point or station and Grid over 5 km resolution tags, and more license tags. Daymet and ERA5-Land now use update cadence for the cadence tag.
- Updated FPA-FOD to the 7th edition (1992 to 2024, 2.66 million records).
- Added 11 datasets: GlobPOP, NIFC GACC boundaries, NBAC, CAL FIRE FRAP perimeters, Alaska Fire History, VIIRS VNP64A1, Fire_cci Sentinel-3 SYN, FEDS, Globe-LFMC, US Drought Monitor and RAWS.
- Corrected licenses for building-based WUI, FIA, GABAM, FIRED, SILVIS WUI, CAL FIRE DINS and RAP. Flagged conflicting RAP license listings.
- Updated NLCD to 2024, GFED to GFED5 years and caveats, SVI edition, and added NRI, HRRR and MODIS end-of-mission notices.
- Added optional `doi`, `citation`, `verified` and `snippets` fields, JSON-LD for Google Dataset Search, and `catalog.json` and `catalog.csv` exports.
- Added a sortable, filterable all-datasets table, a decision flowchart, per-page edit links to the YAML, and an announcement banner.

- Added themes: prescribed fire, suppression, fire behavior, lightning, social vulnerability, boundaries.
- Added 37 datasets, including USGS Landsat Burned Area, SE FireMap, GlobalRx, RAP, RCMAP, LCMAP, LCMS, TreeMap, FIA, PRISM, ERA5-Land, HRRR and Daymet.
- Added schema validation, a weekly link check, a compare page and an RSS feed of new dataset pages.
- Initial site with 10 themes and seed datasets.
