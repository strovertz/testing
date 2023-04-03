import folium
import folium.plugins
import json
import os
from datetime import datetime
from libs.escalas import *

def create_map(google_api_key):
    mapa = folium.Map(location=[-28.899666, -54.555794], zoom_start=13)
    add_google_satellite_layer(mapa, google_api_key)
    return mapa

def add_google_satellite_layer(map_obj, google_api_key):
    tile_url = f"https://mt1.google.com/vt/lyrs=s&x={{x}}&y={{y}}&z={{z}}&key={google_api_key}"
    folium.TileLayer(tile_url, attr="Google Maps Satellite", name="Satélite Google").add_to(map_obj)
    folium.LayerControl().add_to(map_obj)

def add_route_planner(map_obj):
    folium.plugins.AntPath(locations=[], color='blue', weight=5).add_to(map_obj)

def add_points_from_json_to_map(file_paths, map_obj):
    for file_path in file_paths:
        if os.path.exists(file_path) and os.stat(file_path).st_size > 0:
            with open(file_path) as json_file:
                data = json.load(json_file)
            for ponto in data['pontos']:
                if ponto['tipo'] == 'marcador':
                    folium.Marker(
                        location=[ponto['latitude'], ponto['longitude']],
                        popup=ponto['nome']
                    ).add_to(map_obj)
                elif ponto['tipo'] == 'demarcacao':
                    data_demarcacao = datetime.strptime(ponto['data'], '%Y-%m-%d')
                    # Calculando a diferença entre a data da demarcação e a data atual
                    dias_desde_plantio = (datetime.now() - data_demarcacao).days
                    fill_color = escala_maturacao_soja(dias_desde_plantio)
                    situacao = situacao_maturidade(dias_desde_plantio)
                    popup_content = f"Situação do Plantio: {situacao} <br>Data do plantio: {ponto['data']}<br>Dias desde o plantio: {dias_desde_plantio}<br>Identificador: {ponto['nome']}"
                    folium.Polygon(
                        locations=ponto['coordenadas'],
                        popup=folium.Popup(popup_content,max_width=500),
                        color='red',
                        fill=True,
                        fill_opacity=0.5,
                        fill_color=fill_color
                    ).add_to(map_obj)
            folium.plugins.Draw().add_to(map_obj)

            return folium.plugins.Draw()
    print('Nenhum arquivo de pontos válido encontrado.')

def add_draw_control(map_obj):
    def save_drawn_data(drawn_data):
        with open('data/drawn_data.json', 'w') as f:
            json.dump(drawn_data, f)
        print('Dados salvos com sucesso.')

    draw = folium.plugins.Draw(export=True)
    draw.add_to(map_obj)

    custom_js = f"""
        <script>
            document.addEventListener('DOMContentLoaded', function() {{
                var map = document.querySelector('div.folium-map');
                if (map) {{
                    map.addEventListener('draw:created', function(e) {{
                        var drawn_features = e.detail.geojson;
                        save_drawn_data(drawn_features);
                    }});
                }}
            }});
        </script>
    """

    map_obj.get_root().header.add_child(folium.Element(custom_js))

