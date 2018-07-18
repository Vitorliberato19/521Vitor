#!/usr/bin/python3

from flask import Flask, jsonify, request, make_response
from datetime import datetime
import json

from bson.json_util import dumps as bdumps
from config.mongo import db
from blueprint.usuario import usuario


app = Flask(__name__)
app.register_blueprint(usuario)

@app.route('/')
def home():
    return jsonify({'status' : 'Running...'})

@app.route('/teste')
def teste():
    usuarios = []
    for x in db.usuarios.find():
        usuarios.append(json.loads(bdumps(x)))
    return jsonify(usuarios)

if __name__ == '__main__':
    app.run(debug=True)