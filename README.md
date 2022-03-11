# DataAnalyze

## 1. Introduction
__This script is used for location-based dataset analysis and processing.__  
__We have collected four dataset, AIS data from https://marinecadastre.gov/ and check-in 
 data from https://snap.stanford.edu/.__

## 2. Demo

### 2.1 AIS dataset
|   MMSI   | BaseDateTime  | LAT | LON | SOG | COG | Heading|
|:----:|  :----:  | :----:  | :----: |:----:|:----:|:----:|
| 367396710 | 2021-01-01T00:00:53  |37.79217 | -122.28554 |0.1 |341.9 |270|
| 367396710 |2021-01-01T00:08:13   | 37.79218 |-122.28555 | 0.1  |121.7 |266|
| 367396710 | 2020-01-06T15:49:46  | 37.81316 |-122.33117| 3.8  | 248.9 |60|

### 2.2 Check-in dataset
|   User   | Check-in time  | Latitude | Longitude | Location id|
|:----:|  :----:  | :----:  | :----: |:----:|
| 1922 | 2010-10-21T02:12:25Z  |32.8687665333 | -97.2460158833 |617335|
| 1922 |2010-10-21T02:06:53Z   |32.8555987238 |-97.2382092476 | 235850|
| 1922| 2010-10-12T00:26:46Z   | 32.9543800667 |-97.0039908333 | 899984|

## 3. Visualization
![demo1](https://github.com/AmazingCY/DataAnalyze/blob/main/visualization/demo1.JPG)
![demo2](https://github.com/AmazingCY/DataAnalyze/blob/main/visualization/demo2.JPG)

## 4. Requirement
 __Python 1.5  
     Folium 0.12.1  
     numpy 1.18.1__
