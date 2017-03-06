class NodoPila:

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class Pila:

    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    def estaVacia(self):
        if self.cabeza is None:
            return True
        else:
            return False

    def push(self, Nodo):
        print("EN METODO PUSH")
        if self.estaVacia() is True:
            self.cabeza = Nodo
            self.ultimo = Nodo
            self.cabeza.siguiente = self.ultimo
            print("INSERTANDO NODO")
        else:
            print("INSERTANDO NODO")
            Nodo.siguiente = self.cabeza
            self.cabeza = Nodo

    def pop(self):
        if self.estaVacia() is True:
            return "Pila Vacía!"
        else:
            if self.cabeza == self.ultimo:
                retorno = self.cabeza.numero
                self.cabeza = None
                self.ultimo = None
                return retorno
            else:
                retorno = self.cabeza.numero
                self.cabeza = self.cabeza.siguiente
                return retorno

    def showPila(self):
        if self.estaVacia() is True:
            return "Pila Vacía!"
        else:
            retorno = ""
            aux = self.cabeza
            while aux is not self.ultimo:
                retorno = retorno + " | " + str(aux.numero) + " |--->"
                print(str(aux.numero))
                aux = aux.siguiente
            return str(retorno)

    def textoParaDot(self):
        if self.estaVacia() is False:
            retorno = "digraph g {"
            aux = self.cabeza
            while aux is not self.ultimo:
                if aux.siguiente is not None:
                    retorno = "\n" + retorno + str(aux.numero) + \
                        "->" + str(aux.siguiente.numero) + ";"
                else:
                    retorno = "\n" + retorno + str(aux.numero) + ";"
                print(str(aux.numero))
                aux = aux.siguiente
            retorno = retorno + "}"
            return str(retorno)
