from ucimlrepo import fetch_ucirepo
from pandas import *

from ucimlrepo import fetch_ucirepo 



def crearArbol(data: DataFrame,categoria:int,indice:str):
    datoPrueba = data["Class"].iloc[0]
    for dato in data["Class"]:
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
            nuevaCategoria = categoria + 1 if categoria + 1 != len(data.columns) else 0
            crearArbol(data.iloc[:mitad],nuevaCategoria,indice+".1")
            crearArbol(data.iloc[mitad:],nuevaCategoria,indice+".2")
            return
    print(str(indice) +" - "+ str(data["Class"].iloc[0]))    
  
# fetch dataset 
repo = fetch_ucirepo(id=15) 
  
# data (as pandas dataframes) 
X:DataFrame = repo.data.features 
y:DataFrame = repo.data.targets 
  
# variable information 
#print(repo.variables) 

X.insert(len(X.columns),column="Class",value=y["Class"])

crearArbol(X,0,"1")








