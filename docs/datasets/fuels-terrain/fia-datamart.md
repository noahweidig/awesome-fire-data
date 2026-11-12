---
title: "FIA DataMart"
icon: lucide/database
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fuels-terrain.yml
tags:
  - United States
  - Bulk download
  - CSV
  - SQLite
  - Annual
  - Free to use
  - Point or station
  - Vegetation
  - Fuels
---

# FIA DataMart

Forest Inventory and Analysis plot, tree, fuel and down woody material measurements for US forests.

[:lucide-download: Access data](https://apps.fs.usda.gov/fia/datamart/datamart.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://research.fs.usda.gov/products/dataandtools/fia-datamart){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | USDA Forest Service FIA program |
| :lucide-map:{ title="Geographic extent" } Coverage | United States |
| :lucide-calendar:{ title="Years covered" } Period | Varies by state |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Plots |
| :lucide-file:{ title="File and service formats" } Format | CSV, SQLite |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Free to use, no fees (US Government data). Cite FIA. |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Annual |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    Public plot coordinates are fuzzed and swapped for privacy. The R packages rFIA and FIESTA download from DataMart. No license is stated on DataMart itself. Some catalogs label it CC BY 4.0.

## Quick start

=== "R"

    ```r
    library(rFIA)
    getFIA(states = "CA", dir = "fia_data")
    db <- readFIA("fia_data")
    ```


## Related datasets

- [TreeMap](../fuels-terrain/treemap.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "FIA DataMart", "description": "Forest Inventory and Analysis plot, tree, fuel and down woody material measurements for US forests.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fuels-terrain/fia-datamart/", "creator": {"@type": "Organization", "name": "USDA Forest Service FIA program"}, "spatialCoverage": "United States", "temporalCoverage": "Varies by state", "keywords": ["United States", "Bulk download", "CSV", "SQLite", "Annual", "Free to use", "Point or station", "Vegetation", "Fuels"], "license": "Free to use, no fees (US Government data). Cite FIA.", "sameAs": "https://research.fs.usda.gov/products/dataandtools/fia-datamart", "distribution": [{"@type": "DataDownload", "contentUrl": "https://apps.fs.usda.gov/fia/datamart/datamart.html", "encodingFormat": "CSV"}, {"@type": "DataDownload", "contentUrl": "https://apps.fs.usda.gov/fia/datamart/datamart.html", "encodingFormat": "SQLite"}]}</script>

[:lucide-arrow-left: Back to Fuels, vegetation & terrain](index.md){ .md-button }
