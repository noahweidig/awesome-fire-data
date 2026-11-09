---
icon: lucide/compass
---

# Choosing a dataset

| Question | Start with | Theme |
| --- | --- | --- |
| Where is a fire burning right now? | FIRMS, GOES-R, NOAA HMS | [Active fire](../datasets/active-fire/index.md) |
| How big was a past fire and where did it burn? | MTBS, WFIGS, MCD64A1 | [Perimeters](../datasets/perimeters/index.md) |
| How many fires, what caused them? | FPA-FOD, EFFIS | [Occurrence](../datasets/occurrence/index.md) |
| What will burn and how fast? | LANDFIRE, gridMET | [Fuels](../datasets/fuels-terrain/index.md), [Weather](../datasets/weather-danger/index.md) |
| How bad is the smoke? | GFED, GFAS, AirNow | [Smoke](../datasets/smoke-emissions/index.md) |
| Which homes were lost? | CAL FIRE DINS | [Impacts](../datasets/impacts/index.md) |
| Training a model? | WildfireSpreadTS, Sen2Fire | [Benchmarks](../datasets/benchmarks-ml/index.md) |

## Trade-offs to check

- **Latency.** Geostationary data arrives in minutes. Polar-orbiting products take hours. Annual products lag by months.
- **Resolution.** Fine pixels miss nothing small but cover less history. Coarse products suit global trends.
- **Burn definition.** Perimeters, burned-area pixels and burn severity measure different things. Do not mix them without checking.
- **License.** Check terms before redistributing. Entries show the license the provider states.
