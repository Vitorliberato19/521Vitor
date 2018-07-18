#!/usr/bin/python3
import json

from flask import Blueprint, jsonify, request, make_response, Response, render_template
from config.mongo import db
from bson.json_util import dumps as bdumps

usuario  = Blueprint('usuarios', __name__)

@usuario.route('/usuarios', methods = ['GET','POST'])
def usuarios():
    if request.method == 'GET':
        # return Response('{"id":0}',content_type='application/json')
        # return Response(bdumps(db.usuarios.find()),content_type='application/json')
        # rs = [u for u in db.usuarios.find({'_id':2345})]
        rs = [u for u in db.usuarios.find()]
        return render_template('usuarios.html', usuarios = rs, title = 'Usuarios')
    else:
        usuario = request.get_json()
        keys = usuario.keys()
        for k in ('nome','email'):
            if k not in keys or not usuario[k].strip():
                return make_response(jsonify({'message': 'propriedade {0} obrigatória...'.format(k)}),400)

        # if 'nome' not in usuario.keys() or not usuario['nome'].strip():
        #     return make_response(jsonify({'message' : 'propriedade nome obrigatória '}), 400)
        # if 'email' not in usuario.keys() or not usuario['email'].strip():
        #     return make_response(jsonify({'message' : 'propriedade email obrigatória '}), 400)  


        db.usuarios.insert(usuario)
        return jsonify({'message' : 'usuario cadastrado com sucesso'})

@usuario.route('/usuarios/delete', methods=['POST'])
def delete_usuarios():
    email = request.args.get('email')
    db.usuarios.remove({'email': email})
    rs = [u for u in db.usuarios.find()]
    return render_template('usuarios.html', usuarios = rs)
    # return request.args.get('email')
# def erro():

