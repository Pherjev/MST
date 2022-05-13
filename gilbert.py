# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph

def randomGilbert(n,p,directed=False, selfloop=False):
        """
        Generación aleatorio de grafos utilizando el modelo de Gilbert
        Crear n vértices y poner una arista entre cada par independiente y uniforme con probabilidad p
        n: número de nodos
        p: probabilidad 
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        return: grafo aleatorio generado
        """
        g = Graph(digraph=directed)

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0

        if p <= 0:
                print("p <= 0: not valid")
                print("Setting p = 0")
                p = 0
        elif p > 1:
                print("p > 1: not valid")
                print("Setting p = 1")
                p = 1

        for i in range(n):
                g.addNode(str(i))

        for i in range(n):
                for j in range(n):
                        if random.random() < p:
                                if directed and selfloop:
                                        g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                
                                elif directed and not selfloop:
                                        if (j != i):
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))

                                elif not directed and selfloop:
                                        if i <= j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                
                                elif not directed and not selfloop:
                                        if i < j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                

        return g

#g = randomGilbert(500,0.05)
#g.show()
