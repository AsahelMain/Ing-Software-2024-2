from flask import Blueprint, request, render_template, flash, url_for
from model import model_usuario

blueprint_usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@blueprint_usuario.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'GET':
        return render_template('agrega_usuario.html')
    else:
        name = request.form['name'] or None
        ap_pat = request.form['ap_pat'] or None
        ap_mat = request.form['ap_mat'] or None
        password = request.form['password'] or None
        email = request.form['email'] or None
        super_user = request.form['super_user'] or None
        
        is_super_user = super_user == 'yes'

        try:
            model_usuario.add_user(name,ap_pat,password,ap_mat,email,None,is_super_user)
            return render_template('resultado.html', titulo="Agregar usuario", resultado="Se agregó el usuario exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Agregar usuario", resultado="Ocurrió un problema al agregar el usuario :(")

@blueprint_usuario.route('/consultar', methods=['GET'])
def consultar_usuarios():
    try:
        usuarios = model_usuario.get_users()
        return render_template('consultar_usuarios.html', usuarios=usuarios)
    except Exception as e:
        print(e)
        return render_template('resultado.html', titulo="Consultar usuarios", resultado="Ocurrió un problema al consultar los usuarios :/")

@blueprint_usuario.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == 'GET':
        return render_template('actualiza_usuario.html')
    else:
        user_id = request.form['id'] or None
        name = request.form['name'] or None
        ap_pat = request.form['ap_pat'] or None
        ap_mat = request.form['ap_mat'] or None
        password = request.form['password'] or None
        email = request.form['email'] or None
        super_user = request.form['super_user']

        is_super_user = super_user == 'yes'

        try:
            model_usuario.update_user(user_id, name, ap_pat, ap_mat, password, email, is_super_user)
            return render_template('resultado.html', titulo="Actualiza usuario", resultado="Se actualizó el usuario exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Actualiza usuario", resultado="Ocurrió un problema al actualizar el usuario :(")

@blueprint_usuario.route('/eliminar', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'GET':
        return render_template('elimina_usuario.html')
    else:
        user_id = request.form['user_id'] or None

        try:
            model_usuario.delete_user(user_id)
            return render_template('resultado.html', titulo="Elimina usuario", resultado="Se eliminó el usuario exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Elimina usuario", resultado="Ocurrió un problema al eliminar el usuario :(")