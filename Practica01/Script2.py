
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

class Nodo:
    def __init__(self, datos):
        self.valor = datos
        self.izquierdo = None
        self.derecho = None
        self.padre = None

    def agrega(self, valor):
        if valor <= self.valor:
            if self.izquierdo is None:
                self.izquierdo = Nodo(valor)
            else:
                self.izquierdo.agrega(valor)
        else:
            if self.derecho is None:
                self.derecho = Nodo(valor)
            else:
                self.derecho.agrega(valor)

    def pre_orden(self):
        print(self.valor, end=" ")
        if self.izquierdo is not None:
            self.izquierdo.pre_orden()
        if self.derecho is not None:
            self.derecho.pre_orden()

    def post_orden(self):
        if self.izquierdo is not None:
            self.izquierdo.post_orden()
        if self.derecho is not None:
            self.derecho.post_orden()
        print(self.valor, end=" ")

    def in_orden(self):
        if self.izquierdo is not None:
            self.izquierdo.in_orden()
        print(self.valor, end=" ")
        if self.derecho is not None:
            self.derecho.in_orden()


if __name__ == '__main__':
    cadena = input("Ingrese una cadena que consista solo de caracteres 'D' y 'U': ")
    while not validar_input_valles(cadena):
        print("Cadena invalida.")
        cadena = input("Ingrese una cadena que consista solo de caracteres 'D' y 'U': ")
    print("Numero de valles ", numero_de_valles(cadena))

    nodo = Nodo(10)
    nodo.agrega(5)
    nodo.agrega(16)
    nodo.agrega(2)
    nodo.agrega(8)
    nodo.agrega(1)
    nodo.agrega(3)
    nodo.agrega(12)
    nodo.agrega(18)

    nodo.pre_orden()
    print(" ")
    nodo.in_orden()
    print(" ")
    nodo.post_orden()


