---
title: "GFED (Global Fire Emissions Database)"
icon: lucide/wind
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/smoke-emissions.yml
tags:
  - Global
  - Bulk download
  - HDF
  - Periodic
---

# GFED (Global Fire Emissions Database)

Burned area, fuel consumption and fire emissions of carbon and trace gases, globally.

[:lucide-download: Access data](https://www.globalfiredata.org/data.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://www.globalfiredata.org/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | GFED team (Vrije Universiteit Amsterdam and partners) |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 1997 to 2020 (GFED5 burned area) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 0.25 degrees (1 degree for 1997 to 2000) |
| :lucide-file:{ title="File and service formats" } Format | HDF5, ASCII |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Free for research (see site) |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Periodic |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    GFED5 burned area has discontinuities in 1998, 2001 and 2003 where new sensor data enter. Use caution for pre-MODIS trends. Emissions years differ by version.

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "GFED (Global Fire Emissions Database)", "description": "Burned area, fuel consumption and fire emissions of carbon and trace gases, globally.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/smoke-emissions/gfed/", "creator": {"@type": "Organization", "name": "GFED team (Vrije Universiteit Amsterdam and partners)"}, "spatialCoverage": "Global", "temporalCoverage": "1997 to 2020 (GFED5 burned area)", "keywords": ["Global", "Bulk download", "HDF", "Periodic"], "license": "Free for research (see site)", "sameAs": "https://www.globalfiredata.org/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://www.globalfiredata.org/data.html", "encodingFormat": "HDF5"}, {"@type": "DataDownload", "contentUrl": "https://www.globalfiredata.org/data.html", "encodingFormat": "ASCII"}]}</script>

[:lucide-arrow-left: Back to Smoke, emissions & air quality](index.md){ .md-button }
