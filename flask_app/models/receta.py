import os
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.modelo_base import ModeloBase

class Receta(ModeloBase):

    modelo = 'recetas' #nombre de la tabla
    campos = ['nombre', 'descripcion','instruccion','date_made','under_30', 'usuario_id']

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.descripcion = data['descripcion']
        self.instruccion = data['instruccion']
        self.date_made = data['date_made']
        self.under_30 = data['under_30']
        self.usuario_id = data['usuario_id']
        self.usuario_nombre = data['usuarios.nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_with_users(cls):
        query = f"SELECT * FROM {cls.modelo} join usuarios on usuarios.id = {cls.modelo}.usuario_id;"
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data

    @staticmethod
    def validar(user):
        is_valid = True
        if len(user['nombre']) < 3:
            is_valid = False
            flash(f'El largo del nombre no puede ser menor a 3', 'error')
        if len(user['descripcion']) < 3:
            is_valid = False
            flash(f'El largo de la descripción no puede ser menor a 3', 'error')
        if len(user['instruccion']) < 3:
            is_valid = False
            flash(f'El largo de la instruccion no puede ser menor a 3', 'error')
        if len(user['date_made']) < 9:
            is_valid = False
            flash(f'El largo del date_made no puede ser menor a 3', 'error')

        return is_valid


    @classmethod
    def update(cls,data):
        query = """UPDATE recetas 
                        SET nombre = %(nombre)s,
                        descripcion = %(descripcion)s,
                        instruccion = %(instruccion)s,
                        date_made = %(date_made)s,
                        under_30 = %(under_30)s,
                        updated_at=NOW() 
                    WHERE id = %(id)s"""
        resultado = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        return resultado

    @classmethod
    def get_by_id_with_users(cls, id):
        query = f"SELECT * FROM {cls.modelo} join usuarios on usuarios.id = {cls.modelo}.usuario_id where recetas.id = %(id)s;"
        data = {'id': id}
        results = connectToMySQL(os.environ.get("BASEDATOS_NOMBRE")).query_db(query, data)
        all_data = []
        for data in results:
            all_data.append(cls(data))
        return all_data