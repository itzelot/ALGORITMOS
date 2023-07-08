# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 23:27:42 2021

@author: lenovo
"""

def factorial(n):
    if(n==0):
        resultado = 1
        print(resultado)
    else:
        resultado = n * factorial(n-1)
    return resultado

def swap(lista, indiceUno, indiceDos):
    aux = lista[indiceUno]
    lista[indiceUno] = lista[indiceDos]
    lista[indiceDos] = aux
    return lista

def permutaciones(n):
    s = []
    listaF = []
    for i in n:
        s.append(i)
    print(s)
    listaF.append(list(s))
    for i in range(1, factorial(len(n))):
        m = len(n)-2
        while(s[m]>=s[m+1]):
            m= m-1
        k= len(n)-1
        while(s[m]>=s[k]):
            k= k-1
        swap(s, m, k)
        p= m+1
        q= len(n)-1
        while(p<q):
            swap(s, p, q)
            p= p+1
            q= q-1
        if(s not in listaF):
            listaF.append(list(s))
    return listaF
            
if __name__=="__main__":
    lista=[1,1,1,2,2,2,2,2]
    l= permutaciones(lista)
    print(l)
    print(len(l))
    
