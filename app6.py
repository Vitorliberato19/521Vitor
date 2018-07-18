#!/usr/bin/python3

from flask import Flask, jsonify, request, make_response, render_template
from datetime import datetime

from blueprint.usuario3 import usuario

app = Flask(__name__)
app.register_blueprint(usuario)

# 127.0.0.1:5000
@app.route('/')
def home():
    return render_template('index.html', title='Home')


if __name__ == '__main__':
    app.run(debug=True)