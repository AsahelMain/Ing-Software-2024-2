from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def get_users():
    for user in Usuario.query.all():
        print(f'{user}\n')

def get_user_by_id(user_id):
    print(f'{Usuario.query.filter(Usuario.idUsuario == user_id).first()}\n')