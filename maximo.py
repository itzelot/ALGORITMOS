# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:36:37 2021

@author: lenovo
"""

def maximo(s):
    grande = s[0]
    grandeDos = 0
    for i in s:
        if(i > grande):
            grande = i
        else:
            if(i > grandeDos):
                if(i != grande):
                    grandeDos = i
    print(grande)
    print(grandeDos)
            
if __name__ == "__main__":
    sucesion = [48, 99, 132, 0, 22, 12, 32]
    maximo(sucesion)