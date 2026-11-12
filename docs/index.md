---
icon: lucide/flame
hide:
  - navigation
  - toc
  - tags
---

<div class="hero" markdown>
<div class="hero-text" markdown>

# Awesome Fire Datasets

A curated catalog of datasets for fire science, management and modeling. Each entry lists provider, coverage, resolution, format, license and a direct link to the data.

[:lucide-database: Browse datasets](datasets/index.md){ .md-button .md-button--primary }
[:lucide-tag: Filter by tag](browse/tags.md){ .md-button }
[:lucide-git-pull-request: Add a dataset](contribute/index.md){ .md-button }

<div class="hero-chips"><span>Perimeters</span><span>Active fire</span><span>Fuels</span><span>Weather</span><span>Smoke</span><span>Risk</span></div>

</div>
<div class="hero-art" aria-hidden="true">
<svg viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
<defs>
<radialGradient id="hg" cx="50%" cy="55%" r="55%"><stop offset="0" stop-color="#ffb300" stop-opacity=".95"/><stop offset=".45" stop-color="#f4511e" stop-opacity=".75"/><stop offset="1" stop-color="#f4511e" stop-opacity="0"/></radialGradient>
<linearGradient id="fl" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#f4511e"/><stop offset="1" stop-color="#ffb300"/></linearGradient>
<pattern id="dots" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.3" fill="currentColor" opacity=".22"/></pattern>
<clipPath id="disc"><circle cx="200" cy="200" r="180"/></clipPath>
</defs>
<circle cx="200" cy="200" r="180" fill="url(#hg)" opacity=".35"/>
<g clip-path="url(#disc)">
<rect width="400" height="400" fill="url(#dots)" style="color:var(--md-default-fg-color)"/>
<g fill="none" stroke="#f4511e" stroke-linejoin="round">
<path d="M70 215C60 150 120 95 190 90c70-5 135 40 140 115 4 70-55 120-125 122C130 329 78 285 70 215Z" stroke-opacity=".22" stroke-width="1.5"/>
<path d="M105 210c-5-55 40-95 95-98 60-3 105 38 108 95 3 58-42 98-100 99-55 1-98-38-103-96Z" stroke-opacity=".4" stroke-width="1.8"/>
<path d="M140 205c-3-38 25-66 62-68 42-2 70 27 71 65 1 40-30 68-70 68-38 0-61-27-63-65Z" stroke-opacity=".65" stroke-width="2"/>
</g>
</g>
<circle cx="200" cy="200" r="180" fill="none" stroke="currentColor" stroke-opacity=".18" style="color:var(--md-default-fg-color)"/>
<ellipse cx="200" cy="200" rx="210" ry="70" fill="none" stroke="#ffb300" stroke-opacity=".5" stroke-dasharray="3 7" transform="rotate(-28 200 200)"/>
<g transform="translate(335 108) rotate(-28)"><rect x="-9" y="-5" width="18" height="10" rx="2" fill="#f4511e"/><rect x="-24" y="-3" width="13" height="6" fill="#ffb300"/><rect x="11" y="-3" width="13" height="6" fill="#ffb300"/></g>
<g fill="#f4511e"><circle cx="150" cy="170" r="4"/><circle cx="250" cy="150" r="3"/><circle cx="275" cy="235" r="4"/><circle cx="165" cy="268" r="3"/><circle cx="118" cy="225" r="3"/><circle cx="232" cy="290" r="2.5"/><circle cx="215" cy="122" r="2.5"/></g>
<g fill="none" stroke="#f4511e" stroke-opacity=".5"><circle cx="150" cy="170" r="9"/><circle cx="275" cy="235" r="9"/><circle cx="250" cy="150" r="7"/></g>
<path d="M200 118c14 28 42 44 42 82 0 28-19 48-42 48s-42-20-42-48c0-18 9-30 18-42 2 14 9 22 16 26-4-26 2-46 8-66Z" fill="url(#fl)"/>
<path d="M200 206c9 14 20 22 20 38 0 14-9 22-20 22s-20-8-20-22c0-10 6-17 12-24 1 7 4 11 8 13-2-12-1-20 0-27Z" fill="#fff" fill-opacity=".85"/>
</svg>
</div>
</div>

## Themes

<!-- BEGIN THEMES -->
<div class="grid cards" markdown>

-   :lucide-flame:{ .lg .middle } __[Perimeters & burned area](datasets/perimeters/index.md)__

    ---

    Mapped fire footprints and burn severity, from agency perimeters to satellite burned-area products.

    13 datasets

    [:lucide-arrow-right: Explore](datasets/perimeters/index.md)

-   :lucide-satellite:{ .lg .middle } __[Active fire & detection](datasets/active-fire/index.md)__

    ---

    Near-real-time hotspots and thermal anomalies from polar and geostationary satellites.

    3 datasets

    [:lucide-arrow-right: Explore](datasets/active-fire/index.md)

