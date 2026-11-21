---
title: "FireSpread_MedEU"
icon: lucide/wind-arrow-down
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/fire-behavior.yml
tags:
  - Europe
  - Bulk download
  - Shapefile
  - CC BY 4.0
  - Static
  - Vector
  - Fire events
---

# FireSpread_MedEU

Multi-day fire propagation steps for 103 wildfires in the Mediterranean and Europe, mapped from daily Planet imagery.

[:lucide-download: Access data](https://zenodo.org/records/18200075){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://doi.org/10.1038/s41597-026-06965-2){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | Scientific Data authors, Zenodo |
| :lucide-map:{ title="Geographic extent" } Coverage | Mediterranean and Europe |
| :lucide-calendar:{ title="Years covered" } Period | 2017 to 2023 |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Event polygons (from daily Planet imagery) |
| :lucide-file:{ title="File and service formats" } Format | Shapefile |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | CC BY 4.0 |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Static |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-21 |

!!! warning "Caveat"

    320 propagation steps across 103 events, so it is small. Burned areas come from semi-automated NIR thresholding with manual refinement.

## Cite

DOI: [10.5281/zenodo.18200075](https://doi.org/10.5281/zenodo.18200075)

## Related datasets

- [GlobFire](../fire-behavior/globfire.md)
- [FEDS](../fire-behavior/feds.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "FireSpread_MedEU", "description": "Multi-day fire propagation steps for 103 wildfires in the Mediterranean and Europe, mapped from daily Planet imagery.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/fire-behavior/firespread-medeu/", "creator": {"@type": "Organization", "name": "Scientific Data authors, Zenodo"}, "spatialCoverage": "Mediterranean and Europe", "temporalCoverage": "2017 to 2023", "keywords": ["Europe", "Bulk download", "Shapefile", "CC BY 4.0", "Static", "Vector", "Fire events"], "license": "CC BY 4.0", "sameAs": "https://doi.org/10.1038/s41597-026-06965-2", "distribution": [{"@type": "DataDownload", "contentUrl": "https://zenodo.org/records/18200075", "encodingFormat": "Shapefile"}], "identifier": "https://doi.org/10.5281/zenodo.18200075"}</script>

[:lucide-arrow-left: Back to Fire behavior & spread](index.md){ .md-button }
