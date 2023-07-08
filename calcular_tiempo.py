# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:48:33 2021

@author: lenovo
"""
import ordenamiento
import random as rn
import copy
from time import time

def crear_list(longitud):
    lista=[]
    for i in range(0,longitud):
        lista.append(rn.randint(0,200))
    return lista

if __name__=="__main__":
    archivo=open("m1.csv","w")
    archivo.write("N;Tiempo\n")
    lista=crear_list(500)
    x=100
    for i in range(100,510,10):
        lista_nueva=copy.deepcopy(lista[:x])
        inicio_tiempo=time()
        ordenamiento.burbuja(lista_nueva)
        transcurrido=time()-inicio_tiempo
        archivo.write(str(x)+";"+format(transcurrido,'.5f')+'\n')
        x=x+100
    archivo.close()