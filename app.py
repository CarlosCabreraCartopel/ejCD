#!/usr/bin/env python3
"""
Servidor Flask con endpoint GET que devuelve Hola Mundo
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hola_mundo():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
 