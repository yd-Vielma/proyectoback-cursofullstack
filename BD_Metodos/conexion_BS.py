import mysql.connector

config_dev = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'restaurante'
}

try:
    conexion = mysql.connector.connect(**config_dev)
    print("Conexión establecida")
except mysql.connector.Error as err:
    print(f"Error al conectar a la base de datos: {err}")

def obtener_conexion():
    try:
        if not conexion.is_connected():
            conexion.reconnect()
        print("Conexión establecida")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error al obtener la conexión: {err}")
        return None

