from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def get_movies():
    for movie in Pelicula.query.all():
        print(f'{movie}\n')

def get_movie_by_id(movie_id):
    print(f'{Pelicula.query.filter(Pelicula.idPelicula == movie_id).first()}\n')