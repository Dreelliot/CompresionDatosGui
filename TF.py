import tkinter as tk
import graphviz as gv
import numpy as np
import matplotlib as plt
import collections 
import heapq

class Nodohuff:
    def __init__(self, sym, frec, izq=None, der=None):
        self.sym = sym
        self.frec = frec
        self.izq = izq
        self.der = der
        self.dir= ''

    def __lt__(self, otro):
        return self.frec < otro.frec 

    def __repr__(self):
        return f"Nodohuff(sym={self.sym}, frec={self.frec})"
    
    def frecuencia_caracter(string):
        frecuencia_caracter = collections.Counter(string)
        #print(frecuencia_caracter)
        lista=[]
        for key, value in frecuencia_caracter.items():
            sym = key 
            frec = value
            nodo = Nodohuff(sym, frec)
            lista.append(nodo)

        no_usado = []
        for key, value in frecuencia_caracter.items():
            sym=key
            frec=value
            nodo= Nodohuff(sym, frec)
            heapq.heappush(no_usado,nodo) 

        #print(lista)    
        return lista, no_usado
    
    def mkarbol_huff(string): 
        frecuencia_caracter = collections.Counter(string)

        no_usado = []
        for key, value in frecuencia_caracter.items():
            sym=key
            frec=value
            nodo= Nodohuff(sym, frec)
            heapq.heappush(no_usado,nodo)
        return no_usado
    
    def sortarbol_huff(no_usado):
        while len(no_usado)>1:
            izq = heapq.heappop(no_usado)
            der = heapq.heappop(no_usado)
           
            izq.dir = '0'
            der.dir = '1'

            newnodo = Nodohuff(None, izq.frec + der.frec, izq, der)
            heapq.heappush(no_usado, newnodo)
        return no_usado
    
    def printnodos(nodo, val=''):
        newval=val+str(nodo.dir)

        if nodo.izq:
            Nodohuff.printnodos(nodo.izq, newval) 
        if nodo.der:
            Nodohuff.printnodos(nodo.der, newval)

        if(not nodo.izq and not nodo.der):
            print(f"{nodo.sym} -> {newval}")
        

string = "agua clara"

lista = Nodohuff.frecuencia_caracter(string)
no_usado = Nodohuff.mkarbol_huff(string)
#print(no_usado)

Nodohuff.sortarbol_huff(no_usado)
Nodohuff.printnodos(no_usado[0])
