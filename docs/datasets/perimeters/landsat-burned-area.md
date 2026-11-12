---
title: "USGS Landsat Burned Area (Collection 2 Level-3)"
icon: lucide/flame
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/perimeters.yml
tags:
  - United States
  - Bulk download
  - GeoTIFF
  - Public domain
  - 30 m
  - Ongoing
  - Landsat
  - Burned area
---

# USGS Landsat Burned Area (Collection 2 Level-3)

Scene-level burn classification and burn probability rasters from Landsat 4 to 9.

[:lucide-download: Access data](https://www.usgs.gov/landsat-missions/landsat-collection-2-level-3-burned-area-science-product){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-collection-2-level-3-burned-area-ba-science-product){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | USGS EROS |
| :lucide-map:{ title="Geographic extent" } Coverage | Conterminous US |
| :lucide-calendar:{ title="Years covered" } Period | 1984 to present |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 30 m |
| :lucide-file:{ title="File and service formats" } Format | GeoTIFF |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Public domain |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Ongoing; latest data release v5.0 (April 2026) |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-12 |

!!! warning "Caveat"

    Acquisition-based products: each scene gets a burn classification and probability, not a fire perimeter. Order through EarthExplorer. The April 2026 data release (v5.0) covers the conterminous US. Collection 2 ARD exists for Alaska, but I found no Alaska burned-area product.

## Related datasets

- [MTBS](../perimeters/mtbs.md)
- [Southeast FireMap Burned Area](../perimeters/se-firemap.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "USGS Landsat Burned Area (Collection 2 Level-3)", "description": "Scene-level burn classification and burn probability rasters from Landsat 4 to 9.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/perimeters/landsat-burned-area/", "creator": {"@type": "Organization", "name": "USGS EROS"}, "spatialCoverage": "Conterminous US", "temporalCoverage": "1984 to present", "keywords": ["United States", "Bulk download", "GeoTIFF", "Public domain", "30 m", "Ongoing", "Landsat", "Burned area"], "license": "Public domain", "sameAs": "https://www.usgs.gov/centers/eros/science/usgs-eros-archive-landsat-collection-2-level-3-burned-area-ba-science-product", "distribution": [{"@type": "DataDownload", "contentUrl": "https://www.usgs.gov/landsat-missions/landsat-collection-2-level-3-burned-area-science-product", "encodingFormat": "GeoTIFF"}]}</script>

[:lucide-arrow-left: Back to Perimeters & burned area](index.md){ .md-button }
