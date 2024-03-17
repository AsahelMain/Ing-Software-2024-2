from flask import Blueprint, request, render_template, flash, url_for
from model import model_renta
from datetime import datetime

blueprint_renta = Blueprint('renta', __name__, url_prefix='/renta')

@blueprint_renta.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'GET':
        return render_template('agrega_renta.html')
    else:
        user_id = request.form['user_id']
        movie_id = request.form['movie_id']
        rent_date = request.form['rent_date']
        rent_days = request.form['rent_days']
        status = request.form['status']

        status = status == 'true'

        try:
            model_renta.add_rent(user_id, movie_id, rent_date, rent_days, status)
            return render_template('resultado.html', titulo="Agregar renta", resultado="Se agregó la renta exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Agregar renta", resultado="Ocurrió un problema al agregar la renta :(")

@blueprint_renta.route('/consultar', methods=['GET'])
def consultar_usuarios():
    try:
        rentas = model_renta.get_rents()
        fecha_actual = datetime.now()
        return render_template('consultar_rentas.html', rentas=rentas, fecha_actual=fecha_actual)
    except Exception as e:
        print(e)
        return render_template('resultado.html', titulo="Consultar rentas", resultado="Ocurrió un problema al consultar las rentas :/")
    


