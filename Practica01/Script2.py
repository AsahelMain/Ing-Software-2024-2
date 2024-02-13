
def numero_de_valles(cadena):
    """
    Calcula el numero de valles de una cadena

    :param cadena: cadena formada por caracteres 'D' y 'U'
    :return: numero de valles
    """
    contador = 0
    es_valle = False
    respuesta = 0
    for letra in cadena:
        if letra == 'U':
            contador += 1
        else:
            contador -= 1
        if es_valle and contador == 0:
            es_valle = False
            respuesta += 1

        if contador < 0:
            es_valle = True
    return respuesta

def validar_input_valles(cadena):
    caracteres_validos = {'D', 'U'}
    return all(caracter in caracteres_validos for caracter in cadena)

if __name__ == '__main__':
    cadena = input("Ingrese una cadena que consista solo de caracteres 'D' y 'U': ")
    while not validar_input_valles(cadena):
        print("Cadena invalida.")
        cadena = input("Ingrese una cadena que consista solo de caracteres 'D' y 'U': ")
    print(numero_de_valles(cadena))


