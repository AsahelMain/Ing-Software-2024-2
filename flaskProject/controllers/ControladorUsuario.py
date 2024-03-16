from flask import Blueprint, request, render_template, flash, url_for

blueprint_usuario = Blueprint('usuario', __name__, url_prefix='/usuario')

@blueprint_usuario.route('/agregar', methods=['GET', 'POST'])
def agregar_alumno():
    if request.method == 'GET':
        return render_template('agrega_usuario.html')
    else:
        name = request.form['name']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']
        super_user = request.form['super_user']
        
        is_super_user = super_user == 'yes'

        
        v = randint(0, 2)
        if v == 1:
            flash("Hello from flash!")
            return url_for('alumno.agregar_alumno')
        # Y regreso al flujo que me hayan especificado.
        return render_template('user_added.html', name=name, num_cta=num_cta)