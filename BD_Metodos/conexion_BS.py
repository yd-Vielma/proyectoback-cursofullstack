import mysql.connector


config_dev = {
    'user': 'root', 
    'password': '',
    'host': '127.0.0.1',
    'database':'restaurante'
}

config_prod = {} # en el python anywhere

conexion = mysql.connector.connect(**config_dev)

