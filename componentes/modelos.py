from BD_Metodos.conexion_BS import conexion as con
from BD_Metodos.tabla import Tabla


class Comentario(Tabla):

    nombre_tabla= 'comentarios'
    conexion=con
    atributos_tabla=('ID_comentario','nombre','Apellido','Correo_electronico', 'Comentario')

    def __init__(self, *args, de_bbdd=False):
        super().__init__(*args, de_bbdd=de_bbdd)

    @classmethod
    def obtener(cls):
        consulta = "SELECT * FROM comentarios"
        return cls.__conectar(consulta)    


class Valoracion(Tabla):

    nombre_tabla= 'valoracion'
    conexion=con
    atributos_tabla=('ID_valoracion', 'usuario_number','platillo_number', 'puntos')

    def __init__(self, *args, de_bbdd=False):
        super().__init__(*args, de_bbdd=de_bbdd)

    @classmethod
    def obtener(cls):
        consulta = "SELECT * FROM valoracion"
        return cls.__conectar(consulta)
    

class Platillo(Tabla):

    nombre_tabla='platillo'
    conexion=con
    atributos_tabla=('platillo_ID','imagen_id', 'plato', 'descripcion','precio')

    def __init__(self, *args, de_bbdd=False):
        super().__init__(*args, de_bbdd=de_bbdd)

    @classmethod
    def obtener(cls):
        consulta = "SELECT * FROM platillo"
        return cls.__conectar(consulta)


class Imagen(Tabla):

    nombre_tabla='imagen'
    conexion=con
    atributos_tabla=('Id_imagen','url', 'texto_alternativo')

    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)