from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def add_user(name, ap_pat, password, ap_mat=None, email=None, profile_picture=None, super_user=None):
    new_user = Usuario(nombre=name, apPat=ap_pat, password=password, apMat=ap_mat, email=email, profilePicture=profile_picture, superUser=super_user)
    db.session.add(new_user)
    db.session.commit()
    return 0;


def get_users():
    return Usuario.query.all()

def get_user_by_id(user_id):
    return Usuario.query.filter(Usuario.idUsuario == user_id).first()

def update_user(user_id, name=None, ap_pat=None, ap_mat=None, password=None, email=None, super_user=None):
    user = get_user_by_id(user_id)

    updates = {
        'nombre': name,
        'apPat': ap_pat,
        'apMat': ap_mat,
        'password': password,
        'email': email,
        'superUser': super_user
    }

    for key, value in updates.items():
        if value is not None:
            setattr(user, key, value)
    
    db.session.commit()
    
    return 0;

    

def change_user_name(user_id, new_name):
    user = get_user_by_id(user_id)
    if user:
        user.nombre = new_name
        db.session.commit()
        return True
    else:
        return False

def delete_user(user_id):
    user = get_user_by_id(user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False

def delete_all_users():
    users = Usuario.query.all()

    for user in users:
        db.session.delete(user)

    db.session.commit()