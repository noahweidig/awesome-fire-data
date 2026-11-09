---
title: "VIIRS VNP64A1 Burned Area"
icon: lucide/satellite
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/perimeters.yml
tags:
  - Global
  - Bulk download
  - API
  - NASA open data
  - Monthly
  - 500 m
---

# VIIRS VNP64A1 Burned Area

Global monthly 500 m burned area with burn date from Suomi NPP VIIRS, designed as the successor to MCD64A1.

[:lucide-download: Access data](https://doi.org/10.5067/VIIRS/VNP64A1.002){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://doi.org/10.5067/VIIRS/VNP64A1.002){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NASA LP DAAC |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 2012 to present |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 500 m |
| :lucide-file:{ title="File and service formats" } Format | HDF5 |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | NASA open data |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Monthly |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    Version 2 was released in October 2024. Uses 750 m VIIRS imagery with 750 m active fire detections. Earth Engine and the DAAC list different end dates, so check current coverage.

## Cite

DOI: [10.5067/VIIRS/VNP64A1.002](https://doi.org/10.5067/VIIRS/VNP64A1.002)

## Related datasets

- [MODIS MCD64A1 Burned Area](../perimeters/mcd64a1.md)
- [ESA Fire_cci MODIS Burned Area](../perimeters/fire-cci51.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "VIIRS VNP64A1 Burned Area", "description": "Global monthly 500 m burned area with burn date from Suomi NPP VIIRS, designed as the successor to MCD64A1.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/perimeters/vnp64a1/", "creator": {"@type": "Organization", "name": "NASA LP DAAC"}, "spatialCoverage": "Global", "temporalCoverage": "2012 to present", "keywords": ["Global", "Bulk download", "API", "NASA open data", "Monthly", "500 m"], "license": "NASA open data", "sameAs": "https://doi.org/10.5067/VIIRS/VNP64A1.002", "distribution": [{"@type": "DataDownload", "contentUrl": "https://doi.org/10.5067/VIIRS/VNP64A1.002", "encodingFormat": "HDF5"}], "identifier": "https://doi.org/10.5067/VIIRS/VNP64A1.002"}</script>

[:lucide-arrow-left: Back to Perimeters & burned area](index.md){ .md-button }
