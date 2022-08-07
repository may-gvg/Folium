from flask import Flask
import json

import folium

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (45.27416700, -66.05863300)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    f = open('stops_202203021451.json')
    data = json.load(f)
    x = 0
    for i in data['stops']:

        location = i['stop_lat'], i['stop_lon']
        stop_name = i['stop_name']
        folium.Marker(location=location,
                      popup=stop_name,
                      tooltip='Click for more information!').add_to(folium_map)

        if x > 0:
            end = (i['stop_lat'], i['stop_lon'])
        if x > 0:
            loc = [start, end]

        start = (i['stop_lat'], i['stop_lon'])
        x += 1



    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=False)
