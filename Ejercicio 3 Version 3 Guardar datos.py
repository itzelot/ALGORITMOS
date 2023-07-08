# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:30:55 2021

@author: wendy
"""

def sumaMax(lista):
    tabla = [0] * len(lista)
    for i in range(len(lista)):
        tabla[i] = [0] * len(lista)
    #Metemos los datos al arreglo
    for i in range(len(lista)):
        for j in range(0, i):
            tabla[i][j] = tabla[i - 1][j] + lista[i]
        tabla[i][i] = lista[i]
    #Buscamos la suma que sea mas larga
    maximo = 0
    suma = 0
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        if(suma + lista[i] > 0):
            suma = suma + lista[i]
        else:
            suma = 0
            indiceUno = i + 1
        if(suma > maximo):
            maximo = suma
            indiceDos = i
    return(maximo, indiceDos, indiceUno)

if __name__ == "__main__":
    datos = [-27,-12,0,9,28,65,88]
    maximo, indiceDos, indiceUno = sumaMax(datos)
    print(maximo)
    print(indiceUno)
    print(indiceDos)
    print(datos[indiceDos:indiceUno + 1])