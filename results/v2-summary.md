# Historical NDVI pilot V2 — Santa Cruz

January 2026 compared with January 2018–2025. Sentinel-2 SR Harmonized, Cloud Score+ >= 0.60, SCL classes 4, 5 and 7, minimum three observations per annual composite and six historical years per pixel. UTM 19S, 10 m grid. The original raster provides the study mask.

## Results

Total study area: 1,211.89 ha. Comparable area: 597.79 ha (49.33%); excluded: 614.10 ha. Spatial historical NDVI quartiles: 0.09701803, 0.10725291, 0.12593123.

| January 2026 relative to pixel-specific historical interquartile range | ha | % comparable area |
|---|---:|---:|
| Below | 7.12 | 1.19 |
| Within | 45.02 | 7.53 |
| Above | 545.65 | 91.28 |

Source: exported V2 CSV tables and methodology.txt from the Colab run. Percentages above use comparable area, not total field area. No all-year common-pixel time series was available. Results cannot be generalized to the excluded area. Quartiles and anomalies are exploratory greenness metrics, not validated forage classes, biomass, degradation or carrying capacity estimates.

## Next steps

Evaluate summer composites, historical coverage sensitivity, SAVI and NDMI, and validate against field observations. The exact property raster and georeferenced outputs are not published in this public repository.
