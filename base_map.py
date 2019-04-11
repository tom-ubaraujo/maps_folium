import folium
from folium.plugins import MarkerCluster
import pandas as pd 

#load data of volcanos/maps
data = pd.read_csv("Volcanoes_USA.csv")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#creating base map at this location
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 5, tiles = "CartoDB dark_matter")

#creating cluster
marker_cluster = MarkerCluster().add_to(map)

#defining the, arker color by the elevation
def vulc_color(elevation):
    if elevation < 1000:
        return "green"
    elif elevation >= 1000 and elevation <= 3000:
        return "orange"
    else:
        return "red"

for lat, lon, elevation in zip(lat, lon, elevation):
    #add markers
    folium.CircleMarker(location = [lat,lon], radius = 9, popup = str(elevation)+'m', fill_color = vulc_color(elevation), color = "gray", fill_opacity = 0.9).add_to(marker_cluster)

#saving the map
map.save("base_map.html")