-   :lucide-map-pin:{ .lg .middle } __[Occurrence & ignitions](datasets/occurrence/index.md)__

    ---

    Point records of wildfire events, causes, sizes and national statistics.

    3 datasets

    [:lucide-arrow-right: Explore](datasets/occurrence/index.md)

-   :lucide-flame-kindling:{ .lg .middle } __[Prescribed fire & fuel treatments](datasets/prescribed-fire/index.md)__

    ---

    Prescribed burn records, permits, treatment footprints and monitoring. MTBS and WFIGS also contain prescribed fire perimeters.

    5 datasets

    [:lucide-arrow-right: Explore](datasets/prescribed-fire/index.md)

-   :lucide-siren:{ .lg .middle } __[Suppression & resources](datasets/suppression/index.md)__

    ---

    Incident reports, fireline and containment records from firefighting operations.

    2 datasets

    [:lucide-arrow-right: Explore](datasets/suppression/index.md)

-   :lucide-wind-arrow-down:{ .lg .middle } __[Fire behavior & spread](datasets/fire-behavior/index.md)__

    ---

    Individual fire events with daily spread, speed and direction.

    3 datasets

    [:lucide-arrow-right: Explore](datasets/fire-behavior/index.md)

-   :lucide-trees:{ .lg .middle } __[Fuels, vegetation & terrain](datasets/fuels-terrain/index.md)__

    ---

    Fuel models, canopy, land cover and elevation inputs for fire behavior and risk.

    12 datasets

    [:lucide-arrow-right: Explore](datasets/fuels-terrain/index.md)

-   :lucide-thermometer-sun:{ .lg .middle } __[Weather, climate & danger](datasets/weather-danger/index.md)__

    ---

    Gridded weather, drought and fire danger indices, historical and forecast.

    10 datasets

    [:lucide-arrow-right: Explore](datasets/weather-danger/index.md)

-   :lucide-zap:{ .lg .middle } __[Lightning & ignition drivers](datasets/lightning/index.md)__

    ---

    Lightning detections and climatologies for natural ignitions.

    2 datasets

    [:lucide-arrow-right: Explore](datasets/lightning/index.md)

-   :lucide-wind:{ .lg .middle } __[Smoke, emissions & air quality](datasets/smoke-emissions/index.md)__

    ---

    Fire emissions inventories, smoke plumes and air quality observations.

    6 datasets

    [:lucide-arrow-right: Explore](datasets/smoke-emissions/index.md)

-   :lucide-house:{ .lg .middle } __[Impacts & post-fire](datasets/impacts/index.md)__

    ---

    Structure damage, burn severity response, and post-fire hazards such as debris flows.

    4 datasets

    [:lucide-arrow-right: Explore](datasets/impacts/index.md)

-   :lucide-shield-alert:{ .lg .middle } __[Risk, WUI & management](datasets/risk-management/index.md)__

    ---

    Community wildfire risk, wildland-urban interface maps and land management layers.

    5 datasets

    [:lucide-arrow-right: Explore](datasets/risk-management/index.md)

-   :lucide-users:{ .lg .middle } __[Social vulnerability & communities](datasets/social-vulnerability/index.md)__

    ---

    Community vulnerability and national hazard risk indices for fire exposure studies.

    3 datasets

    [:lucide-arrow-right: Explore](datasets/social-vulnerability/index.md)

-   :lucide-map-pinned:{ .lg .middle } __[Boundaries & reference layers](datasets/boundaries/index.md)__

    ---

    Administrative, ecological and protected-area boundaries for joining and summarizing fire data.

    6 datasets

    [:lucide-arrow-right: Explore](datasets/boundaries/index.md)

-   :lucide-brain-circuit:{ .lg .middle } __[Benchmarks & ML-ready](datasets/benchmarks-ml/index.md)__

    ---

    Curated, model-ready datasets for wildfire detection and spread prediction.

    3 datasets

    [:lucide-arrow-right: Explore](datasets/benchmarks-ml/index.md)

-   :lucide-history:{ .lg .middle } __[Paleo & historical](datasets/paleo/index.md)__

    ---

    Charcoal records and tree-ring fire scars for long-term fire history.

    2 datasets

    [:lucide-arrow-right: Explore](datasets/paleo/index.md)

</div>
<!-- END THEMES -->

## Start here

<div class="grid cards" markdown>

-   :lucide-compass:{ .lg .middle } __Not sure what you need?__

    ---

    Match your question to a data type and scale.

    [:lucide-arrow-right: Choosing a dataset](learn/choosing-a-dataset.md)

-   :lucide-table:{ .lg .middle } __See everything at once__

    ---

    One table with coverage, period, resolution and license.

    [:lucide-arrow-right: All datasets](browse/all-datasets.md)

-   :lucide-wrench:{ .lg .middle } __Working with the data__

    ---

    Formats, Python and R libraries, and cloud access.

    [:lucide-arrow-right: Tools and APIs](learn/tools-and-apis.md)

</div>
