# -*- coding: utf-8 -*-

import math
import random
import numpy as np
import graphviz
from PIL import Image
from colormap import rgb2hex
from graph import Graph


def dorogovtsevMendes(n, directed=False,diagonals=False):
        """
        Generación de grafos utilizando el modelo de Dorogovtsev-Mendes.
        Crear 3 nodos y 3 aristas formando un triángulo. Después, para cada nodo 
        adicional, se selecciona una arista al azar y se crean aristas entre el 
        nodo nuevo y los extremos de la arista seleccionada.
        n: número de nodos.
        directed: grafo dirigido
        selfloop: permitir auto-ciclos
        diagonals: permitir diagonales 
        return: grafo aleatorio generado       
        """

        g = Graph(digraph=directed,eng='sfdp')

        if n < 0:
                print("n < 0: not valid")
                print("Setting n = 0")
                n = 0


        # First, we add all nodes

        for i in range(n):
                g.addNode(str(i))


        if n >= 2:
                g.addEdge(str(0) + '->' + str(1),str(0),str(1))

        if n >= 3:
                g.addEdge(str(1) + '->' + str(2),str(1),str(2))
                g.addEdge(str(0) + '->' + str(2),str(0),str(2))       



        for i in range(2,n-1):
                E = list(g.edges.keys()) #list(np.arange(0,i))
                a = random.choice(E)
                nd0 = g.getEdge(a).n0.id
                nd1 = g.getEdge(a).n1.id
                #print(a,nd0,nd1)
                g.addEdge(str(i+1) + '->' + nd0,str(i+1),nd0)  
                g.addEdge(str(i+1) + '->' + nd1,str(i+1),nd1)


        return g 

#g = dorogovtsevMendes(500)

#g.show()
