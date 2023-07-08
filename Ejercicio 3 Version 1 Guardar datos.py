# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 10:49:09 2021

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
    maximo = tabla[0][0]
    indiceUno = 0
    indiceDos = 0
    for i in range(len(lista)):
        for j in range(len(lista)):
            if (tabla[i][j] > maximo):
                maximo = tabla[i][j]
                indiceUno = i
                indiceDos = j
    return(maximo, indiceUno, indiceDos)

def sumaMax2(lista):
    tabla =[0]*len(lista)
    for i in range(len(lista)):
        tabla[i]=[0]*len(lista)
    sumaS=[0]*len(lista)
    for i in range(len(lista)):
        sumaS[i]=[0]*len(lista)
    maximo=0
    for i in range(len(lista)):
        for j in range(i):
            sumaS[i][j]=sumaS[i-1][j]+lista[i]
            if(sumaS[i][j]>maximo):
                maximo=sumaS[i][j]
                indiceDos=j
                indiceUno=i
        sumaS[i][i]=lista[i]
        if(sumaS[i][i]>maximo):
            maximo=sumaS[i][i]
            indiceUno=i
            indiceDos=i
    return(maximo, indiceUno, indiceDos)


if __name__ == "__main__":
    datos = [27, 6, -50, 21, -3, 14, 16, -8, 42, 33, -21, 9]
    maximo, rangoUno, rangoDos = sumaMax2(datos)
    print(maximo)
    print(rangoUno)
    print(rangoDos)
    print(datos[rangoDos:rangoUno +1])