class Nodo:

    def __init__(self):
        self.col = 0
        self.fil = 0
        self.dato = ""
        self.dom = ""
        self.letra = ""
        self.arriba = None
        self.abajo = None
        self.anterior = None
        self.siguiente = None
        self.atras = None
        self.adelante = None


class Matriz:

    raiz = Nodo()
    node = raiz

    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
              "N", "M" "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y",
              "Z"]

    def __init__(self):
        self.raiz.dato = "Raiz"

    def matrizVacia(self):
        if self.raiz.siguiente is None or self.raiz.abajo is None:
            return True
        else:
            return False

    def existeColumna(self, dominio):
        bandera = False
        auxiliarColumnas = self.raiz.siguiente
        while auxiliarColumnas is not None:
            if auxiliarColumnas.dato == dominio:
                bandera = True
                break
            auxiliarColumnas = auxiliarColumnas.siguiente
        return bandera

    def existeFila(self, letter):
        bandera = False
        auxiliarFilas = self.raiz.abajo
        while auxiliarFilas is not None:
            if auxiliarFilas.dato == letter:
                bandera = True
                break
            auxiliarFilas = auxiliarFilas.abajo
        return bandera


# CREA LAS CABEZERAS QUE CONTENTRAN A LOS DOMINIOS DE LA MATRIZ DISPERSA
    def crearCabezeraDominio(self, dominio):

        auxiliar = self.raiz.siguiente
        nuevo = Nodo()
        nuevo.dato = dominio
        if self.matrizVacia() is True:
            self.raiz.siguiente = nuevo
            nuevo.anterior = self.raiz
            return nuevo
        else:
            while auxiliar.siguiente is not None:
                auxiliar = auxiliar.siguiente
            auxiliar.siguiente = nuevo
            nuevo.anterior = auxiliar
            return nuevo

# CREA LAS CABECERAS PARA LAS LETRAS Y LAS ORDENA EN ORDEN ALFABETICO
    def crearCabezeraDeLetras(self, letter):
        bandera = 0
        auxiliar = self.raiz.abajo
        nuevo = Nodo()
        nuevo.dato = letter
        if self.matrizVacia() is True:
            self.raiz.abajo = nuevo
            nuevo.arriba = self.raiz
        else:
            while auxiliar is not None:
                if letter < auxiliar.dato:
                    bandera = 1
                    break
                if auxiliar.abajo is not None:
                    auxiliar = auxiliar.abajo
                else:
                    break
            if bandera == 1:
                auxiliar.arriba.abajo = nuevo
                nuevo.arriba = auxiliar.arriba
                nuevo.abajo = auxiliar
                auxiliar.arriba = nuevo
            if bandera == 0:
                auxiliar.abajo = nuevo
                nuevo.arriba = auxiliar
        return nuevo

    def ingresarAMatriz(self, dominio, letra, dato):
        if self.existeColumna(dominio) is False and self.existeFila(letra) is False:
            print("PrimerCaso")
            punteroCol = self.crearCabezeraDominio(dominio)
            punterofil = self.crearCabezeraDeLetras(letra)
            nuevo = Nodo()
            nuevo.dato = dato
            nuevo.letra = letra
            nuevo.dominio = dominio
            punteroCol.abajo = nuevo
            nuevo.arriba = punteroCol
            punterofil.siguiente = nuevo
            nuevo.anterior = punterofil
            return None
        if self.existeColumna(dominio) is False and self.existeFila(letra) is True:
            print("SegundoCaso")
            punteroCol = self.crearCabezeraDominio(dominio)
            punteroFil = self.encuentraFila(letra)
            posicion = self.recorreLaFilaDeLetra(punteroFil)
            nuevo = Nodo()
            nuevo.dato = dato
            nuevo.letra = letra
            nuevo.dominio = dominio
            punteroCol.abajo = nuevo
            nuevo.arriba = punteroCol
            posicion.siguiente = nuevo
            nuevo.anterior = posicion
            return None
        if self.existeColumna(dominio) is True and self.existeFila(letra) is False:
            print("TercerCaso")
            punteroCol = self.encuentraColumna(dominio)
            punterofil = self.crearCabezeraDeLetras(letra)
            nuevo = Nodo()
            nuevo.dato = dato
            nuevo.letra = letra
            nuevo.dominio = dominio
            nodoColocado = self.recorreLaColumnaDeDominios(punteroCol, nuevo)
            punterofil.siguiente = nodoColocado
            nodoColocado.anterior = punterofil
            return None
        if self.existeColumna(dominio) is True and self.existeFila(letra) is True:
            print("CuartoCaso")
            punteroCol = self.encuentraColumna(dominio)
            punteroCol.dominio = dominio
            punterofil = self.encuentraFila(letra)
            punterofil.letra = letra
            nuevo = Nodo()
            nuevo.dato = dato
            nuevo.letra = letra
            nuevo.dominio = dominio
            colFil = self.colocaDatoEnFilaConPosicionCorrecta(punterofil, dominio, nuevo)
            if colFil is not None:
                self.colocarDatoEnColumnaConPosicionCorrecta(punteroCol, colFil)

