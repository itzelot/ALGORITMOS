# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:54:30 2021

@author: lenovo
"""

def binario(listaNumeros,clave):
    inferior = 0
    superior = len(listaNumeros) - 1
    central = (inferior + superior) / 2
    if (central.is_integer()):
        central = int(central)
    else:
        central = int(central + 0.5)
    if (listaNumeros[central] == clave):
        return listaNumeros[central]
    if (inferior > superior):
        return - 1
    else:
        if (clave < listaNumeros[central]):
            return binario(listaNumeros[:central- 1], clave)
        if (clave > listaNumeros[central]):
            return binario(listaNumeros[central + 1:], clave)
    
    
if __name__ == "__main__":
    listaNum = [2, 34, 45, 60, 93, 103]
    print(binario(listaNum, 2))