'''
    Autor: Reyna Yazmin Ríos Martínez
    Fecha: 09 de nov de 2023
    Descripción: Creando un servidor Web con Flask para proporcionar servicios
    mediante los métodos GET, PUT, DELETE, POST
'''

import json
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('crud.db')
    conn.row_factory = sqlite3.Row
    return conn

# Método GET
@app.route('/', methods=['GET'])
def query_records():
    name = request.args.get('serie')
    registros = []
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM libros')
    data = cursor.fetchall()
    for reg in data:
       registros.append(dict(reg))
    conn.close()
    return jsonify(json.dumps(registros))

#Método Insertar
@app.route('/', methods=['PUT'])
def create_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    insert = 'INSERT INTO libros(serie,nombre,paginas,editorial) VALUES(?,?,?,?)'
    cursor.execute(insert, [record['serie'],record['nombre'], record['paginas'], record['editorial']])
    conn.commit()
    conn.close()
    return jsonify(record)

#Método ELIMINAR
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'DELETE FROM libros WHERE nombre= ?'
    cursor.execute(delete, [record['nombre']])
    conn.commit()
    conn.close()
    return jsonify(record)

#MODIFICAR
@app.route('/', methods=['POST'])
def update_record():
    record = json.loads(request.data)
    conn = get_db_connection()
    cursor = conn.cursor()
    delete = 'UPDATE libros SET nombre = ? WHERE serie= ?'
    cursor.execute(delete, [record['nombre'], record['serie']])
    conn.commit()
    conn.close()
    return jsonify(record)

app.run(debug=True)