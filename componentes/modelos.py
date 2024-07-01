from BD_Metodos.conexion_BS import conexion as con
from BD_Metodos.tabla import Tabla


class Comentario(Tabla):

    nombre_tabla= 'comentarios'
    conexion=con
    atributos_tabla=('ID_comentario','nombre','Apellido','Correo_electronico', 'Comentario')

    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)


class Valoracion(Tabla):

    nombre_tabla= 'valoracion'
    conexion=con
    atributos_tabla=('ID_valoracion', 'platillo_ID', 'puntos')

    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
    

class Platillo(Tabla):

    nombre_tabla='platillo'
    conexion=con
    atributos_tabla=('platillo_ID', 'plato', 'descripcion','precio')

    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

