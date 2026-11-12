---
title: "Global Fire Atlas"
icon: lucide/globe
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fire-behavior.yml
tags:
  - Global
  - Bulk download
  - GeoTIFF
  - Shapefile
  - NASA open data
  - Static
  - 500 m
  - MODIS
  - Fire events
---

# Global Fire Atlas

Individual fire size, duration, daily expansion, speed and direction derived from MODIS burned area.

[:lucide-download: Access data](https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1642){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://doi.org/10.3334/ORNLDAAC/1642){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NASA ORNL DAAC (CMS) |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 2003 to 2016 |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 500 m (annual grids), 0.25 degrees (monthly) |
| :lucide-file:{ title="File and service formats" } Format | GeoTIFF, Shapefile |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | NASA open data |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Static |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-12 |

!!! warning "Caveat"

    Fires smaller than 21 ha are not included. Direction is only given for multiday fires. The ORNL release covers 2003 to 2016. A Zenodo update (v20250411) moves to MODIS Collection 6.1 and redefines fire seasons. Its year range was not confirmed here.

## Related datasets

- [MODIS MCD64A1 Burned Area](../perimeters/mcd64a1.md)
- [FIRED](../fire-behavior/fired.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "Global Fire Atlas", "description": "Individual fire size, duration, daily expansion, speed and direction derived from MODIS burned area.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fire-behavior/global-fire-atlas/", "creator": {"@type": "Organization", "name": "NASA ORNL DAAC (CMS)"}, "spatialCoverage": "Global", "temporalCoverage": "2003 to 2016", "keywords": ["Global", "Bulk download", "GeoTIFF", "Shapefile", "NASA open data", "Static", "500 m", "MODIS", "Fire events"], "license": "NASA open data", "sameAs": "https://doi.org/10.3334/ORNLDAAC/1642", "distribution": [{"@type": "DataDownload", "contentUrl": "https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1642", "encodingFormat": "GeoTIFF"}, {"@type": "DataDownload", "contentUrl": "https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=1642", "encodingFormat": "Shapefile"}]}</script>

[:lucide-arrow-left: Back to Fire behavior & spread](index.md){ .md-button }
