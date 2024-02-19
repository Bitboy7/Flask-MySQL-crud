from flask import render_template,redirect,url_for, request
from app import app
from flask_mysqldb import MySQL
import conexion as db
from datetime import datetime
from datetime import date
from tkinter import *
from tkinter import messagebox as MessageBox

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')


@app.route('/insertarpedido', methods=['POST'])
def insertarpedido():
    # Importamos las variables desde el form del indexUsuario.html
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    pedido = request.form["pedido"]
    notas = request.form["notas"]
    sugerencia = request.form["sugerencia"]
    current_date = datetime.now().strftime(
        "%H:%M:%S")  

    if nombre and pedido:
        cursor = db.conexion.cursor()
        cursor.execute("INSERT INTO Cafeteria (Nombre, Apellido, Pedido, Notas, Sugerencia, Hora) VALUES (%s, %s, %s,%s, %s, %s) ",
                       (nombre, apellido, pedido, notas, sugerencia, current_date))
        # Declaramos a "datos" como una variable tipo tupla para mandar información
        db.conexion.commit()
    return render_template('pedidos.html', current_date=current_date)
    
@app.route('/mostrar', methods=['GET'])
def mostrar():
    cursor = db.conexion.cursor()
    cursor.execute("SELECT * FROM Cafeteria")
    datosDB_Pedido = cursor.fetchall()
    # Convertir los datos a diccionario para la tabla Usuario
    insertpedido = []
    columnName_Pedido = [column[0] for column in cursor.description]
    for registro in datosDB_Pedido:
        insertpedido.append(dict(zip(columnName_Pedido, registro)))
            
    cursor.close()
    return render_template('mostrar.html', data=insertpedido)

@app.route('/eliminar/<string:IdPedido>')
def eliminar(IdPedido):
    resultado = MessageBox.askokcancel(
        "Eliminar...", "¿Estas seguro de eliminar el registro?")
    if resultado == TRUE:
        cursor = db.conexion.cursor()
        sql = """DELETE FROM Cafeteria
                    WHERE IdPedido=%s"""
        # Declaramos a "datos" como una variable tipo tupla para mandar la información
        datos = (IdPedido,)
        cursor.execute(sql, datos)
        db.conexion.commit()
    return redirect(url_for('mostrar'))