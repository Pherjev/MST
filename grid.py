# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph

def grid(m,n, directed=False,diagonals=False):
        """
        Generación de grafos utilizando el modelo de malla.
        Crear  𝑚×𝑛  nodos. Para el nodo  𝑛𝑖,𝑗  crear una arista con 
        el nodo  𝑛𝑖+1,𝑗  y otra con el nodo  𝑛𝑖,𝑗+1 , para  𝑖<𝑚  y  𝑗<𝑛 .
        n: número de columnas
        m: número de filas
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        return: grafo aleatorio generado
        """

        if n == 0:
                n = m

        m = max(2,m)
        n = max(2,n)

        g = Graph(digraph=directed,eng='neato')

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0
        #if m > n*n:
        #        print("m>n*n: maximum number of edges reached")
        #        print("Setting m = n*n")
        #        m = n*n

        #for i in range(n):
        #        g.addNode(str(i))

        # First, we add all nodes

        for i in range(m):
                for j in range(n):
                        #print(i*n+j)
                        g.addNode(str(i*n+j),pos=str(i) + ','+ str(j)+'!')
                        g.getNode(str(i*n+j)).x = str(i)
                        g.getNode(str(i*n+j)).y = str(j)


        for i in range(m):
                for j in range(n):
                        
                        #g.addNode(str(i*n+j),pos=str(i) + ','+ str(j)+'!')
                        #g.addNode(str(i*n+j)).x = float(i)
                        #g.addNode(str(i*n+j)).y = float(j)

                        if j < n-1:
                                a = i*n + j
                                b = i*n + j + 1
                                g.addEdge(str(a)+'->' + str(b),str(a),str(b))

                        if i < m - 1:
                                a = i*n + j
                                b = (i+1)*n + j
                                g.addEdge(str(a)+'->' + str(b),str(a),str(b))

                        if i < m - 1 and j < n - 1 and diagonals:
                                a = i*n + j
                                b = (i+1)* n + j + 1
                                g.addEdge(str(a)+'->' + str(b),str(a),str(b))       

                        if i > 0 and j < n - 1 and diagonals:
                                a = i*n + j
                                b = (i-1)* n + j + 1
                                g.addEdge(str(a)+'->' + str(b),str(a),str(b)) 

        return g 

#g = grid(25,20)
#g.show()
