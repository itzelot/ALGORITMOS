# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 11:41:18 2021

@author: wendy
"""

def metodo_burbuja(lista):
    for i in range(1, len(lista)):
        for j in range(0, len(lista) - 1):
            if(lista[j] > lista[j + 1]):
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux


def metodo_seleccion(lista):
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

def metodo_insercion(lista):
   for i in range(1, len(lista)):
     valorActual = lista[i]
     posicion = i
     while (posicion > 0 and lista[posicion - 1] > valorActual):
         lista[posicion] = lista [posicion - 1]
         posicion = posicion - 1
     lista[posicion] = valorActual

if __name__ == "__main__":
    lista = [34, 5, 23, 98, 11, 6, 7, 34]
    metodo_insercion(lista)
    print(lista)