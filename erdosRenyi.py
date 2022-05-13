# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph

def randomErdosRenyi(n,m, directed=False, selfloop=False):
        """
        Generación de grafos aleatorios con el modelo de Erdös-Rényi
        Crear n vértices y elegir uniformement al azar m distintos pares de distintos vértices.
        n: número de nodos
        m: número de aristas
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        return: genera grafo aleatorio
        """

        g = Graph(digraph=directed)

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0
        if m > n*n:
                print("m>n*n: maximum number of edges reached")
                print("Setting m = n*n")
                m = n*n

        for i in range(n):
                g.addNode(str(i))

        added = []

        for i in range(m):
                #print(i)
                keepg = True
                while keepg: 
                        keepg = False
                        if directed and selfloop:
                                u = random.randint(0,n-1)
                                v = random.randint(0,n-1)    
                                nameEdge = str(u) + '->' + str(v)
                                if nameEdge not in added:
                                        added.append(nameEdge)
                                        g.addEdge(nameEdge,str(u),str(v))
                                else:
                                        keepg = True 

                        elif not directed and selfloop:
                                u = random.randint(0,n-1)
                                v = random.randint(0,n-1)    
                                nameEdge = str(u) + '->' + str(v)
                                nameEdgeA= str(v) + '->' + str(u)
                                if nameEdge not in added:
                                        added.append(nameEdge)
                                        added.append(nameEdgeA)
                                        g.addEdge(nameEdge,str(u),str(v))
                                else:
                                        keepg = True

                        elif directed and not selfloop:
                                u = random.randint(0,n-1)
                                v = random.randint(0,n-1)    
                                nameEdge = str(u) + '->' + str(v)
                                if nameEdge not in added and u != v:
                                        added.append(nameEdge)
                                        g.addEdge(nameEdge,str(u),str(v))
                                else:
                                        keepg = True

                        elif not directed and not selfloop:
                                u = random.randint(0,n-1)
                                v = random.randint(0,n-1)    
                                nameEdge = str(u) + '->' + str(v)
                                nameEdgeA= str(v) + '->' + str(u)
                                if nameEdge not in added and u != v:
                                        added.append(nameEdge)
                                        added.append(nameEdgeA)
                                        g.addEdge(nameEdge,str(u),str(v))
                                else:
                                        keepg = True
        return g 


#g = randomErdosRenyi(500,7000)
#g = randomErdosRenyi(500,7000)

#g.show()
