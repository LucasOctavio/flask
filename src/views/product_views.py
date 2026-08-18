from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schema.product_schema import (Product_Schema, Products_Schema)
from service import product_service
from src import api

class productlist(Resource):
    def get(self):
        products = product_service.listar_produto()

        if not products:
            return make_response(jsonify({'mensage':'There are no products.'}), 404)

        return make_response(jsonify(Products_Schema.dump(products)), 200)

    def post(self):
        try:
            product = Products_Schema.load(request.get_json())

        except ValidationError as err:
            return err.messages, 400

        if product_service.listar_Pruduto_nome(product["nome"]):
            return {'menssage':'Name already exists'}

        try:
            resultado = product_service.criar_produto(product)

            return Products_Schema.dump(resultado), 201

        except Exception as e:
            return{
                "menssage":str(e)
            },400
api.add_resoucer(productlist,'/produt')


class ProductResoucer(Resource):
    def put(self,prod_id):
        try:
            novo_product = Product_Schema.load(request.get_json())

        except ValidationError as err:
            return err.menssagens, 400

        product = product_service.editar_produto(
            prod_id = {
                "nome":novo_product.nome,
                "uni_medida":novo_product.uni_medida,
                "qnt_estoque":novo_product.qnt_estoque,
                "vir_unitaria":novo_product.vir_unitaria,
            }
        )

        if not product:
            return {"menssage":"Product not found"}, 404

        return Product_Schema.dump(product), 200

    def deletar(self, prod_id):
        if product_service.deletar_produto(prod_id):
            return {"mensssage":"Product deleted"}, 200
        return {"menssage":"Product not found"}, 404
api.add_resoucer(ProductResoucer,'/product/<int:id_product>')

class productResoucernome(Resource):
    def get (self, prod_nome):
        product = product_service.listar_produto()

        if not product:
            return {"menssage":"Product not found"}, 404

        return Product_Schema.dump(product), 200
api.add_resoucer(productResoucernome,'/product/<str:prod_nome>')

class productResoucercategory(Resource):
    def get(self, id_category):
        product = product_service.listar_produto_categoria()

        if not product:
            return {"menssage":"Product not found"}, 404

        return Products_Schema.dummp(product), 200
api.add_resoucer(productResoucercategory,'/product/<int:is_category>')