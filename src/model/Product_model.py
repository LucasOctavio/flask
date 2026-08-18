from connection import db
from sqlalchemy import Float, Integer,String, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

class ProdutoModel(db.Model):
    __tablename__ = 'produtos'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    nome = db.Column(String(120), nullable=False)
    uni_medida = db.Column(String(120), nullable=False)
    qnt_estoque = db.Column(Integer, nullable=False)
    vir_unitaria = db.Column(Float, nullable=False)
    id_categoria = db.Column(Integer, db.ForeignKey('categorias.id',ondelete="CASCADE"), nullable=False)




    registro = db.relationship(
        "registro", 
        back_populates="registro",
        cascade="all, delete",
        passive_deletes=True
    )
    produto = db.relationship(
        "id",
        back_populates="consumo"
    )
    categoria = relationship(
            "Categoria",
            back_populates="produtos"
        )


    def __init__(self, id, nome, uni_medida, qnt_estoque, vir_unitaria):
        self.id = id
        self.nome = nome
        self.uni_medida = uni_medida
        self.qnt_estoque = qnt_estoque
        self.vir_unitaria = vir_unitaria