# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph


def dist(a,b,x,y):
        return math.sqrt((x-a)**2 + (y-b)**2)

def randomGeographic(n,r,directed=False, selfloop=False):
        """
        Generación automática grafos utilizando el modelo geográfico simple.
        Colocar n vértices en un rectángulo unitario con coordenadas uniformes (o normales) 
        y colocar una arista entre cada par que queda en distancia r o menor.
        n: número de nodos.
        r: distancia máxima para generar el nodo.
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        return: grafo aleatorio generado
        """

        g = Graph(digraph=directed,eng='neato')

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0

        if r < 0:
                print("r < 0: not valid")
                print("Setting p = 0")
                r = 0

        for i in range(n):
                x = 4*random.random()
                y = 4*random.random()
                g.addNode(str(i),pos=str(x) + ','+ str(y)+'!')
                g.getNode(str(i)).x = x
                g.getNode(str(i)).y = y

        for i in range(n):
                a = g.getNode(str(i)).x
                b = g.getNode(str(i)).y

                for j in range(n):
                        c = g.getNode(str(j)).x
                        d = g.getNode(str(j)).y

                        rho = dist(a,b,c,d)
                        #print(a,b,c,d,rho)

                        if rho < r:
                                if directed and selfloop:
                                        g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                        g.getEdge(str(i) + '->' + str(j)).distance = rho
                                
                                elif directed and not selfloop:
                                        if (j != i):
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                                g.getEdge(str(i) + '->' + str(j)).distance = rho
                                elif not directed and selfloop:
                                        if i <= j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                                g.getEdge(str(i) + '->' + str(j)).distance = rho

                                elif not directed and not selfloop:
                                        if i < j:
                                                g.addEdge(str(i) + '->' + str(j),str(i),str(j))
                                                g.getEdge(str(i) + '->' + str(j)).distance = rho

        return g

#g = randomGeographic(500,0.3)
#g.show()
