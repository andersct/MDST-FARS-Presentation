## Team Bidiu !

![alt tag](bidiu-car.jpg)

## Introduction

This is the Team Bidiu repo for the MDST-FARS dataset competition.

## Choropleth Maps - Chengyu

### Source Code
/Chengyu/viz/Chengyu.ipynb

### Dependency
Folium is a python wrapper to Leaflet.js which is an extremely powerful tool for creating interactive maps. We found that folium doesn't work well sometimes when installed with Conda, but with its source code stored in /Chengyu/example/folium, we can still use it by adding that directory into the python path.

Also to create the plots we need each county's geographic location data, stored in /Chengyu/viz/us_counties_20m_topo.json

### Example
![alt tag](choropleth.png)

