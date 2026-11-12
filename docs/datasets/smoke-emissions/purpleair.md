---
title: "PurpleAir"
icon: lucide/gauge
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/smoke-emissions.yml
tags:
  - Global
  - API
  - JSON
  - Custom terms
  - Near real time
  - Point or station
  - Air quality
  - Smoke
---

# PurpleAir

Real-time PM2.5 readings from a crowd-sourced network of low-cost sensors.

[:lucide-download: Access data](https://api.purpleair.com/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://api.purpleair.com/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | PurpleAir, Inc. |
| :lucide-map:{ title="Geographic extent" } Coverage | Global |
| :lucide-calendar:{ title="Years covered" } Period | Continuous |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Sensor points |
| :lucide-file:{ title="File and service formats" } Format | JSON |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | PurpleAir terms of use |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Continuous |

!!! warning "Caveat"

    Needs an API key. Raw PM2.5 reads high in smoke, so apply a correction such as the EPA US-wide one.

## Related datasets

- [EPA AirNow API](../smoke-emissions/airnow.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "PurpleAir", "description": "Real-time PM2.5 readings from a crowd-sourced network of low-cost sensors.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/smoke-emissions/purpleair/", "creator": {"@type": "Organization", "name": "PurpleAir, Inc."}, "spatialCoverage": "Global", "temporalCoverage": "Continuous", "keywords": ["Global", "API", "JSON", "Custom terms", "Near real time", "Point or station", "Air quality", "Smoke"], "license": "PurpleAir terms of use", "sameAs": "https://api.purpleair.com/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://api.purpleair.com/", "encodingFormat": "JSON"}]}</script>

[:lucide-arrow-left: Back to Smoke, emissions & air quality](index.md){ .md-button }
