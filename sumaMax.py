# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 12:49:05 2021

@author: lenovo
"""
def sumaMaxima(lista):
    tabla=[0]*len(lista)
    for i in range(len(lista)):
        tabla[i]=[0]*len(lista)
    for i in range(len(lista)):
        for j in range(0,i):
            tabla[i][j]=tabla[i-1][j]+lista[i]
        tabla[i][i]=lista[i]
    maximo=tabla[0][0]
    indiceUno=0
    indiceDos=0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if(tabla[i][j]>maximo):
                maximo=tabla[i][j]
                indiceUno=i
                indiceDos=j
    return (maximo,indiceUno,indiceDos)

if __name__=="__main__":
    datos=[27,6,-50,21,-3,14,16,-8,42,33,-21,9]
    maximo,rango1,rango2=sumaMaxima(datos)
    print(maximo)
    print(rango1)
    print(rango2)