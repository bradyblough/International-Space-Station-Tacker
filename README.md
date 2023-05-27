# ISS Tracker

This Python script utilizes the Open Notify API to track the International Space Station (ISS) and generate a map displaying its current location. The map is created using the Folium library and saved as an HTML file that can be opened in a web browser.

## Prerequisites

Before running the script, ensure that you have the following requirements:

- Python 3.x installed on your system.
- The `requests` library installed. You can install it using `pip install requests`.
- The `json` library, which comes pre-installed with Python.
- The `folium` library installed. You can install it using `pip install folium`.

## Usage

1. Import the necessary libraries at the beginning of your Python script:

```python
import requests
import json
import folium
```

2. Use the Open Notify API to fetch the latitude and longitude of the ISS:

```python
api = requests.get('http://api.open-notify.org/iss-now.json')
data = api.text
parse_json = json.loads(data)
position = parse_json['iss_position']
longitude = position["longitude"]
latitude = position["latitude"]
```

3. Create a map using the obtained latitude and longitude:

```python
m = folium.Map(location=[latitude, longitude], zoom_start=2.5, min_zoom=2.5, max_zoom=5,
               tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
               attr='Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, '
                    'METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012')
```

4. Add a marker to the map representing the ISS:

```python
tooltip_ISS = "International Space Station"
marker = folium.Marker(
        location=[latitude, longitude],
        tooltip=tooltip_ISS,
        icon=folium.Icon(color='red', icon_color='white', icon='info-sign'))
marker.add_to(m)
```

5. Save the map as an HTML file:

```python
m.save('iss_tracker.html')
```

## Running the Script

To run the script and generate the ISS tracker map, follow these steps:

1. Save the script to a Python file, e.g., `iss_tracker.py`.
2. Open a command prompt or terminal.
3. Navigate to the directory where the Python file is located.
4. Run the script using the command `python iss_tracker.py`.
5. The script will fetch the ISS's current location, generate the map, and save it as `iss_tracker.html` in the same directory.
6. Open `iss_tracker.html` in a web browser to view the ISS tracker map.

Please note that the ISS's location is continuously changing, so each time you run the script, a new map will be generated with the updated location. Therefore, the html file is best run in something like live server, which will constantly save and update.

Enjoy tracking the International Space Station!
