# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:17:20 2021

@author: lenovo
"""

if __name__=="__main__":
    tupla0=(34,3,56)
    tupla1=(54,45,"Mexico")
    print(tupla0)
    print(tupla0[2])
    print(tupla1[:2])
    
    print(max(tupla0))
    
    lista=list(tupla1) #conversión de tupla a lista
    print(tupla1)  #tupla parentesis
    print(lista)   #lista corchetes
    
    lista2=[45,23,"de",67,45]  #conversión de lista a tupla
    tupla2=tuple(lista2)
    print(tupla2)
    
    print('de' in tupla2) #buscar datos en la tupla
    
    print(tupla2.count(45))
          
    datos=("Miguel",4,10,1978)
    nombre,dia,mes,an=datos
    print(nombre+" "+str(dia)+" "+str(mes)+" "+str(an))