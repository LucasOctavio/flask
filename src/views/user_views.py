from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schema.user_schema import (Usuario_Schema, Usuarios_Schema)
from service import user_service
from src import api

class usuariolist(Resource):
    def get(self):
        usuarios = user_service.listar_usuario()

        if not usuarios:
            return make_response(jsonify({'mensagem':'Não existem usuarios'}),404)

        return make_response(jsonify(Usuarios_Schema.dump(usuarios)), 200)

    def post(self):
        try:
            usuario = Usuarios_Schema.load(request.get_json())
            
        except ValidationError as err:
            return err.menssages, 400

        if user_service.listar_usuario_email(usuario["email"]):
            return {"menssage":"Email já cadastrado!"}, 409

        try:
            resultado = user_service.cadastrar_usuario(usuario)

            return Usuarios_Schema.dump(resultado), 201

        except Exception as e:
            return {
                "menssage":str(e)
            }, 400
api.add_resource(usuariolist,'/usuarios')


class UsuarioResource(Resource):
    def get(self,user_id):
        usuario = user_service.listar_usuario_id(user_id)

        if not usuario:
            return {"menssage":"Usuário não encontrado"}, 404

        return Usuario_Schema.dump(usuario), 200
    
    def put(self, user_id):
        try:
            novo_usuario = Usuario_Schema.load(request.get_json())

        except ValidationError as err:
            return err.menssagens, 400

        usuario = user_service.editar_usuario(
            user_id = {
                "nome":novo_usuario.nome,
                "email":novo_usuario.email,
                "senha":novo_usuario.senha
            }
        )

        if not usuario:
            return{"menssage":"Usuário não emcontrado"}, 404

        return Usuario_Schema.dump(usuario), 200
    def deletar(self, user_id):
        if user_service.deletar_usuario(user_id):
            return {"menssage":"Usuário deletado"}, 200
        return {"menssage":"Usuário não encontrado"}, 404 
api.add_resource(UsuarioResource, '/usuario/<int:user_id>')