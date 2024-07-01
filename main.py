from flask import Flask


app=Flask (__name__)
from componentes.vista_api import *


if __name__== '__main__':
    app.run()
