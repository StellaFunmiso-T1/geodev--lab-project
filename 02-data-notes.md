# Data notes

**Week 2 deliverable.** 
GeoDev Lab Africa, Cohort One. Author: Stella Taiwo

What I downloaded, where it came from, what is in it, and what is wrong with it.

## **Summary**
|Dataset|Type|Retrieved|Status|
|---|---|---|---|
|Nigeria LGA Level Data|Vector (polygon)|13/09/2026|OK|
|Health Facilities| Vector (points)|13/09/2026|OK|
|Road and Transport network|Vector (Lines)|12/09/2026|OK|
|Population count|Raster (GeoTIFF)|17/09/2026|OK|
|DEM|Raster (GeoTIFF)|17/09/2026|OK|

### **1. Nigeria LGA Level Data**

- Source: https://data.grid3.org
- Retrieved: 13/9/2026
- File: GeoDEVLab/my-project/Data/raw/NGA_LGA_Boundaries_2_2609687066015738692\grid3_nga_boundary_vacclgas.shp
- Format: Shapefile
- Geometry type: Polygon (MultiPolygon)
- Feature count: 774
- CRS as downloaded: EPSG:4326-WGS 84

**Key columns**

|Column|What it holds|Nulls|
|---|---|---|
|lganame|Name of the LGA|0|
|lgacode|LGA code|0|
|statename|Name of each state in Nigeria|0|
|statecode|State code (text)|0|
|globalid, uniq_id, timestamp,editor, source, amapcode|Metadata fields|0|

**What I noticed**

There are 774 features (polygons) in the datasets. The dataset is a multipolygon and each polygon depicts the extent and shape of each Local Government area in Nigeria. No nulls found acroos the attributes of the data ans it covers and identifies the study area.

### **2. Health Facilities Data**

- Source: https://data.grid3.org
- Retrieved: 13/9/2026
- File: GeoDEVLab/my-project/Data/raw/GRID3_NGA_health_facility_v3_0_7942856774494319084\main_GRID3_NGA_health_facilities_v3_0.shp
- Format: Shapefile
- Geometry type: Point
- Feature count: 41,778
- CRS as downloaded: EPSG:4326-WGS 84

**Key columns**

|Column|What it holds|Nulls|
|---|---|---|
|latitude|The latitudinal coordinate of the location each Health Facilities|0|0|
|longitude|The longitudinal coordinate of the location each Health Facilities|0|
|state_stan|Name of each state in Nigeria|0|
|lga_standa|State code (text)|0|
|ward_stand|Ward name|0|
|facility_n|Name of the Health Facility|0|
|settlement|Name of Settlment close to the Health Facility|40,039|
|facility_l|Category of the Health Facility(Primary, Secondary, Tertiary or Unknown)|7,524|
|facility_t|The type of Health facility|3,031|
|facility_o|Facility ownership (Private or Public)|2,673|
|facility_1||11,584|
|functional|The working condition of each facility|2,673|
|alt_name|the alternative name of the feature|22,698|
|sett_ext_t||2,702|
|uniqueid, country, iso,ward_in_gr, date_creat, input_data, input_da_1, nhfr_facil, gps_accura, sett_ext_d, dist_ward_, flag1, flag2, flag3, flag4, flag5, flag6, issues, flag_count -there are null data in alt_n, settlement, facility_l, facility_t, facility_o, facility_1, functional, date_creat, nhfr_facil, issues|Metadata|varies based on each column|

**What I noticed**

The dataset has point geometry and each point is the location of each Health Facilities in Nigeria. Quite a number of null attribte were in the data.

In my study area,there are 36 health Facilities.3 of the Health facilities are not functional, 20 are functional,the working state or condition of 9 of the health facilities are unknown and 4 of the Health facilities recorded functionality are NULL.


### **3. Road and Transport network**

- Source: https://www.openstreetmap.org (extracted via QuickOSM plugin in QGIS)
- Retrieved: 12/09/2026
- File: GeoDEVLab/my-project/Data/raw/Highway_AtibaLGA.gpkg
- Format: Geopackage
- Geometry type: Polygon (MultilineString)
- Feature count: 1276
- CRS as downloaded: EPSG:4326-WGS 84

|Column|What it holds|Nulls|
|---|---|---|
highway|The classification of roads within the study area (construction, motorway, path, resiential, trunk, secondary, tertairy, track and others)|0|
|Surface|decsribes the road surface material|1,101|
|fid, full_id, osm_id, osm_type|metadata|0|
|Constructi, tunnel, motor_vehi and others|OSM tag fields|varies based on column|

**What I noticed**
The roads are of different classes and there are quite a number of null in the attribute table.

### **3. Population count**

- Source: hub.worldpop.org
- Retrieved: 17/09/2026
- File: GeoDEVLab/my-project/Data/raw/nga_pop_2026_CN_1km_R2025A_UA_v1.tif"
- Format: GeoTIFF
- Resolution: 1km
- CRS as downloaded: EPSG:4326-WGS 84

**What I noticed**
There are cells with No Data values and they are found to be areas with no visible settlemnt when compared with Google satellite imagery. 

### **4. DEM**

- Source:https://portal.opentopography.org
- Retrieved: 17/09/2026
- File: GeoDEVLab/my-project/Data/raw/output_hh.tif"
- Format: GeoTIFF
- Resolution:30m
- CRS as downloaded: EPSG:4326-WGS 84

**What I noticed**
There are no cells with No Data values and the downloaded raster dat extends beyond my study area which will be subsequently clipped.

### Cross-cutting problems

**Coordinate reference system:** the datasets arrived in a geographic coordinate system and needs to be reprojected before spatial calculations or analysis can be performed.All needed reprojection to a projected coordinate system will be addressed in Week 3.

**Missing attributes:** High null rates in the facility functional status (13 missing/unknown) and road surface types (1,101 missing) create data gaps. This requires running analysis scenarios based on verified functional facilities and estimating travel speeds via road classification rather than surface type

**Status:** Week 2 complete. Reprojection and quality checks in Week 3, see [03-data-preparation.md](C:\Users\HP\Documents\GeoDEVLab\my-project\03-data-preparation.md)