# ESTE METODO ME BUSCA LA FILA CUANDO LA LETRAS COINCIDEN
    def encuentraFila(self, letra):
        nodoBusquedad = self.raiz
        while nodoBusquedad is not None:
            if nodoBusquedad.dato == letra:
                break

            if nodoBusquedad.abajo is not None:
                nodoBusquedad = nodoBusquedad.abajo
            else:
                break
        return nodoBusquedad

# ESTE METODO ME BUSCA LA COLUMNA CUANDO LOS DOMINIOS COINCIDEN

    def encuentraColumna(self, dominio):
        nodoBusquedad = self.raiz
        while nodoBusquedad is not None:
            if nodoBusquedad.dato == dominio:
                break
            if nodoBusquedad.siguiente is not None:
                nodoBusquedad = nodoBusquedad.siguiente
            else:
                break
        return nodoBusquedad

# ESTE METODO SE ENCARGA DE RECORRER LAS FILA DE LAS LETRAS PARA ENCONTRAR
# SU INTERSECCIÓN CON LA COLUMNA
    def recorreLaFilaDeLetra(self, nodoB):
        retorno = None
        while nodoB.siguiente is not None:
            nodoB = nodoB.siguiente
        retorno = nodoB
        return retorno

# ESTE MEDTOODO SE ENCARGA DE RECORRER LAS COLUMNAS DEL DOMINIO
# CONRRESPONDIENTE cuando la columna existe y la letra no
    def recorreLaColumnaDeDominios(self, nodoB, nuevo):
        bandera = 0
        retorno = None
        while nodoB.abajo is not None:
            if nuevo.letra < nodoB.abajo.letra:
                bandera = 1
                break
            if nodoB.abajo is not None:
                nodoB = nodoB.abajo
        if bandera == 1:
            nodoB.abajo.arriba = nuevo
            nuevo.abajo = nodoB.abajo
            nodoB.abajo = nuevo
            nuevo.arriba = nodoB
        if bandera == 0:
            nodoB.abajo = nuevo
            nuevo.arriba = nodoB

        retorno = nuevo
        return retorno

    # CUANDO FILA Y COLUMNAS EXITEN USARE ESTE METODO QUE COLOCA EL DATO EN POSICION CORRECTA
    def colocaDatoEnFilaConPosicionCorrecta(self, nodoB, dominio, nuevo):
        bandera = 0
        retorno = None
        while nodoB.siguiente is not None:
            if self.devuelvemeElIndiceDelDominio(dominio) < self.devuelvemeElIndiceDelDominio(nodoB.siguiente.dominio):
                bandera = 1
                break
            if self.devuelvemeElIndiceDelDominio(dominio) == self.devuelvemeElIndiceDelDominio(nodoB.siguiente.dominio):
                bandera = 2
                break
            if nodoB.siguiente is not None:
                nodoB = nodoB.siguiente
            else:
                break
        if bandera == 1:
            nodoB.siguiente.anterior = nuevo
            nuevo.siguiente = nodoB.siguiente
            nodoB.siguiente = nuevo
            nuevo.anterior = nodoB
            retorno = nuevo
        if bandera == 0:
            nodoB.siguiente = nuevo
            nuevo.anterior = nodoB
            retorno = nuevo
        if bandera == 2:
            retorno = None
            self.colocaEnLaTerceraDimensionDelCubo(nodoB.siguiente, nuevo)

        #retorno = nuevo
        return retorno

    def colocaEnLaTerceraDimensionDelCubo(self, nodoB, nuevo):
        while True:
            if nodoB.adelante is None:
                print("3D")
                break
            nodoB = nodoB.adelante
        nodoB.adelante = nuevo
        nuevo.atras = nodoB
        return nuevo

    def colocarDatoEnColumnaConPosicionCorrecta(self, nodoB, nuevo):
        bandera = 0
        retorno = None
        while nodoB.abajo is not None:
            if nuevo.letra < nodoB.abajo.letra:
                bandera = 1
                break
            if nodoB.abajo is not None:
                nodoB = nodoB.abajo
        if bandera == 1:
            nodoB.abajo.arriba = nuevo
            nuevo.abajo = nodoB.abajo
            nodoB.abajo = nuevo
            nuevo.arriba = nodoB
        if bandera == 0:
            nodoB.abajo = nuevo
            nuevo.arriba = nodoB
        retorno = nuevo
        return retorno

    def printDomains(self):
        auxiliar = self.raiz.siguiente
        while auxiliar is not None:
            print(" | " + str(auxiliar.dato) + " | ")
            auxiliar = auxiliar.siguiente

    def printLetters(self):
        auxiliar = self.raiz.abajo
        while auxiliar is not None:
            print(" | " + str(auxiliar.dato) + " | ")
            auxiliar = auxiliar.abajo

    def moverAbajo(self):
        if self.node.abajo is not None:
            self.node = self.node.abajo
            print(str("| " + self.node.dato + " |"))

    def moverArriba(self):
        if self.node.arriba is not None:
            self.node = self.node.arriba
            print(str("| " + self.node.dato + " |"))

    def moverSiguiente(self):
        if self.node.siguiente is not None:
            self.node = self.node.siguiente
            print(str("| " + self.node.dato + " |"))

    def moverAnterior(self):
        if self.node.anterior is not None:
            self.node = self.node.anterior
            print(str("| " + self.node.dato + " |"))

    def moverAdelante(self):
        if self.node.adelante is not None:
            self.node = self.node.adelante
            print(str("| " + self.node.dato + " |"))

    def moverAtras(self):
        if self.node.atras is not None:
            self.node = self.node.atras
            print(str("| " + self.node.dato + " |"))

    def devuelvemeElIndiceDelDominio(self, dominio):
        index = 0
        nodoB = self.raiz
        while nodoB.siguiente is not None:
            if nodoB.siguiente.dato == dominio:
                break
            index = index + 1
            nodoB = nodoB.siguiente
        return index

    def nombresConletra(self, letra):
        aux = self.encuentraFila(letra)
        retorno = ""
        while aux is not None:
            if aux.dato is not None:
                retorno = retorno + "| " + str(aux.dato) + " |---->"
                retorno = retorno + str(self.recorreSubListaDeNombres(aux)) + "\n"
            aux = aux.siguiente
        return retorno

    def recorreSubListaDeNombres(self, aux):
        aux1 = aux.adelante
        retorno = ""
        while aux1 is not None:
            retorno = retorno + " | " + str(aux1.dato) + " |----->"
            aux1 = aux1.adelante
        return retorno

    def nombresConDominio(self, dominio):
        aux = self.encuentraColumna(dominio)
        retorno = ""
        while aux is not None:
            if aux.dato is not None:
                retorno = retorno + " | " + str(aux.dato) + " |----->"
                retorno = retorno + str(self.recorreSubListaDeNombres(aux)) + "\n"
            aux = aux.abajo
        return retorno
