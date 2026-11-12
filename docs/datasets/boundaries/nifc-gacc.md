---
title: "NIFC Geographic Area Coordination Center (GACC) Boundaries"
icon: lucide/map-pinned
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/boundaries.yml
tags:
  - United States
  - API
  - GeoJSON
  - Shapefile
  - Periodic
  - See provider
  - Vector
  - Boundaries
  - Suppression
---

# NIFC Geographic Area Coordination Center (GACC) Boundaries

Polygons of the 10 US geographic areas used to coordinate wildland fire resources and report fire statistics.

[:lucide-download: Access data](https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services/DMP_NationalGACCBoundaries_Public/FeatureServer/0){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://data-nifc.opendata.arcgis.com/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NIFC and National Wildfire Coordinating Group |
| :lucide-map:{ title="Geographic extent" } Coverage | United States |
| :lucide-calendar:{ title="Years covered" } Period | Current boundaries (layer dated 2025-01-13) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Vector |
| :lucide-file:{ title="File and service formats" } Format | Shapefile, GeoJSON, ArcGIS feature service |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | See NIFC Open Data item page |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Periodic |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    The service returns at most 2,000 records per query. A border area between Utah and Colorado changed in September 2024. The list of coordination centers is in the National Interagency Mobilization Guide. A separate simplified copy exists for zooming only, not for mapping.

## Related datasets

- [NIFC Wildfire Statistics](../occurrence/nifc-statistics.md)
- [WFIGS Interagency Fire Perimeters](../perimeters/wfigs-perimeters.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "NIFC Geographic Area Coordination Center (GACC) Boundaries", "description": "Polygons of the 10 US geographic areas used to coordinate wildland fire resources and report fire statistics.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/boundaries/nifc-gacc/", "creator": {"@type": "Organization", "name": "NIFC and National Wildfire Coordinating Group"}, "spatialCoverage": "United States", "temporalCoverage": "Current boundaries (layer dated 2025-01-13)", "keywords": ["United States", "API", "GeoJSON", "Shapefile", "Periodic", "See provider", "Vector", "Boundaries", "Suppression"], "license": "See NIFC Open Data item page", "sameAs": "https://data-nifc.opendata.arcgis.com/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services/DMP_NationalGACCBoundaries_Public/FeatureServer/0", "encodingFormat": "Shapefile"}, {"@type": "DataDownload", "contentUrl": "https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services/DMP_NationalGACCBoundaries_Public/FeatureServer/0", "encodingFormat": "GeoJSON"}, {"@type": "DataDownload", "contentUrl": "https://services3.arcgis.com/T4QMspbfLg3qTGWY/ArcGIS/rest/services/DMP_NationalGACCBoundaries_Public/FeatureServer/0", "encodingFormat": "ArcGIS feature service"}]}</script>

[:lucide-arrow-left: Back to Boundaries & reference layers](index.md){ .md-button }
