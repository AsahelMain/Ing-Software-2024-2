
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

if __name__ == '__main__':
    print(numero_de_valles("UDDU"))
    print(numero_de_valles("UDUUDDDUDU"))