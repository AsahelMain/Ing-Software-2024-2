from flask import Blueprint, request, render_template, flash, url_for
from model import model_pelicula

blueprint_pelicula = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@blueprint_pelicula.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('agrega_pelicula.html')
    else:
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']
        super_user = request.form['super_user']
        
        is_super_user = super_user == 'yes'

        try:
            model_usuario.add_user(name,ap_pat,password,ap_mat,email,None,is_super_user)
            return render_template('resultado.html', titulo="Agregar usuario", resultado="Se agregó el usuario exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Agregar usuario", resultado="Ocurrió un problema al agregar el usuario :(")


