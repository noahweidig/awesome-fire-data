---
icon: lucide/triangle
---

# Fire triangles

Three triangles describe fire at three scales. Each has three corners, and removing or changing one corner changes the fire at that scale. The multi-scale framing is attributed to [Moritz et al. (2005)](https://doi.org/10.1073/pnas.0508985102){ title="Wildfires, complexity, and highly optimized tolerance. PNAS 102(50), 17912-17917" } and illustrated in a [USGS graphic](https://www.usgs.gov/media/images/multi-scale-fire-triangle-fire-growth-and-complexity-simplified){ title="Multi-scale fire triangle" }.

<div class="fire-triangles" markdown>

<div class="ft-card ft-combustion" markdown>

### :lucide-flame: Combustion triangle

<p class="ft-scale">Scale: a flame</p>

<div class="ft-tri" role="img" aria-label="Combustion triangle with heat, oxygen and fuel at the corners" markdown>
<div class="ft-shape"></div>
<div class="ft-core" markdown>:lucide-flame: Burning</div>
<div class="ft-v ft-top c-heat" markdown>:lucide-thermometer-sun: Heat</div>
<div class="ft-v ft-right c-oxygen" markdown>:lucide-wind: Oxygen</div>
<div class="ft-v ft-left c-fuel" markdown>:lucide-trees: Fuel</div>
</div>

Fire needs all three at the same place. Remove one and combustion stops.

</div>

<div class="ft-card ft-behavior" markdown>

### :lucide-activity: Fire behavior triangle

<p class="ft-scale">Scale: a burning fire, minutes to days</p>

<div class="ft-tri" role="img" aria-label="Fire behavior triangle with fuel, weather and topography at the corners" markdown>
<div class="ft-shape"></div>
<div class="ft-core" markdown>:lucide-gauge: Spread and intensity</div>
<div class="ft-v ft-top c-fuel" markdown>:lucide-trees: Fuel</div>
<div class="ft-v ft-right c-weather" markdown>:lucide-cloud-sun: Weather</div>
<div class="ft-v ft-left c-topo" markdown>:lucide-mountain: Topography</div>
</div>

Once a fire starts, these three set how fast it spreads and how intense it is.

</div>

<div class="ft-card ft-regime" markdown>

### :lucide-calendar-clock: Fire regime triangle

<p class="ft-scale">Scale: a landscape, years to centuries</p>

<div class="ft-tri" role="img" aria-label="Fire regime triangle with ignition, climate and vegetation at the corners" markdown>
<div class="ft-shape"></div>
<div class="ft-core" markdown>:lucide-calendar-clock: Fire regime</div>
<div class="ft-v ft-top c-ignition" markdown>:lucide-zap: Ignition</div>
<div class="ft-v ft-right c-climate" markdown>:lucide-thermometer-sun: Climate</div>
<div class="ft-v ft-left c-veg" markdown>:lucide-sprout: Vegetation</div>
</div>

Over decades these three decide how often fires occur, how large they get and how severe they are.

</div>

</div>

## Data for each corner

| Triangle | Corner | Datasets |
| --- | --- | --- |
| Fire behavior | :lucide-trees: Fuel | [LANDFIRE](../datasets/fuels-terrain/landfire.md), [TreeMap](../datasets/fuels-terrain/treemap.md), [RAP](../datasets/fuels-terrain/rap.md) |
| Fire behavior | :lucide-cloud-sun: Weather | [gridMET](../datasets/weather-danger/gridmet.md), [HRRR](../datasets/weather-danger/hrrr.md) |
| Fire behavior | :lucide-mountain: Topography | [USGS 3DEP](../datasets/fuels-terrain/usgs-3dep.md) |
| Fire regime | :lucide-zap: Ignition | [GOES GLM](../datasets/lightning/goes-glm.md), [FPA-FOD](../datasets/occurrence/fpa-fod.md) |
| Fire regime | :lucide-thermometer-sun: Climate | [PRISM](../datasets/weather-danger/prism.md), [ERA5-Land](../datasets/weather-danger/era5-land.md) |
| Fire regime | :lucide-sprout: Vegetation | [LCMS](../datasets/fuels-terrain/lcms.md), [LCMAP](../datasets/fuels-terrain/lcmap.md) |

The combustion triangle is chemistry at one point in space, so no dataset maps it directly. To model fire behavior with these inputs, see [Fire behavior software](software-and-models.md).
