---
title: "RAWS (Remote Automatic Weather Stations)"
icon: lucide/thermometer-sun
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/weather-danger.yml
tags:
  - United States
  - Tabular
  - Continuous
---

# RAWS (Remote Automatic Weather Stations)

Hourly fire weather observations from interagency stations, archived by the Western Regional Climate Center.

[:lucide-download: Access data](https://raws.dri.edu/){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://raws.dri.edu/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | Western Regional Climate Center (Desert Research Institute) for NWCG agencies |
| :lucide-map:{ title="Geographic extent" } Coverage | United States |
| :lucide-calendar:{ title="Years covered" } Period | Varies by station |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Station |
| :lucide-file:{ title="File and service formats" } Format | Tabular web download |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | See WRCC terms |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Continuous |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-09 |

!!! warning "Caveat"

    Public data are not quality controlled. A 2025 mailing-list post quoting WRCC says raw public access is limited to the prior 30 days, with older data on request and possibly for a fee. I could not confirm that on an official page. The R package RAWSmet downloads and parses WRCC data.

## Related datasets

- [gridMET](../weather-danger/gridmet.md)
- [WFAS](../weather-danger/wfas.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "RAWS (Remote Automatic Weather Stations)", "description": "Hourly fire weather observations from interagency stations, archived by the Western Regional Climate Center.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/weather-danger/raws/", "creator": {"@type": "Organization", "name": "Western Regional Climate Center (Desert Research Institute) for NWCG agencies"}, "spatialCoverage": "United States", "temporalCoverage": "Varies by station", "keywords": ["United States", "Tabular", "Continuous"], "license": "See WRCC terms", "sameAs": "https://raws.dri.edu/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://raws.dri.edu/", "encodingFormat": "Tabular web download"}]}</script>

[:lucide-arrow-left: Back to Weather, climate & danger](index.md){ .md-button }
