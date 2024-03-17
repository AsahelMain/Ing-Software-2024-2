from flask import Blueprint, request, render_template, flash, url_for
from model import model_pelicula

blueprint_pelicula = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@blueprint_pelicula.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'GET':
        return render_template('agrega_pelicula.html')
    else:
        name = request.form['name']
        stock = request.form['stock']
        genre = request.form['genre']
        length = request.form['length']

        try:
            model_pelicula.add_movie(name,stock,genre,length)
            return render_template('resultado.html', titulo="Agregar película", resultado="Se agregó la película exitosamente :)")
        except Exception as e:
            print(e)
            return render_template('resultado.html', titulo="Agregar película", resultado="Ocurrió un problema al agregar la película :(")

@blueprint_pelicula.route('/consultar', methods=['GET'])
def consultar_usuarios():
    try:
        peliculas = model_pelicula.get_movies()
        return render_template('consultar_peliculas.html', peliculas=peliculas)
    except Exception as e:
        print(e)
        return render_template('resultado.html', titulo="Consultar peliculas", resultado="Ocurrió un problema al consultar las películas :/")

    


