# **Project brief**
Week 1 deliverable. GeoDev Lab Africa, Cohort One. Author: Stella Taiwo
## **1. The question**

> #### How physically close are communities across Atiba Local Government Area to the nearest health facility, and which community are currently underserved?

## **2. Why this question?**

#### Atiba LGA holds dense urban neighborhoods near Oyo town and sprawling, sparsely populated rural wards. In emergencies or routine maternal checkups, travel distance directly determines survival.

Before building new facilities or deploying mobile clinics, decision-makers need empirical geographic answers:
- Who lives too far from care?
- Are facilities clustered only in the urban core while rural farming communities are neglected?
- Exactly how many people fall outside acceptable travel limits?


## **3. Study area**

Atiba Local Government Area, Oyo State, Nigeria. Boundary defined by the GRID3 Nigeria Operational LGA Boundaries dataset, filtered to the single LGA.

## **4. What I mean by the terms**

- Spatial Proximity: How close or far a clinic is to where people actually sleep at night, measured along real roads and walking tracks.
- Underserved Location (Healthcare Desert): A populated settlement sitting outside the acceptable travel threshold (e.g., further than a 5 km trip or a 30-minute walk to any clinic).
- Travel Threshold: The "safe limit" cutoff line, if a patient must travel farther than this distance to reach first aid, the system has failed them.
- Functional Facility: A facility that is physically present, open, and actively providing clinical care, as opposed to an abandoned or unstaffed building.

## **5. Datasets**

|SN|Dataset|What it gives me| Source| Format| Size|
|---|---|---|---|---|---|
|1 | Nigeria LGA Level Data|The Administrative boundary to define the extent and shape of study area |https://data.grid3.org|Shapefile |2.62mb|
|2|Health Facilities|The location of captured Health facilities within Nigeria and clipped to define and identify those within the study area |https://data.grid3.org| Shapefile|4.73mb|
|3|Road and Transport network| The network of roads and paths within the study area |OpenStreetMap|Shapefile|399kb |
|4|Population count|The total number of people per grid-pixel in Nigeria to be clipped |hub.worldpop.org|GeoTIFF|4.15MB|
|5|DEM|The elevation model of points or positions within the study area |https://portal.opentopography.org/| GeoTIFF|98.9mb|

## **6. What "done" looks like?**

A geospatial model showing how physically close communities within Atiba Local Government Area are to healthcare services, and isolating exactly which populated areas are geographically underserved


## **7. Known risks**

- Out of the 36 health facilities in Atiba, 3 are non-functional, 9 have unknown status, and 4 have null functionality attributes.

- 1,101 out of 1,276 road segments lack surface material tags (`surface = NULL`)


### Status: Week 1 complete. Data acquisition in Week 2, see [02-data-notes.md](C:\Users\HP\Documents\GeoDEVLab\my-project\02-datanotes.md)


