class NodoLista:

    def __init__(self, palabra):
        self.palabra = palabra
        self.siguiente = None


class Lista:

    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    def estaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def insertarALista(self, Nodo):
        if self.estaVacia() == True:
            self.cabeza = Nodo
            self.ultimo = Nodo
            self.cabeza.siguiente = self.ultimo
        else:
            self.ultimo.siguiente = Nodo
            self.ultimo = Nodo

    def buscarPalabra(self, palabra):
        bandera = False
        if self.estaVacia() == True:
            return "Lista Vacia!"
        else:
            contador = 0
            indexfound = 0
            aux = self.cabeza
            while aux != None:
                if aux.palabra == palabra:
                    bandera = True
                    indexfound = contador
                aux = aux.siguiente
                contador = contador + 1
            if bandera == True:
                return "Encontrado en Inidice: " + str(indexfound)
            else:
                return "NO SE ENCONTRO"

    def eliminarDeLista(self, index):
        if self.estaVacia() == True:
            return "Lista Vacia"
        else:
            if index == 0:
                self.cabeza = self.cabeza.siguiente
                return "Elemento Eliminado"
            else:
                contador = 1
                aux = self.cabeza
                aux2 = self.cabeza
                while aux.siguiente != None:
                    aux = aux.siguiente
                    if index == contador:
                        break
                    aux2 = aux2.siguiente
                    contador = contador + 1
                aux2.siguiente = aux.siguiente
                return "Elemento eliminado en Indice " + str(contador)

    def showList(self):
        if self.estaVacia() == True:
            return "Lista Vacia"
        else:
            retorno = ""
            aux = self.cabeza
            while aux != None:
                retorno = retorno + " | " + str(aux.palabra) + " |---->"
                aux = aux.siguiente
            return retorno
