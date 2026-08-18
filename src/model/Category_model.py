from connection import db
from sqlalchemy import INTEGER, DATETIME, String, relationship
from passlib.context import CryptContext

class CategoriaModel(db.Model):
    __tablename__ = 'categorias'

    id = db.Column(INTEGER, primary_key=True, autoincrement=True)
    descricao = db.Column(String, nullable=False)

    categoria = relationship(
    "Produto", 
    back_populates="produtos",
    cascade="all, delete",
    passive_deletes=True
    )
    
    def __init__(self, descricao):
        self._descricao = descricao
