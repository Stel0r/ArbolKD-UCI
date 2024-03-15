from Node import Nodo
import numpy as np
from ucimlrepo import fetch_ucirepo
from PyQt5 import QtCore,QtWidgets
from panelGrafico import panelGrafico
import sys
from pandas import *

from ucimlrepo import fetch_ucirepo




def crearArbol(data: DataFrame,categoria:int,indice:str,nodo:Nodo,nodoRaiz:Nodo,nivel:int):
    nodoRaiz.profundidad = nivel if nivel > nodoRaiz.profundidad else nodoRaiz.profundidad
    datoPrueba = data[data.columns[len(data.columns)-1]].iloc[0]
    for dato in data[data.columns[len(data.columns)-1]]:
        if dato != datoPrueba:
            data = data.sort_values(by=data.columns[categoria])
            mitad = len(data.index)//2
            if len(data.index) % 2 != 0:
                mitad = mitad + 1
            if mitad+1 == len(data.index):
                val = data[data.columns[categoria]].iloc[mitad]
            else:
                val = (data[data.columns[categoria]].iloc[mitad] + data[data.columns[categoria]].iloc[mitad+1])/2
            print(str(indice) +" - "+ data.columns[categoria] + " <= " + str(val))
            nodo.valor = data.columns[categoria] + " <= " + str(val)
            nuevaCategoria = categoria + 1 if categoria + 1 != len(data.columns)-1 else 0
            nodo.izq = Nodo()
            nodo.der = Nodo()
            crearArbol(data.iloc[:mitad],nuevaCategoria,indice+".1",nodo.izq,nodoRaiz,nivel+1)
            crearArbol(data.iloc[mitad:],nuevaCategoria,indice+".2",nodo.der,nodoRaiz,nivel+1)
            return
    print(str(indice) +" - "+ str(data[data.columns[len(data.columns)-1]].iloc[0]))   
    nodo.valor = str(data[data.columns[len(data.columns)-1]].iloc[0])
  
def graficarArbol(nodoRaiz:Nodo):
    app = QtWidgets.QApplication([])
        
    ventana = QtWidgets.QWidget()
    layout = QtWidgets.QBoxLayout(1,ventana)
    ventana.setWindowTitle("visualizacion")
    ventana.setGeometry(0,0,720,720) 
    scroll = QtWidgets.QScrollArea()
    scroll.setGeometry(0,0,720,720)
    layout.addWidget(scroll)
    panel = panelGrafico(nodoRaiz)
    scroll.setWidget(panel)
        
    ventana.show()
    sys.exit(app.exec())
    
  
# fetch dataset 
repo = fetch_ucirepo(id=15) 
  
# data (as pandas dataframes) 
X:DataFrame = repo.data.features 
y:DataFrame = repo.data.targets 

#purgar el repositorio de todos los datos categoricos

X = X.select_dtypes(np.number) 
# variable information 
#print(repo.variables) 
try:
    X.insert(len(X.columns),column=y.columns[len(y.columns)-1],value=y[y.columns[len(y.columns)-1]])
except:
    print("no se ha agregado la fila target o no esta definida")
nodoRaiz = Nodo()
crearArbol(X,0,"1",nodoRaiz,nodoRaiz,1)

graficarArbol(nodoRaiz)














