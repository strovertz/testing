import folium

def add_polygon_to_map(map_obj, coordinates, popup_text='', color='red', fill_color='red', fill_opacity=0.5):
    folium.Polygon(
        locations=coordinates,
        popup=popup_text,
        color=color,
        fill=True,
        fill_opacity=fill_opacity,
        fill_color=fill_color
    ).add_to(map_obj)
