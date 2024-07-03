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
            datos['platillo_ID'],
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


@app.route('/eliminar_platillo/<int:id>', methods = ['GET'])
def eliminar_platillo(id):
  # Implementa esta función para eliminar un platillo de la base de datos
    if request.method == 'GET':
        Platillo.eliminar_de_tabla(id)
        return redirect(url_for('platillos'))


    
