# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:34:35 2021

@author: lenovo
"""

if __name__=="__main__":
    diccionario={'A0':23,'A1':89,"A2":90}
    print(diccionario)
    diccionario['A2']=100  #para cambiar un valor del diccionario
    print(diccionario)
    
    diccionario2={34:'Rebeca','A0':101} #los valores pueden tener llaves de distintos tipos de dato
    diccionario2[34]=100
    print(diccionario2)
    print(type(diccionario2))
    
    cadena=str(diccionario) #conversión de diccionario a cadena
    print(cadena)
    print(type(cadena))
    
    #copiar diccionarios
    copia1=diccionario.copy() #se copia el diccionario "diccionario"
    print(copia1)
    copia1["A1"]=2000  #se pueden modificar valores en la copia
    print(diccionario)
    print(copia1)
    
    llaves=[1,2,3,4]  #para relacionar datos
    datos=["A1","C1","L1","F45"]
    diccionario3=diccionario.fromkeys(llaves,datos)
    print(diccionario3)
    print(diccionario3[3])
    
    diccionario4={} #iniciar un diccionario vacío para ir agregando datos, crece dinamicamente
    diccionario4[llaves[0]]=datos[0] 
    print(diccionario4)
    
    #otra forma
    for i range(len(llaves)):
        diccionario4[llaves[i]]=datos[i]
    print(diccionario4)