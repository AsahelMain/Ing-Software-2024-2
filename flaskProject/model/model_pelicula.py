from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db

def add_movie(nombre, inventario=1, genero=None, duracion=None):
    new_movie = Pelicula(nombre=nombre, inventario=inventario, genero=genero, duracion=duracion)
    db.session.add(new_movie)
    db.session.commit()
    return 0;


def get_movies():
    return Pelicula.query.all()

def get_movie_by_id(movie_id):
    return Pelicula.query.filter(Pelicula.idPelicula == movie_id).first()


def update_movie(movie_id, name=None, genre=None, length=None, stock=None):
    movie = get_movie_by_id(movie_id)
    
    updates = {
        'idPelicula': movie_id,
        'nombre': name,
        'genero': genre,
        'duracion': length,
        'inventario': stock,
    }

    for key, value in updates.items():
        if value is not None:
            setattr(movie, key, value)
    
    db.session.commit()
    
    return 0;

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