---
title: "HRRR-Smoke"
icon: lucide/wind
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/smoke-emissions.yml
tags:
  - United States
  - Cloud bucket
  - GRIB
  - Public domain
  - Hourly
  - 3 km
  - Hourly steps
  - Smoke
  - Forecast
---

# HRRR-Smoke

Hourly smoke forecasts from the HRRR model, run with satellite fire radiative power as the emissions source.

[:lucide-download: Access data](https://registry.opendata.aws/noaa-hrrr-pds/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://rapidrefresh.noaa.gov/hrrr/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NOAA GSL and NCEP |
| :lucide-map:{ title="Geographic extent" } Coverage | Conterminous US |
| :lucide-calendar:{ title="Years covered" } Period | 2020 to present (operational) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 3 km |
| :lucide-file:{ title="File and service formats" } Format | GRIB |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Public domain |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Hourly |

!!! warning "Caveat"

    Smoke fields are variables inside the HRRR GRIB2 files. A forecast is not an observation.

## Related datasets

- [HRRR](../weather-danger/hrrr.md)
- [NASA FIRMS](../active-fire/firms.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "HRRR-Smoke", "description": "Hourly smoke forecasts from the HRRR model, run with satellite fire radiative power as the emissions source.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/smoke-emissions/hrrr-smoke/", "creator": {"@type": "Organization", "name": "NOAA GSL and NCEP"}, "spatialCoverage": "Conterminous US", "temporalCoverage": "2020 to present (operational)", "keywords": ["United States", "Cloud bucket", "GRIB", "Public domain", "Hourly", "3 km", "Hourly steps", "Smoke", "Forecast"], "license": "Public domain", "sameAs": "https://rapidrefresh.noaa.gov/hrrr/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://registry.opendata.aws/noaa-hrrr-pds/", "encodingFormat": "GRIB"}]}</script>

[:lucide-arrow-left: Back to Smoke, emissions & air quality](index.md){ .md-button }
