# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:45:04 2021

@author: lenovo
"""
if __name__=="__main__":
    nombres = ["Juan", "Rosa", "Rebecca"]
    edad = [34, 10, 23]
    print(nombres)
    print(edad)
    
    for i in nombres:
        print(i)
    for i in edad:
        print(i * 2)
    for i in nombres:
        print(len(i))
        
    for i in range(len(nombres)):
        print(nombres[i])
    
    print(max(edad))
    print(max(nombres))
    
    edad.append(100) #añade elementos al final
    print(max(edad))
    print(edad.count(10))
    
    nombres.extend(edad)
    print(nombres)
    
    edad.sort()
    print(edad)
    edad.sort(reverse=True)
    print(edad)
    edad.insert(2, 100)
    print(edad)
    print(edad.pop(2))  #remueve un valor
    print(edad)
    print(edad.remove(10))  #remueve el valor 10 y te regresa un none
    del edad[2]
    print(edad)
    edad[1]=121
    print(edad)
    