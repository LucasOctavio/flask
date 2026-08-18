from src import ma
from model import record_model
from marshmallow import fields, validate, ValidationError, validates
from datetime import datetime

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = record_model.RegistroModel
        fields = ('id_registro', 'dth_registro', 'tipo')

    data_registro = fields.DateTime(required=True)
    tipo = fields.String(required=True, validate=validate.OneOF(
        ['Escritório e Administração',
         'Limpeza e Copa', 'Manutenção e segurança'],
         error = 'Tipo de produtp de almoxarifado inválido'

                                                                ))
    @validates('dth_registro')
    def menos_que_agora(self, value):
        agora = datetime.now(value.tzinfo)

        if value > agora:
            raise ValidationError("A data de registro não pode estar no futuro.")

Record_Schema = RegistroSchema()
Records_Schema = RegistroSchema(many=True)