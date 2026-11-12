---
title: "HRRR (High-Resolution Rapid Refresh)"
icon: lucide/cloud-lightning
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/weather-danger.yml
tags:
  - United States
  - Cloud bucket
  - GRIB
  - Public domain
  - Hourly
  - 3 km
  - Hourly steps
  - Weather
  - Forecast
---

# HRRR (High-Resolution Rapid Refresh)

Hourly 3 km convection-allowing weather analyses and forecasts, including wind, humidity and temperature.

[:lucide-download: Access data](https://registry.opendata.aws/noaa-hrrr-pds/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://rapidrefresh.noaa.gov/hrrr/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | NOAA NCEP and ESRL/GSL |
| :lucide-map:{ title="Geographic extent" } Coverage | Conterminous US and Alaska |
| :lucide-calendar:{ title="Years covered" } Period | 2014 to present (AWS archive) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | 3 km |
| :lucide-file:{ title="File and service formats" } Format | GRIB |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | Public domain |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Hourly |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    The Herbie Python package simplifies retrieval of individual fields. NOAA says HRRR is not retired with the RRFS v1 implementation. A retirement date has not been announced.

## Quick start

=== "Python"

    ```python
    from herbie import Herbie
    H = Herbie("2024-07-01 12:00", model="hrrr", product="sfc", fxx=0)
    ds = H.xarray("TMP:2 m")
    ```


## Related datasets

- [HRRR-Smoke](../smoke-emissions/hrrr-smoke.md)
- [gridMET](../weather-danger/gridmet.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "HRRR (High-Resolution Rapid Refresh)", "description": "Hourly 3 km convection-allowing weather analyses and forecasts, including wind, humidity and temperature.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/weather-danger/hrrr/", "creator": {"@type": "Organization", "name": "NOAA NCEP and ESRL/GSL"}, "spatialCoverage": "Conterminous US and Alaska", "temporalCoverage": "2014 to present (AWS archive)", "keywords": ["United States", "Cloud bucket", "GRIB", "Public domain", "Hourly", "3 km", "Hourly steps", "Weather", "Forecast"], "license": "Public domain", "sameAs": "https://rapidrefresh.noaa.gov/hrrr/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://registry.opendata.aws/noaa-hrrr-pds/", "encodingFormat": "GRIB"}]}</script>

[:lucide-arrow-left: Back to Weather, climate & danger](index.md){ .md-button }
