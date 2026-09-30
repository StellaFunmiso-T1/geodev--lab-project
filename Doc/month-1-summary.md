# Month 1 summary

**Week 4 deliverable.** GeoDev Lab Africa, Cohort One. Author: Taiwo Stella Oluwafunmiso

## The question
How physically close are communities across Atiba Local Government Area to the nearest health facility, and which community are currently underserved?

## Which operation I ran, and why
A Network Service Area coupled with a Spatial Difference (Select by Location - disjoint) operation.

A standard circular buffer assumes people can travel in straight lines, ignoring the reality of road layouts, unbridged rivers, and physical terrain. By calculating a 5,000-meter service area along the OSM road grid from each active clinic, and then buffering those network lines into a catchment polygon, the model creates a realistic travel boundary. Subtracting this served boundary from the Atiba LGA boundary (and identifying disjoint settlement extents) explicitly isolates the underserved geographic areas, establishing the true healthcare deserts.

Before executing the network analysis, health facilities were filtered to include only those actively providing care, discarding abandoned or unstaffed buildings. All datasets were also reprojected to EPSG:32631 (UTM Zone 31N), as calculating network distances in degrees (EPSG:4326) produces meaningless results.

## What I expected, and what I got
I expected a single polygon output representing all landmass in Atiba LGA located more than 5km (by road) from a functional health facility. By running zonal statistics on this polygon against the WorldPop raster, I expected to extract a calculated sum of the population living within it to quantify the exact human impact.

The operation successfully delivered this. The output sat perfectly within the Atiba LGA boundary, and visual inspection confirmed that no functional facilities were located inside the resulting desert polygons. Manual measurement of random road segments within the desert polygon confirmed distances to the nearest facility exceeded 5,000 meters.

## What surprised me

- The most significant surprises emerged during the data preparation phase, specifically regarding data completeness and the resulting impact on the analysis:
- Out of 36 recorded health facilities in the study area, 3 were explicitly marked non-functional, 9 had an unknown status, and 4 contained null functionality attributes. This required running the model strictly on the 20 verified functional facilities, drastically altering the mapped coverage area.
- The road network data contained severe attribute gaps, with 1,101 out of 1,276 road segments lacking surface material tags (surface = NULL).
- During reprojection checks, calculating the area of the LGA boundary in its native EPSG:4326 CRS returned an almost identical value (~672,544,957 sqm) to the projected EPSG:32631 CRS.

## Result
- Total Underserved Population: 2,403,957.091
- Percentage of LGA Underserved: 46.9% (calculated as 13038.80301 / 27792.86153 * 100)

## What data I still need
While the model effectively maps physical road distances, it relies entirely on road geometry and classification. Because 1,101 road segments lack surface tags, the model cannot distinguish between a paved highway and a degraded dirt track, which severely impacts actual travel time. Future iterations will require comprehensive road surface data or empirical travel-speed surveys to upgrade the model from a distance-based threshold (5km) to a time-based threshold (e.g., a 30-minute drive).