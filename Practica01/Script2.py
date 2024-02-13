
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
    """
    Clase que representa un nodo en un arbol binario ordenado
    """

    def __init__(self, datos):
        """
        Constructor para la clase nodo
        :param datos: el valor que tendrá el nodo
        :attribute valor: el valor del nodo
        :attribute izquierdo: la referencia al nodo izquierdo
        :attribute derecho: la referencia al nodo derecho
        :attribute padre: la referencia al nodo padre
        """
        self.valor = datos
        self.izquierdo = None
        self.derecho = None
        self.padre = None

    def agrega(self, valor):
        """
        Agrega un nodo al arbol binario ordenado. Los nodos con valores menores o iguales
        son agregados al subarbol izquierdo.
        :param valor: el valor que tendrá el nuevo nodo
        """
        if valor <= self.valor:
            if self.izquierdo is None:
                self.izquierdo = Nodo(valor)
                self.izquierdo.padre = self
            else:
                self.izquierdo.agrega(valor)
        else:
            if self.derecho is None:
                self.derecho = Nodo(valor)
                self.derecho.padre = self
            else:
                self.derecho.agrega(valor)

    def pre_orden(self):
        """
        Recorrido preorden del árbol. Imprime el valor del nodo actual y después realiza las llamadas
        al subárbol izquierdo y derecho.
        """
        print(self.valor, end=" ")
        if self.izquierdo is not None:
            self.izquierdo.pre_orden()
        if self.derecho is not None:
            self.derecho.pre_orden()

    def post_orden(self):
        """
        Recorrido postorden del árbol. Realiza las llamadas al subárbol izquierdo y derecho,
        posteriormente se imprime el nodo actual
        :return:
        """
        if self.izquierdo is not None:
            self.izquierdo.post_orden()
        if self.derecho is not None:
            self.derecho.post_orden()
        print(self.valor, end=" ")

    def in_orden(self):
        """
        Recorrido inordern del árbol. Realiza la llamada al subárbol izquierdo, después
        imprime el nodo actual y finalmente realiza la llamada al subárbol derecho
        :return:
        """
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

    print("Pre-orden: ", end="")
    nodo.pre_orden()
    print(" ")
    print("In-orden: ", end="")
    nodo.in_orden()
    print(" ")
    print("Post-orden: ", end="")
    nodo.post_orden()


