from model import RegistroModel
from connection import db

#CREATE
def criar_registro(registro):
    registro_db = RegistroModel(dth_registro=registro.dth_registro, tipo=registro.tipo)
    db.session.add(registro_db)
    db.session.commit()
    return registro_db

#READ
def listar_registro(id):
    return RegistroModel.query.all()

def listar_registro_dth(dth_registro):
    return RegistroModel.query.filter_by(dth_registro=dth_registro).first()

def listar_registro_tipo(tipo):
    return RegistroModel.query.filter_by(tipo=tipo).first()

def list_registration_product(registration):
    return RegistroModel.session.query.filter_by(prod_id=registration.product).first()

#DELETE
def deletar_registro(id):
    registro = RegistroModel.query.get(id)
    if registro:
        db.session.delete(registro)
        db.session.commit()
        return True
    return False

#UPDATE
def editar_registro(id, novo_registro):
    registro = RegistroModel.query.get(id)
    if registro:
        registro.dth_registro = novo_registro['dth_registro']
        registro.tipo = novo_registro['tipo']
    