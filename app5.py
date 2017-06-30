#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import Tunnel

app = Flask(__name__)

tasks = [
    {

    }
]

@auth.get_password
def get_password(username):
    if username == 'annabelle':
        return 'Passw0rd!'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/createtunnel', methods=['POST'])
@auth.login_required
def createtunnel():
        function = {
                'vti_id' : request.json['vti_id'],
                'ip' : request.json['ip']
        }
        tasks.append(function)
        Tunnel.createtunnel(function['vti_id'],function['ip'])
        return jsonify({'tunnel' : Tunnel.readtunnel()})

@app.route('/readtunnel', methods=['GET'])
@auth.login_required
def readtunnel():
        return jsonify({'tunnel': Tunnel.readtunnel()})

@app.route('/deltunnel', methods=['GET','POST'])
@auth.login_required
def deltunnel():
        function = {
                'vti_id' : request.json['vti_id']
        }
        tasks.append(function)
        Tunnel.deltunnel(function['vti_id'])
        return jsonify({'tunnel' : Tunnel.readtunnel()})

@app.route('/updatetunnel', methods=['POST'])
@auth.login_required
def updatetunnel():
        function = {
                'vti_id' : request.json['vti_id'],
                'vti_id1' : request.json['vti_id1'],
                'ip' : request.json['ip']
        }
        tasks.append(function)
        Tunnel.updatetunnel(function['vti_id'],function['vti_id1'],function['ip'])
        return jsonify({'tunnel' : Tunnel.readtunnel()})

if __name__ == '__main__':
    app.run(debug=True)

