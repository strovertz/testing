from libs.map_utils import create_map, add_points_from_json_to_map

def get_map_html():
    mapa = create_map()
    add_points_from_json_to_map('data/data.json', mapa)
    return mapa._repr_html_()
