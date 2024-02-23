from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def get_movies():
    for movie in Pelicula.query.all():
        print(f'{movie}\n')

def get_movie_by_id(movie_id):
    return Pelicula.query.filter(Pelicula.idPelicula == movie_id).first()

def change_movie_name(movie_id, new_name):
    movie = get_movie_by_id(movie_id)
    if movie:
        movie.nombre = new_name
        db.session.commit()
        return True
    else:
        return False