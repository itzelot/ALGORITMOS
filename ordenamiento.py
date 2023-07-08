# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 11:33:51 2021

@author: lenovo
"""
def burbuja(lista):
    for i in range (1,len(lista)):
        for j in range(0,len(lista)-1):
            if(lista[j]>lista[j+1]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                
def metodoQuickSort(lista1, izquierdo, derecho):
    if(type(lista1) == list and type(izquierdo and derecho) == int):
        pivote = lista1[izquierdo]
        i = izquierdo
        j = derecho
        
        while (i < j):
            while (lista1[i] <= pivote and i < j):
                i += 1
            
            while (lista1[j] > pivote):
                j -= 1
            
            if(i < j):
                auxiliar = lista1[i]
                lista1[i] = lista1[j]
                lista1[j] = auxiliar
        
        lista1[izquierdo] = lista1[j]
        lista1[j] = pivote
        
        if(izquierdo < j - 1):
            metodoQuickSort(lista1, izquierdo, j - 1)
        
        if(j + 1 < derecho):
            metodoQuickSort(lista1, j + 1, derecho)
    else:
        print("Se necesita una lista para trabajar el metodo")
        
if __name__=="__main__":
    lista1=[34,5,23,98,557,34]
    metodoQuickSort(lista1, 0, len(lista1)-1)
    print(lista1)