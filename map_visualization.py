import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

import folium
import branca.colormap as cm
import os
import json
import plot_function

def map_vis(data, year, path = "Plots", key = True):

    data = plot_function.upload_data(data, key)
    # define the color scale (one single year)
    y_year = [data[r][year] for r in data.keys()]
    linear = cm.LinearColormap(
        #['r', 'y', 'g', 'c', 'b', 'm']
        #['red', 'blue'],
        ['green', 'yellow', 'red'],
        vmin=min(y_year), vmax=max(y_year)
    )

    # all the bounds files
    all_geo_json_d = os.listdir("geo_json_it_area/")
    all_geo_json_d_center = os.listdir("geo_json_it_center/")


    it_lat = 42.50
    it_long = 12.50
    my_map = folium.Map(location=[it_lat, it_long], zoom_start=6, tiles="openstreetmap")

    for d in all_geo_json_d:
        geo_json_d = json.load(open("geo_json_it_area/"+d))
        '''every region has multiple information (under geo_json_d["features"]), 
        the first one is always about the region, the other once about specific cities in it'''
        globals()[d+"_area"] = folium.GeoJson(
            geo_json_d["features"][0],
            style_function=lambda feature: {
            'fillColor': linear(data[feature['properties']['name']][year]),
            'color': 'black',
            'weight': 1,
            'dashArray': '5, 5'
        }
        ).add_to(my_map)


    for d in all_geo_json_d_center:
        geo_json_d = json.load(open("geo_json_it_center/"+d))  
        # to handle Valle d'Aosta
        country_name = (" ").join(geo_json_d["features"][0]['properties']['name'].split("'"))
        globals()[d+"_center"] = folium.Marker(
            [geo_json_d["features"][0]["geometry"]["coordinates"][1], geo_json_d["features"][0]["geometry"]["coordinates"][0]], 
            popup=folium.Popup(country_name+": "+str(data[geo_json_d["features"][0]['properties']['name']][year]))
        ).add_to(my_map)


    colormap = linear
    colormap.caption = 'Resident Foreigners %d' %year
    my_map.add_child(colormap)
    #list_layer = [d+"_center" for d in all_geo_json_d_center] + [d+"_area" for d in all_geo_json_d_center] 
    #folium.FeatureGroup(list_layer).add_to(my_map)

    my_map.save("%s/resident_foreigners_%d.html"%(path, year))