---
icon: lucide/file
---

# Data formats

| Format | Type | Typical use | Read with |
| --- | --- | --- | --- |
| GeoTIFF | Raster | Fuel layers, burn severity | rasterio, GDAL |
| NetCDF | Multi-dimensional array | Gridded weather, emissions | xarray |
| GRIB | Multi-dimensional array | Reanalysis, forecasts | xarray with cfgrib |
| HDF | Multi-dimensional array | MODIS products, GFED | GDAL, h5py |
| Shapefile | Vector | Perimeters, detections | geopandas |
| GeoJSON | Vector | Web services, small extracts | geopandas |
| CSV | Table | Point detections, tabular stats | pandas |
| TFRecord | Tensor records | Machine learning inputs | TensorFlow |
