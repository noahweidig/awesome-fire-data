---
title: "TreeMap"
icon: lucide/tree-pine
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fuels-terrain.yml
tags:
  - United States
  - Bulk download
  - GeoTIFF
  - CSV
  - Public domain
  - Periodic
  - 30 m
---

# TreeMap

Tree-level model of US forests, made by imputing FIA plot data onto a 30 m grid.

[:lucide-download: Access data](https://doi.org/10.2737/RDS-2025-0032){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://doi.org/10.2737/RDS-2025-0032){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | USDA Forest Service Rocky Mountain Research Station |
| :lucide-map:{ title="Geographic extent" } Coverage | Conterminous US |
| :lucide-calendar:{ title="Years covered" } Period | Editions for 2014, 2016, 2020 and 2022 |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 30 m |
| :lucide-file:{ title="File and service formats" } Format | GeoTIFF, CSV |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Public domain |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Periodic |

!!! warning "Caveat"

    Each pixel holds an imputed plot ID. Test fit before using it for applications the publication does not list.

## Related datasets

- [FIA DataMart](../fuels-terrain/fia-datamart.md)
- [LANDFIRE](../fuels-terrain/landfire.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "TreeMap", "description": "Tree-level model of US forests, made by imputing FIA plot data onto a 30 m grid.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fuels-terrain/treemap/", "creator": {"@type": "Organization", "name": "USDA Forest Service Rocky Mountain Research Station"}, "spatialCoverage": "Conterminous US", "temporalCoverage": "Editions for 2014, 2016, 2020 and 2022", "keywords": ["United States", "Bulk download", "GeoTIFF", "CSV", "Public domain", "Periodic", "30 m"], "license": "Public domain", "sameAs": "https://doi.org/10.2737/RDS-2025-0032", "distribution": [{"@type": "DataDownload", "contentUrl": "https://doi.org/10.2737/RDS-2025-0032", "encodingFormat": "GeoTIFF"}, {"@type": "DataDownload", "contentUrl": "https://doi.org/10.2737/RDS-2025-0032", "encodingFormat": "CSV"}]}</script>

[:lucide-arrow-left: Back to Fuels, vegetation & terrain](index.md){ .md-button }
