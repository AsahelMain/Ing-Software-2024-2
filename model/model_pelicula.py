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

def delete_movie(movie_id):
    movie = get_movie_by_id(movie_id)

    if movie:
        db.session.delete(movie)
        db.session.commit()
        return True
    else: 
        return False

def delete_all_movies():
    movies = Pelicula.query.all()

    for movie in movies:
        db.session.delete(movie)
        
    db.session.commit()