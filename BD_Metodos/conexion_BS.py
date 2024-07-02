import mysql.connector


config_dev = {
    'user': 'root', 
    'password': '',
    'host': '127.0.0.1',
    'database':'restaurante'
}

config_prod = {} # cuando entendamos jajaja

conexion = mysql.connector.connect(**config_dev)

