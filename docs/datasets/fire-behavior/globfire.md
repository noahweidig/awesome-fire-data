---
title: "GlobFire"
icon: lucide/globe
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fire-behavior.yml
tags:
  - Global
  - Bulk download
  - Shapefile
  - CC BY 4.0
  - Static
  - Vector
  - MODIS
  - Fire events
  - Fire perimeters
---

# GlobFire

Global fire event polygons with daily progression, built from MODIS MCD64A1 burned area.

[:lucide-download: Access data](https://developers.google.com/earth-engine/datasets/catalog/JRC_GWIS_GlobFire_v2_FinalPerimeters){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://doi.org/10.1038/s41597-019-0312-2){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | JRC Global Wildfire Information System |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 2001 to 2021 |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Event polygons (from 500 m MODIS) |
| :lucide-file:{ title="File and service formats" } Format | Shapefile |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | CC BY 4.0 |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Static |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-12 |

!!! warning "Caveat"

    Based on 500 m MODIS, so small fires are missed. Earth Engine v2 lists 2001 to 2021 and the PANGAEA record lists 2000 to 2021. Check GWIS for later releases.

## Related datasets

- [MODIS MCD64A1 Burned Area](../perimeters/mcd64a1.md)
- [FIRED](../fire-behavior/fired.md)
- [Global Fire Atlas](../fire-behavior/global-fire-atlas.md)
- [FEDS](../fire-behavior/feds.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "GlobFire", "description": "Global fire event polygons with daily progression, built from MODIS MCD64A1 burned area.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fire-behavior/globfire/", "creator": {"@type": "Organization", "name": "JRC Global Wildfire Information System"}, "spatialCoverage": "Global", "temporalCoverage": "2001 to 2021", "keywords": ["Global", "Bulk download", "Shapefile", "CC BY 4.0", "Static", "Vector", "MODIS", "Fire events", "Fire perimeters"], "license": "CC BY 4.0", "sameAs": "https://doi.org/10.1038/s41597-019-0312-2", "distribution": [{"@type": "DataDownload", "contentUrl": "https://developers.google.com/earth-engine/datasets/catalog/JRC_GWIS_GlobFire_v2_FinalPerimeters", "encodingFormat": "Shapefile"}]}</script>

[:lucide-arrow-left: Back to Fire behavior & spread](index.md){ .md-button }
