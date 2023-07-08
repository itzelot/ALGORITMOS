# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 12:12:30 2021

@author: lenovo
"""
import pandas as pd
import matplotlib.pyplot as plt

if __name__=="__main__":
    datos=pd.read_csv("m1.csv",sep=";")
    
    x=datos.N
    y=datos.Tiempo
    plt.plot(x,y)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Burbuja")
    plt.grid()
    plt.show()