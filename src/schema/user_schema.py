from src import ma
from src.model import usuario_model
from marshmallow import fields


class UsuarioSchema(ma.SQAlchemyAutoSchema):
    class Meta:
        model = usuario_model.UsuarioModel
        load_instance = True
        fields = ('id', 'nome', 'email', 'senha')

    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)

Usuario_Schema = UsuarioSchema()
Usuarios_Schema = UsuarioSchema(many=True)