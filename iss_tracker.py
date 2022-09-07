import requests
import json
import folium
# uses api to get latitude and longitude of ISS
api = requests.get('http://api.open-notify.org/iss-now.json')
data = api.text
parse_json = json.loads(data)
position = parse_json['iss_position']
longitude = position["longitude"]
latitude = position["latitude"]
# Generates a map using api-given latitude and longitude
m = folium.Map(location=[latitude, longitude], zoom_start=2.5, min_zoom=2.5, max_zoom=5,
                   tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
                   attr='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, '
                        'METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012')
tooltip_ISS = "International Space Station"
marker = folium.Marker(
        location=[latitude, longitude],
        tooltip=tooltip_ISS,
        icon=folium.Icon(color='red', icon_color='white', icon='info-sign'))
marker.add_to(m)
# saves to a html file that can be locally rendered in a web browser
m.save('iss_tracker.html')



