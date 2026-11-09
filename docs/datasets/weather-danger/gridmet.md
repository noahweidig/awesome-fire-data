---
title: "gridMET"
icon: lucide/thermometer-sun
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/weather-danger.yml
tags:
  - United States
  - API
  - Bulk download
  - NetCDF
  - Public domain
  - Daily
  - 4 km
---

# gridMET

Daily gridded surface meteorology, fuel moisture and fire danger indices for the contiguous US.

[:lucide-download: Access data](https://www.climatologylab.org/gridmet.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://www.climatologylab.org/gridmet.html){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | University of Idaho / Climatology Lab |
| :lucide-map:{ title="Geographic extent" } Coverage | CONUS |
| :lucide-calendar:{ title="Years covered" } Period | 1979 to present |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 4 km |
| :lucide-file:{ title="File and service formats" } Format | NetCDF |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Public domain |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Daily |

## Quick start

=== "Earth Engine (Python)"

    ```python
    import ee
    ee.Initialize()
    erc = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET").filterDate("2024-07-01", "2024-07-08").select("erc")
    ```


<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "gridMET", "description": "Daily gridded surface meteorology, fuel moisture and fire danger indices for the contiguous US.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/weather-danger/gridmet/", "creator": {"@type": "Organization", "name": "University of Idaho / Climatology Lab"}, "spatialCoverage": "CONUS", "temporalCoverage": "1979 to present", "keywords": ["United States", "API", "Bulk download", "NetCDF", "Public domain", "Daily", "4 km"], "license": "Public domain", "sameAs": "https://www.climatologylab.org/gridmet.html", "distribution": [{"@type": "DataDownload", "contentUrl": "https://www.climatologylab.org/gridmet.html", "encodingFormat": "NetCDF"}]}</script>

[:lucide-arrow-left: Back to Weather, climate & danger](index.md){ .md-button }
