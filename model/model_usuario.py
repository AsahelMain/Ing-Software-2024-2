from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def get_users():
    for user in Usuario.query.all():
        print(f'{user}\n')

def get_user_by_id(user_id):
    return Usuario.query.filter(Usuario.idUsuario == user_id).first()

def change_user_name(user_id, new_name):
    user = get_user_by_id(user_id)
    if user:
        user.nombre = new_name
        db.session.commit()
        return True
    else:
        return False
