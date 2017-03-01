# Clase de la cola en python

import os


class NodoCola:

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class Cola:

    def __init__(self):
        self.cabeza = None
        self.ultimo = None

    def estaVacia(self):
        if self.cabeza == None:
            return True
        else:
            return False

    def insertarCola(self, Nodo):
        if self.estaVacia() == True:
            self.cabeza = Nodo
            self.ultimo = Nodo
            self.cabeza.siguiente = self.ultimo
        else:
            self.ultimo.siguiente = Nodo
            self.ultimo = Nodo

    def desencolar(self):
        if self.estaVacia() == True:
            retornar = "NO HAY NADA"
            return retornar
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

    def showCola(self):
        if self.estaVacia() == True:
            return "Cola Vacía!"
        else:
            retorno = ""
            aux = self.cabeza
            while aux != self.ultimo.siguiente:
                retorno = retorno + " | " + str(aux.numero) + " |---->"
                aux = aux.siguiente
            return str(retorno)
