# Spatial analysis

**Week 4 deliverable.** GeoDev Lab Africa, Cohort One. Author: Stella Taiwo

One spatial operation, run on my own data, answering part of my own question.


## 1. The operation chosen

Network Service Area and Spatial Difference.

This is to identify communities located farther than the WHO 5km standard from a functional health facility. A standard circular buffer assumes people can fly; it ignores the reality of road layouts and physical terrain. By calculating a 5,000-meter service area along the OSM road grid from each active clinic, and then buffering those lines into a catchment polygon, the model creates a realistic travel boundary. Subtracting this served boundary from the Atiba LGA boundary explicitly isolates the underserved geographic areas (healthcare deserts).

## 2. Inputs

| Layer | Source | Features | CRS |
| :--- | :--- | :--- | :--- |
|AtibaLGA_UTM31|GRID3LGA boundaries, clipped to Atiba| 1 | EPSG:32631 |
|Functional_Facilities| GRID3 health facilities, clipped and filtered to active clinics |20|EPSG:32631|
|Highway_in_AtibaLGA_UTM31| OSM roads, reprojected and clipped | 1,276 | EPSG:32631 |
|PopulationCount_AtibaLGA_UTM31| WorldPop raster, reprojected and resampled|Raster| EPSG:32631 |
|Settlement_extent_AtibaLGA_UTM31|GRID3 NGA Settlemnt extent|1,593| EPSG:32631 

All vector and raster layers were confirmed in a projected CRS (EPSG:32631) before running the operation, as stated in the Week 3: distance in degrees is meaningless.

## 3. What I expected

A single polygon output representing all landmass in Atiba LGA located more than 5km (by road) from a functional health facility. Using zonal statistics, this polygon would carry a calculated sum of the population living within it, quantifying the exact human impact of the healthcare deficit.

## 4. Running it

**Step A: Service Area Generation**
Tool: Service area (from layer)
Input network: Highway_in_AtibaLGA_UTM31
Start points:Functional_Facilities
Travel distance: 5000 meters

**Step B: Polygon Conversion**
Tool: Buffer (with Dissolve enabled)
Input: Network lines from Step A
Distance: 500 meters

**Step C: Isolating Underserved**
Tool: Select by Location (disjoint)
Input layer:AtibaLGA_UTM31
Overlay layer: Served Catchment Polygon (from Step B)

## 5. Checking the result in four ways

1. **Map:** The Underserved areas output sat perfectly within the Atiba LGA boundary. Visual inspection confirmed that no functional facilities were located inside the resulting desert polygons.

2. **Attribute table row count:** Based on the output

3. **One feature by hand:** Picked a random road segment inside the resulting desert polygon and used the QGIS Measure tool to trace it back to the nearest facility. The distance exceeded 5,000 meters, confirming the tool cut off the catchment at the correct threshold.

4. **Empty geometry:** Checked the output layer. Geometry was valid and successfully generated.

## 6. The analysis-ready output

**File:**
- Data\Processed\Catchment_Area_Polygon_Clipped.gpkg"
- Data\Processed\Underserved_communities_UTM31.gpkg"
- Format:** GeoPackage (Polygon)
- CRS:EPSG:32631
- Features: 
- Key field: pop_sum (Total population living outside the 5km network catchment, generated via Zonal Statistics against the WorldPop raster).

## 7. Result

- Total Underserved Population: 2403957.091

- Percentage of LGA:13038.80301/27792.86153 * 100 = 46.9%

- By defining access via road networks rather than straight lines, the model reveals that a significant portion of Atiba's rural periphery exists entirely outside acceptable healthcare travel thresholds.

## 8. Map

The final layout overlays the Served_Catchment_Area against the Underserved_Deserts 
 Functional facilities are marked with prominent cross icons. This visual representation communicates to decision makers where Functional Facilities are located and where they are required.
 
 Exported as a print layout with map, legend, title, and scale bar.