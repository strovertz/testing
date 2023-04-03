from flask import *
from agriscan import get_map_html
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    get_map_html()  # Gera o arquivo 'mapa.html' no diretório 'templates'
    return render_template('mapa.html')

@app.route('/save_drawn_data', methods=['POST'])
def save_drawn_data(drawn_data):
    # Obter o caminho do diretório atual
    current_dir = os.getcwd()

    # Definir o caminho completo para o arquivo
    file_path = os.path.join(current_dir, 'data', 'drawn_data.json')

    # Salvar os dados no arquivo
    with open(file_path, 'w') as f:
        json.dump(drawn_data, f)

    # Retornar uma mensagem informando que os dados foram salvos com sucesso
    return 'Dados salvos com sucesso.'

if __name__ == '__main__':
    app.run(debug=True)
