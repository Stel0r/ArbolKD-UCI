import numpy as np
from ucimlrepo import fetch_ucirepo
from pandas import *

from ucimlrepo import fetch_ucirepo

from Node import Node 



def crearArbol(data: DataFrame,categoria:int,indice:str,nodo:Node):
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
            nodo.izq = Node()
            nodo.der = Node()
            crearArbol(data.iloc[:mitad],nuevaCategoria,indice+".1",nodo.izq)
            crearArbol(data.iloc[mitad:],nuevaCategoria,indice+".2",nodo.der)
            return
    print(str(indice) +" - "+ str(data[data.columns[len(data.columns)-1]].iloc[0]))   
    nodo.valor = str(data[data.columns[len(data.columns)-1]].iloc[0])
  
# fetch dataset 
repo = fetch_ucirepo(id=15) 
  
# data (as pandas dataframes) 
X:DataFrame = repo.data.features 
y:DataFrame = repo.data.targets 

#purgar el repositorio de todos los datos categoricos

X = X.select_dtypes(np.number) 
# variable information 
#print(repo.variables) 
print(y)
try:
    X.insert(len(X.columns),column=y.columns[len(y.columns)-1],value=y[y.columns[len(y.columns)-1]])
except:
    print("no se ha agregado la fila target o no esta definida")
print(X)
nodoRaiz = Node()
crearArbol(X,0,"1",nodoRaiz)
















