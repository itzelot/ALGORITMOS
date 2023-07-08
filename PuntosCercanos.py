# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import csv
import pprint
import math

class Datos:
    puntos=[]
    def abrirArchivo(self,archivo):
        id=open(archivo,"r")
        for filas in id:
            fila=filas.split(";")
            fila[1]=fila[1].rstrip('\n')
            self.puntos.append(fila)
        id.close()
    def getPuntos(self):
        return self.puntos

def graficas(puntos):
    for indice in range(len(puntos)):
        x.append(int(puntos[indice][0]))
        y.append(int(puntos[indice][1]))
    line, =ax.plot(x,y,'o',picker=5)
    puntosSeleccionado=fig.canvas.mpl_connect('pick_event',onpick)
    plt.show()
    
def onpick(event):
    thisline=event.artist
    xdata=thisline.get_xdata()
    ydata=thisline.get_ydata()
    ind=event.ind
    listaPunto=[]
    puntoSeleccionado=tuple(zip(xdata[ind],ydata[ind]))
    listaPunto.append(puntoSeleccionado[0][0])
    listaPunto.append(puntoSeleccionado[0][1])
    segundaVentana(listaPunto)

def segundaVentana(listaPunto):
    figDos=plt.figure()
    a=figDos.add_subplot(111)
    b=figDos.add_subplot(111)
    c=figDos.add_subplot(111)
    line, =a.plot(x,y,'b.', picker=5)
    line2, =b.plot(listaPunto[0],listaPunto[1],'ro')
    #puntos=distanciaMinima(listaPunto)
    #line3, =c.plot(puntos[0],puntos[1],'g^')

def distanciaMinima(listaPunto):
    minimo=math.sqrt(pow((int(x[0])-int(listaPunto[0])),2)+pow((int(y[0])-int(listaPunto[0])),2))
    puntos=[]
    for indice in range(len(x)):
        d=math.sqrt(pow((int(x[indice])-int(listaPunto[0])),2)+pow((int(y[indice])-int(listaPunto[1])),2))
        if(d!=0 and d<minimo):
            minimo=d
            puntos=[]
            puntos.append(x[indice])
            puntos.append(y[indice])
    return puntos

fig=plt.figure()
ax=fig.add_subplot(111)
ax.set_title('Escoja puntos')
puntosSeleccionado={}
x=[]
y=[]
datos=Datos()
datos.abrirArchivo("Ejemplo.csv")
graficas(datos.getPuntos())
