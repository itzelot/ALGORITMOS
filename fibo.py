# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:53:28 2021

@author: lenovo
"""

def suma(n):
    if n==1:
        return 1
    sumas=n+suma(n-1)
    return sumas

def sumaDos(n):
    return ((n*(n+1))/2)

def fibo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    fib= fibo(n-1)+fibo(n-2) 
    return fib

def fibonacci(n):
    if (n==0 or n==1):
        return n
    fibmenor=0
    fibmayor=1
    for i in range(2,n):
        x= fibmenor
        fibmenor=fibmayor
        fibmayor=x+fibmenor
    return fibmayor

if __name__=="__main__":
    print(fibonacci(8))