from model import CategoriaModel
from connection import db

#CREATE
def criar_categoria(categoria):
    categoria_db = CategoriaModel(descricao=categoria.categoria)
    db.session.add(categoria_db)
    db.sessio.commit()

#READ
def listar_categoria_id(id):
    return CategoriaModel.query.get(id)

def listar_categoria_descricao(descricao_id):
    return CategoriaModel.query.filter_by(descricao=descricao_id).first()

#UPDATE
def editar_categoria(id, nova_categoria):
    categoria = CategoriaModel.query.get(id)
    if categoria:
        categoria.descricao = nova_categoria['descricao']