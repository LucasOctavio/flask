from src import ma
from models import Product_model
from marshmallow import fields, validate
from schemas import CategoriaSchema

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    categoria = fields.Nested(CategoriaSchema, dump_only=True)

    class Meta:
        model = Product_model.ProdutoModel
        load_instance = True
        include_fk = True
        fields = ('id_produto', 'nome_produto', 'uni_medida', 'vlr_unitario', 'qtd_estoque')

    uni_medida = fields.String(
        requered=True,
        validate=validate.OneOF(
            ['UN', 'KG', 'L', 'CX'],
            error = 'Unidade de medida inválida'
        )
    )

produto_schema = ProdutoSchema(many=True)

nome_produto = fields.String(
    required=True,
    validate=validate.Length(
        min='3' ,
        error= 'O nome deve ter no mínimo 3 letras'
    ))


vlr_unitario = fields.Decimal(
    required=True,
    places=2,
    validate=validate.Range(
    min=0, 
    error='O valor unitario deve ser maior ou igual a 0.')
    )


categoria = fields.Nested(
    CategoriaSchema,
      dump_only=True)

quantidade_estoque = fields.Integer(
    required=True,
    validate=validate.Range(
        min=0,
        error= "O valor deve ser maior ou igual a 1"
    ))

Product_Schema = ProdutoSchema()
Products_Schema = ProdutoSchema(many=True)