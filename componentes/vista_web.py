# Vistas segun patron MVT (Model View Templeate)
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from app import app
from BD_Metodos.conexion_BS import conexion
from componentes.modelos import Platillo
from componentes.modelos import Valoracion
from componentes.modelos import Comentario

# Vistas HTML

# ****** Inicio ******
@app.route('/')
def home():
    return render_template('inicio.html')

@app.route("/platillos")
def platillos():
    try:
        cursor = conexion.cursor(dictionary=True)
    except Exception as e:
        print(e)
        print('reconexión')
        conexion.connect()
        cursor = conexion.cursor(dictionary=True)
        
    cursor.execute('SELECT * FROM platillo;')
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()

    return render_template('platillos.html', platillos=datos)


@app.route("/comentarios")
def comentarios():
    try:
        cursor = conexion.cursor(dictionary=True)
    except Exception as e:
        print(e)
        print('reconexión')
        conexion.connect()
        cursor = conexion.cursor(dictionary=True)
        
    cursor.execute('SELECT * FROM comentarios;')
    datos = cursor.fetchall()
    cursor.close()
    conexion.close()

    return render_template('comentarios.html', comentarios=datos)

if __name__ == '__main__':
    app.run(debug=True)

