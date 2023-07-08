# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 19:11:36 2021

@author: wendy & itzel
"""

import matplotlib.pyplot as plt
import math

class Datos:
    puntos = []
    def abrirArchivo(self,archivo):
        id = open(archivo,"r")
        for filas in id:
            fila = filas.split(";")
            fila[1] = fila[1].rstrip('\n')
            self.puntos.append(fila)
        id.close()
        
    def getPuntos(self):
        return self.puntos

class Punto:
    def __init__(self, x, y, rango = 0):
        self.x = x
        self.y = y
        self.rango = rango

def graficas(puntos):
    for indice in range(len(puntos)):
        x.append(int(puntos[indice][0]))
        y.append(int(puntos[indice][1]))
        puntosArreglo.append(Punto(int(puntos[indice][0]), int(puntos[indice][1])))
    
    for i in range(0, len(puntosArreglo)):
        line, = ax.plot(puntosArreglo[i].x,puntosArreglo[i].y,'o',picker = 5)
    
    fig.canvas.mpl_connect('pick_event', onpick)
    plt.show()
    
def onpick(event):
    thisline = event.artist
    xdata = thisline.get_xdata()
    ydata = thisline.get_ydata()
    ind = event.ind
    listaPunto = []
    puntoSeleccionado = tuple(zip(xdata[ind],ydata[ind]))
    listaPunto.append(puntoSeleccionado[0][0])
    listaPunto.append(puntoSeleccionado[0][1])
    segundaVentana(listaPunto)

def segundaVentana(listaPunto):
    figDos = plt.figure()
    a = figDos.add_subplot(111)
    puntos = distanciaMinima(listaPunto)
    line, = a.plot(x,y, 'o', marker = (5, 2), picker=5)
    line, = a.plot(listaPunto[0], listaPunto[1],'m', marker = 'D')
    line, = a.plot(puntos[0], puntos[1], 'rD')

def distanciaMinima(listaPunto):
    minimo = 100
    puntos = []
    for indice in range(len(puntosArreglo)):
        d = math.sqrt(pow((int(puntosArreglo[indice].x) - int(listaPunto[0])), 2) + pow((int(puntosArreglo[indice].y) - int(listaPunto[1])), 2))
        if(d!=0 and d<minimo):
            minimo=d
            puntos=[]
            puntos.append(puntosArreglo[indice].x)
            puntos.append(puntosArreglo[indice].y)
    return puntos
                
def ordenarRangosSeleccion(puntosArreglo):
    for i in range(len(puntosArreglo) - 1):
        for j in range(i + 1, len(puntosArreglo)):
            if puntosArreglo[i].x > puntosArreglo[j].x:
                puntosArreglo[i].x,  puntosArreglo[j].x = puntosArreglo[j].x, puntosArreglo[i].x
                puntosArreglo[i].y, puntosArreglo[j].y = puntosArreglo[j].y, puntosArreglo[i].y

def ordenarRangosBurbuja(puntosArreglo):
    for i in range(1, len(puntosArreglo)):
        for j in range(0, len(puntosArreglo) - 1):
            if(puntosArreglo[j].x > puntosArreglo[j + 1].x):
                auxUno = puntosArreglo[j].x
                auxDos = puntosArreglo[j].y
                puntosArreglo[j].x = puntosArreglo[j + 1].x
                puntosArreglo[j].y = puntosArreglo[j + 1].y
                puntosArreglo[j + 1].x = auxUno
                puntosArreglo[j + 1].y = auxDos

def encontrarRangosIterativoOrdenado(puntosArreglo):
    for i in range(0, len(puntosArreglo)):
        for j in range(i + 1, len(puntosArreglo)):
            if(puntosArreglo[j].y > puntosArreglo[i].y):
                puntosArreglo[j].rango += 1

def encontrarRangosRecursivo(puntosArreglo):
    if(len(puntosArreglo) < 2):
        return puntosArreglo
    else:
        j = len(puntosArreglo) - 1
        for i in range(0, len(puntosArreglo) - 1):
            if(puntosArreglo[j].x > puntosArreglo[i].x):
                if(puntosArreglo[j].y > puntosArreglo[i].y):
                    puntosArreglo[j].rango += 1
        puntosArreglo = encontrarRangosRecursivo(puntosArreglo[:len(puntosArreglo) - 1])
        return puntosArreglo
    
if __name__=="__main__":
    fig=plt.figure()
    ax=fig.add_subplot(111)
    ax.set_title('Escoja puntos')
    puntosSeleccionado={}
    x=[]
    y=[]
    datos=Datos()
    puntosArreglo = []
    datos.abrirArchivo("Ejemplo.csv")
    graficas(datos.getPuntos())
    ordenarRangosBurbuja(puntosArreglo)
    encontrarRangosRecursivo(puntosArreglo)
    print("-----------------------")
    print("x        y         rango")
    print("-----------------------")
    for i in range(0, len(puntosArreglo)):
        print(puntosArreglo[i].x,"     ",puntosArreglo[i].y, "          ", puntosArreglo[i].rango)