# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:37:30 2021

@author: lenovo
"""

def factorial(n):
    if(n==0):
        resultado = 1
        print(resultado)
    else:
        resultado = n * factorial(n-1)
    return resultado

def nCombinacion(n,r):
    nCom= int(factorial(n)/(factorial(r)*factorial(n-r)))
    return nCom

def combinaciones(r, n):
    s=[]
    listaF = []
    for i in range(1, r+1):
        s.append(i)
    print(s)
    for i in range(1, nCombinacion(n,r)):
        m= r-1
        val_max = n
        while(s[m] == val_max):
            m= m-1
            val_max = val_max - 1
        s[m] = s[m]+1
        for j in range(m+1, r):
            s[j] = s[j - 1] + 1
        print(s)
        
if __name__=="__main__":
    n=3
    r=3
    combinaciones(r, n)