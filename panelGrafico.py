import math
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent,QPainter
from PyQt5.QtWidgets import QWidget

from Node import Nodo



class panelGrafico(QWidget):
    def __init__(self, n:Nodo ,parent: QWidget | None = ..., flags: Qt.WindowFlags | Qt.WindowType = ...,) -> None:
        self.nodo = n
        super().__init__()
        self.setGeometry(0,0,int(55*(2**self.nodo.profundidad)),(self.nodo.profundidad*300)+100)
    
    def paintEvent(self, a0: QPaintEvent | None) -> None:
        super().paintEvent(a0)
        painter = QPainter(self)
        if(self.nodo):
            self.pintarNodo((self.width()//2),100,painter,self.nodo,self.nodo.profundidad)
            
        
    def pintarNodo(self,x,y,painter:QPainter,nodo:Nodo,profRestante):
        profRestante = profRestante - 1
        painter.drawText(x-(len(nodo.valor)//2)*6,y,nodo.valor)
        if(nodo.izq):
            self.pintarNodo(x-((self.width())//(2**(self.nodo.profundidad-profRestante+1))),y+300,painter,nodo.izq,profRestante)
            painter.drawLine(x,y+5,x-((self.width()//2)//(2**(self.nodo.profundidad-profRestante))),y+285)
        if(nodo.der):
            self.pintarNodo(x+((self.width())//(2**(self.nodo.profundidad-profRestante+1))),y+300,painter,nodo.der,profRestante)
            painter.drawLine(x,y+5,x+((self.width()//2)//(2**(self.nodo.profundidad-profRestante))),y+285)
        