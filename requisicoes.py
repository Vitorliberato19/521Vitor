#!/usr/bin/python3

import requests

#data = {"nome" :"Maria Madalena ", "email" : "maria@ig.com.br" }       
#data = {"nome" :"Leonardo" }       


response = requests.get('http://127.0.0.1:5000/usuarios')
data = response.json()

print('{0:.>10}{1:.>30}'.format('ID','NOME'))
for x in data['usuarios']:
    if x['id']%2 == 0:
        print('{0:.>10}{1:.>30}'.format(x['id'],x['nome']))

#response = requests.post('http://127.0.0.1:5000/usuarios', json=data)
#response = requests.put('http://127.0.0.1:5000/usuarios/5', json=data)
#response = requests.delete('http://127.0.0.1:5000/usuario/5s', json=data)


