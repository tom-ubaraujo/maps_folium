import folium
import pandas as pd 

#Load data of volcanos/maps
data = pd.read_csv("Data/Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']

#creating base map
map = folium.Map(location=[37.296933,-121.9574983], zoom_start = 8)

for lat, lon, elevation in zip(lat, lon, elevation):
    #add markers
    folium.Marker(location = [lat,lon], popup = str(elevation) + 'm', icon = folium.Icon(color = 'red')).add_to(map)

#saving the map
map.save("base_map.html")

