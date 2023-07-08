# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 00:12:46 2021

@author: lenovo
"""

def mcd(a,b):
    if(b > a):
        aux = a
        a = b
        b = aux
    if(a % b == 0):
        return b
    else:
         return mcd(b, a % b)
      
if __name__ == "__main__":
    a=124
    b=6
    print(mcd(a,b))
    