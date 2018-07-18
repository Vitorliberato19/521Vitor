#!/usr/bin/python3

from flask import Flask, jsonify, request, make_response
from datetime import datetime
import json

app = Flask(__name__)

def contar():
    contador = 0
    with open('contador','r') as f:
        contador = f.read()
        contador = 1 if not contador else int(contador) + 1
    with open('contador','w') as f:
        f.write(str(contador))
    return contador

@app.route('/')
def home():
    c = contar()
    return jsonify({'status' : 'Running...','x':c})

@app.route('/acessos')
def acessos():
    c = contar()
    date  = datetime.now().strftime('%Y-%m-%d %H:%I:%S')
    return jsonify({'date' : date, 'count':c})

@app.route('/celular', methods=['POST','GET'])
def celular():
    #return jsonify(request.get_json())   
    retorno = json.dumps({'status' : 'não encontrado!'})
    headers = {'Content-Type' : 'application/json'}
    return make_response(retorno, 404, headers)

app.run(debug=True)
