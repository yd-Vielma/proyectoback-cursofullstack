# Vistas segun patron MVT (Model View Templeate)
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from app import app
from componentes.modelos import Platillo
from componentes.modelos import Valoracion
from componentes.modelos import Platillo

# Vistas HTML

# ****** Inicio ******
@app.route('/')
def home():

    return render_template('inicio.html')


@app.route("/platillos")
def platillo():
    return render_template('platillos.html', platillo=platillo)


@app.route("/comentarios")
def comentarios():
    return render_template('comentarios.html')

if __name__ == '__main__':
    app.run(debug=True)

