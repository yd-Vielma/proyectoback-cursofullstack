class Tabla:

    def __init__ (self, nombre_tabla, conexion, atributos_tabla):
        self.nombre_tabla=nombre_tabla
        self.conexion=conexion
        self.atributos_tabla=atributos_tabla

    
    def crear(self, valores,de_bbdd =False):
        if de_bbdd:
            for c,v in zip(self.atributos_tabla,*valores):
                setattr(self,c,v)
        else:
            for c,v in zip(self.atributos_tabla[1:], valores):
                setattr(self,c,v)
        


    def guardar_db(self):
        campos = str(self.atributos_tabla).replace("'","`")
        valores = f"('%s ,'* {(len(self.atributos_tabla)-2)} %s)"
        consulta = (f"INSERT INTO {self.nombre_tabla} {campos}"
                    f"VALUES {valores};")
        datos = tuple(vars(self).values())
        rta_bd = self.__conectar(consulta,datos)

        if rta_bd:
            return 'Creacion exitosa'
        return 'No se pudo crear el registro'
    
    

    @classmethod
    def obtener(cls, campo=None, valor=None):

        if campo==None or valor==None:
            consulta= ("SELECT * "
                        f"FROM {cls.nombre_tabla}")
            resultado= cls.__conectar(consulta)
        
        else:
            consulta=("SELECT * "
                      f"FROM {cls.nombre_tabla} "
                        f"WHERE {campo} = %s")
            resultado=cls.__conectar(consulta, (valor,))

        return resultado


   # @classmethod
    #def eliminar(cls,id):
     #   consulta= (f"DELETE FROM {cls.nombre_tabla} WHERE id = %s ;")
     #   rta_bd= cls.__conectar(consulta, (id,))

      #  if rta_bd:
       #     return 'Eliminacion exitosa'
        
        #return 'No se puede eliminar el registro'
    
    @classmethod
    def eliminar_de_tabla(cls,id):
        #objecto_a_eliminar = cls.obtener(id)
        consulta_eliminar = f"DELETE FROM {cls.nombre_tabla} WHERE platillo_id=%s"
        parametros_consulta = (id,)
        try:
            cursor = cls.conexion.cursor()
            cursor.execute(consulta_eliminar, parametros_consulta)
            cls.conexion.commit()
            cls.conexion.close()
            print("Objeto borrado")       
        except Exception as e:
            print(f"Error al eliminar el objeto: {str(e)}")
            raise      
    
    
    @classmethod
    def modificar(cls, registro):
        if 'id' not in registro:
            raise ValueError("El registro debe contener un campo 'id'")
        
        id = registro.pop('id')
        id = int(id) if not isinstance(id, int) else id

        up = f"UPDATE {cls.nombre_tabla} "
        st = 'SET'

        # Construir la parte SET de la consulta SQL
        set_parts = []
        values = []
        for key, value in registro.items():
            set_parts.append(f"{key} = %s")
            values.append(value)

        st = ', '.join(set_parts)
        where_i = " WHERE id = %s;"
        consulta = up + st + where_i
        values.append(id)

        rta_bd = cls.__conectar(consulta, values)

        if rta_bd:
            return 'Modificación exitosa'
        
        return 'No se puede modificar el registro.'

    @classmethod 
    def __conectar(cls,consulta,datos=None):

        try:
            cursor= cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor= cls.conexion.cursor()
        
        if consulta.startswith('SELECT'):

            if datos!= None:
                cursor.execute(consulta,datos)
            
            else:
                cursor.execute(consulta)

            rta_bd=cursor.fetchall()
            
            if rta_bd !=[]:
                resultado=[cls(registro,de_bbdd=True) for registro in rta_bd]

                if len(resultado)==1:
                    resultado=resultado[0]
            
            else:
                resultado=False
            
            cls.conexion.close()
        
        else:

            try:
                cursor.execute(consulta,datos)
                cls.conexion.commit()
                cls.conexion.close()
                resultado=True

            except Exception as e:
                resultado= False
        
        return resultado