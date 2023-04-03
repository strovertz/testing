import folium
import folium.plugins
import json
from datetime import datetime
from escalas import *

def create_map():
    mapa = folium.Map(location=[-28.899666, -54.555794], zoom_start=13)
    add_satellite_layer(mapa)
    return mapa

def add_satellite_layer(map_obj):
    tile_url = "https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}"
    folium.TileLayer(tile_url, attr="Esri World Imagery", name="Satélite").add_to(map_obj)
    folium.LayerControl().add_to(map_obj)

def add_points_from_json_to_map(file_path, map_obj):

    with open(file_path) as json_file:
        data = json.load(json_file)

    # Adicionando os pontos geográficos ao mapa folium
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

