from connection import db
from sqlalchemy import Integer, DATETIME, String
from sqlalchemy.orm import relationship
from passlib.context import CryptContext

class RegistroModel(db.Model):
    __tablename__ = 'registros'

    id = db.Column(Integer, primary_key=True, autoincrement=True)
    dth_registro = db.Column(DATETIME, nullable=False)
    tipo = db.Column(String(120), nullable=False)
    id_produto = db.Column(Integer, db.ForeignKey('categorias.id',ondelete="CASCADE"), nullable=False)

    registro = relationship(
            "Registro",
            back_populates="produtos"
        )

    def __init__(self, id, dth_registro, tipo):
        self.id = id
        self.dth_registro = dth_registro
        self.tipo = tipo