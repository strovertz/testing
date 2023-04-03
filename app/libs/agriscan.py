from map_utils import *
from escalas import *

def get_map_html():
    mapa = create_map()
    add_points_from_json_to_map('data/data.json', mapa)
    map
    return mapa._repr_html_()

map_html = get_map_html()
with open('mapa.html', 'w') as f:
    f.write(map_html)
