---
title: "MODIS MCD64A1 Burned Area"
icon: lucide/satellite
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/perimeters.yml
tags:
  - Global
  - Bulk download
  - API
  - HDF
  - NASA open data
  - Monthly
  - 500 m
  - Monthly steps
  - GeoTIFF
  - MODIS
  - Burned area
---

# MODIS MCD64A1 Burned Area

Global monthly burned-area product with burn date, from MODIS surface reflectance.

[:lucide-download: Access data](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NASA LP DAAC |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 2000 to present |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 500 m |
| :lucide-file:{ title="File and service formats" } Format | HDF4, GeoTIFF |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | NASA open data |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Monthly |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-12 |

!!! warning "Caveat"

    NASA plans to stop Terra MODIS science data collection in February 2027 and Aqua in September 2027 (LAADS DAAC). Earthdata describes shutdown as beginning in late 2026 to early 2027, with both orbits drifting. VNP64A1 is the VIIRS continuity product, but see its caveat on S-NPP.

## Related datasets

- [VIIRS VNP64A1 Burned Area](../perimeters/vnp64a1.md)
- [ESA Fire_cci MODIS Burned Area](../perimeters/fire-cci51.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "MODIS MCD64A1 Burned Area", "description": "Global monthly burned-area product with burn date, from MODIS surface reflectance.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/perimeters/mcd64a1/", "creator": {"@type": "Organization", "name": "NASA LP DAAC"}, "spatialCoverage": "Global", "temporalCoverage": "2000 to present", "keywords": ["Global", "Bulk download", "API", "HDF", "NASA open data", "Monthly", "500 m", "Monthly steps", "GeoTIFF", "MODIS", "Burned area"], "license": "NASA open data", "sameAs": "https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061", "distribution": [{"@type": "DataDownload", "contentUrl": "https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061", "encodingFormat": "HDF4"}, {"@type": "DataDownload", "contentUrl": "https://www.earthdata.nasa.gov/data/catalog/lpcloud-mcd64a1-061", "encodingFormat": "GeoTIFF"}]}</script>

[:lucide-arrow-left: Back to Perimeters & burned area](index.md){ .md-button }
