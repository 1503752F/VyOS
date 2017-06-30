#!/usr/bin/python

from flask import Flask, jsonify
from flask import abort, make_response
from flask.ext.httpauth import HTTPBasicAuth
import json
from flask import request
auth = HTTPBasicAuth()

import dns

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

@app.route('/createdns', methods=['POST'])
@auth.login_required
def createdns():
        function = {
                'cache_size' : request.json['cache_size'],
                'port' : request.json['port'],
		'ip' : request.json['ip']
	        }
        tasks.append(function)
        dns.createdns(function['cache_size'],function['port'],function['ip'])
        return jsonify({'dns' : dns.readdns()})

@app.route('/readdns', methods=['GET'])
@auth.login_required
def readdns():
        return jsonify({'dns': dns.readdns()})

@app.route('/deldns', methods=['GET','POST'])
@auth.login_required
def deldns():
        function = {
     		'ip':request.json['ip']
        }
        tasks.append(function)
        dns.deldns(function['ip'])
        return jsonify({'dns' : dns.readdns()})

@app.route('/updatedns', methods=['POST'])
@auth.login_required
def updatedns():
        function ={
		'cache_size':request.json['cache_size'],
                'port1':request.json['port1'],
        	'ip':request.json['ip'],
		'port':request.json['port']
              	}

        tasks.append(function)
        dns.updatedns(function['cache_size'],function['port1'],function['ip'],function['port'])
        return jsonify({'dns' : dns.readdns()})

if __name__ == '__main__':
    app.run(debug=True)

