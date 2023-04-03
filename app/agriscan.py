from libs.map_utils import *
from libs.escalas import *

def get_map_html():
    with open('access_token.txt', 'r') as f:
        mapbox_access_token = f.readline().strip()
    mapa = create_map(mapbox_access_token)
    add_points_from_json_to_map('data/data.json', mapa)
    map
    return mapa._repr_html_()

map_html = get_map_html()
with open('../mapa.html', 'w') as f:
    f.write(map_html)
