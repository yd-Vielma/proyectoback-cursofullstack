from flask import Flask
from flask_cors import CORS

# Crear la aplicación Flask
app = Flask(__name__)

# Configuraciones de la aplicación
app.config['JSON_AS_ASCII'] = False
app.config['SECRET_KEY'] = 'tu_clave_secreta'

# Configurar CORS
cors = CORS(app, resources={r"/api-restaurante/*": {"origins": "*"}})

# Importar las vistas
from componentes.vista_api import *
from componentes.vista_web import *

# Ejecutar la aplicación en modo de desarrollo
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)