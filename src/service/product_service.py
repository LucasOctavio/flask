from model import ProdutoModel
from connection import db

#CREATE
def criar_produto(produto):
    produto_db = ProdutoModel(nome=produto.nome, uni_medida=produto.uni_medida, qnt_estoque=produto.qnt_estoque, vir_unitaria=produto.vir_unitaria)
    db.session.add(produto_db)
    db.session.commit()
    return produto_db

#READ
#listagem dos produtos
def listar_produto():
    return ProdutoModel.query.all()

def listar_Pruduto_nome(nome):
    return ProdutoModel.query.filter_by(nome=nome).first()

#listagem dos produtos por categoria
def listar_produto_categoria(id_categoria):
    return ProdutoModel.query.filter_by(id_categoria=id_categoria).first()

#DELETE
def deletar_produto(id):
    produto = ProdutoModel.query.get(id)
    if produto:
        db.session.delete(produto)
        db.session.commit()
        return True
    return False

#UPDATE
def editar_produto(id, novo_produto):
    produto = ProdutoModel.query.get(id)
    if produto:
        produto.nome = novo_produto['nome']
        produto.uni_medida = novo_produto['uni_medida']
        produto.qnt_estoque = novo_produto['qnt_estoque']
        produto.vir_unitaria = novo_produto['vir_unitaria']

        db.session.commit()
        return produto
    return None