---
title: "NASA FIRMS (Fire Information for Resource Management System)"
icon: lucide/satellite
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/active-fire.yml
tags:
  - Global
  - API
  - Bulk download
  - CSV
  - Shapefile
  - NASA open data
  - Near real time
  - 375 m
---

# NASA FIRMS (Fire Information for Resource Management System)

Near-real-time active fire detections from MODIS and VIIRS, with map, download and API access.

[:lucide-download: Access data](https://firms.modaps.eosdis.nasa.gov/active_fire/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://firms.modaps.eosdis.nasa.gov/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NASA |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | 2000 to present (MODIS), 2012 to present (VIIRS) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 375 m to 1 km |
| :lucide-file:{ title="File and service formats" } Format | CSV, Shapefile, GeoJSON, KML |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | NASA open data |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Near real time |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    MODIS detections depend on Terra and Aqua, which NASA expects to shut down in late 2026 to early 2027. VIIRS detections continue.

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "NASA FIRMS (Fire Information for Resource Management System)", "description": "Near-real-time active fire detections from MODIS and VIIRS, with map, download and API access.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/active-fire/firms/", "creator": {"@type": "Organization", "name": "NASA"}, "spatialCoverage": "Global", "temporalCoverage": "2000 to present (MODIS), 2012 to present (VIIRS)", "keywords": ["Global", "API", "Bulk download", "CSV", "Shapefile", "NASA open data", "Near real time", "375 m"], "license": "NASA open data", "sameAs": "https://firms.modaps.eosdis.nasa.gov/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://firms.modaps.eosdis.nasa.gov/active_fire/", "encodingFormat": "CSV"}, {"@type": "DataDownload", "contentUrl": "https://firms.modaps.eosdis.nasa.gov/active_fire/", "encodingFormat": "Shapefile"}, {"@type": "DataDownload", "contentUrl": "https://firms.modaps.eosdis.nasa.gov/active_fire/", "encodingFormat": "GeoJSON"}, {"@type": "DataDownload", "contentUrl": "https://firms.modaps.eosdis.nasa.gov/active_fire/", "encodingFormat": "KML"}]}</script>

[:lucide-arrow-left: Back to Active fire & detection](index.md){ .md-button }
