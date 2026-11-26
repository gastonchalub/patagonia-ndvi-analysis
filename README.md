# Patagonia NDVI Analysis

Applied remote sensing prototype for vegetation monitoring in southern Patagonia, Argentina, using Sentinel-2 red (B04) and near-infrared (B08) imagery.

## Methodology

NDVI = (NIR - Red) / (NIR + Red). The Python utility computes a float32 NDVI GeoTIFF from aligned, cloud-masked surface reflectance bands and preserves georeferencing. QGIS can be used to inspect and classify the output.

## Earlier experiment

The earlier QGIS classification produced 167,605, 39,327, 8,690 and 564 pixels in classes 1–4 respectively. These counts were recovered from project notes, not independently verified against the original raster. Class thresholds and acquisition metadata were not recovered; no ecological meaning is assigned to these class IDs here.

## Usage

Install requirements, prepare co-registered B04 and B08 reflectance rasters, mask clouds and invalid pixels, then run:

```bash
python src/ndvi.py B04.tif B08.tif ndvi.tif
```

Use physical reflectance values, applying product-specific scale and offset before running. Inputs must share CRS, transform and dimensions. The utility does not perform atmospheric correction, cloud detection or reprojection.

## Limitations

NDVI is a vegetation greenness proxy, not a direct measure of biomass, forage quality or carrying capacity. Field calibration and seasonal comparisons are necessary. Original imagery, property boundaries and classified raster are not included. Code is reconstructed and not yet tested on the original imagery.

## Historical monitoring — V2

The [Colab notebook](notebooks/Pastizales_Rio_Belgrano_V2.ipynb) implements local historical NDVI quartiles and pixel-level anomalies using Google Earth Engine. See the [pilot results and limitations](results/v2-summary.md) for January 2026 versus January 2018–2025. The notebook was run in Colab; the comparable coverage was 49.33%. Run with your own Earth Engine project and classified input raster. Exact property geometry and raster outputs remain excluded from the public repository.
