---
title: "US Drought Monitor"
icon: lucide/sun
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/weather-danger.yml
tags:
  - United States
  - API
  - Bulk download
  - Shapefile
  - GeoJSON
  - Weekly
---

# US Drought Monitor

Weekly drought category maps for the US, with polygon, grid and statistics downloads.

[:lucide-download: Access data](https://droughtmonitor.unl.edu/DmData/GISData.aspx){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://droughtmonitor.unl.edu/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | National Drought Mitigation Center (University of Nebraska-Lincoln), USDA and NOAA |
| :lucide-map:{ title="Geographic extent" } Coverage | United States |
| :lucide-calendar:{ title="Years covered" } Period | 2000 to present |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Vector (500 m grid also offered) |
| :lucide-file:{ title="File and service formats" } Format | Shapefile, KMZ, GML, GeoJSON, WMS |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | See NDMC terms |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Weekly |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    NDMC says its shapefiles were modified from the originals. Use a vector dataset to match official statistics. Community GeoParquet mirrors exist.

## Related datasets

- [gridMET](../weather-danger/gridmet.md)
- [WFAS](../weather-danger/wfas.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "US Drought Monitor", "description": "Weekly drought category maps for the US, with polygon, grid and statistics downloads.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/weather-danger/us-drought-monitor/", "creator": {"@type": "Organization", "name": "National Drought Mitigation Center (University of Nebraska-Lincoln), USDA and NOAA"}, "spatialCoverage": "United States", "temporalCoverage": "2000 to present", "keywords": ["United States", "API", "Bulk download", "Shapefile", "GeoJSON", "Weekly"], "license": "See NDMC terms", "sameAs": "https://droughtmonitor.unl.edu/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://droughtmonitor.unl.edu/DmData/GISData.aspx", "encodingFormat": "Shapefile"}, {"@type": "DataDownload", "contentUrl": "https://droughtmonitor.unl.edu/DmData/GISData.aspx", "encodingFormat": "KMZ"}, {"@type": "DataDownload", "contentUrl": "https://droughtmonitor.unl.edu/DmData/GISData.aspx", "encodingFormat": "GML"}, {"@type": "DataDownload", "contentUrl": "https://droughtmonitor.unl.edu/DmData/GISData.aspx", "encodingFormat": "GeoJSON"}, {"@type": "DataDownload", "contentUrl": "https://droughtmonitor.unl.edu/DmData/GISData.aspx", "encodingFormat": "WMS"}]}</script>

[:lucide-arrow-left: Back to Weather, climate & danger](index.md){ .md-button }
