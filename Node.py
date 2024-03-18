
from pandas import DataFrame


class Nodo:
    def __init__(self):
        self.valor: str = ""
        self.izq:Nodo = None
        self.der:Nodo = None
        self.profundidad = 0
        self.reglas = []
        
    def reescritura(self,registro:DataFrame):
        if self.izq or self.der:
            expresion = self.valor.split("<=")
            if(registro[expresion[0].strip()][registro.index[0]] <= float(expresion[1])):
                return self.izq.reescritura(registro)
            else:
                return self.der.reescritura(registro)
        else:
            try:
                return float(self.valor) == float(registro[registro.columns[len(registro.columns)-1]][registro.index[0]])
            except:
                return self.valor == registro[registro.columns[len(registro.columns)-1]][registro.index[0]]
                
    