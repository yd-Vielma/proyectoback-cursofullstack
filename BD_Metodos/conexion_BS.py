import mysql.connector


config_dev = {
    'user': 'root', 
    'password': '',
    'host': '127.0.0.1',
    'database':'restaurante'
}

# Asegúrate de que la conexión esté siempre disponible
def obtener_conexion():
    if not conexion.is_connected():
        print("Conexión no está activa, intentando reconectar...")
        conexion.reconnect()
    print("Conexión establecida")
    return conexion


config_prod = {} # en el python anywhere

conexion = mysql.connector.connect(**config_dev)

