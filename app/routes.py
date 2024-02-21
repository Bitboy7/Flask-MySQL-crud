from flask import render_template, redirect, url_for, request, jsonify
from app import app
import conexion as db
from datetime import datetime
from datetime import date
from tkinter import *
from tkinter import messagebox as MessageBox


@app.route('/')
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
    notas = request.form["notas"]
    sugerencia = request.form["sugerencia"]
    current_date = datetime.now().strftime(
        "%H:%M:%S") # Hora actual del sistema
    platillo_id = request.form["platillo_id"]
    cantidad = request.form['cantidad']
    # Verificar que los campos no estén vacíos    
    if nombre and platillo_id and cantidad:
        cursor = db.conexion.cursor()
        # Obtener el precio del platillo desde la tabla 'platillos'
        cursor.execute(
            "SELECT precio FROM platillos WHERE id = %s", (platillo_id,))
        precio = cursor.fetchone()[0]
        # Calcular el total del pedido
        total = precio * int(cantidad)
        cursor.execute("INSERT INTO Cafeteria (Nombre, Apellido, Notas, Sugerencia, Hora, platillo_id, cantidad, total) VALUES (%s, %s, %s,%s, %s, %s, %s, %s) ",
                       (nombre, apellido, notas, sugerencia, current_date, platillo_id, cantidad, total))
        # Declaramos a "datos" como una variable tipo tupla para mandar información
        db.conexion.commit()
    return render_template('nuevo-pedido.html', message=F'Total: ${total} pesos / A nombre de: {nombre} {apellido} / Cantidad {cantidad} / Notas: {notas}', current_date=current_date)

@app.route('/mostrar', methods=['GET'])
def mostrar():
    cursor = db.conexion.cursor()
    cursor.execute("SELECT Cafeteria.*, platillos.nombre FROM Cafeteria JOIN platillos ON Cafeteria.platillo_id = id")
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


@app.route('/menu', methods=['GET'])
def menu():
    cursor = db.conexion.cursor()
    cursor.execute("SELECT * FROM platillos")
    r = cursor.fetchall()
    cursor.close()
    return render_template('menu.html', platillos=r)




