# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def funcionUno(a):    #funciones
    print(a*2)
    
def funcionDos(a):
    return len(a)

if __name__=="__main__":
    cadena="México siempre fiel"
    print(cadena)
    
    #recorrer la cadena
    print(cadena[0:5])   #n-1
    print(cadena[7:])
    print(cadena[:8])
    print(cadena[-4:])
    print(cadena[:-5])
    
    print(len(cadena)) 
    
    print(cadena.split())
    print(cadena.split("e"))
    
    print(cadena*3)
    
    nueva_cadena="m" + cadena[1:] #concatenación
    print(nueva_cadena)
    
    cadena.replace("é", "e")
    print(cadena)
    
    cadena=cadena.replace("s","")
    print(cadena)
    
    if("fiel" in cadena):
        print("sí está")
    else:
        print("no está")
    if(len(cadena)>7):
        print("mayor o igual a 7")
        
    funcionUno(cadena)