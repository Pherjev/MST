# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph


def randomBarabasiAlbert(n,d,directed=False, selfloop=False):
        """
        Generación aleatoria de grafos utilizando el modelo de Barabasi-Albert
        Colocar n vértices uno por uno, asignando a cada uno d aristas o vértices 
        distintos de tal manera que la probabilidad de que el vértice nuevo se conecte 
        a un vértice existente v es proporcional a la cantidad de aristas que v
        tiene actualmente – los primeros d vértices se conectan todos con todos.
        n: número de nodos
        d: nuevos nodos
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        return: grafo aleatorio generado
        """
        g = Graph(digraph=directed)

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0

        if d < 0:
                print("d < 0: not valid")
                print("Setting d = 0")
                d = 0


        #g.addNode(str(0))

        for i in range(n):
                g.addNode(str(i))

        #g.addEdge(str(0) + '->' + str(1),str(0),str(1))

        for u in range(1,n):
                randomNodes = np.arange(u)
                np.random.shuffle(randomNodes)

                for v in range(u):
                        j = randomNodes[v]
                        deg = g.getNode(str(j)).degree
                        p = 1 - deg / d
                        

                        if random.random() < p:
                                i = u*1
                                #print(p)

                                if directed and selfloop:
                                        g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                
                                elif directed and not selfloop:
                                        if (j != i):
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))

                                elif not directed and selfloop:
                                        if i >= j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                
                                elif not directed and not selfloop:
                                        if i > j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                

        return g

#g = randomBarabasiAlbert(500,10)
#g.show()
