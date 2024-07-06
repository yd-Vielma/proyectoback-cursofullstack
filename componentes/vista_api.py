from flask import jsonify
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template
from flask import flash

from app import app
from componentes.modelos import Comentario
from componentes.modelos import Valoracion
from componentes.modelos import Platillo
from componentes.modelos import Imagen


#GET
@app.route("/api-restaurante/platillo", methods=['GET'])
def api_platillo():
    platillos = Platillo.obtener()
    datos = [platillo.__dict__ for platillo in platillos]

    return jsonify(datos)


@app.route("/api-restaurante/comentario", methods=['GET'])
def api_comentario():
    comentarios = Comentario.obtener()
    datos = [comentario.__dict__ for comentario in comentarios]

    return jsonify(datos)

@app.route("/api-restaurante/valoracion", methods=['GET'])
def api_valoracion():
    valoraciones = Valoracion.obtener()
    datos = [valoracion.__dict__ for valoracion in valoraciones]
    
    
   # for dato in datos:
    #    dato["platillo"] = Valoracion.obtener('id', dato['platillo_ID']).__dict__["platillo"]
     #   dato["comentario"] = Valoracion.obtener('id', dato['ID_comentario'])

      #  del dato["platillo_ID"]
       # del dato["ID_comentario"]

    return jsonify(datos) 


@app.route("/api-restaurante/imagen", methods=['GET'])
def api_imagen():
    imagenes = Imagen.obtener()
    datos = [imagen.__dict__ for imagen in imagenes]
    return jsonify(datos)   
  
#POST
@app.route("/api-restaurante/comentario", methods=['POST'])
def crear_comentario():

    if request.method == 'POST':
        datos = request.json["datos"]
        comentario_nuevo = Comentario(
            datos['nombre'],
            datos['apellido'],
            datos['correo_electronico'],
            datos['comentario'],
        )

        respuesta = {}
        rta_bbd = comentario_nuevo.guardar_db()

        if not rta_bbd:
            respuesta['mensaje'] = 'No se pudo enviar los datos!'
            respuesta['status'] = 409
        else:
            comentario_nuevo.guardar_db()
            respuesta['mensaje'] = 'Datos enviados con exito!'
            respuesta['status'] = 200

    else:
        respuesta['mensaje'] = 'No se recibieron datos'
        respuesta['status'] = 204

    return jsonify(respuesta)

@app.route("/api-restaurante/valoracion", methods=['POST'])
def crear_valoracion():

    if request.method == 'POST':
        datos = request.json["datos"]
        nva_valoracion = Valoracion(
            datos['platillo_id'],
            datos['puntos'],
        )

        respuesta = {}
        rta_bbd = nva_valoracion.guardar_db()

        if not rta_bbd:
            respuesta['mensaje'] = 'No se pudo enviar los datos!'
            respuesta['status'] = 409
        else:
            nva_valoracion.guardar_db()
            respuesta['mensaje'] = 'Datos enviados con exito!'
            respuesta['status'] = 200

    else:
        respuesta['mensaje'] = 'No se recibieron datos'
        respuesta['status'] = 204

    return jsonify(respuesta)

    
@app.route('/eliminar_platillo/<int:id>', methods=['POST'])
def eliminar_platillo(id):
    try:
        Platillo.eliminar_de_tabla(id)
        flash('Platillo eliminado exitosamente.')
    except Exception as e:
        flash(f'Error al eliminar el platillo: {str(e)}')
    return redirect(url_for('platillos'))    

@app.route('/modificar_platillo/<int:id>', methods=['GET', 'POST'])
def modificar_platillo(id):
    if request.method == 'POST':
        registro = {
            'id': id,
            'nombre': request.form['nombre'],
            'descripcion': request.form['descripcion'],
            'precio': request.form['precio']
        }
        mensaje = Platillo.modificar(registro)
        flash(mensaje)
        return redirect(url_for('platillos'))

    # Obtener datos del platillo a modificar
    platillo = Platillo.obtener('platillo_id', id)
    if platillo:
        platillo = platillo[0]  # Obtenemos el primer (y único) resultado
    return render_template('modificar_platillo.html', platillo=platillo)

    
if __name__ == '__main__':
    app.run(debug=True)

