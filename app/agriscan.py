from libs.map_utils import *
from libs.escalas import *

def get_map_html():
    with open('access_token.txt', 'r') as f:
        google_api_key = f.readline().strip()
    mapa = create_map(google_api_key)
    add_points_from_json_to_map(["libs/data/data.json", "libs/data/drawn_data.json"], mapa)
    add_draw_control(mapa)
    add_route_planner(mapa)
    return mapa._repr_html_()

map_html = get_map_html()
with open('../mapa.html', 'w') as f:
    f.write(map_html)
