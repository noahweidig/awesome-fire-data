---
title: "FEDS (Fire Event Data Suite)"
icon: lucide/wind-arrow-down
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fire-behavior.yml
tags:
  - North America
  - API
  - GeoJSON
  - NASA open data
  - Near real time
  - 375 m
  - VIIRS
  - Fire events
  - Active fire
---

# FEDS (Fire Event Data Suite)

Fire event perimeters, new fire pixels and active fire lines updated about every 12 hours from VIIRS 375 m detections.

[:lucide-download: Access data](https://earth-information-system.github.io/fireatlas/docs/data.html){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://earth-information-system.github.io/fireatlas/docs/data_overview.html){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NASA Earth Information System |
| :lucide-map:{ title="Geographic extent" } Coverage | CONUS and Canada (Alaska and Hawaii through FIRMS when released) |
| :lucide-calendar:{ title="Years covered" } Period | Near real time, with static outputs tied to publications |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 375 m detections, vector events |
| :lucide-file:{ title="File and service formats" } Format | GeoJSON, ArcGIS REST service |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | NASA open data |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Near real time |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    Satellite-derived perimeters are less accurate than operational ones. For US incidents the official incident data give a more precise perimeter. Vector output arrives about 4 hours after VIIRS data reach FIRMS.

## Related datasets

- [NASA FIRMS](../active-fire/firms.md)
- [WFIGS Interagency Fire Perimeters](../perimeters/wfigs-perimeters.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "FEDS (Fire Event Data Suite)", "description": "Fire event perimeters, new fire pixels and active fire lines updated about every 12 hours from VIIRS 375 m detections.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fire-behavior/feds/", "creator": {"@type": "Organization", "name": "NASA Earth Information System"}, "spatialCoverage": "CONUS and Canada (Alaska and Hawaii through FIRMS when released)", "temporalCoverage": "Near real time, with static outputs tied to publications", "keywords": ["North America", "API", "GeoJSON", "NASA open data", "Near real time", "375 m", "VIIRS", "Fire events", "Active fire"], "license": "NASA open data", "sameAs": "https://earth-information-system.github.io/fireatlas/docs/data_overview.html", "distribution": [{"@type": "DataDownload", "contentUrl": "https://earth-information-system.github.io/fireatlas/docs/data.html", "encodingFormat": "GeoJSON"}, {"@type": "DataDownload", "contentUrl": "https://earth-information-system.github.io/fireatlas/docs/data.html", "encodingFormat": "ArcGIS REST service"}]}</script>

[:lucide-arrow-left: Back to Fire behavior & spread](index.md){ .md-button }
