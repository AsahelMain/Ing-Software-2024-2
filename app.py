from flask import Flask
from sqlalchemy import and_, or_

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
      
        opcion = 0
        while opcion not in [1,2,3,4]:
            try:
                opcion = int(input("Ingresa la accion que deseas realizar: "))
                if opcion not in [1,2,3,4]:
                    print("Ingresa una opcion válida")
            except ValueError:
                print("Ingresa una opcion válida")
        
        if opcion == 1:
            print("Tablas disponibles:")
            print("1. Usuario")
            print("2. Peliculas")
            print("3. Rentar")
            
            tabla = 0
            while tabla not in [1,2,3]:
                try:
                    tabla = int(input("Ingresa la tabla de la que quieres ver los registros: "))
                    if tabla not in [1,2,3]:
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
            
            tabla = 0
            while tabla not in [1,2,3]:
                try:
                    tabla = int(input("Ingresa la tabla de la que quieres ver los registros: "))
                    if tabla not in [1,2,3]:
                        print("Ingresa una tabla válida")
                except ValueError:
                    print("Ingresa una tabla válida")

            if tabla == 1:
                user_id = int(input("Ingresa el id del usuario que deseas consultar: "))
                print(f'El usuario con id {user_id} tiene los siguientes datos: ')
                print(f'{get_user_by_id(user_id)}\n')

            elif tabla == 2:
                movie_id = int(input("Ingresa el id de la pelicula que deseas consultar: "))
                print(f'La pelicula con id {movie_id} tiene los siguientes datos: ')
                print(f'{get_movie_by_id(movie_id)}\n')
            
            elif tabla == 3:
                rent_id = int(input("Ingresa el id de la renta que deseas consultar: "))
                print(f'La renta con id {rent_id} tiene los siguientes datos: ')
                print(f'{get_rent_by_id(rent_id)}\n')
        
        elif opcion == 3:
            print("Tablas disponibles:")
            print("1. Usuario")
            print("2. Peliculas")
            print("3. Rentar")
            
            tabla = 0
            while tabla not in [1,2,3]:
                try:
                    tabla = int(input("Ingresa la tabla sobre la que quieres trabajar: "))
                    if tabla not in [1,2,3]:
                        print("Ingresa una tabla válida")
                except ValueError:
                    print("Ingresa una tabla válida")
            
            if tabla == 1:
                user_id = int(input("Ingresa el id del usuario del que quieres cambiar su nombre: "))
                new_name = input("Ingresa el nuevo nombre del usuario: ")
                
                if change_user_name(user_id, new_name):
                    print("Nombre cambiado exitosamente")
                else: 
                    print("Error. Input inválido o usuario no encontrado")
            elif tabla == 2:
                movie_id = int(input("Ingresa el id de la película de la que quieres cambiar su nombre: "))
                new_name = input("Ingresa el nuevo nombre de la película: ")
                
                if change_movie_name(movie_id, new_name):
                    print("Nombre cambiado exitosamente")
                else: 
                    print("Error. Input inválido o película no encontrada")
            elif tabla == 3:
                rent_id = int(input("Ingresa el id de la renta de la que quieres cambiar la fecha: "))
                new_date = get_new_date()

                if change_rent_date(rent_id, new_date):
                    print("Fecha cambiada exitosamente")
                else:
                    print("Error. Input inválido o renta no encontrada")
        
        elif opcion == 4:
            print("Eliminar registro/s: ")
            print("1. Por id")
            print("2. Eliminar todos los registros")

            accion = -1
            while accion < 1 or accion > 2:
                accion = int(input("Ingresa la opcion que deseas realizar:"))
                if accion < 1 or accion > 2:
                    print("Ingresa una opcion valida")
            
            
      
