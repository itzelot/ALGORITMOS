# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 10:24:37 2021

@author: lenovo
"""

def sumaDig(lista):
    suma = 0
    for i in lista:
        suma = suma + i
    return suma

def sumaDig2(lista):
    if len(lista) == 0:
        return 0
    else:
        return int(lista[0])+sumaDig2(lista[1:])

if __name__ == "__main__":
    num = 34
    x = [int(a) for a in str(num)]
    print(x)
    print(sumaDig(x))
    