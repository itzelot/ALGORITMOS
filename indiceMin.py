# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:03:09 2021

@author: lenovo
"""

#Codigo de sucesion nombres
def menor(n):
    chico = 0
    largo = len(n[0])
    indice = 0
    for i in n:
        if(len(i) < largo):
            chico = indice
            largo = len(i)
        indice = indice + 1
    print(chico)
            
if __name__== "__main__":
    nombres = ["anastacia", "wendy", "jose", "itzel", "parangaricutirimicuaro"]
    menor(nombres)
