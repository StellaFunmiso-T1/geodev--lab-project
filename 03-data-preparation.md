 # Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One. Author: Stella Taiwo

What I reprojected, what I clipped, what I checked, and what I fixed.

## 1. Coordinate system decisions

**Working CRS:** EPSG:32631 (UTM zone 31N)

**Why this one:** Atiba is located in western Nigeria, within UTM zone 31N. The project's core requires the data to be in a projected CRS and EPSG:4326 (geographic, degrees) is unsuitable for this.

|Dataset|CRS as downloaded|CRS after|Operation
|---|---|---|---|
|Nigeria LGA Level Data|EPSG:4326|EPSG:32631|Reprojected|
|Health Facilities|EPSG:4326|EPSG:32631|Reprojected|
|Road and Transport network|EPSG:4326|EPSG:32631|Reprojected|
|Population count|EPSG:4326|EPSG 32631|Reprojected and Resampled
|DEM|EPSG:4326|EPSG 32631|Reprojected and Resampled

Before reprojecting, area calculation was carried out on the LGA boundaries layer in its native EPSG:4326 CRS to confirm the failure mode: this returned a value of 672544957.700 while after it was reprojected a value of 672544957.7107584 sqm (6725.449577107584 sqkm). This is a concern as the source CRS is in EPSG 4326-WGS 84 and approximately same value was returned for the projected CRS.

## 2. Clipping to the study area

- **Boundary used:** Single polygon was exported from GRID3 Nigeria LGA Level Data (Atiba LGA), saved as > Data\Processed\Atiba_LGA.gpkg
- **Features before clipping:** Highway 2,687 (LGA extent from QuickOSM query); Health Facilities 41,778 (nationwide)
- **Features after clipping:** Roads 1276; Health Facilities(36)
- Visual inspection confirmed no clipped features from all the layer fall outside the study area boundary.

## 3. The five quality checks

|Check|Result|Action taken|
|---|---|---|
|Is the CRS what I think it is?|Confirmed, the CRS of all downloaded datasets are in EPSG:4326-WGS 84|Reprojected all layers to EPSG:32631|
|Are there nulls in the fields I need?|	Yes, there are nulls in the fields for Highway attributes (e.g name, surface,motor_vehi, foots); there are null in (facility_n, settlemEnt, functional, sett_ext_t and others); there are no data value cells in the Population count raster|No action has been taken on the Population count data; analysis will be based on verified functional facilities and estimating travel speeds via road classification rather than surface type|
|Are there duplicate features?|There are no duplicate features|No action required|
|Is the geometry valid?|The geometry are valid|No action required|
|Does coverage span the whole study area?|Yes, this was confirmed by comparing visually to Google Satellite imagery|No action required|

## 4. Problems found, and what I did

High null rates in the Health facility functional status (13 missing/unknown) and road surface types (1,101 missing) create data gaps. This requires running analysis scenarios based on verified functional facilities and estimating travel speeds via road classification rather than surface type

## 5. The analysis-ready output
- File: Data\Processed\HealthFacilities_AtibaLGA_UTM31.gpkg, Data\Processed\Highway_in_AtibaLGA_UTM31.gpkg, Data\Processed\AtibaLGA_UTM31.gpkg, Data\Processed\PopulationCount_AtibaLGA_UTM31.tif", Data\Processed\DEM_AtibaLGA_UTM31.tif"
- Format: GeoPackage, GeoTIFF
- CRS: EPSG:32631
- Features: Study area 1; Roads 1276; HealthFacilities 36, Population count, DEM
- Produced by: Manually in QGIS (Reproject Layer, resampled, Clip)
- Status: Week 3 complete. First spatial analysis in Week 4.
