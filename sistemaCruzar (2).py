# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 08:59:54 2021

@author: wendy & itzel
"""

def sistemaCruzar(izquierda):
    print("A = Persona, B = Gallina, C = Lobo, D = Maiz")
    print("La primera pocision corresponde a A, la segunda a B, y asi sucesivamente")
    print("Empezamos con todos en el lado izquierdo del río")
    print("lado izquierdo: ", izquierda)
    print("----------")
    derecha = [0, 0 , 0 , 0]
    comprobar = [1, 1, 1, 1, 1, 1, 1]
    banderaIzq = True
    
    while(True):
        if(derecha == [1, 1, 1, 1]):
            break
        if(comprobar == [0, 0, 0, 0, 0, 0, 0]):
            print("No se llegó al objetivo por falta de reglas")
            break
        
        if(banderaIzq):
            if(izquierda[0] == 1 and izquierda[1] == 1 and comprobar[0] == 1):
                print("Tomamos la regla 1")
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                comprobar[0] = 0
            elif(izquierda[0] == 1 and izquierda[2] == 1 and comprobar[2] == 1):
                print("Tomamos la regla 3")
                izquierda[0], izquierda[2] = 0, 0
                derecha[0], derecha[2] = 1, 1
                comprobar[2] = 0
            elif(izquierda[0] == 1 and izquierda[3] == 1 and comprobar[4] == 1):
                print("Tomamos la regla 5")
                izquierda[0], izquierda[3] = 0, 0
                derecha[0], derecha[3] = 1, 1
                comprobar[4] = 0
            elif(izquierda[0] == 1 and izquierda[1] == 1 and comprobar[6] == 1):
                print("Tomamos la regla 7")
                izquierda[0], izquierda[1] = 0, 0
                derecha[0], derecha[1] = 1, 1
                comprobar[0] = 0
            else:
                print("No se llegó al objetivo porque ya no se cumple con ninguna regla")
                break
            banderaIzq = False
            print("lado izquierdo: ", izquierda)
            print("lado derecho:   ", derecha)
            print("----------")
                
        else:
            if(derecha[0] == 1 and derecha[1] == 1 and comprobar[1] == 1):
                print("Tomamos la regla 2")
                derecha[0] = 0
                izquierda[0] = 1
                comprobar[1] = 0
            elif(derecha[0] == 1 and derecha[2] == 1 and comprobar[3] == 1):
                print("Tomamos la regla 4")
                derecha[0], derecha[1] = 0, 0
                izquierda[0], izquierda[1] = 1, 1
                comprobar[3] = 0
            elif(derecha[0] == 1 and derecha[3] == 1 and comprobar[5] == 1):
                print("Tomamos la regla 6")
                derecha[0] = 0
                izquierda[0]= 1
                comprobar[5] = 0
            else:
                print("No se llegó al objetivo porque ya no se cumple con ninguna regla")
                break
            banderaIzq = True
            print(izquierda)
            print(derecha)
            print("----------")
    
    return derecha

if __name__=="__main__":
    izquierda = [1, 1, 1, 1]
    salida = sistemaCruzar(izquierda)
    print("--------------------------------------------")
    print("Terminamos el proceso al llegar al resultado buscado")
    print("lado derecho:  ", salida)