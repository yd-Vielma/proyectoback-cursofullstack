from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
app.json.ensure_ascii = False
app.secret_key = 'ntra_clave_secreta'

cors = CORS(app, resources={r"/api-restaurante/*": {"origins": "*"}})


# Importar las vistas
from componentes.vista_api import *
from componentes.vista_web import *


# Lo siguiente sólo en desarrollo, no en producción
if __name__ == '__main__':
    app.run()