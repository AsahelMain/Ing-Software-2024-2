from flask import Flask
from sqlalchemy import and_, or_, select

from alchemyClasses import db
from alchemyClasses.Usuario import Usuario
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta

from model.model_usuario import *
from model.model_pelicula import *
from model.model_renta import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://asmc:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        print("Menu: ")
        print("1. Ver los registros de una tabla")
        print("2. Filtrar los registros de una tabla por id")
        print("3. Actualizar la columna nombre de un registro")
        print("4. Eliminar un registro por id o todos los registros")
      
        opcion = 7777
        while opcion < 1 or opcion > 4:
            opcion = int(input("Ingresa la accion que deseas realizar: "))
            if opcion < 1 or opcion > 4:
                print("Ingresa una opcion válida")
        
        if opcion == 1:
            print("Tablas disponibles:")
            print("1. Usuario")
            print("2. Peliculas")
            print("3. Rentar")
            
            tabla = -1

            while tabla < 1 or tabla > 3:
                try:
                    tabla = int(input("Ingresa la tabla de la que quieres ver los registros: "))
                    if opcion < 1 or tabla > 3:
                        print("Ingresa una tabla válida")
                except ValueError:
                    print("Ingresa una tabla válida")

            if tabla == 1:
                print("La tabla usuarios tiene los siguientes registros: \n")
                get_users()

            elif tabla == 2:
                print("La tabla películas tiene los siguientes registros: \n")
                get_movies()
            
            elif tabla == 3:
                print("La tabla renta tienes los siguientes registros: \n")
                get_rents()
            

            

        elif opcion == 2:
            print("Tablas disponibles:")
            print("1. Usuario")
            print("2. Peliculas")
            print("3. Rentar")
            
            tabla = -1

            while tabla < 1 or tabla > 3:
                try:
                    tabla = int(input("Ingresa la tabla de la que quieres ver los registros: "))
                    if opcion < 1 or tabla > 3:
                        print("Ingresa una tabla válida")
                except ValueError:
                    print("Ingresa una tabla válida")

            if tabla == 1:
                user_id = int(input("Ingresa el id del usuario que deseas consultar: "))
                print(f'El usuario con id {user_id} tiene los siguientes datos: ')
                get_user_by_id(user_id)

            elif tabla == 2:
                movie_id = int(input("Ingresa el id de la pelicula que deseas consultar: "))
                print(f'La pelicula con id {movie_id} tiene los siguientes datos: ')
                get_movie_by_id(movie_id)
            
            elif tabla == 3:
                rent_id = int(input("Ingresa el id de la renta que deseas consultar: "))
                print(f'La renta con id {rent_id} tiene los siguientes datos: ')
                get_rent_by_id(rent_id)
        
        elif opcion == 3:
            print("3")
        
        elif opcion == 4:
            print("Eliminar registro/s: ")
            print("1. Por id")
            print("2. Eliminar todos los registros")

            accion = -1
            while accion < 1 or accion > 2:
                accion = int(input("Ingresa la opcion que deseas realizar:"))
                if accion < 1 or accion > 2:
                    print("Ingresa una opcion valida")
            
            
      
