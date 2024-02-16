def juego(jugador1, jugador2):
    puntuaciones = ["0", "15", "30", "40", "Adv"]
    puntuacion_jugador1 = 0
    puntuacion_jugador2 = 0

    while abs(puntuacion_jugador1 - puntuacion_jugador2) < 2 or max(puntuacion_jugador1, puntuacion_jugador2) <= 3:
        input_valido = False
        while not input_valido:
            try:
                ganador_punto = input("Ingrese el jugador que ganará el siguiente punto: ")
                if ganador_punto not in [jugador1, jugador2]:
                    raise ValueError("Input no válido")
                input_valido = True
            except ValueError as e:
                print(e)
                print("Ese jugador no existe :/ Intenta de nuevo!")

        if ganador_punto == jugador1:
            puntuacion_jugador1 += 1
        else:
            puntuacion_jugador2 += 1

        if puntuacion_jugador1 == 4 and puntuacion_jugador2 == 4:
            puntuacion_jugador1 -= 1
            puntuacion_jugador2 -= 1

        if abs(puntuacion_jugador1 - puntuacion_jugador2) < 2 or max(puntuacion_jugador1, puntuacion_jugador2) <= 3:
            print(f"Puntuación actual: {puntuaciones[puntuacion_jugador1]} - {puntuaciones[puntuacion_jugador2]}")

    if puntuacion_jugador1 > puntuacion_jugador2:
        print(f"El jugador que ganó el juego es {jugador1}")
        return True
    else:
        print(f"El jugador que ganó el juego es {jugador2}")
        return False



def set(jugador1, jugador2, contador_sets, saque):
    juegos_jugador1 = 0
    juegos_jugador2 = 0
    contador_juegos = 1

    while abs(juegos_jugador1 - juegos_jugador2) < 2 or (juegos_jugador1 < 6 and juegos_jugador2 < 6):
        print(f"Set {contador_sets} - Juego: {contador_juegos}  Sirve: {saque}")
        print("----------------------")
        contador_juegos += 1
        if(juego(jugador1, jugador2)):
            juegos_jugador1 += 1
        else:
            juegos_jugador2 += 1
        saque = jugador1 if saque == jugador2 else jugador2

        print(f"\nMarcador de juegos: {juegos_jugador1} - {juegos_jugador2}")
        if (juegos_jugador1 + juegos_jugador2) % 2 != 0:
            print("--- Cambio de cancha ---")

    if juegos_jugador1 > juegos_jugador2:
        print(f"El jugador que ganó el set es {jugador1}")
        return True
    else:
        print(f"El jugador que ganó el set es {jugador2}")
        return False

def partido():
    print("El partido consistirá de 3 sets.")
    jugador1 = input("Cuál es el nombre del jugador 1?: ")
    jugador2 = input("Cuál es el nombre del jugador 2?: ")
    num_sets_jugador1 = 0
    num_sets_jugador2 = 0

    contador_sets = 1
    saque = jugador1


    for i in range(3):
        if(set(jugador1, jugador2, contador_sets, saque)):
            num_sets_jugador1 += 1
        else:
            num_sets_jugador2 += 1

        print(f"Marcador de sets: {num_sets_jugador1} - {num_sets_jugador2}")

        if num_sets_jugador1 >= 2:
            print("El jugador que resultó ganador en el partido fue: ", jugador1)
            break
        elif num_sets_jugador2 >= 2:
            print("El jugador que resultó ganador en el partido fue: ", jugador2)
            break
        contador_sets += 1

        saque = jugador1 if saque == jugador2 else jugador2

if __name__ == '__main__':
    partido()

