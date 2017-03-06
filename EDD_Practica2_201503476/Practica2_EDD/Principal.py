from flask import Flask, request
from Estructuras import Cola
from Estructuras import Pila
from Estructuras import Lista
from Estructuras import Matriz
import os

app = Flask("Practica2")

ColaPython = Cola.Cola()
pilaDePrueba = Pila.Pila()
ListaPython = Lista.Lista()
MatrizP = Matriz.Matriz()


@app.route('/Conectar')
def conectar():
    return 'Conexión Exitosa!'


# INICIO DE LOS METODOS DE COLA
@app.route('/Encolar', methods=['POST'])
def encolar():
    numero = str(request.form['dato'])
    Nodo = Cola.NodoCola(numero)
    ColaPython.insertarCola(Nodo)
    return "Elemento: " + str(numero) + " Insertado a la Cola"


@app.route('/VerCola')
def verCola():
    retorno = ColaPython.showCola()
    return str(retorno)


@app.route('/DesEncolar')
def sacarDeCola():
    return "Elemento Sacado de La Cola: " + str(ColaPython.desencolar())


@app.route('/ReporteCola')
def repCola():
    archi = open('repPila.txt', 'wt')
    archi.write(str(ColaPython.textoParaDot))
    archi.close()

    return str(ColaPython.textoParaDot())


@app.route('/Apilar', methods=['POST'])
def meterAPila():
    numero = str(request.form['numero'])
    print(numero)
    NodoParaPila = Pila.NodoPila(numero)
    pilaDePrueba.push(NodoParaPila)
    return "Elemento Apilado: " + str(numero)


@app.route('/DesApilar')
def sacarDePila():
    return "Elemento sacado de la Pila: " + str(pilaDePrueba.pop())


@app.route('/VerPila')
def verEstadoPila():
    retornoP = pilaDePrueba.showPila()
    return str(retornoP)


@app.route('/ReportePila')
def repPila():
    return str(pilaDePrueba.textoParaDot())


@app.route('/MeterALista', methods=['POST'])
def meterLista():
    palabra = str(request.form['palabra'])
    NodoListaP = Lista.NodoLista(palabra)
    ListaPython.insertarALista(NodoListaP)
    return "Elemento: " + palabra + " Insertado a la Lista"


@app.route('/BuscarEnLaLista', methods=['POST'])
def buscarLista():
    palabraBuscar = str(request.form['search'])
    index = ListaPython.buscarPalabra(palabraBuscar)
    return index


@app.route('/EliminarDeLista', methods=['POST'])
def eliminarDeLista():
    indexAEliminar = int(request.form['index'])
    mensaje = ListaPython.eliminarDeLista(indexAEliminar)
    return str(mensaje)


@app.route('/verLista')
def verLista():
    retorno = str(ListaPython.showList())
    return str(retorno)


@app.route('/ReporteLista')
def ReporteLista():
    return str(ListaPython.textoParaDot())


@app.route('/ingresarMatriz', methods=['POST'])
def ingMat():
    letra = str(request.form['letra'])
    dominio = str(request.form['dominio'])
    dato = str(request.form['dato'])
    MatrizP.ingresarAMatriz(dominio, letra, dato)
    return "Se ingreso a Matriz Correctamente"


@app.route('/ListarPorLetra', methods=['POST'])
def listLetter():
    letra = str(request.form['letra'])
    salida = str(MatrizP.nombresConletra(letra))
    return salida


@app.route('/ListaPorDominio', methods=['POST'])
def domainList():
    dominio = str(request.form['dominio'])
    salida = str(MatrizP.nombresConDominio(dominio))
    return salida


@app.route('/ReporteMatriz')
def ReporteMatriz():
    return "aun trabajando en eso..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
