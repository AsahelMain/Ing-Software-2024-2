import pymysql
import random
import datetime

names = ["Patricio", 
          "Patricia", 
          "Omar", 
          "Abraham", 
          "Arsenio", 
          "Dulce", 
          "Alan", 
          "Jorge", 
          "Pedro",
          "Arturo",
          "Laura",
          "Carmen"
          ]

last_names = ["Garcia",
             "Gonzalez",
             "Perez",
             "Estrella",
             "Lopez",
             "Burger",
             "Paramo",
             "Verde",
             "Cholula",
             "Lechuga",
             "Selano"
            ]

movies = ["Toy Story 1",
             "Toy Story 2",
             "Toy Story 3",
             "Toy Story 4",
             "Cars 1",
             "Cars 2",
             "Cars 3",
             "Star Wars 4",
             "Star Wars 5",
             "Star Wars 6",
             ]

genre = ["Terror", "Aventura", "Misterio", "Comedia", "Fantasia"]

# 1.4 Una función que elimine todas las rentas anteriores a 3 días a la fecha en que se
# ejecuta la función
def remove_rents(connection):
    with connection.cursor() as cursor:
        limit = datetime.date.today() - datetime.timedelta(days=3)
        formatted_limit = limit.strftime("%Y-%m-%d")
        cursor.execute(
            "DELETE FROM `rentar` WHERE `fecha_renta` < %s",
            (formatted_limit,)
        )

    connection.commit()

# 1.3 Una función que dado el nombre de una película y un género, se cambia
# el género a dicha película
def change_movie_genre(connection, movie, genre):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE `peliculas` SET `genero` = %s WHERE `nombre` = %s",
            (genre, movie)
        )
    
    connection.commit()


# 1.2 Una función que filtre a la tabla Usuario a todos los usuarios cuyo
# apellido termine en alguna cadena especificada por el usuario
def filter_users(connection, filter_string):
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT * FROM `usuarios` WHERE `apPat` LIKE  %s OR `apMat` LIKE %s",
            (f"%{filter_string}", f"%{filter_string}")
        )

        output = cursor.fetchall()
        for user in output:
            print(user)

# 1.1 Una función que inserte al menos 1 registro en cada tabla
def insert(connection):
    with connection.cursor() as cursor:
        name = random.choice(names)
        last_name1 = random.choice(last_names)
        last_name2 = random.choice(last_names)
        password = "myuniquesecretpassword" + str(random.randint(1,900))
        email = name + str(random.randint(1,300)) + "@test.com"

        cursor.execute(
            "INSERT INTO `usuarios` (`nombre`, `apPat`, `apMat`, `password`, `email`, `superuser`) VALUES (%s, %s, %s, %s, %s, %s)",
            (name, last_name1, last_name2, password, email, 0)
        )
        
        user_id = cursor.lastrowid

        movie_name = random.choice(movies)
        movie_genre = random.choice(genre)
        movie_length = random.randint(80,160)
        inventario = random.randint(1,20)
        
        cursor.execute(
            "INSERT INTO `peliculas` (`nombre`, `genero`, `duracion`, `inventario`) VALUES (%s, %s, %s, %s)",
            (movie_name, movie_genre, movie_length, inventario)
        )

        movie_id = cursor.lastrowid
        rent_date = datetime.date(random.randint(2023,2024), random.randint(1, 12), random.randint(1,29))

        cursor.execute(
            "INSERT INTO `rentar` (`idUsuario`, `idPelicula`, `fecha_renta`, `dias_de_renta`, `estatus`) VALUES (%s, %s, %s, %s, %s)",
            (user_id, movie_id, rent_date, random.randint(30, 360), random.randint(0,1))
        )

    connection.commit()

if __name__ == "__main__":
    connection = pymysql.connect(
        host="localhost",
        user="asmc",
        password="Developer123!",
        database="lab_ing_software",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor)   

    insert(connection) 
    filter_string = input("Enter a string to filter users: ")
    filter_users(connection, filter_string)

    movie_name = input("Enter a movie name to change its genre: ")
    genre_name = input("Enter the new genre: ")
    change_movie_genre(connection, movie_name, genre_name)

