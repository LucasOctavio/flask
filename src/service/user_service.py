from model import UsuarioModel
from connection import db

#CREATE
def cadastrar_usuario(usuario):
    usuario_db = UsuarioModel(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.gen_senha(usuario.senha)
    db.session.add(usuario_db)
    db.session.commit()
    return usuario_db

#READ
#listagem dos usuarios
def listar_usuario():
    return UsuarioModel.query.all()

#listagem dos usuarios por id
def listar_usuario_id(id):
    usuario_encontrado = UsuarioModel.query.get(id)
    return usuario_encontrado

#listagem dos usuario por email
def listar_usuario_email(email):
    return UsuarioModel.query.filter_by(email=email).first()

#DELETE
def deletar_usuario(id):
    usuario = UsuarioModel.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
        return True
    return False

#UPDATE
def editar_usuario(id, novo_usuario):
    usuario = UsuarioModel.query.get(id)
    if usuario:
        usuario.nome = novo_usuario['nome']
        usuario.email = novo_usuario['email']
        if novo_usuario.get('senha'):
            usuario.gen_senha(novo_usuario['senha'])

        db.session.commit()
        return usuario
    return None