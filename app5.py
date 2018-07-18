#!/usr/bin/python3

from flask import Flask, jsonify, request, make_response
from datetime import datetime

from blueprint.usuario3 import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
    return jsonify({'status' : 'Running...'})


if __name__ == '__main__':
    app.run(debug=True)