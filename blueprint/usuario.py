#!/usr/bin/python3

from flask import Blueprint, jsonify

usuario  = Blueprint('usuarios', __name__)

@usuario.route('/usuarios')
def usuarios():
    var =  [{"nome" : "Jim Jones"},{"nome" : "Charles Manson"},{"nome" : "outro nome"}]
    return jsonify({'Nome' : var})
    

