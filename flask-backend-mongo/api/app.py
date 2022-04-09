from urllib import response
from flask import Flask, request, jsonify
from bson.json_util import dumps
from bson.objectid import ObjectId
import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
######################################## CONSULTAS CITAS MEDICAS #################################################


#crea una cita medica
@app.route("/citas", methods=['POST'])
def create_appoinment():
    data = request.get_json()
    con = db.get_connection()
    dbAppoinment = con.dbAppoinment 
    try:
        medAppoinment = dbAppoinment.medAppoinment
        medAppoinment.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/citas", methods=['GET'])
def get_all_appoinments():
    con = db.get_connection()
    dbAppoinment = con.dbAppoinment 
    try:
        medAppoinment = dbAppoinment.medAppoinment
        response = app.response_class(
            response=dumps(
                medAppoinment.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")


#lee una cita medica por id de la cita
@app.route("/citas/<code>", methods=['GET'])
def get_appoinment(code):
    con = db.get_connection()
    dbAppoinment = con.dbAppoinment 
    try:
        medAppoinment = dbAppoinment.medAppoinment
        response = app.response_class(
            response=dumps(medAppoinment.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

#Modifica una cita medica
@app.route("/citas/<code>", methods=['PUT'])
def update_appoinment(code):
    data = request.get_json()
    con = db.get_connection()
    dbAppoinment = con.dbAppoinment
    try:
        medAppoinment = dbAppoinment.medAppoinment
        medAppoinment.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

#Cancela una cita medica
@app.route("/citas/<code>", methods=['DELETE'])
def delete_appoinment(code):
    con = db.get_connection()
    dbAppoinment = con.dbAppoinment
    try:
        medAppoinment = dbAppoinment.medAppoinment
        medAppoinment.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")


######################################## CONSULTAS DE PACIENTES #################################################

@app.route("/pacientes", methods=['GET'])
def get_all_users():
    con = db.get_connection()
    usuarios = con.usuarios
    try:
        pacientes = usuarios.pacientes
        response = app.response_class(
            response=dumps(
                pacientes.find()
            ),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/pacientes/<code>", methods=['GET'])
def get_user(code):
    con = db.get_connection()
    usuarios = con.usuarios
    try:
        pacientes = usuarios.pacientes
        response = app.response_class(
            response=dumps(pacientes.find_one({'_id': ObjectId(code)})),
            status=200,
            mimetype='application/json'
        )
        return response
    finally:
        con.close()
        print("Connection closed")

@app.route("/pacientes", methods=['POST'])
def create_user():
    data = request.get_json()
    con = db.get_connection()
    usuarios = con.usuarios  
    try:
        pacientes = usuarios.pacientes
        pacientes.insert_one(data)
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/pacientes/<code>", methods=['PUT'])
def update_user(code):
    data = request.get_json()
    con = db.get_connection()
    usuarios = con.usuarios
    try:
        pacientes = usuarios.pacientes
        pacientes.replace_one(
            {'_id': ObjectId(code)},
            data, True
        )
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")

@app.route("/pacientes/<code>", methods=['DELETE'])
def delete_user(code):
    con = db.get_connection()
    usuarios = con.usuarios
    try:
        pacientes = usuarios.pacientes
        pacientes.delete_one({'_id': ObjectId(code)})
        return jsonify({"message":"OK"})
    finally:
        con.close()
        print("Connection closed")
