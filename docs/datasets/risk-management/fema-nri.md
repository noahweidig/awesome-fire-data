---
title: "FEMA National Risk Index"
icon: lucide/shield-alert
edit_url: https://github.com/noahweidig/awesome-fire-data/edit/main/data/datasets/risk-management.yml
tags:
  - United States
  - Bulk download
  - CSV
  - Shapefile
  - GeoDatabase
  - Periodic
  - See provider
  - Vector
  - Risk
---

# FEMA National Risk Index

Expected annual loss, social vulnerability and community resilience for 18 natural hazards, including wildfire.

[:lucide-download: Access data](https://hazards.fema.gov/nri/data-resources){ .md-button .md-button--primary }
[:lucide-book-open: Documentation](https://hazards.fema.gov/nri/){ .md-button }

## At a glance

| Field | Value |
| --- | --- |
| :lucide-building-2:{ title="Who publishes the data" } Provider | FEMA |
| :lucide-map:{ title="Geographic extent" } Coverage | United States |
| :lucide-calendar:{ title="Years covered" } Period | Periodic releases (latest December 2025, version 1.20.0) |
| :lucide-ruler:{ title="Pixel size, grid spacing or feature type" } Resolution | Census tract and county |
| :lucide-file:{ title="File and service formats" } Format | CSV, Shapefile, GeoDatabase |
| :lucide-scale:{ title="Terms of use. Check the provider before redistributing" } License | See FEMA terms |
| :lucide-refresh-cw:{ title="How often new data is published" } Updates | Periodic |
| :lucide-badge-check:{ title="Date this entry was last checked against the provider" } Last verified | 2026-11-12 |

!!! warning "Caveat"

    The wildfire score comes from a modeled hazard layer. Check the technical documentation before comparing with local risk assessments. In December 2025 FEMA said NRI data moves into the Resilience Analysis and Planning Tool, so links on hazards.fema.gov may change. Confirm the current download location. GAO reports that DHS plans no further routine NRI updates after folding it into RAPT.

## Related datasets

- [CDC/ATSDR Social Vulnerability Index](../social-vulnerability/cdc-svi.md)
- [Wildfire Risk to Communities](../risk-management/wildfire-risk-to-communities.md)
- [Wildfire Hazard Potential](../risk-management/whp.md)

<script type="application/ld+json">{"@context": "https://schema.org/", "@type": "Dataset", "name": "FEMA National Risk Index", "description": "Expected annual loss, social vulnerability and community resilience for 18 natural hazards, including wildfire.", "url": "https://noahweidig.github.io/awesome-fire-data/datasets/risk-management/fema-nri/", "creator": {"@type": "Organization", "name": "FEMA"}, "spatialCoverage": "United States", "temporalCoverage": "Periodic releases (latest December 2025, version 1.20.0)", "keywords": ["United States", "Bulk download", "CSV", "Shapefile", "GeoDatabase", "Periodic", "See provider", "Vector", "Risk"], "license": "See FEMA terms", "sameAs": "https://hazards.fema.gov/nri/", "distribution": [{"@type": "DataDownload", "contentUrl": "https://hazards.fema.gov/nri/data-resources", "encodingFormat": "CSV"}, {"@type": "DataDownload", "contentUrl": "https://hazards.fema.gov/nri/data-resources", "encodingFormat": "Shapefile"}, {"@type": "DataDownload", "contentUrl": "https://hazards.fema.gov/nri/data-resources", "encodingFormat": "GeoDatabase"}]}</script>

[:lucide-arrow-left: Back to Risk, WUI & management](index.md){ .md-button }
