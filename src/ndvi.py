import argparse
import numpy as np
import rasterio

def calculate(red_path, nir_path, output_path):
    with rasterio.open(red_path) as red, rasterio.open(nir_path) as nir:
        if (red.crs, red.transform, red.shape) != (nir.crs, nir.transform, nir.shape):
            raise ValueError("Input rasters must be aligned")
        r = red.read(1, masked=True).astype("float32").filled(np.nan)
        n = nir.read(1, masked=True).astype("float32").filled(np.nan)
        denominator = n + r
        valid = np.isfinite(r) & np.isfinite(n) & (r >= 0) & (n >= 0) & (denominator > 0)
        result = np.full(r.shape, -9999, dtype="float32")
        np.divide(n-r, denominator, out=result, where=valid)
        profile = red.profile.copy()
        profile.update(driver="GTiff", dtype="float32", count=1, nodata=-9999, compress="deflate")
        with rasterio.open(output_path, "w", **profile) as dst:
            dst.write(result, 1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute NDVI from aligned reflectance rasters")
    parser.add_argument("red")
    parser.add_argument("nir")
    parser.add_argument("output")
    args = parser.parse_args()
    calculate(args.red, args.nir, args.output)
