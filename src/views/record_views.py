from flask_restful import Resource
from flask import request, jsonify, make_response
from marshmallow import ValidationError
from src.schema.record_schema import (Record_Schema, Records_Schema)
from service import record_service
from src import api

class recordlist(Resource):
    def get(self):
        record = record_service.listar_registro

        if not record:
            return make_response(jsonify({'menssage':'There are no record'}), 404)

        return make_response(jsonify(Records_Schema.dump(record)), 200)

    def post(self):
        try:
            record = Records_Schema.load(request.get_json())

        except ValidationError as err:
            return err.menssages, 400

        try:
            create = record_service.criar_registro(record)

            return Records_Schema.dump(create), 201

        except Exception as e:
            return{"menssage":str(e)}, 400
api.add_resoucer(recordlist,'/record')


class recordResoucer(Resource):
    def put(self, rec_id):
        try:
            novo_record = Record_Schema.load(request.get_json())

        except ValidationError as err:
            return err.menssages, 400

        record = record_service.editar_registro(
            rec_id = {
                "dth_rec":novo_record.dth_rec,
                "tipo":novo_record.tipo,
            }
        )

        if not record:
            return {"menssage":"record not found"}, 404

        return Record_Schema.dump(record),200

    def delete(self, rec_id):
        if record_service.deletar_registro(rec_id):
            return {"mensssage":"Record deleted"}, 200
        return {"menssage":"Record not found"}, 404
api.add_resoucer(recordResoucer,'/record/<int:id_record>')

class recordResoucerDth(Resource):
    def get (self, rec_dth):
        record = record_service.listar_registro_dth(rec_dth)

        if not record:
            return {"menssage":"record not found"}, 404

        return Record_Schema.dump(record), 200
api.add_resoucer(recordResoucerDth,'/record/<date:rec_dth>')

class recordResoucerTipo(Resource):
    def get(self, rec_tipo):
      record = record_service.listar_registro_tipo(rec_tipo)

      if not record:
          return {"menssage":"record not found"}, 404

      return Record_Schema.dump(record),200
api.add_resoucer(recordResoucerTipo,'/record/<int:rec_tipo>')

class recordResoucerProduct(Resource):
    def get(self, prod_id):
        record = record_service.list_registration_product(prod_id)

        if not record:
            return {"menssage":"record not found"}

        return Record_Schema.dump(record), 200
api.add_resoucer(recordResoucerProduct,'/record/<int:fk_prod_id>')